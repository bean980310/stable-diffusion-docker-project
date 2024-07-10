
# Stage 1: Base Image
ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

RUN mkdir -p /sd-models

RUN mkdir /sd-models/Stable-diffusion
RUN mkdir /sd-models/VAE
RUN mkdir /sd-models/ControlNet
RUN mkdir /sd-models/Lora
RUN mkdir /sd-models/embeddings
RUN mkdir /sd-models/ESRGAN
RUN mkdir /sd-models/RealESRGAN
RUN mkdir /sd-models/GFPGAN
RUN mkdir /sd-models/LDSR
RUN mkdir /sd-models/adetailer
RUN mkdir /sd-models/sam
RUN mkdir /sd-models/clip-interrogator

RUN mkdir /sd-models/Stable-diffusion/SD15
RUN mkdir /sd-models/Stable-diffusion/SDXL
RUN mkdir /sd-models/Stable-diffusion/Pony
RUN mkdir /sd-models/Stable-diffusion/SD3
RUN mkdir /sd-models/Stable-diffusion/upscale

RUN mkdir /sd-models/VAE/SD15
RUN mkdir /sd-models/VAE/SDXL

RUN mkdir /sd-models/ControlNet/SD15
RUN mkdir /sd-models/ControlNet/SDXL

RUN mkdir /sd-models/Lora/SD15
RUN mkdir /sd-models/Lora/SDXL
RUN mkdir /sd-models/Lora/Pony

RUN mkdir /sd-models/embeddings/SD15
RUN mkdir /sd-models/embeddings/SDXL

# Add SDXL models and VAE
# These need to already have been downloaded:
#   wget https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors
#   wget https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors
#   wget https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/sdxl_vae.safetensors
# COPY v1-5-pruned-emaonly.safetensors /sd-models/v1-5-pruned-emaonly.safetensors
# COPY sd-v1-5-inpainting.ckpt /sd-models/sd-v1-5-inpainting.ckpt
# COPY vae-ft-mse-840000-ema-pruned.safetensors /sd-models/vae-ft-mse-840000-ema-pruned.safetensors
# COPY sd_xl_base_1.0.safetensors /sd-models/sd_xl_base_1.0.safetensors
# COPY sd_xl_refiner_1.0.safetensors /sd-models/sd_xl_refiner_1.0.safetensors
# COPY sdxl_vae.safetensors /sd-models/sdxl_vae.safetensors

COPY sd-models/Stable-diffusion/SD15/* /sd-models/Stable-diffusion/SD15/
COPY sd-models/Stable-diffusion/SDXL/* /sd-models/Stable-diffusion/SDXL/
COPY sd-models/Stable-diffusion/Pony/* /sd-models/Stable-diffusion/Pony/
COPY sd-models/Stable-diffusion/SD3/* /sd-models/Stable-diffusion/SD3/
COPY sd-models/Stable-diffusion/upscale/* /sd-models/Stable-diffusion/upscale/

COPY sd-models/VAE/SD15/* /sd-models/VAE/SD15/
COPY sd-models/VAE/SDXL/* /sd-models/VAE/SDXL/

COPY sd-models/ControlNet/SD15/* /sd-models/ControlNet/SD15/
COPY sd-models/ControlNet/SDXL/* /sd-models/ControlNet/SDXL/

COPY sd-models/Lora/SD15/* /sd-models/Lora/SD15/
COPY sd-models/Lora/SDXL/* /sd-models/Lora/SDXL/
COPY sd-models/Lora/Pony/* /sd-models/Lora/Pony/

COPY sd-models/embeddings/SD15/* /sd-models/embeddings/SD15/
COPY sd-models/embeddings/SDXL/* /sd-models/embeddings/SDXL/

COPY sd-models/ESRGAN/* /sd-models/ESRGAN/
COPY sd-models/RealESRGAN/* /sd-models/RealESRGAN/
COPY sd-models/GFPGAN/* /sd-models/GFPGAN/
COPY sd-models/LDSR/* /sd-models/LDSR/

COPY sd-models/adetailer/* /sd-models/adetailer/

COPY sd-models/sam/* /sd-models/sam/

COPY sd-models/clip-interrogator/* /sd-models/clip-interrogator/

WORKDIR /

# Start the container
SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]
