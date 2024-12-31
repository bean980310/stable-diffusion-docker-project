ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG WEBUI_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda create -y --name a1111-sdwebui python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia
ENV PATH=/opt/miniconda3/envs/a1111-sdwebui/bin:$PATH

RUN conda init && echo "conda activate a1111-sdwebui" >> ~/.bashrc
RUN conda init bash && . ~/.bashrc

RUN conda install -y jupyter jupyterlab jupyterlab_widgets ipykernel ipywidgets -c conda-forge
RUN conda install -y huggingface_hub transformers safetensors tokenizers datasets -c huggingface
RUN conda install -y diffusers accelerate sentence-transformers -c conda-forge 

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /app/stable-diffusion-webui
RUN git checkout tags/${WEBUI_VERSION}

RUN mkdir -vp /app/stable-diffusion-webui/models/Stable-diffusion/sd15 && \
    mkdir -vp /app/stable-diffusion-webui/models/Stable-diffusion/sdxl
RUN wget -P /app/stable-diffusion-webui/models/Stable-diffusion/sd15 https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors
RUN wget -P /app/stable-diffusion-webui/models/Stable-diffusion/sd15 https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3A1B_orangemixs.safetensors
RUN wget -P /app/stable-diffusion-webui/models/Stable-diffusion/sdxl https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors
RUN wget -P /app/stable-diffusion-webui/models/Stable-diffusion/sdxl https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx
RUN pip install -r requirements_versions.txt
RUN pip install -U pip

RUN pip install -r requirements.txt
RUN python -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test

# Install DeForum
RUN git clone https://github.com/deforum-art/sd-webui-deforum extensions/deforum && \
    cd extensions/deforum && \
    pip install basicsr && \
    pip install -r requirements.txt

# Install ControlNet
RUN git clone https://github.com/Mikubill/sd-webui-controlnet.git extensions/sd-webui-controlnet && \
    cd extensions/sd-webui-controlnet && \
    pip install -r requirements.txt

RUN pip cache purge

COPY --from=start cache-sd-model.py /app/stable-diffusion-webui/

RUN mkdir /app/downloader && git clone https://github.com/jjangga0214/sd-models-downloader.git /app/downloader

COPY --from=start relauncher.py /app/stable-diffusion-webui/
COPY --from=start webui-user.sh /app/stable-diffusion-webui/

COPY --from=start pre_start.sh /pre_start.sh
COPY --from=scripts start.sh /
RUN chmod +x /pre_start.sh
RUN chmod +x /start.sh

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]
