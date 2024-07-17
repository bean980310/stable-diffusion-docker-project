#!/usr/bin/env bash

mkdir -vp models/Stable-diffusion/SD15 \
    models/Stable-diffusion/SDXL \
    models/Stable-diffusion/Pony \
    models/Stable-diffusion/SD3 \
    models/Stable-diffusion/upscale

mkdir -vp models/VAE/SD15 \
    models/VAE/SDXL \
    models/VAE/SD3

mkdir -vp models/ControlNet/SD15 \
    models/ControlNet/SDXL \
    models/ControlNet/SD3

mkdir -vp models/Lora/SD15 \
    models/Lora/SDXL \
    models/Lora/Pony \
    models/Lora/SD3

mkdir -vp embeddings/SD15 \
    embeddings/SDXL \
    embeddings/SD3

# mkdir -vp models/ESRGAN \
#     models/RealESRGAN \
#     models/GFPGAN \
#     models/LDSR

# mkdir models/adetailer
# mkdir models/sam
# mkdir models/clip-interrogator
