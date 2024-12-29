ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG FACEFUSION_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name facefusion python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/facefusion/bin:$PATH 

RUN echo "conda activate facefusion" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN git clone https://github.com/facefusion/facefusion.git
WORKDIR /app/facefusion
RUN git checkout tags/${FACEFUSION_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN python install.py --onnxruntime cuda --skip-conda
RUN pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python3", "run.py", "--execution-provides", "cuda" ]