FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG COMFYUI_VERSION
ARG WEBUI_VERSION
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name comfyui python=3.12 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH=/opt/miniconda3/envs/comfyui/bin:$PATH

RUN conda init && echo "conda activate comfyui" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc

RUN git clone https://github.com/comfyanonymous/ComfyUI.git
WORKDIR /app/ComfyUI
RUN git checkout tags/${COMFYUI_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip install -r requirements.txt && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python", "main.py"," --listen", "0.0.0.0", "--port", "8188" ]