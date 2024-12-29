ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG INVOKEAI_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name invokeai python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate invokeai

WORKDIR /app/InvokeAI

RUN pip install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517
RUN pip cache purge
RUN conda deactivate

RUN mkdir -vp /app/InvokeAI/models \
    /app/InvokeAI/outputs

RUN conda activate invokeai

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "invokeai-web", "--root", "/app/InvokeAI" ]
