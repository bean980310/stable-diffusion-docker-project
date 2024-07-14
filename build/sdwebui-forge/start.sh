#!/bin/bash
set -e

export HF_HOME="/app"

cd /app/stable-diffusion-webui-forge
nohup ./webui.sh -f > /app/forge.log 2>&1 &