ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG SWARMUI_VERSION
ARG COMFYUI_VERSION

COPY --chmod=755 ./install.* ./
RUN ./install.sh

WORKDIR /app

COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]