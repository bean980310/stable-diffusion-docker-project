#!/bin/bash
set -e

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd /app/stable-diffusion-webui
git checkout tags/${WEBUI_VERSION}

cd /app

# Clone the repo
git clone https://github.com/comfyanonymous/ComfyUI.git
cd /app/ComfyUI
git checkout tags/${COMFYUI_VERSION}

# Install requirements

pip install -r requirements.txt
pip cache purge