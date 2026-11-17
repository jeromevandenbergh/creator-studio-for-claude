@echo off
REM Windows: transcribe footage manually.
REM Usage: drag a video or folder onto this file, or run in PowerShell:
REM   .\run-windows.bat "C:\path\to\footage" --lang nl --prompt "names, brands"
where py >nul 2>nul || (echo Python is not installed. See README.md. & pause & exit /b 1)
py -c "import faster_whisper" 2>nul || py -m pip install -q faster-whisper
py "%~dp0transcribe.py" %*
echo.
pause
