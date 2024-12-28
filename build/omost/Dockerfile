ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG OMOST_COMMIT

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev ca-certificates python3-pip python3-venv python3-dev && \
    update-ca-certificates

RUN git clone https://github.com/lllyasviel/Omost.git
WORKDIR /app/Omost
RUN git checkout ${OMOST_COMMIT}

RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx
RUN pip3 install -U bitsandbytes

RUN pip install -r requirements.txt && \
    pip cache purge

CMD [ "python3" "gradio_app.py" ]