ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

# COPY --chmod=755 ./install.sh ./
# RUN /install.sh && rm /install.sh

# COPY ../../workspace/stable-diffusion/webui/config.json /stable-diffusion-webui
# COPY ../../workspace/stable-diffusion/webui/webui-user.json /stable-diffusion-webui

ARG INVOKEAI_VERSION
COPY --chmod=755 ./install.sh ./
RUN /install.sh && rm /install.sh

# COPY ../../workspace/InvokeAI/invokeai.yaml /InvokeAI

# RUN rm /start.sh
COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]