FROM bean980310/node:20 AS build

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ARG USE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
ARG USE_RERANKING_MODEL=""

ARG UID=0
ARG GID=0

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git && apt-get clean

ARG OPEN_WEBUI_VERSION

RUN git clone https://github.com/open-webui/open-webui.git

WORKDIR /app/open-webui

RUN git checkout tags/${OPEN_WEBUI_VERSION} && \
    cp -RPp .env.example .env && \
    npm install && \
    npm run build

FROM bean980310/base:main AS base

ARG TORCH_VERSION
ARG TORCH_CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

# Use args
ARG USE_EMBEDDING_MODEL
ARG USE_RERANKING_MODEL
ARG UID
ARG GID

## Basis ##
ENV ENV=prod \
    PORT=8080 \
    # pass build args to the build
    USE_EMBEDDING_MODEL_DOCKER=${USE_EMBEDDING_MODEL} \
    USE_RERANKING_MODEL_DOCKER=${USE_RERANKING_MODEL}

## Basis URL Config ##
ENV OLLAMA_BASE_URL="/ollama" \
    OPENAI_API_BASE_URL=""

## API Key and Security Config ##
ENV OPENAI_API_KEY="" \
    WEBUI_SECRET_KEY="" \
    SCARF_NO_ANALYTICS=true \
    DO_NOT_TRACK=true \
    ANONYMIZED_TELEMETRY=false

## whisper TTS model settings ##
ENV WHISPER_MODEL="base" \
    WHISPER_MODEL_DIR="/app/open-webui/backend/data/cache/whisper/models"

## RAG Embedding model settings ##
ENV RAG_EMBEDDING_MODEL="$USE_EMBEDDING_MODEL_DOCKER" \
    RAG_RERANKING_MODEL="$USE_RERANKING_MODEL_DOCKER" \
    SENTENCE_TRANSFORMERS_HOME="/app/open-webui/backend/data/cache/embedding/models"

## Tiktoken model settings ##
ENV TIKTOKEN_ENCODING_NAME="cl100k_base" \
    TIKTOKEN_CACHE_DIR="/app/backend/data/cache/tiktoken"

## Hugging Face download cache ##
ENV HF_HOME="/app/open-webui/backend/data/cache/embedding/models"

WORKDIR /app

RUN conda create -y --name open-webui python=3.11 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${TORCH_CUDA_VERSION} -c pytorch -c nvidia
ENV PATH /opt/miniconda3/envs/open-webui/bin:$PATH

RUN echo "conda activate open-webui" >> ~/.bashrc && \
    conda init bash && . ~/.bashrc

COPY --from=build /app/open-webui /app/open-webui

WORKDIR /app/open-webui/backend

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip install tensorflow && pip install tf_keras && \
    curl -fsSL https://ollama.com/install.sh | sh && \
    pip install -r requirements.txt -U && \
    python -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.environ['RAG_EMBEDDING_MODEL'], device='cpu')" && \
    python -c "import os; from faster_whisper import WhisperModel; WhisperModel(os.environ['WHISPER_MODEL'], device='cpu', compute_type='int8', download_root=os.environ['WHISPER_MODEL_DIR'])" && \
    python -c "import os; import tiktoken; tiktoken.get_encoding(os.environ['TIKTOKEN_ENCODING_NAME'])" && \
    pip cache purge

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "start.sh" ]