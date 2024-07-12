#!/usr/bin/env bash
# set -e

# Create and activate venv
mkdir /InvokeAI
cd /InvokeAI

# Install InvokeAI
pip3 install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517