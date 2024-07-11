FROM bean980310/ubuntu-docker:1.0.0-cuda-12.1.1-torch2.3.1 AS base

WORKDIR /
ARG WEBUI_VERSION

COPY --chmod=755 ./install.sh ./
RUN /install.sh && rm /install.sh

COPY ../../workspace/stable-diffusion/webui/config.json /stable-diffusion-webui
COPY ../../workspace/stable-diffusion/webui/webui-user.json /stable-diffusion-webui

RUN rm /start.sh
COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]