#!/bin/bash
set -e

git clone https://github.com/lllyasviel/stable-diffusion-webui-forge.git
cd /app/stable-diffusion-webui-forge
git checkout ${FORGE_VERSION}
pip3 install -r requirements_versions.txt

if [ "${FORGE_VERSION}" != previous ]; then git clone https://github.com/lllyasviel/forge-legacy-extensions.git extensions

pip3 install -r extensions-builtin/sd_forge_controlnet/requirements.txt
pip3 install -r extensions-builtin/forge_legacy_preprocessors/requirements.txt
pip3 install insightface
pip3 uninstall -y onnxruntime
pip3 install onnxruntime-gpu
pip3 install pydantic==1.10.15

python3 -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test