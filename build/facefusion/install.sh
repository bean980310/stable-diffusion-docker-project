#!/bin/bash
set -e

git clone https://github.com/facefusion/facefusion.git
cd /app/facefusion
git checkout tags/${FACEFUSION_VERSION}

python3.11 -m venv venv
source venv/bin/activate

pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
pip3 install tensorflow tensorboard tensorboardx
pip3 install -U bitsandbytes

python3 install.py --onnxruntime cuda --skip-conda
pip3 cache purge