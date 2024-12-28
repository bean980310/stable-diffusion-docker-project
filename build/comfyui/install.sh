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

python3 -m venv venv
source venv/bin/activate

pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
pip3 install tensorflow tensorboard tensorboardx
pip3 install -U bitsandbytes

# Install requirements

pip3 install -r requirements.txt
pip3 cache purge
deactivate