#!/usr/bin/env python3
"""Transcribe footage with Whisper (faster-whisper), fully local.

Usage:
  python3 transcribe.py <video|folder> [--model large-v3-turbo|small] [--lang nl|en|fr|auto] [--prompt "names, brands, jargon"]
  python3 transcribe.py --download-only [--model large-v3-turbo]   # download the model once, then exit

Output per file in a _Transcripties/ folder next to the footage:
  <name>.txt (with timecodes), <name>.srt, <name>.words.json (word-level timestamps)
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

EXT = {".mp4", ".mov", ".m4v", ".mkv", ".m4a", ".wav", ".mp3", ".aac"}
DEFAULT_CACHE = str(Path(__file__).resolve().parent / "models")

def ts(t, srt=False):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}" if srt else f"{int(h):02d}:{int(m):02d}:{s:05.2f}"

def files(target):
    p = Path(target)
    if p.is_file(): return [p]
    return sorted(f for f in p.rglob("*") if f.suffix.lower() in EXT and "_Transcripties" not in f.parts)

def main():
    a = argparse.ArgumentParser()
    a.add_argument("target", nargs="?")
    a.add_argument("--model", default="large-v3-turbo", help="large-v3-turbo (best) or small (faster, lighter)")
    a.add_argument("--lang", default="auto", help="nl, en, fr, ... or auto")
    a.add_argument("--prompt", default="", help="names, brands or jargon to help recognition")
    a.add_argument("--cache", default=DEFAULT_CACHE)
    a.add_argument("--force", action="store_true", help="re-transcribe files that already have a transcript")
    a.add_argument("--download-only", action="store_true", help="only download the model, then exit")
    o = a.parse_args()

    from faster_whisper import WhisperModel
    model = WhisperModel(o.model, device="cpu", compute_type="int8", cpu_threads=os.cpu_count(), download_root=o.cache)
    if o.download_only:
        print(f"Model {o.model} ready in {o.cache}", flush=True); return
    if not o.target:
        sys.exit("Give a video file or folder.")

    has_ffmpeg = shutil.which("ffmpeg") is not None
    todo = files(o.target)
    print(f"{len(todo)} file(s)", flush=True)
    for f in todo:
        out = f.parent / "_Transcripties"; out.mkdir(exist_ok=True)
        base = out / f.stem
        if base.with_suffix(".txt").exists() and not o.force:
            print(f"skip (already done): {f.name}", flush=True); continue
        t0 = time.time()
        with tempfile.TemporaryDirectory() as tmp:
            src = str(f)
            if has_ffmpeg:  # faster with ffmpeg; otherwise faster-whisper decodes the file itself
                wav = Path(tmp) / "a.wav"
                r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(f), "-vn", "-ac", "1", "-ar", "16000", str(wav)])
                if r.returncode or not wav.exists() or wav.stat().st_size < 1000:
                    print(f"no audio: {f.name}", flush=True); continue
                src = str(wav)
            try:
                segs, info = model.transcribe(src, language=None if o.lang == "auto" else o.lang,
                    word_timestamps=True, vad_filter=True, initial_prompt=o.prompt or None)
                segs = list(segs)
            except Exception as e:
                print(f"failed: {f.name} ({e})", flush=True); continue
        lines, srt, words = [], [], []
        for i, s in enumerate(segs, 1):
            lines.append(f"[{ts(s.start)} - {ts(s.end)}] {s.text.strip()}")
            srt.append(f"{i}\n{ts(s.start, True)} --> {ts(s.end, True)}\n{s.text.strip()}\n")
            words += [{"w": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2), "p": round(w.probability, 2)} for w in (s.words or [])]
        head = f"# {f.name} | model {o.model} | language {info.language} | duration {ts(info.duration)}\n"
        base.with_suffix(".txt").write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
        base.with_suffix(".srt").write_text("\n".join(srt), encoding="utf-8")
        Path(str(base) + ".words.json").write_text(json.dumps({"file": f.name, "language": info.language, "words": words}, ensure_ascii=False), encoding="utf-8")
        print(f"done: {f.name} ({len(segs)} lines, {time.time() - t0:.0f}s)", flush=True)
    print("ALL DONE", flush=True)

if __name__ == "__main__":
    main()
