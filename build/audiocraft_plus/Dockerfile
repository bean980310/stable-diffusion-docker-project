ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name audiocraft_plus python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
ENV PATH=/opt/miniconda3/envs/audiocraft_plus/bin:$PATH

RUN echo "conda activate audiocraft_plus" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN git clone https://github.com/GrandaddyShmax/audiocraft_plus.git
WORKDIR /app/audiocraft_plus

RUN python3.11 -m venv venv && \
    source venv/bin/activate

RUN pip install -U pip wheel

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN pip install -r requirements.txt
RUN pip install -e .
RUN pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python3", "app.py", "--server_port 7877", "--listen 0.0.0.0" ]
