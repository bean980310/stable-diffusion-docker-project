ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG FOOOCUS_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name fooocus python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
RUN conda activate fooocus

RUN ln -s ~/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate fooocus" >> ~/.bashrc

RUN git clone https://github.com/lllyasviel/Fooocus.git
WORKDIR /app/Fooocus
RUN git checkout tags/${FOOOCUS_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx

RUN pip install -r requirements_versions.txt --extra-index-url ${INDEX_URL}

RUN pip cache purge
RUN conda deactivate
RUN conda activate fooocus

SHELL ["/bin/bash", "--login", "-c"]
CMD ["python3", "entry_with_update.py", "--listen", "--port", "7860"]