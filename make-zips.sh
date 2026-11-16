#!/bin/sh
# Rebuilds the upload-ready skill ZIPs in install/ after you edit a skill.
cd "$(dirname "$0")/skills" || exit 1
mkdir -p ../install
for d in */; do d=${d%/}; rm -f "../install/$d.zip"; zip -rq "../install/$d.zip" "$d" -x '*.DS_Store'; echo "built install/$d.zip"; done
