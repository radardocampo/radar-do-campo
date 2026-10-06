#!/usr/bin/env bash
# Prepara a maquina da nuvem para montar videos.
set -e
cd "$(dirname "$0")/.."
if ! command -v ffmpeg >/dev/null || [ ! -d /usr/share/fonts/truetype/liberation ]; then
  sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg fonts-liberation
fi
pip install -q numpy pillow opencv-python-headless soundfile faster-whisper
export RADAR_BASE="$PWD"
grep -q RADAR_BASE ~/.bashrc 2>/dev/null || echo "export RADAR_BASE=\"$PWD\"" >> ~/.bashrc
mkdir -p "Videos prontos/Shorts"
ffmpeg -version | head -1
echo "RADAR_BASE=$RADAR_BASE"
