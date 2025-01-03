FROM bean980310/conda:cu124 AS base
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Seoul \
    PYTHONUNBUFFERED=1 \
    SHELL=/bin/bash

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN conda install -y pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia && \
    conda install -y jupyter jupyterlab jupyterlab_widgets ipykernel ipywidgets -c conda-forge