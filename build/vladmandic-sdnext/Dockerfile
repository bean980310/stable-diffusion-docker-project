ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ENV TZ=Asia/Seoul

WORKDIR /app
ARG SDNEXT_COMMIT
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
RUN conda create -y --name vladmandic-sdnext python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate vladmandic-sdnext

RUN git clone https://github.com/vladmandic/automatic
COPY --chmod=755 ./install.py /automatic
WORKDIR /app/automatic
RUN git checkout ${SDNEXT_COMMIT}

RUN git submodule --quiet update --init --recursive
RUN git submodule --quiet sync --recursive

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN python install.py
RUN rm /install.py
RUN pip cache purge
RUN conda deactivate
RUN conda activate vladmandic-sdnext

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python3", "launch.py", "--listen", "--port 7860" ]