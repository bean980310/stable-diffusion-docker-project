ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG SWARMUI_VERSION
ARG COMFYUI_VERSION

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common bash wget curl git build-essential libgl1 libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 ffmpeg libgoogle-perftools4 libtcmalloc-minimal4 pkg-config libcairo2-dev libnvrtc11.2 ca-certificates python3-pip python3-venv python3-dev python3-launchpadlib && \
    update-ca-certificates

RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x dotnet-install.sh
RUN ./dotnet-install.sh --channel 7.0
RUN ./dotnet-install.sh --channel 8.0

RUN git clone https://github.com/mcmonkeyprojects/SwarmUI.git
WORKDIR /app/SwarmUI
RUN checkout tags/${SWARMUI_VERSION}

RUN python3 -m venv venv && \
    source venv/bin/activate

RUN pip3 install --no-cache-dir torch==${TORCH_VERSION} torchvision torchaudio --index-url ${INDEX_URL}
RUN pip3 install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip3 install tensorflow tensorboard tensorboardx
RUN pip3 install -U bitsandbytes

WORKDIR /app/SwarmUI/dlbackend
RUN git clone https://github.com/comfyanonymous/ComfyUI.git
WORKDIR /app/SwarmUI/dlbackend/ComfyUI
RUN git checkout tags/${COMFYUI_VERSION}

RUN pip3 install -r requirements.txt
RUN pip3 cache purge
RUN deactivate

WORKDIR /app/SwarmUI
RUN source venv/bin/activate

COPY --chmod=755 ./start.sh ./

CMD [ "bash", "launch-linux.sh" ]