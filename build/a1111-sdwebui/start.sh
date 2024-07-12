#!/usr/bin/env bash
export PYTHONUNBUFFERED=1

cd /app/stable-diffusion-webui
nohup ./webui.sh -f > /app/webui.log 2>&1 &