#!/usr/bin/env bash

mkdir models/Stable-diffusion/SD2
mkdir models/VAE/SD2
mkdir models/ControlNet/SD2
mkdir models/Lora/SD2
mkdir embeddings/SD2

# echo "Downloading SD 2.0 model"
# wget -P models/Stable-diffusion/SD2 -i ./download_link/download_ckpt_sd20.txt

echo "Downloading SD 2.1 model"
wget -P models/Stable-diffusion/SD2 -i ./download_link/download_ckpt_sd21.txt