#!/usr/bin/env bash

echo "Login to huggingface"

huggingface-cli login --token

echo "Downloading SVD model"

huggingface-cli download stabilityai/stable-video-diffusion-img2vid svd.safetensors --local-dir=./models
huggingface-cli download stabilityai/stable-video-diffusion-img2vid-xt svd_xt.safetensors --local-dir=./models
huggingface-cli download stabilityai/stable-video-diffusion-img2vid-xt-1-1 svd_xt_1_1.safetensors --local-dir=./models
huggingface-cli download stabilityai/stable-video-diffusion-img2vid svd_image_decoder.safetensors --local-dir=./models
huggingface-cli download stabilityai/stable-video-diffusion-img2vid-xt svd_xt_image_decoder.safetensors --local-dir=./models