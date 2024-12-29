ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG SDNEXT_COMMIT
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name vladmandic-sdnext python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate vladmandic-sdnext

RUN ln -s ~/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate vladmandic-sdnext" >> ~/.bashrc

RUN git clone https://github.com/vladmandic/automatic
COPY --chmod=755 ./install.py /automatic
WORKDIR /app/automatic
RUN git checkout ${SDNEXT_COMMIT}

RUN git submodule --quiet update --init --recursive
RUN git submodule --quiet sync --recursive

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN python install.py
RUN rm /install.py
RUN pip cache purge
RUN conda deactivate
RUN conda activate vladmandic-sdnext

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python3", "launch.py", "--listen", "--port 7860" ]