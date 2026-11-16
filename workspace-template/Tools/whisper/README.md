# Whisper — local transcription (optional)

Lets the video editor read **what is said** in your footage, so it can find quotes, hooks and punchlines by content.
Everything runs **locally**: no footage is sent to an external service.

## One-time setup on your Mac (± 10 minutes)
1. Keep this `whisper` folder inside a folder you connect to your Claude Project (e.g. your Studio workspace folder → `Tools/whisper`). Don't move or delete the `models` folder once it exists.
2. Open **Terminal** and run (replace the path with where this folder is):
   ```
   cd "/path/to/Tools/whisper"
   pip3 install faster-whisper
   python3 transcribe.py --download-only
   ```
   This downloads the model (± 1.6 GB for `large-v3-turbo`) into `models/`. Short on space or an older Mac? Use `--model small` (± 0.5 GB).
3. Optional, faster: install ffmpeg with Homebrew (`brew install ffmpeg`). Without it, transcription still works.

## Use
You don't have to do anything: the video editor runs it before Version 1. Manually:
```
bash run.sh "/path/to/footage" --lang nl --prompt "names, brands"
```
Output appears in a `_Transcripties` folder next to the footage: `.txt` (timecodes), `.srt` and `.words.json`.

Transcripts are a working aid: always check key quotes, names and dialect against the footage.
