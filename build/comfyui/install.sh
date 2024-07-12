#!/usr/bin/env bash
set -e

# Clone the git repo of the Stable Diffusion Web UI by Automatic1111
# and set version
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd /stable-diffusion-webui
git checkout tags/${WEBUI_VERSION}

# Clone the repo
git clone https://github.com/comfyanonymous/ComfyUI.git /ComfyUI
cd /ComfyUI
git checkout ${COMFYUI_COMMIT}

# Install requirements
pip3 install -r requirements.txt
pip3 cache purge