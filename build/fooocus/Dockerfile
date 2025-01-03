FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG FOOOCUS_VERSION
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name fooocus python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/fooocus/bin:$PATH

RUN echo "conda activate fooocus" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc

RUN git clone https://github.com/lllyasviel/Fooocus.git
WORKDIR /app/Fooocus
RUN git checkout tags/${FOOOCUS_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip install -r requirements_versions.txt --extra-index-url ${INDEX_URL} && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD ["python3", "entry_with_update.py", "--listen", "--port", "7860"]