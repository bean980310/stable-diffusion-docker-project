ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

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

ENV HF_HUB_ENABLE_HF_TRANSFER="1"

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y bash ca-certificates wget curl file git git-lfs inotify-tools jq libgl1 libglib2.0-0 libgl1 libxrender1 libnvrtc11.2 libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev lsof vim nano tmux openssh-server procps rsync sudo software-properties-common unzip p7zip-full zip pandoc net-tools netcat-openbsd && \
    apt-get install -y build-essential gcc g++ make cmake gfortran libblas-dev liblapack-dev && \ 
    apt-get install -y ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev libjpeg-dev libpng-dev libpostproc-dev libswresample-dev libswscale-dev libtiff-dev libv4l-dev libx264-dev libxext6 libxrender-dev libxvidcore-dev && \
    apt-get install -y libatlas-base-dev libffi-dev libhdf5-serial-dev libsm6 libssl-dev && \
    apt-get install -y python3-pip python3-tk python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh

ENV CONDA_DIR /opt/miniconda3

RUN /bin/bash /tmp/miniconda.sh -b -p /opt/miniconda3
ENV PATH /root/.local/bin:$CONDA_DIR/bin:$PATH

RUN conda init && echo "conda activate base" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm@latest

RUN apt apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN echo "ko_KR.UTF-8 UTF-8" > /etc/locale.gen

# Install Torch and xformers
ARG INDEX_URL
ARG TORCH_VERSION
ARG REQUIRED_CUDA_VERSION
ARG XFORMERS_VERSION

RUN conda install -y pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${REQUIRED_CUDA_VERSION} -c pytorch -c nvidia
RUN conda install -y jupyter jupyterlab jupyterlab_widgets ipykernel ipywidgets -c conda-forge
RUN conda install -y huggingface_hub transformers safetensors tokenizers datasets -c huggingface
RUN conda install -y diffusers accelerate sentence-transformers -c conda-forge 
RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION}
RUN pip install tensorflow tensorboard tensorboardx

RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x dotnet-install.sh
RUN ./dotnet-install.sh --channel 8.0 --runtime aspnetcore
RUN ./dotnet-install.sh --channel 8.0

RUN python -m ipykernel install --name "python3" --display-name "Python 3"
RUN pip cache purge

# Remove existing SSH host keys
RUN rm -f /etc/ssh/ssh_host_*

# Start the container
CMD ["bin/bash"]