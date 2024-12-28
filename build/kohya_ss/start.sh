#!/bin/bash
set -e

cd /app/kohya_ss
source venv/bin/activate

./gui.sh --listen 0.0.0.0 --server_port 7860 --headless