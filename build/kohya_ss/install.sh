#!/bin/bash
set -e

apt-get update
apt-get install -y wget git libgl1 libglib2.0-0
apt-get install -y python3-launchpadlib

git clone https://github.com/bmaltais/kohya_ss.git
cd /app/kohya_ss
git checkout tags/${KOHYA_VERSION}
git submodule update --init --recursive

pip3 install -U ninja pip setuptools wheel

pip3 install -r requirements_linux_docker.txt
pip3 install -r requirements.txt
pip3 cache purge
