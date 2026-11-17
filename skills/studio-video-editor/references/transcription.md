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
- If the model isn't downloaded yet and the download fails, ask the user to do the one-time setup (README: Terminal on Mac, PowerShell on Windows) and continue on image meanwhile.
- Works the same on Mac and Windows: the device shell is a Linux environment with the connected folders mounted, so always use `run.sh` there — use the folder paths as the shell sees them, not `C:\…` paths.
- If the device shell isn't available, ask the user to start it themselves and continue on image meanwhile: 🍎 Mac (Terminal): `bash "<whisper folder>/run.sh" "<footage>" --lang <lang>` · 🪟 Windows: double-click `run-windows.bat` and drag the footage folder onto it, or in PowerShell `.\run-windows.bat "<footage>" --lang <lang>`.

## 3. Use the transcripts
- Read the `.txt` files of all clips; mark the strongest lines (hook candidates, punchlines, key messages, CTA-worthy quotes) with their timecodes.
- Build a short "paper edit": the order of lines/moments with file + timecode, then build V1 from it in the editing software.
- Use `.words.json` for precise in/out points on a word.

## 4. Rules
- Transcripts are a **working aid**: always check key quotes, names, brands and dialect against the footage itself.
- Never put subtitles in the montage phase. In the finishing phase (after explicit approval) the `.srt` is the default subtitle source when the video has speech: correct it against the audio (names, dialect, brands), save the corrected file next to the original, and import it as a caption track directly into the editing project — not via another app. Skip when there's no speech, only music, or the creator chose "No subtitles".
- Everything stays **local**: never upload footage or transcripts to external services.
- Never delete or move transcripts, the `models` folder or the Whisper scripts.
