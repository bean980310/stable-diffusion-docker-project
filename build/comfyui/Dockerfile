ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

# COPY --chmod=755 ../a1111-sdwebui/install.sh ./
# RUN /install.sh && rm /install.sh

# COPY ../../workspace/stable-diffusion-webui/config.json /stable-diffusion-webui
# COPY ../../workspace/stable-diffusion-webui/webui-user.json /stable-diffusion-webui

ARG COMFYUI_COMMIT

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /app/stable-diffusion-webui
RUN git checkout tags/${WEBUI_VERSION}

WORKDIR /app

# COPY --chmod=755 ./install.sh ./
# RUN /install.sh && rm /install.sh

RUN git clone https://github.com/comfyanonymous/ComfyUI.git /ComfyUI
WORKDIR /app/ComfyUI
RUN git checkout ${COMFYUI_COMMIT}

RUN pip3 install -r requirements.txt
RUN pip3 cache purge

# COPY ../../workspace/ComfyUI/extra_model_paths.yaml /ComfyUI

# RUN rm /start.sh
# COPY --chmod=755 ./start.sh ./

# ENV TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
RUN export LD_PRELOAD="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"

SHELL ["/bin/bash", "--login", "-c"]
# CMD [ "/start.sh" ]
CMD ["python3", "main.py"," --listen", "0.0.0.0", "--port", "8188" ,">" ,"/app/comfyui.log" ,"2>&1" ,"&"]