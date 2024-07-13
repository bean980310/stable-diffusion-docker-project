ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

# COPY --chmod=755 ./install.sh ./
# RUN /install.sh && rm /install.sh

# COPY ../../workspace/stable-diffusion/webui/config.json /stable-diffusion-webui
# COPY ../../workspace/stable-diffusion/webui/webui-user.json /stable-diffusion-webui

ARG INVOKEAI_VERSION
# WORKDIR /app/InvokeAI
# RUN pip3 install InvokeAI[xformers]==${INVOKEAI_VERSION} --use-pep517
# RUN pip3 cache purge

COPY --chmod=755 ./install.sh /
RUN /install.sh

WORKDIR /app

# COPY ../../workspace/InvokeAI/invokeai.yaml /InvokeAI

# RUN rm /start.sh
COPY --chmod=755 ./start.sh /

WORKDIR /app/data

RUN mkdir -vp /app/data/models \
    /app/data/embeddings

WORKDIR /app

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "invokeai-web", "--root", "/workspace/InvokeAI", ">", "/workspace/logs/invokeai.log", "2>&1", "&"]
CMD [ "/start.sh" ]
