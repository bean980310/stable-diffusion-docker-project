#!/usr/bin/env bash

# mkdir sd-models

# mkdir -vp sd-models/Stable-diffusion \
#     sd-models/Stable-diffusion/SD15 \
#     sd-models/Stable-diffusion/SDXL \
#     sd-models/Stable-diffusion/Pony \
#     sd-models/Stable-diffusion/SD3 \
#     sd-models/Stable-diffusion/upscale

# mkdir -vp sd-models/VAE \
#     sd-models/VAE/SD15 \
#     sd-models/VAE/SDXL \
#     sd-models/VAE/SD3

# mkdir -vp sd-models/ControlNet \
#     sd-models/ControlNet/SD15 \
#     sd-models/ControlNet/SDXL \
#     sd-models/ControlNet/SD3

# mkdir -vp sd-models/Lora \
#     sd-models/Lora/SD15 \
#     sd-models/Lora/SDXL \
#     sd-models/Lora/Pony \
#     sd-models/Lora/SD3

# mkdir -vp embeddings \
#     embeddings/SD15 \
#     embeddings/SDXL \
#     embeddings/SD3

# mkdir -vp sd-models/ESRGAN \
#     sd-models/RealESRGAN \
#     sd-models/GFPGAN \
#     sd-models/LDSR
    
mkdir sd-models/adetailer
mkdir sd-models/sam
mkdir sd-models/clip-interrogator

echo "Downloading SD 1.5 model"
wget -P sd-models/Stable-diffusion/SD15 -i ./download_link/download_ckpt_sd15.txt

echo "Downloading SD XL model"
wget -P sd-models/Stable-diffusion/SDXL -i ./download_link/download_ckpt_sdxl.txt

echo "Downloading SD 1.5 VAE"
wget -P sd-models/VAE/SD15 https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors

echo "Downloading SD XL VAE"
wget -P sd-models/VAE/SDXL https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/sdxl_vae.safetensors

echo "Downloading SD 1.5 LoRA"
wget -O sd-models/Lora/SD15/lcm-lora-sdv1-5.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdv1-5/resolve/main/pytorch_lora_weights.safetensors

echo "Downloading SD XL LoRA"
wget -O sd-models/Lora/SDXL/lcm-lora-sdxl.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdxl/resolve/main/pytorch_lora_weights.safetensors

echo "Downloading SD 1.5 embedding"
wget -P embeddings/SD15 -i ./download_link/download_embeddings_sd15.txt

echo "Downloading SD XL embedding"
wget -P embeddings/SDXL -i ./download_link/download_embeddings_sdxl.txt

echo "Downloading Upscaler models"
wget -P sd-models/ESRGAN -i ./download_link/download_esrgan.txt
wget -P sd-models/RealESRGAN -i ./download_link/download_realesrgan.txt
wget -P sd-models/GFPGAN -i ./download_link/download_gfpgan.txt
wget -P sd-models/LDSR --content-disposition -i ./download_link/download_ldsr.txt

echo "Downloading adetailer model"
wget -P sd-models/adetailer -i ./download_link/download_adetailer.txt

echo "Downloading Segment Anything model"
wget -P sd-models/sam -i ./download_link/download_sam.txt
wget -P sd-models/sam -i ./download_link/download_sam_hq.txt

echo "Downloading Clip Vision model"
wget -O sd-models/clip-interrogator/ViT-L-14_openai.safetensors https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/model.safetensors
wget -O sd-models/clip-interrogator/ViT-H-14_laion2b_s32b_b79k.safetensors https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/open_clip_pytorch_model.safetensors
wget -O sd-models/clip-interrogator/ViT-bigG-14_laion2b_s39b_b160k.safetensors https://huggingface.co/laion/CLIP-ViT-bigG-14-laion2B-39B-b160k/resolve/main/open_clip_pytorch_model.safetensors