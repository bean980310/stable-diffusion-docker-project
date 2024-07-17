#!/bin/bash
set -e

git clone https://github.com/facefusion/facefusion.git
cd /app/facefusion
git checkout ${FACEFUSION_VERSION}

python3 install.py --onnxruntime cuda-11.8 --skip-conda