#!/bin/bash

# export PYTHONUNBUFFERED=1
# source /venv/bin/activate
# rsync -au --remove-source-files /ComfyUI/ /workspace/ComfyUI/
# ln -s /comfy-models/* /workspace/ComfyUI/models/checkpoints/

cd /app/ComfyUI
python main.py --listen --port 8188 &
