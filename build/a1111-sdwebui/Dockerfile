FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG WEBUI_VERSION
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name a1111-sdwebui python=3.10
ENV PATH=/opt/miniconda3/envs/a1111-sdwebui/bin:$PATH

RUN conda init bash && echo "conda activate a1111-sdwebui" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /app/stable-diffusion-webui
RUN git checkout tags/${WEBUI_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip install -r requirements_versions.txt && \
    pip install -r requirements.txt && \
    python -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "webui.sh", "-f" ]
