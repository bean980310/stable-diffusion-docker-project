#!/bin/bash
set -e

export HF_HOME="/app"

cd /app/automatic
python3 launch.py --listen --port 7860