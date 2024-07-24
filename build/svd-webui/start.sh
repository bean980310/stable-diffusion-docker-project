#!/bin/bash
set -e

cd /app/svd-webui
python3 gradio_app.py --listen --port 7860