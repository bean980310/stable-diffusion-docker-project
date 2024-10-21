ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y wget git libglib2.0-0 libgl1 curl && \
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

WORKDIR /app/open-webui/backend

RUN pip3 install -r requirements.txt -U

WORKDIR /app

COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]