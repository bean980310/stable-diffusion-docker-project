#!/bin/bash
set -e

export HF_HOME="/app"

cd /app/automatic
nohup python3 launch.py --listen --port 7860 --skip-env> /app/sdnext.log 2>&1 &