#!/bin/bash
set -e

apt-get update
apt-get install -y wget git libgl1 libglib2.0-0 python-is-python3

git clone https://github.com/vladmandic/automatic
cp ./install.py /app/automatic/install.py
cd /app/automatic
git checkout ${SDNEXT_COMMIT}

git submodule --quiet update --init --recursive
git submodule --quiet sync --recursive

python3 install.py
rm install.py
pip3 cache purge