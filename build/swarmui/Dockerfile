ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app
ARG SWARMUI_VERSION
ARG COMFYUI_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name swarmui python=3.12 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate swarmui

RUN git clone https://github.com/mcmonkeyprojects/SwarmUI.git
WORKDIR /app/SwarmUI
RUN checkout tags/${SWARMUI_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

WORKDIR /app/SwarmUI/dlbackend
RUN git clone https://github.com/comfyanonymous/ComfyUI.git
WORKDIR /app/SwarmUI/dlbackend/ComfyUI
RUN git checkout tags/${COMFYUI_VERSION}

RUN pip install -r requirements.txt
RUN pip cache purge
RUN conda deactivate

WORKDIR /app/SwarmUI
RUN conda activate swarmui

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "launch-linux.sh" ]