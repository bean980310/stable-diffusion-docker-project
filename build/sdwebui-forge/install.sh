#!/bin/bash
set -e

apt-get update
apt-get install -y wget git libgl1 libglib2.0-0

git clone https://github.com/lllyasviel/stable-diffusion-webui-forge.git
cd /app/stable-diffusion-webui-forge
# git checkout ${FORGE_VERSION}
pip3 install -r requirements_versions.txt

if [ "${FORGE_VERSION}" != "previous" ]; then 
    git clone https://github.com/lllyasviel/forge-legacy-extensions.git extensions/forge-legacy-extensions
    mv extensions/forge-legacy-extensions/sd_forge_hypertile extensions/sd_forge_hypertile
    mv extensions/forge-legacy-extensions/sd_forge_svd extensions/sd_forge_svd
    mv extensions/forge-legacy-extensions/sd_forge_z123 extensions/sd_forge_z123
    rm -rf extensions/forge-legacy-extensions
fi

pip3 install -r extensions-builtin/sd_forge_controlnet/requirements.txt
pip3 install -r extensions-builtin/forge_legacy_preprocessors/requirements.txt
pip3 install insightface
pip3 uninstall -y onnxruntime
pip3 install onnxruntime-gpu
pip3 install pydantic==1.10.15
pip3 install xformers

python3 -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test

pip3 cache purge