ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ENV TZ=Asia/Seoul

WORKDIR /app
ARG FORGE_VERSION
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
RUN conda create -y --name sdwebui-forge python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate sdwebui-forge

RUN git clone https://github.com/lllyasviel/stable-diffusion-webui-forge.git
WORKDIR /app/stable-diffusion-webui-forge
RUN git checkout ${FORGE_COMMIT}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN pip install -r requirements_versions.txt

RUN if [ "${FORGE_VERSION}" != "previous" ]; then && \
    git clone https://github.com/lllyasviel/forge-legacy-extensions.git extensions/forge-legacy-extensions && \
    mv extensions/forge-legacy-extensions/sd_forge_hypertile extensions/sd_forge_hypertile && \
    mv extensions/forge-legacy-extensions/sd_forge_svd extensions/sd_forge_svd && \
    mv extensions/forge-legacy-extensions/sd_forge_z123 extensions/sd_forge_z123 && \
    rm -rf extensions/forge-legacy-extensions && \
    fi

RUN pip install -r extensions-builtin/sd_forge_controlnet/requirements.txt && \
    pip install -r extensions-builtin/forge_legacy_preprocessors/requirements.txt && \
    pip install insightface && \
    pip uninstall -y onnxruntime && \
    pip install onnxruntime-gpu && \
    pip install pydantic==1.10.15

RUN python -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test

RUN pip cache purge
RUN conda deactivate
RUN conda activate sdwebui-forge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "webui.sh", "-f" ]