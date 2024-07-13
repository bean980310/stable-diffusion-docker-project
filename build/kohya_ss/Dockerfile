ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

# RUN apt update \
#     && apt install -y python3-launchpadlib \
#     && apt clean

ARG KOHYA_VERSION

# RUN git clone https://github.com/bmaltais/kohya_ss.git /kohya_ss
# WORKDIR /app/kohya_ss
# RUN git checkout ${KOHYA_VERSION}

# RUN pip3 install -U ninja pip setuptools wheel

# RUN pip3 install -r requirements_linux_docker.txt
# RUN pip3 install -r requirements.txt
# RUN pip3 cache purge
# WORKDIR /app

COPY --chmod=755 ./install.sh /
RUN /install.sh

WORKDIR /app

COPY ../../workspace/kohya_ss/accelerate.yaml /kohya_ss

# RUN rm /start.sh
COPY --chmod=755 ./start.sh /

# RUN export HF_HOME="/app"

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "./gui.sh", "--listen", "0.0.0.0", "--server_port", "7860", "--headless", ">", "/workspace/logs/kohya_ss.log", "2>&1", "&" ]
CMD [ "/start.sh" ]