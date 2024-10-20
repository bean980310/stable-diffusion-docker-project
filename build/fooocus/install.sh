#!/bin/bash
set -e

apt-get update
apt-get install -y wget git libgl1 libglib2.0-0 python-is-python3

git clone https://github.com/lllyasviel/Fooocus.git
cd /app/Fooocus
git checkout tags/${FOOOCUS_VERSION}

pip3 install -r requirements_versions.txt --extra-index-url https://download.pytorch.org/whl/cu124
sed '$d' launch.py > setup.py
python3 -m setup

pip3 cache purge