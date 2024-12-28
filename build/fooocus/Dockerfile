ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ENV TZ=Asia/Seoul

WORKDIR /app
ARG FOOOCUS_VERSION
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3.11-dev

RUN git clone https://github.com/lllyasviel/Fooocus.git
WORKDIR /app/Fooocus
RUN git checkout tags/${FOOOCUS_VERSION}

RUN python3.11 -m venv venv && \
    source venv/bin/activate

RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx

RUN pip3 install -r requirements_versions.txt --extra-index-url https://download.pytorch.org/whl/cu124

RUN pip3 cache purge
RUN source venv/bin/deactivate
RUN source venv/bin/activate

SHELL ["/bin/bash", "--login", "-c"]
CMD ["python3", "entry_with_update.py", "--listen", "--port", "7860"]