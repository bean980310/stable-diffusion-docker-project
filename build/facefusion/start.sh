#!/bin/bash
set -e

# export HF_HOME="/app"
# export GRADIO_SERVER_NAME="0.0.0.0"

cd /app/facefusion
source venv/bin/activate
python3 run.py --execution-provides cuda