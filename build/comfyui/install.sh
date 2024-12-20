#!/bin/bash
set -e

# Clone the git repo of the Stable Diffusion Web UI by Automatic1111
# and set version
apt-get update
apt-get install -y wget git libgl1 libglib2.0-0

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd /app/stable-diffusion-webui
git checkout tags/${WEBUI_VERSION}

cd /app

# Clone the repo
git clone https://github.com/comfyanonymous/ComfyUI.git
cd /app/ComfyUI
git checkout tags/${COMFYUI_VERSION}

# Install requirements
# rm requirements.txt
# cp /app/requirements.txt /app/ComfyUI/requirements.txt
# rm /app/requirements.txt
pip3 install xformers
pip3 install -r requirements.txt
pip3 cache purge