ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ENV TZ=Asia/Seoul

WORKDIR /app
ARG SWARMUI_VERSION
ARG COMFYUI_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates

RUN wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
RUN bash Anaconda3-2024.10-1-Linux-x86_64.sh -b -p ./anaconda3
RUN source ./anaconda3/bin/activate && conda init --all
RUN conda config --set auto_activate_base true
RUN conda create -y --name swarmui python=3.12 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate swarmui

RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x dotnet-install.sh
RUN ./dotnet-install.sh --channel 7.0
RUN ./dotnet-install.sh --channel 8.0

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