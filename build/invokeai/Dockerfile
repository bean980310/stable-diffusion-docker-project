ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG INVOKEAI_VERSION
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev ca-certificates python3-pip && \
    update-ca-certificates
    
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv

COPY --chmod=755 ./install.sh ./
RUN ./install.sh

# ARG TORCH_VERSION
# ARG INDEX_URL
# ARG XFORMERS_VERSION
WORKDIR /app

# RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL} && \
#     pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} && \
#     pip3 cache purge

# COPY ../../workspace/InvokeAI/invokeai.yaml /InvokeAI

# RUN rm /start.sh
COPY --chmod=755 ./start.sh ./

WORKDIR /app/InvokeAI

RUN mkdir -vp /app/InvokeAI/models \
    /app/InvokeAI/outputs

WORKDIR /app

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "invokeai-web", "--root", "/workspace/InvokeAI", ">", "/workspace/logs/invokeai.log", "2>&1", "&"]
CMD [ "./start.sh" ]
