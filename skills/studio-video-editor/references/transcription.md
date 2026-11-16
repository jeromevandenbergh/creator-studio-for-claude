# Transcription with Whisper (optional — before Version 1)

When the footage contains speech (interviews, vlogs, conversations, voice-over), transcribe it **before** building V1, so you can find the strongest quotes, hooks and punchlines by content and not only by image.

## 1. Find Whisper
- Use the Whisper folder named in the profile/settings, or look in the connected folders for `whisper/transcribe.py` (usually `Tools/whisper`).
- Not found → say once: "Whisper isn't installed, so I'll work on image only (see Tools/whisper/README.md to install it)" and continue without transcription. Never install it in the user's folders yourself.

## 2. Run it (on the user's computer, in the device shell)
```
bash "<whisper folder>/run.sh" "<footage file or folder>" --lang <content language, or auto> --prompt "<names, brands, places from the briefing/profile>"
```
- It runs in the background and writes a log; check the log about once a minute until it says `ALL DONE`. Long footage can take several minutes.
- Files that already have a transcript are skipped (use `--force` only when asked).
- Output: a `_Transcripties` folder next to the footage with `.txt` (timecodes), `.srt` and `.words.json`.
- If the model isn't downloaded yet and the download fails, ask the user to do the one-time setup in Terminal (README) and continue on image meanwhile.

## 3. Use the transcripts
- Read the `.txt` files of all clips; mark the strongest lines (hook candidates, punchlines, key messages, CTA-worthy quotes) with their timecodes.
- Build a short "paper edit": the order of lines/moments with file + timecode, then build V1 from it in the editing software.
- Use `.words.json` for precise in/out points on a word.

## 4. Rules
- Transcripts are a **working aid**: always check key quotes, names, brands and dialect against the footage itself.
- Never use the `.srt` as finished subtitles in V1. In V2 (only after approval and only if subtitles are requested) it may be a starting point, corrected against the audio.
- Everything stays **local**: never upload footage or transcripts to external services.
- Never delete or move transcripts, the `models` folder or the Whisper scripts.
