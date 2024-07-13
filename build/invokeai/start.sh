#!/bin/bash
set -e

cd /app/InvokeAI

nohup invokeai-web --root /workspace/InvokeAI > /workspace/logs/invokeai.log 2>&1 &