# Changelog

## v3.0 — November 2026
**Video editor**
- **Numbered versions:** every round of changes is a new timeline (V1, V2, V3 … up to the final result) in the same project. Claude duplicates the latest timeline and only edits the copy, so you can always go back and compare.
- **Subtitles by default:** when a video has speech, Claude corrects the Whisper `.srt` and imports it straight into your CapCut project in the finishing phase. New briefing question to switch it off. Skipped for music-only or no-speech videos.
- **Background only:** Claude uses computer use in the background and never asks for full control of your screen.

**Mac & Windows**
- The guides (README + HANDLEIDING) now cover **Windows 10/11** next to Mac: folder paths, CapCut drafts folder, permissions and Whisper setup. Steps that differ are marked 🍎 Mac / 🪟 Windows.
- Whisper: new `Tools/whisper/run-windows.bat` to transcribe manually on Windows (drag a folder onto it).

**How to update:** delete the old `studio-video-editor` skill in **Customize → Skills** and upload the new `install/studio-video-editor.zip`. Copy the new `project-instructions.md` (section 0 has a new COMPUTER line; section 5 changed) into your Project instructions — keep your filled-in profile values.

## v2 — November 2026
See the v2 release on GitHub.

## v1.0 — November 2026
First public release.
