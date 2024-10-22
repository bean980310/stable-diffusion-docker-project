#!/bin/bash
set -e

cd /app/audiocraft_plus
python3 app.py --server_port 7877 --listen 0.0.0.0