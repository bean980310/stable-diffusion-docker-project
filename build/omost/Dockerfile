ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG OMOST_COMMIT
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name omost python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate omost

RUN git clone https://github.com/lllyasviel/Omost.git
WORKDIR /app/Omost
RUN git checkout ${OMOST_COMMIT}

RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx

RUN pip install -r requirements.txt && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python3", "gradio_app.py" ]