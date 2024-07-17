#!/bin/bash
set -e

wget https://github.com/easydiffusion/easydiffusion/releases/download/${EASYDIFF_VERSION}/Easy-Diffusion-Linux.zip
unzip Easy-Diffusion-Linux.zip
rm Easy-Diffusion-Linux.zip

cd /app/easy-diffusion
sed -i 's/exec .\/scripts\/on_sd_start.sh/#exec .\/scripts\/on_sd_start.sh/g' /app/easy-diffusion/scripts/on_env_start.sh
./start.sh
sed -i 's/#exec .\/scripts\/on_sd_start.sh/#exec .\/scripts\/on_sd_start.sh/g' /app/easy-diffusion/scripts/on_env_start.sh
cp /app/easy-diffusion/scripts/on_sd_start.sh /app/easy-diffusion/scripts/on_sd_start.sh.ori
cp /app/easy-diffusion/scripts/on_env_start.sh /app/easy-diffusion/scripts/on_sd_start.sh.ori
head -n -5 /app/easy-diffusion/scripts/on_sd_start.sh.ori > /app/easy-diffusion/scripts/on_sd_start.sh
sed -i '11,43d' /app/easy-diffusion/scripts/on_env_start.sh
./start.sh
mv /app/easy-diffusion/scripts/on_sd_start.sh.ori /app/easy-diffusion/scripts/on_sd_start.sh
mv /app/easy-diffusion/scripts/on_env_start.sh.ori /app/easy-diffusion/scripts/on_env_start.sh
# echo '{"render_devices": "auto", "update_branch": "main", "ui": {"open_browser_on_start": false}, "net": {"listen_port": 9000,"listen_to_network": true}, "force_save_path: /app/easy-diffusion/outputs"}' > /app/easy-diffusion/scripts/config.json