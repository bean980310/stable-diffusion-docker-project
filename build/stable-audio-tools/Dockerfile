FROM bean980310/base:main AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app
ARG STABLE_AUDIO_TOOLS_COMMIT
ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name stable-audio-tools python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/stable-audio-tools/bin:$PATH

RUN echo "conda activate stable-audio-tools" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN git clone https://github.com/Stability-AI/stable-audio-tools.git
WORKDIR /app/stable-audio-tools
RUN git checkout ${STABLE_AUDIO_TOOLS_COMMIT}

RUN pip install . && \
    pip install flash_attn && \
    pip cache purge
RUN mkdir /app/stable-audio-tools/models

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "python", "run_gradio.py", "--model-config", "/app/stable-audio-tools/models/model_config.json", "--ckpt-path", "/app/stable-audio-tools/models/model.safetensors" ]