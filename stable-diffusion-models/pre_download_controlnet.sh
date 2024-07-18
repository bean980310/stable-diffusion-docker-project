#!/usr/bin/env bash

echo "Downloading ControlNet model for SD 1.5"
wget -P models/controlnet/sd15 -i ./download_link/download_controlnet_sd15.txt

echo "Downloading ControlNet model for SD XL"
wget -P models/controlnet/sdxl -i ./download_link/download_controlnet_sdxl_stabilityai.txt

wget -O models/controlnet/sdxl/controlnet-canny-sdxl-1.0_fp16.safetensors https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.fp16.safetensors
wget -O models/controlnet/sdxl/controlnet-depth-sdxl-1.0_fp16.safetensors https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0/resolve/main/diffusion_pytorch_model.fp16.safetensors

# wget -P models/controlnet/sdxl -i ./download_link/download_controlnet_sdxl_kohya-ss.txt

wget -O models/controlnet/sdxl/controlnet-inpaint-dreamer-sdxl.safetensors https://huggingface.co/destitech/controlnet-inpaint-dreamer-sdxl/resolve/main/v2/diffusion_pytorch_model.fp16.safetensors

wget -P models/controlnet/sdxl -i ./download_link/download_controlnet_sdxl_kataragi.txt

# wget -P models/controlnet/sdxl -i ./download_link/download_controlnet_sdxl_bdsqlsz.txt

wget -O models/controlnet/sdxl/controlnet-union-sdxl-1.0_promax.safetensors https://huggingface.co/xinsir/controlnet-union-sdxl-1.0/resolve/main/diffusion_pytorch_model_promax.safetensors

wget -P models/controlnet/sdxl https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/resolve/main/control-lora-openposeXL2-rank256.safetensors