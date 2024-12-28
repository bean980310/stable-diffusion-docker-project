ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG EASYDIFF_VERSION

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib unzip && \
    update-ca-certificates

RUN wget https://github.com/easydiffusion/easydiffusion/releases/download/${EASYDIFF_VERSION}/Easy-Diffusion-Linux.zip
RUN unzip Easy-Diffusion-Linux.zip
RUN rm Easy-Diffusion-Linux.zip

WORKDIR /app/easy-diffusion

CMD [ "bash", "start.sh" ]