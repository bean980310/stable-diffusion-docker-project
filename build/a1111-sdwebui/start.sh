#!/usr/bin/env bash
export PYTHONUNBUFFERED=1

cd /stable-diffusion-webui
nohup ./webui.sh -f > /webui.log 2>&1 &