#!/bin/bash
# Starts a transcription in the background (long footage takes longer than one command may run).
# Usage: bash run.sh "<video or folder>" [extra options for transcribe.py]
python3 -c "import faster_whisper" 2>/dev/null || pip3 install --break-system-packages -q faster-whisper 2>/dev/null || pip3 install -q faster-whisper
LOG="$HOME/whisper_$(date +%H%M%S)_$$.log"
nohup python3 "$(dirname "$0")/transcribe.py" "$@" > "$LOG" 2>&1 &
echo "Started, log: $LOG  (follow with: tail $LOG — finished when it says 'ALL DONE')"
