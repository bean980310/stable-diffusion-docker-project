#!/usr/bin/env bash

echo "Downloading ControlNet model for SD 1.5"
wget -P sd-models/ControlNet/SD15 -i ./download_controlnet_sd15.txt

echo "Downloading ControlNet model for SD XL"
wget -P sd-models/ControlNet/SDXL -i ./download_controlnet_sdxl_stabilityai.txt

wget -O sd-models/ControlNet/SDXL/controlnet-canny-sdxl-1.0_fp16.safetensors https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.fp16.safetensors
wget -O sd-models/ControlNet/SDXL/controlnet-depth-sdxl-1.0_fp16.safetensors https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0/resolve/main/diffusion_pytorch_model.fp16.safetensors

# wget -P sd-models/ControlNet/SDXL -i ./download_controlnet_sdxl_kohya-ss.txt

wget  -O sd-models/ControlNet/SDXL/controlnet-inpaint-dreamer-sdxl.safetensors https://huggingface.co/destitech/controlnet-inpaint-dreamer-sdxl/resolve/main/v2/diffusion_pytorch_model.fp16.safetensors

wget -P sd-models/ControlNet/SDXL -i ./download_controlnet_sdxl_kataragi.txt

# wget -P sd-models/ControlNet/SDXL -i ./download_controlnet_sdxl_bdsqlsz.txt