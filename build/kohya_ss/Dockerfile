ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app

ARG KOHYA_VERSION
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates
    
RUN git clone https://github.com/bmaltais/kohya_ss.git
WORKDIR /app/kohya_ss
RUN checkout tags/${KOHYA_VERSION}
RUN submodule update --init --recursive

RUN python3 -m venv venv && \
    source venv/bin/activate

RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx
RUN pip3 install -U bitsandbytes

RUN pip3 install -U ninja pip setuptools wheel

RUN pip3 install -r requirements_linux_docker.txt
RUN pip3 install -r requirements.txt
RUN pip3 cache purge
RUN deactivate

RUN source venv/bin/activate

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "gui.sh", "--listen", "0.0.0.0", "--server_port", "7860", "--headless" ]