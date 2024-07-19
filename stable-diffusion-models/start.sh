#!/bin/bash
set -e

./run_first.sh
./pre_download.sh
./pre_download_alt.sh
./pre_download_sd2.sh
./pre_download_sd3.sh
# ./pre_download_svd.sh
./pre_download_controlnet.sh
./pre_download_controlnet_sd2.sh
./pre_download_lora.sh