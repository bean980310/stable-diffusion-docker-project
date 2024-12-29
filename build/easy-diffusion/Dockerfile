ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app
ARG EASYDIFF_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN wget https://github.com/easydiffusion/easydiffusion/releases/download/${EASYDIFF_VERSION}/Easy-Diffusion-Linux.zip
RUN unzip Easy-Diffusion-Linux.zip
RUN rm Easy-Diffusion-Linux.zip

WORKDIR /app/easy-diffusion

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "start.sh" ]