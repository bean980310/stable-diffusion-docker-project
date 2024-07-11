#!/usr/bin/env bash

cd /workspace/ComfyUI

TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
export LD_PRELOAD="${TCMALLOC}"

python3 main.py --listen 0.0.0.0 --port 8188 > /workspace/logs/comfyui.log 2>&1 &