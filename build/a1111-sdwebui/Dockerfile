ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /app

ARG WEBUI_VERSION
ARG TORCH_VERSION
ARG CUDA_VERSION
ARG INDEX_URL
ARG XFORMERS_VERSION

RUN conda init
RUN conda create -y --name a1111-sdwebui python=3.10 pytorch==${TORCH_VERSION} torchvision torchaudio pytorch-cuda=${CUDA_VERSION} -c pytorch -c nvidia


RUN echo $"\
# >>> conda initialize >>> \n\
# !! Contents within this block are managed by 'conda init' !! \n\
__conda_setup="$('/root/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)" \n\
if [ $? -eq 0 ]; then \n\
    eval "$__conda_setup" \n\
else \n\
    if [ -f "/root/miniconda3/etc/profile.d/conda.sh" ]; then \n\
        . "/root/miniconda3/etc/profile.d/conda.sh" \n\
    else \n\
        export PATH="/root/miniconda3/bin:$PATH" \n\
    fi \n\
fi \n\
unset __conda_setup \n\
" \n\
# <<< conda initialize <<<"
>> ~/.bashrc
RUN source ~/.bashrc
RUN ln -s ~/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate a1111-sdwebui" >> ~/.bashrc
RUN source ~/.bashrc
RUN conda activate a1111-sdwebui

RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
WORKDIR /app/stable-diffusion-webui
RUN git checkout tags/${WEBUI_VERSION}

RUN pip install --no-cache-dir xformers==${XFORMERS_VERSION} --index-url ${INDEX_URL}
RUN pip install tensorflow tensorboard tensorboardx
RUN pip install -r requirements_versions.txt

RUN pip install -r requirements.txt
RUN python -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test
RUN pip cache purge 

RUN conda deactivate
RUN conda activate a1111-sdwebui

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "bash", "webui.sh", "-f" ]
