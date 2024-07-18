#!/usr/bin/env bash

echo "Downloading SD 1.5 model"
wget -P models/checkpoints/sd15 -i ./download_link/download_ckpt_sd15.txt

echo "Downloading SD XL model"
wget -P models/checkpoints/sdxl -i ./download_link/download_ckpt_sdxl.txt

echo "Downloading SD 1.5 VAE"
wget -P models/vae/sd15 https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors

echo "Downloading SD XL VAE"
wget -P models/vae/sdxl https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/sdxl_vae.safetensors

echo "Downloading SD 1.5 LoRA"
wget -O models/loras/sd15/lcm-lora-sdv1-5.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdv1-5/resolve/main/pytorch_lora_weights.safetensors

echo "Downloading SD XL LoRA"
wget -O models/loras/sdxl/lcm-lora-sdxl.safetensors https://huggingface.co/latent-consistency/lcm-lora-sdxl/resolve/main/pytorch_lora_weights.safetensors

echo "Downloading SD 1.5 embedding"
wget -P models/embeddings/sd15 -i ./download_link/download_embeddings_sd15.txt

echo "Downloading SD XL embedding"
wget -P models/embeddings/sdxl -i ./download_link/download_embeddings_sdxl.txt

echo "Downloading Upscale models"
wget -P models/upscale_models/ESRGAN -i ./download_link/download_upscale_esrgan.txt
wget -P models/upscale_models/RealESRGAN -i ./download_link/download_upscale_realesrgan.txt
wget -P models/upscale_models/LDSR --content-disposition -i ./download_link/download_upscale_ldsr.txt

echo "Downloading Face Restore models"
wget -P models/facerestore_models/GFPGAN -i ./download_link/download_facerestore_gfpgan.txt
wget -P models/facerestore_models/Codeformer -i ./download_link/download_facerestore_codeformer.txt

echo "Downloading Ultralytics model"
wget -P models/ultralytics/bbox -i ./download_link/download_ultralytics_bbox.txt
wget -P models/ultralytics/segm -i ./download_link/download_ultralytics_segm.txt

echo "Downloading Segment Anything model"
wget -P models/sams -i ./download_link/download_sams.txt
wget -P models/sams -i ./download_link/download_sams_hq.txt

echo "Downloading Clip Vision model"
wget -O models/clip_vision/ViT-L-14_openai.safetensors https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/model.safetensors
wget -O models/clip_vision/ViT-H-14_laion2b_s32b_b79k.safetensors https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/open_clip_pytorch_model.safetensors
wget -O models/clip_vision/ViT-bigG-14_laion2b_s39b_b160k.safetensors https://huggingface.co/laion/CLIP-ViT-bigG-14-laion2B-39B-b160k/resolve/main/open_clip_pytorch_model.safetensors