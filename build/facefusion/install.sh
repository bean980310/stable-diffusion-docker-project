#!/bin/bash
set -e

git clone https://github.com/facefusion/facefusion.git
cd /app/facefusion
git checkout ${FACEFUSION_VERSION}

pip3 install -r requirements.txt
pip3 install -U onnxruntime-gpu
python3 install.py --skip-conda