ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y wget git libglib2.0-0 libgl1 curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest