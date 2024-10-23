#!/usr/bin/env bash

# pip3 install huggingface huggingface-hub

echo "Login to huggingface"

huggingface-cli login --token

echo "Downloading Flux1 model"

huggingface-cli download black-forest-labs/FLUX.1-dev flux1-dev.safetensors --local-dir=./models/checkpoints/flux1