ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG EASYDIFF_VERSION

RUN apt-get update && \
    apt-get install -y wget git libgl1 libglib2.0-0 unzip && \
    apt-get clean

RUN wget https://github.com/easydiffusion/easydiffusion/releases/download/${EASYDIFF_VERSION}/Easy-Diffusion-Linux.zip
RUN unzip Easy-Diffusion-Linux.zip
RUN rm Easy-Diffusion-Linux.zip

WORKDIR /app/easy-diffusion

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]