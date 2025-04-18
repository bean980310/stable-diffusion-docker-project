FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG SDNEXT_COMMIT
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name vladmandic-sdnext python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/vladmandic-sdnext/bin:$PATH

RUN echo "conda activate vladmandic-sdnext" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN git clone https://github.com/vladmandic/automatic
COPY --chmod=755 ./install.py /app/automatic
WORKDIR /app/automatic
RUN git checkout ${SDNEXT_COMMIT} && \
    git submodule --quiet update --init --recursive && \
    git submodule --quiet sync --recursive

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    python install.py && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python3", "launch.py", "--listen", "--port 7860" ]