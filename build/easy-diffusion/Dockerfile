ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG EASYDIFF_VERSION
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3.11-dev

RUN wget https://github.com/easydiffusion/easydiffusion/releases/download/${EASYDIFF_VERSION}/Easy-Diffusion-Linux.zip
RUN unzip Easy-Diffusion-Linux.zip
RUN rm Easy-Diffusion-Linux.zip

WORKDIR /app/easy-diffusion

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "start.sh" ]