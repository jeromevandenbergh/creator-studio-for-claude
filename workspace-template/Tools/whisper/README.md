# Whisper — local transcription (optional)

Lets the video editor read **what is said** in your footage, so it can find quotes, hooks and punchlines by content.
Everything runs **locally**: no footage is sent to an external service.

## One-time setup (± 10 minutes)
Keep this `whisper` folder inside a folder you connect to your Claude Project (e.g. your Studio workspace folder → `Tools/whisper`). Don't move or delete the `models` folder once it exists.

**🍎 Mac** — open **Terminal** and run (replace the path with where this folder is):
```
cd "/path/to/Tools/whisper"
pip3 install faster-whisper
python3 transcribe.py --download-only
```
Optional, faster: install ffmpeg with Homebrew (`brew install ffmpeg`).

**🪟 Windows** — install **Python 3** from python.org (tick **"Add python.exe to PATH"**). Open this folder in File Explorer, type `powershell` in the address bar, press Enter and run:
```
py -m pip install faster-whisper
py transcribe.py --download-only
```
Optional, faster: `winget install Gyan.FFmpeg`.

This downloads the model (± 1.6 GB for `large-v3-turbo`) into `models/`. Short on space or an older computer? Add `--model small` (± 0.5 GB). Without ffmpeg, transcription still works.

## Use
You don't have to do anything: the video editor runs it before Version 1. Manually:
```
bash run.sh "/path/to/footage" --lang nl --prompt "names, brands"          # Mac
.\run-windows.bat "C:\path\to\footage" --lang nl --prompt "names, brands"   # Windows (or drag the folder onto run-windows.bat)
```
Output appears in a `_Transcripties` folder next to the footage: `.txt` (timecodes), `.srt` and `.words.json`.

Transcripts are a working aid: always check key quotes, names and dialect against the footage.
