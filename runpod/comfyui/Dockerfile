ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG COMFYUI_VERSION
ARG WEBUI_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name comfyui python=3.12 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
ENV PATH=/opt/miniconda3/envs/comfyui/bin:$PATH

RUN conda init && echo "conda activate comfyui" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN conda install -y jupyter jupyterlab jupyterlab_widgets ipykernel ipywidgets -c conda-forge
RUN conda install -y huggingface_hub transformers safetensors tokenizers datasets -c huggingface
RUN conda install -y diffusers accelerate sentence-transformers -c conda-forge 

RUN git clone https://github.com/comfyanonymous/ComfyUI.git
WORKDIR /app/ComfyUI
RUN git checkout tags/${COMFYUI_VERSION}

RUN mkdir -vp /app/ComfyUI/models/checkpoints/sd15 && \
    mkdir -vp /app/ComfyUI/models/checkpoints/sdxl
RUN wget -P /app/ComfyUI/models/checkpoints/sd15 https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors
RUN wget -P /app/ComfyUI/models/checkpoints/sd15 https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt
RUN wget -P /app/ComfyUI/models/checkpoints/sd15 https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1B_orangemixs.safetensors
RUN wget -P /app/ComfyUI/models/checkpoints/sdxl https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors
RUN wget -P /app/ComfyUI/models/checkpoints/sdxl https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors
RUN wget -P /app/stable-diffusion-webui/models/Stable-diffusion/sdxl https://huggingface.co/cagliostrolab/animagine-xl-3.1/resolve/main/animagine-xl-3.1.safetensors

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx
RUN pip install -r requirements.txt

RUN git clone https://github.com/ltdrdata/ComfyUI-Manager.git custom_nodes/ComfyUI-Manager && \
    cd custom_nodes/ComfyUI-Manager && \
    pip install -r requirements.txt

RUN pip cache purge

# NGINX Proxy
COPY --from=proxy nginx.conf /etc/nginx/nginx.conf
COPY --from=proxy readme.html /usr/share/nginx/html/readme.html

# Copy the README.md
COPY README.md /usr/share/nginx/html/README.md

# Start Scripts
COPY --from=start pre_start.sh /pre_start.sh
COPY --from=scripts start.sh /
RUN chmod +x /pre_start.sh
RUN chmod +x /start.sh

# Welcome Message
COPY --from=logo runpod.txt /etc/runpod.txt
RUN echo 'cat /etc/runpod.txt' >> /root/.bashrc
RUN echo 'echo -e "\nFor detailed documentation and guides, please visit:\n\033[1;34mhttps://docs.runpod.io/\033[0m and \033[1;34mhttps://blog.runpod.io/\033[0m\n\n"' >> /root/.bashrc

ENV TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
ENV LD_PRELOAD="${TCMALLOC}"

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]