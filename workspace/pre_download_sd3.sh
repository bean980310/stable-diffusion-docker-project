#!/usr/bin/env bash

pip3 install huggingface huggingface-hub

echo "Login to huggingface"

huggingface-cli login

echo "Downloading SD 3 model"

# cd /workspace/stable-diffusion-webui/models/Stable-diffusion

mkdir sd-models/Stable-diffusion/SD3

huggingface-cli download stabilityai/stable-diffusion-3-medium sd3_medium.safetensors --local-dir=./sd-models/Stable-diffusion/SD3
huggingface-cli download stabilityai/stable-diffusion-3-medium sd3_medium_incl_clips.safetensors --local-dir=./sd-models/Stable-diffusion/SD3
huggingface-cli download stabilityai/stable-diffusion-3-medium sd3_medium_incl_clips_t5xxlfp8.safetensors --local-dir=./sd-models/Stable-diffusion/SD3
huggingface-cli download stabilityai/stable-diffusion-3-medium sd3_medium_incl_clips_t5xxlfp16.safetensors --local-dir=./sd-models/Stable-diffusion/SD3