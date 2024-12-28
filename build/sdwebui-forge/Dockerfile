ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ENV TZ=Asia/Seoul

WORKDIR /app
ARG FORGE_VERSION
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3.11-dev

RUN git clone https://github.com/lllyasviel/stable-diffusion-webui-forge.git
WORKDIR /app/stable-diffusion-webui-forge
RUN git checkout ${FORGE_COMMIT}
RUN python3.11 -m venv venv && \
    source venv/bin/activate

RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx

RUN pip3 install -r requirements_versions.txt

RUN if [ "${FORGE_VERSION}" != "previous" ]; then && \
    git clone https://github.com/lllyasviel/forge-legacy-extensions.git extensions/forge-legacy-extensions && \
    mv extensions/forge-legacy-extensions/sd_forge_hypertile extensions/sd_forge_hypertile && \
    mv extensions/forge-legacy-extensions/sd_forge_svd extensions/sd_forge_svd && \
    mv extensions/forge-legacy-extensions/sd_forge_z123 extensions/sd_forge_z123 && \
    rm -rf extensions/forge-legacy-extensions && \
    fi

RUN pip3 install -r extensions-builtin/sd_forge_controlnet/requirements.txt && \
    pip3 install -r extensions-builtin/forge_legacy_preprocessors/requirements.txt && \
    pip3 install insightface && \
    pip3 uninstall -y onnxruntime && \
    pip3 install onnxruntime-gpu && \
    pip3 install pydantic==1.10.15

RUN python3 -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test

RUN pip3 cache purge
RUN deactivate
RUN source venv/bin/activate

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "webui.sh", "-f" ]