ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

COPY --chmod=755 ./install.sh ./
RUN /install.sh && rm /install.sh

# COPY ../../workspace/stable-diffusion-webui/config.json /stable-diffusion-webui
# COPY ../../workspace/stable-diffusion-webui/webui-user.sh /stable-diffusion-webui

# RUN rm /start.sh
COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]