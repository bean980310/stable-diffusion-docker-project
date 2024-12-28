#!/bin/bash
set -e

git clone https://github.com/bmaltais/kohya_ss.git
cd /app/kohya_ss
git checkout tags/${KOHYA_VERSION}
git submodule update --init --recursive

python3.11 -m venv venv
source venv/bin/activate

pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
pip3 install tensorflow tensorboard tensorboardx
pip3 install -U bitsandbytes

pip3 install -U ninja pip setuptools wheel

pip3 install -r requirements_linux_docker.txt
pip3 install -r requirements.txt
pip3 cache purge
deactivate
