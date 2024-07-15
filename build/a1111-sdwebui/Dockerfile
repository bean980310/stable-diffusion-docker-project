ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

# RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
# WORKDIR /app/stable-diffusion-webui
# RUN git checkout tags/${WEBUI_VERSION}

# RUN pip3 install tensorflow[and-cuda]

# RUN pip3 install -r requirements_versions.txt
# RUN python3 -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test
# RUN pip3 cache purge

COPY --chmod=755 ./install.sh ./
RUN ./install.sh

WORKDIR /app

# COPY ../../workspace/stable-diffusion-webui/config.json /stable-diffusion-webui
# COPY ../../workspace/stable-diffusion-webui/webui-user.sh /stable-diffusion-webui

COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "./webui.sh", "-f", ">", "/app/webui.log", "2>&1", "&"]
CMD [ "./start.sh" ]
