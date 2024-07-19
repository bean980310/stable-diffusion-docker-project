#!/usr/bin/env bash

echo "Login to huggingface"

huggingface-cli login --token

echo "Downloading SVD model"

huggingface-cli download stabilityai/stable-video-diffusion-img2vid-xt-1-1 svd_xt_1_1.safetensors --local-dir=./models