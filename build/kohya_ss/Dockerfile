FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG KOHYA_VERSION
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name kohya_ss python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/kohya_ss/bin:$PATH

RUN echo "conda activate kohya_ss" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc
    
RUN git clone https://github.com/bmaltais/kohya_ss.git
WORKDIR /app/kohya_ss
RUN git checkout tags/${KOHYA_VERSION} && \
    git submodule update --init --recursive

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip install -U ninja pip setuptools wheel && \
    pip install -r requirements_linux_docker.txt && \
    pip install -r requirements.txt && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python", "kohya_gui.py", "--listen", "0.0.0.0", "--server_port", "7860", "--headless" ]