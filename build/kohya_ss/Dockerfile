ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app

ARG KOHYA_VERSION
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev ca-certificates python3-pip && \
    update-ca-certificates python3-launchpadlib
    
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv

COPY --chmod=755 ./install.sh ./
RUN ./install.sh

WORKDIR /app

# COPY ../../workspace/kohya_ss/accelerate.yaml /kohya_ss

# RUN rm /start.sh
COPY --chmod=755 ./start.sh ./

# RUN export HF_HOME="/app"

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "./gui.sh", "--listen", "0.0.0.0", "--server_port", "7860", "--headless", ">", "/workspace/logs/kohya_ss.log", "2>&1", "&" ]
CMD [ "./start.sh" ]