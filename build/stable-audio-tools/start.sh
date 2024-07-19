#!/bin/bash
set -e

cd /app/stable-audio-tools
python3 run_gradio.py --model-config /app/stable-audio-tools/models/model_config.json --chpt-path /app/stable-audio-tools/models/model.safetensors