ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG WEBUI_VERSION

# COPY --chmod=755 ../a1111-sdwebui/install.sh ./
# RUN /install.sh && rm /install.sh

# COPY ../../workspace/stable-diffusion-webui/config.json /stable-diffusion-webui
# COPY ../../workspace/stable-diffusion-webui/webui-user.json /stable-diffusion-webui

# ARG COMFYUI_COMMIT

# COPY --chmod=755 ./install.sh ./
# RUN /install.sh && rm /install.sh

# COPY ../../workspace/ComfyUI/extra_model_paths.yaml /ComfyUI

ARG KOHYA_VERSION
# WORKDIR /app

COPY --chmod=755 ./install.sh ./
RUN /install_kohya.sh && rm /install_kohya.sh

# COPY ../../workspace/kohya_ss/accelerate.yaml ./

# RUN rm /start.sh
COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]