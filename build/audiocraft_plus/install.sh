#!/bin/bash
set -e

apt-get update
apt-get install -y \
    wget \
    curl \
    git \
    build-essential \
    pkg-config \
    ffmpeg \
    libnvrtc11.2 \
    libtcmalloc-minimal4

pip3 install -U pip wheel

git clone https://github.com/GrandaddyShmax/audiocraft_plus.git
cd /app/audiocraft_plus

pip3 install -r requirements.txt
pip3 install -e .