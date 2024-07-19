#!/usr/bin/env bash

echo "Downloading SD 1.5 Lora"
wget -P models/loras/sd15 --content-disposition -i ./download_link/download_lora_sd15.txt

echo "Downloading SD XL Lora"
wget -P models/loras/sdxl --content-disposition -i ./download_link/download_lora_sdxl.txt

echo "Downloading Pony Lora"
wget -P models/loras/pony --content-disposition -i ./download_link/download_lora_pony.txt