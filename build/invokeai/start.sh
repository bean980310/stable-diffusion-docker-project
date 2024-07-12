#!/usr/bin/env bash

mkdir /app/data

mkdir -vp /app/data/models \
    /app/data/embeddings

cd /app/InvokeAI

nohup invokeai-web --root /workspace/InvokeAI > /workspace/logs/invokeai.log 2>&1 &