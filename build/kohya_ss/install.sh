#!/usr/bin/env bash
set -e

apt install -y python3-launchpadlib
RUN apt clean

git clone https://github.com/bmaltais/kohya_ss.git /kohya_ss
cd /kohya_ss
git checkout ${KOHYA_VERSION}

pip3 install -U ninja pip setuptools wheel

pip3 install -r requirements_linux_docker.txt
pip3 install -r requirements.txt
pip3 cache purge
