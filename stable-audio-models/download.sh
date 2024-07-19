#!/usr/bin/env bash

echo "Login to huggingface"

huggingface-cli login --token

echo "Downloading Stable Audio model"

huggingface-cli download stabilityai/stable-audio-open-1.0 model.safetensors --local-dir=./models
huggingface-cli download stabilityai/stable-audio-open-1.0 model_config.json --local-dir=./models