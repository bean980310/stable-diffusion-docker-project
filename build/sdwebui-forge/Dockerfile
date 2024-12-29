ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG FORGE_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda init
RUN conda create -y --name sdwebui-forge python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/sdwebui-forge/bin:$PATH

RUN echo "conda activate sdwebui-forge" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN git clone https://github.com/lllyasviel/stable-diffusion-webui-forge.git
WORKDIR /app/stable-diffusion-webui-forge
RUN git checkout ${FORGE_COMMIT}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN pip install -r requirements_versions.txt

# RUN if [ "${FORGE_VERSION}" != "previous" ]; then && \
#     git clone https://github.com/lllyasviel/forge-legacy-extensions.git extensions/forge-legacy-extensions && \
#     mv extensions/forge-legacy-extensions/sd_forge_hypertile extensions/sd_forge_hypertile && \
#     mv extensions/forge-legacy-extensions/sd_forge_svd extensions/sd_forge_svd && \
#     mv extensions/forge-legacy-extensions/sd_forge_z123 extensions/sd_forge_z123 && \
#     rm -rf extensions/forge-legacy-extensions && \
#     fi

# RUN pip install -r extensions-builtin/sd_forge_controlnet/requirements.txt && \
#     pip install -r extensions-builtin/forge_legacy_preprocessors/requirements.txt && \
#     pip install insightface && \
#     pip uninstall -y onnxruntime && \
#     pip install onnxruntime-gpu && \
#     pip install pydantic==1.10.15

RUN python -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test

RUN pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "webui.sh", "-f" ]