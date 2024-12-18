ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

ARG USE_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
ARG USE_RERANKING_MODEL=""

ARG UID=0
ARG GID=0

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git curl wget build-essential pandoc gcc netcat-openbsd libglib2.0-0 libgl1 jq && \
    apt-get install -y python3-dev && \
    apt-get install -y ffmpeg libsm6 libxext6 && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

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

RUN curl -fsSL https://ollama.com/install.sh | sh && \
    pip3 install -r requirements.txt -U && \
    python -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.environ['RAG_EMBEDDING_MODEL'], device='cpu')" && \
    python -c "import os; from faster_whisper import WhisperModel; WhisperModel(os.environ['WHISPER_MODEL'], device='cpu', compute_type='int8', download_root=os.environ['WHISPER_MODEL_DIR'])"

WORKDIR /app

COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]