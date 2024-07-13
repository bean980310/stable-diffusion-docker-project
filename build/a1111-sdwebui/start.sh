#!/bin/bash
set -e

cd /app/stable-diffusion-webui
nohup ./webui.sh -f > /app/webui.log 2>&1 &