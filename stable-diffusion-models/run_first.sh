#!/usr/bin/env bash

mkdir -vp models/checkpoints/sd15 \
    models/checkpoints/sd2 \
    models/checkpoints/sdxl \
    models/checkpoints/pony \
    models/checkpoints/sd3 \
    models/checkpoints/upscale \
    models/checkpoints/flux1

mkdir -vp models/vae/sd15 \
    models/vae/sd2 \
    models/vae/sdxl \
    models/vae/sd3 \
    models/vae/flux1

mkdir -vp models/controlnet/sd15 \
    models/controlnet/sd2 \
    models/controlnet/sdxl \
    models/controlnet/sd3 \
    models/controlnet/flux1

mkdir -vp models/loras/sd15 \
    models/loras/sd2 \
    models/loras/sdxl \
    models/loras/pony \
    models/loras/sd3 \
    models/loras/flux1

mkdir -vp models/embeddings/sd15 \
    models/embeddings/sd2 \
    models/embeddings/sdxl \
    models/embeddings/sd3 \
    models/embeddings/flux1
