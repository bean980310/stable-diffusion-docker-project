#!/bin/bash
set -e

# Clone the git repo of the Stable Diffusion Web UI by Automatic1111
# and set version
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd /app/stable-diffusion-webui
git checkout tags/${WEBUI_VERSION}

# Install A1111
pip3 install -r requirements.txt
python3 -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test
pip3 cache purge