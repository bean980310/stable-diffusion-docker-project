#!/bin/bash
set -e

apt-get update
apt-get install -y wget git libglib2.0-0 libgl1 curl

git clone https://github.com/facefusion/facefusion.git
cd /app/facefusion
git checkout tags/${FACEFUSION_VERSION}

pip3 install xformers

python3 install.py --onnxruntime cuda --skip-conda
pip3 cache purge