#!/usr/bin/env bash

echo "Login to huggingface"

huggingface-cli login --token

echo "Downloading Llama-3.2"

huggingface-cli download meta-llama/Llama-3.2-1B --include "original/*" --local-dir=./models/Llama3.2-1B
huggingface-cli download meta-llama/Llama-3.2-3B --include "original/*" --local-dir=./models/Llama3.2-3B
huggingface-cli download meta-llama/Llama-3.2-11B-Vision --include "original/*" --local-dir=./models/Llama-3.2-11B-Vision
huggingface-cli download meta-llama/Llama-3.2-90B-Vision --include "original/*" --local-dir=./models/Llama-3.2-90B-Vision