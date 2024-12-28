#!/bin/bash
set -e

# Create and activate venv
mkdir /app/InvokeAI
cd /app/InvokeAI

python3.11 -m venv venv
source venv/bin/activate

pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
pip3 install tensorflow tensorboard tensorboardx
pip3 install -U bitsandbytes

# Install InvokeAI
pip3 install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517
pip3 cache purge
deactivate