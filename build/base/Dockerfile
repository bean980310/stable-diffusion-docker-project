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

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y bash ca-certificates wget curl file git git-lfs\
    wget inotify-tools jq pkg-config && \
    apt-get install -y libgl1 libglib2.0-0 libgl1 libxrender1 libnvrtc11.2 libgoogle-perftools4 libtcmalloc-minimal4 libcairo2-dev && \
    apt-get install -y lsof vim nano tmux nginx openssh-server procps rsync sudo software-properties-common unzip p7zip-full zip pandoc net-tools netcat-openbsd && \
    apt-get install -y build-essential gcc g++ make cmake gfortran libblas-dev liblapack-dev && \ 
    apt-get install -y ffmpeg libavcodec-dev libavfilter-dev libavformat-dev libavutil-dev libjpeg-dev libpng-dev libpostproc-dev libswresample-dev libswscale-dev libtiff-dev libv4l-dev libx264-dev libxext6 libxrender-dev libxvidcore-dev && \
    apt-get install -y libatlas-base-dev libffi-dev libhdf5-serial-dev libsm6 libssl-dev && \
    apt-get install -y cifs-utils nfs-common zstd && \
    apt-get install -y python3-dev python3-launchpadlib python3-pip python3-tk python3-venv && \
    update-ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/lists/* && \
    echo "ko_KR.UTF-8 UTF-8" > /etc/locale.gen

ADD https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh /tmp/miniconda.sh

ENV CONDA_DIR /opt/miniconda3

RUN /bin/bash /tmp/miniconda.sh -b -p ${CONDA_DIR}
ENV PATH /root/.local/bin:$CONDA_DIR/bin:$PATH

RUN conda init && echo "conda activate base" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && apt-get clean && \
    npm install -g npm@latest

ADD https://dot.net/v1/dotnet-install.sh /dotnet-install.sh
RUN chmod +x dotnet-install.sh && \
    /dotnet-install.sh --channel 8.0 --runtime aspnetcore && \
    /dotnet-install.sh --channel 8.0

# Start the container
CMD ["bin/bash"]