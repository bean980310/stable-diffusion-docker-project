#!/usr/bin/env bash

mkdir sd-models

mkdir sd-models/Stable-diffusion
mkdir sd-models/VAE
mkdir sd-models/ControlNet
mkdir sd-models/Lora
mkdir sd-models/embeddings
mkdir sd-models/ESRGAN
mkdir sd-models/RealESRGAN
mkdir sd-models/GFPGAN
mkdir sd-models/adetailer
mkdir sd-models/sam
mkdir sd-models/clip-interrogator

mkdir sd-models/Stable-diffusion/SD15
mkdir sd-models/Stable-diffusion/SDXL
mkdir sd-models/Stable-diffusion/Pony
mkdir sd-models/Stable-diffusion/upscale

mkdir sd-models/VAE/SD15
mkdir sd-models/VAE/SDXL

mkdir sd-models/ControlNet/SD15
mkdir sd-models/ControlNet/SDXL

mkdir sd-models/Lora/SD15
mkdir sd-models/Lora/SDXL
mkdir sd-models/Lora/Pony

mkdir sd-models/embeddings/SD15
mkdir sd-models/embeddings/SDXL

echo "Downloading SD 1.5 model"
wget -P sd-models/Stable-diffusion/SD15 -i ./download_ckpt_sd15.txt

echo "Downloading SD XL model"
wget -P sd-models/Stable-diffusion/SDXL -i ./download_ckpt_sdxl.txt

echo "Downloading SD 1.5 VAE"
wget -P sd-models/VAE/SD15 https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors

echo "Downloading SD XL VAE"
wget -P sd-models/VAE/SDXL https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/sdxl_vae.safetensors

echo "Downloading SD 1.5 LoRA"
wget -O sd-models/Lora/SD15/lcm-lora-sdv1-5.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdv1-5/resolve/main/pytorch_lora_weights.safetensors

echo "Downloading SD XL LoRA"
wget -O sd-models/Lora/SDXL/lcm-lora-sdxl.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdxl/resolve/main/pytorch_lora_weights.safetensors

echo "Downloading SD 1.5 embedding"
wget -P sd-models/embeddings/SD15 -i ./download_embeddings_sd15.txt

echo "Downloading SD XL embedding"
wget -P sd-models/embeddings/SDXL -i ./download_embeddings_sdxl.txt

echo "Downloading Upscaler models"
wget -P sd-models/ESRGAN -i ./download_esrgan.txt
wget -P sd-models/RealESRGAN -i ./download_realesrgan.txt
wget -P sd-models/GFPGAN -i ./download_gfpgan.txt

echo "Downloading adetailer model"
wget -P sd-models/adetailer -i ./download_adetailer.txt

echo "Downloading Segment Anything model"
wget -P sd-models/sam -i ./download_sam.txt
wget -P sd-models/sam -i ./download_sam_hq.txt

echo "Downloading Clip Vision model"
wget -O sd-models/clip-interrogator/ViT-L-14_openai.safetensors https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/model.safetensors
wget -O sd-models/clip-interrogator/ViT-H-14_laion2b_s32b_b79k.safetensors https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/open_clip_pytorch_model.safetensors
wget -O sd-models/clip-interrogator/ViT-bigG-14_laion2b_s39b_b160k.safetensors https://huggingface.co/laion/CLIP-ViT-bigG-14-laion2B-39B-b160k/resolve/main/open_clip_pytorch_model.safetensors