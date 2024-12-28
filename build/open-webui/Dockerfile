ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ARG USE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
ARG USE_RERANKING_MODEL=""

ARG UID=0
ARG GID=0

ARG TORCH_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git curl wget build-essential pandoc gcc netcat-openbsd libglib2.0-0 libgl1 jq && \
    apt-get install -y python3-dev && \
    apt-get install -y ffmpeg libsm6 libxext6 && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-venv python3.11-dev python3-pip

ARG OPEN_WEBUI_VERSION

RUN git clone https://github.com/open-webui/open-webui.git

WORKDIR /app/open-webui

RUN git checkout tags/${OPEN_WEBUI_VERSION} && \
    cp -RPp .env.example .env && \
    npm install && \
    npm run build

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

## Hugging Face download cache ##
ENV HF_HOME="/app/open-webui/backend/data/cache/embedding/models"

WORKDIR /app/open-webui/backend

RUN python3.11 -m venv venv && \
    source venv/bin/activate

RUN  pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL} && \
    pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL} && \
    pip3 install tensorflow tensorboard tensorboardx && \
    pip3 install -U bitsandbytes

RUN curl -fsSL https://ollama.com/install.sh | sh && \
    pip3 install -r requirements.txt -U && \
    python -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.environ['RAG_EMBEDDING_MODEL'], device='cpu')" && \
    python -c "import os; from faster_whisper import WhisperModel; WhisperModel(os.environ['WHISPER_MODEL'], device='cpu', compute_type='int8', download_root=os.environ['WHISPER_MODEL_DIR'])"

RUN deactivate

WORKDIR /app/open-webui/backend
RUN source venv/bin/activate

CMD [ "bash", "start.sh" ]