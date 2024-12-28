ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ENV TZ=Asia/Seoul

WORKDIR /app
ARG FOOOCUS_VERSION
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
RUN conda create -y --name fooocus python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate fooocus

RUN git clone https://github.com/lllyasviel/Fooocus.git
WORKDIR /app/Fooocus
RUN git checkout tags/${FOOOCUS_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN pip install -r requirements_versions.txt --extra-index-url ${INDEX_URL}

RUN pip cache purge
RUN conda deactivate
RUN conda activate fooocus

SHELL ["/bin/bash", "--login", "-c"]
CMD ["python3", "entry_with_update.py", "--listen", "--port", "7860"]