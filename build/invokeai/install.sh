#!/bin/bash
set -e

apt-get update
apt-get install -y wget git libglib2.0-0 libgl1-mesa-glx

# Create and activate venv
mkdir /app/InvokeAI
cd /app/InvokeAI

# Install InvokeAI
pip3 install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517
pip3 cache purge