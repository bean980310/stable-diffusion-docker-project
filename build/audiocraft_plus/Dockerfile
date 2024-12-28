ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app

RUN apt-get update
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev && \
    update-ca-certificates

RUN git clone https://github.com/GrandaddyShmax/audiocraft_plus.git
WORKDIR /app/audiocraft_plus

RUN python3 -m venv venv && \
    source venv/bin/activate

RUN pip3 install -U pip wheel

RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx

RUN pip3 install -U bitsandbytes

RUN pip3 install -r requirements.txt
RUN pip3 install -e .
RUN pip3 purge

RUN deactivate
RUN source venv/bin/activate

CMD [ "python3", "app.py", "--server_port 7877", "--listen 0.0.0.0" ]
