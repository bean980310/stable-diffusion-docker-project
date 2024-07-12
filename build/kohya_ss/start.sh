#!/usr/bin/env bash

cd /app/kohya_ss
export HF_HOME="/app"

nohup ./gui.sh --listen 0.0.0.0 --server_port 7860 --headless > /workspace/logs/kohya_ss.log 2>&1 &