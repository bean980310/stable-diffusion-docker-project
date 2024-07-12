ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /app/stable-diffusion-webui
RUN git checkout tags/${WEBUI_VERSION}

ARG COMFYUI_COMMIT
WORKDIR /app

RUN git clone https://github.com/comfyanonymous/ComfyUI.git /ComfyUI
WORKDIR /app/ComfyUI
RUN git checkout ${COMFYUI_COMMIT}

RUN pip3 install -r requirements.txt
RUN pip3 cache purge

# ENV TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
RUN export LD_PRELOAD="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"

SHELL ["/bin/bash", "--login", "-c"]
# CMD [ "/start.sh" ]
CMD ["python3", "main.py"," --listen", "0.0.0.0", "--port", "8188" ,">" ,"/app/comfyui.log" ,"2>&1" ,"&"]