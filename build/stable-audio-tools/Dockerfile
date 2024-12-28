ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG STABLE_AUDIO_TOOLS_COMMIT
ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN apt-get update && \
    apt-get install -y wget git libglib2.0-0 libgl1 curl

RUN git clone https://github.com/Stability-AI/stable-audio-tools.git
WORKDIR /app/stable-audio-tools
RUN git checkout ${STABLE_AUDIO_TOOLS_COMMIT}

RUN pip3 install . && \
    pip3 install flash_attn && \
    pip3 cache purge
RUN mkdir /app/stable-audio-tools/models

WORKDIR /app
COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]