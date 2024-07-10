#!/usr/bin/env bash

echo "Downloading SD 1.5 based model"
wget -P sd-models/Stable-diffusion/SD15 --content-disposition -i ./download_ckpt_sd15_based.txt

echo "Downloading SD XL based model"
wget -P sd-models/Stable-diffusion/SDXL --content-disposition -i ./download_ckpt_sdxl_based.txt

echo "Downloading Pony based model"
wget -P sd-models/Stable-diffusion/Pony --content-disposition -i ./download_ckpt_pony_based.txt

echo "Downloading SD x4 Upscale model"
wget -P sd-models/Stable-diffusion/upscale https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler/resolve/main/x4-upscaler-ema.safetensors

echo "Downloading SD 1.5 based VAE"
wget -P sd-models/VAE/SD15 -i ./download_vae_sd15_based.txt