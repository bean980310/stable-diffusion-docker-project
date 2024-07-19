#!/bin/bash
set -e

# wget https://dot.net/v1/dotnet-install.sh
# chmod +x dotnet-install.sh
# ./dotnet-install.sh --channel 7.0
# ./dotnet-install.sh --channel 8.0

git clone https://github.com/mcmonkeyprojects/SwarmUI.git
cd /app/SwarmUI
git checkout tags/${SWARMUI_VERSION}

mkdir dlbackend

cd /app/SwarmUI/dlbackend
git clone https://github.com/comfyanonymous/ComfyUI.git
cd /app/SwarmUI/dlbackend/ComfyUI
git checkout tags/${COMFYUI_VERSION}

pip3 install -r requirements.txt