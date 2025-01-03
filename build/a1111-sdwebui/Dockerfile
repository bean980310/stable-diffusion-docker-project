FROM bean980310/conda:cu124 AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG WEBUI_VERSION=1.10.1
ARG TORCH_VERSION=2.5.1
ARG CUDA_VERSION=12.4
ARG INDEX_URL="https://download.pytorch.org/whl/cu124"
ARG XFORMERS_VERSION="0.0.28.post3"

RUN conda create -y --name a1111-sdwebui python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
ENV PATH=/opt/miniconda3/envs/a1111-sdwebui/bin:$PATH

RUN conda init && echo "conda activate a1111-sdwebui" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /app/stable-diffusion-webui
RUN git checkout tags/${WEBUI_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx
RUN pip install -r requirements_versions.txt
RUN pip install -U pip

RUN pip install -r requirements.txt
RUN python -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test
RUN pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "webui.sh", "-f" ]
