FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG INVOKEAI_VERSION
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name invokeai python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/invokeai/bin:$PATH

RUN echo "conda activate invokeai" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc

WORKDIR /app/InvokeAI

RUN pip install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517 && \
    pip cache purge && \
    mkdir -vp /app/InvokeAI/models \
    /app/InvokeAI/outputs

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "invokeai-web", "--root", "/app/InvokeAI" ]
