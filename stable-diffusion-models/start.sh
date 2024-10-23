#!/bin/bash
set -e

./run_first.sh
./download.sh
./download_alt.sh
./download_sd2.sh
./download_sd3.sh
./download_flux1.sh
./download_controlnet.sh
./download_controlnet_sd2.sh
./download_lora.sh