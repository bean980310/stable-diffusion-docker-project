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

ENV HF_HOME="/app/.cache/huggingface/"
ENV HF_DATASETS_CACHE="/app/.cache/huggingface/datasets/"
ENV DEFAULT_HF_METRICS_CACHE="/app/.cache/huggingface/metrics/"
ENV DEFAULT_HF_MODULES_CACHE="/app/.cache/huggingface/modules/"
ENV HUGGINGFACE_HUB_CACHE="/app/.cache/huggingface/hub/"
ENV HUGGINGFACE_ASSETS_CACHE="/app/.cache/huggingface/assets/"

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update && \
    apt-get install -y --no-install-recommends bash ca-certificates wget curl file git git-lfs\
    wget inotify-tools jq pkg-config && \
    apt-get install -y --no-install-recommends libgl1 libglib2.0-0 libgl1 libxrender1 libnvrtc11.2 libgoogle-perftools4 libtcmalloc-minimal4 libcairo2-dev && \
    apt-get install -y --no-install-recommends lsof vim nano tmux nginx openssh-server procps rsync sudo software-properties-common unzip p7zip-full zip pandoc net-tools netcat-openbsd && \
    apt-get install -y --no-install-recommends build-essential gcc g++ make cmake gfortran libblas-dev liblapack-dev && \ 
    apt-get install -y --no-install-recommends ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev libjpeg-dev libpng-dev libpostproc-dev libswresample-dev libswscale-dev libtiff-dev libv4l-dev libx264-dev libxext6 libxrender-dev libxvidcore-dev && \
    apt-get install -y --no-install-recommends libatlas-base-dev libffi-dev libhdf5-serial-dev libsm6 libssl-dev && \
    apt-get install -y --no-install-recommends cifs-utils nfs-common zstd && \
    apt-get install -y --no-install-recommends python3-dev python3-launchpadlib python3-pip python3-tk python3-venv && \
    update-ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/lists/* && \
    echo "ko_KR.UTF-8 UTF-8" > /etc/locale.gen

RUN conda install -y pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia && \
    conda install -y jupyter jupyterlab jupyterlab_widgets ipykernel ipywidgets -c conda-forge && \
    conda install -y huggingface_hub transformers safetensors tokenizers datasets -c huggingface && \
    conda install -y diffusers accelerate -c conda-forge && \
    conda clean -all
    
RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip install tensorflow tensorboard tensorboardx && \
    pip install peft gradio && \
    pip cache purge

# Start the container
CMD ["bin/bash"]