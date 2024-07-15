#!/bin/bash
set -e

cd /app/kohya_ss
export HF_HOME="/app"

./gui.sh --listen 0.0.0.0 --server_port 7860 --headless