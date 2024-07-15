#!/bin/bash
set -e

git clone https://github.com/vladmandic/automatic
copy install.py /app/automatic/install.py
cd /app/automatic
git checkout ${SDNEXT_COMMIT}

git submodule --quiet update --init --recursive
git submodule --quiet sync --recursive

python3 install.py
rm install.py