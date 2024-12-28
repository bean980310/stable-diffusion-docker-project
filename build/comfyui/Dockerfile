ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG COMFYUI_VERSION
ARG WEBUI_VERSION
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
# COPY ./requirements.txt ./
RUN ./install.sh

WORKDIR /app

COPY --chmod=755 ./start.sh ./

# ENV TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
# RUN export LD_PRELOAD="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "python3", "main.py"," --listen", "0.0.0.0", "--port", "8188" ,">" ,"/app/comfyui.log" ,"2>&1" ,"&"]
CMD [ "./start.sh" ]