#!/bin/bash
set -e

# Create and activate venv
mkdir /app/InvokeAI
cd /app/InvokeAI

# Install InvokeAI
pip3 install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517