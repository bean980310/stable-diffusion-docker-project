#!/bin/bash
set -e

apt-get update && apt-get upgrade -y
apt-get install -y software-properties-common bash wget curl git libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev ca-certificates python3-pip python3-launchpadlib
update-ca-certificates
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install -y python3.11
update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1
update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.11 1
update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.11 1
pip3 install -U bitsandbytes

# Install torch and xformers
pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
pip3 install tensorflow tensorboard tensorboardx

git clone https://github.com/facefusion/facefusion.git
cd /app/facefusion
git checkout tags/${FACEFUSION_VERSION}

python3 install.py --onnxruntime cuda --skip-conda
pip3 cache purge