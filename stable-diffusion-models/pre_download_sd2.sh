#!/usr/bin/env bash

mkdir sd-models/Stable-diffusion/SD2

echo "Downloading SD 2.0 model"
wget -P sd-models/Stable-diffusion/SD2 -i ./download_link/download_ckpt_sd20.txt

echo "Downloading SD 2.1 model"
wget -P sd-models/Stable-diffusion/SD2 -i ./download_link/download_ckpt_sd21.txt