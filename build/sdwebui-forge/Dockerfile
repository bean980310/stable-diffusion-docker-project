ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG FORGE_COMMIT

# RUN git clone https://github.com/lllyasviel/stable-diffusion-webui-forge.git
# WORKDIR /app/stable-diffusion-webui-forge
# RUN git checkout ${FORGE_COMMIT}
# RUN pip3 install -r requirements_versions.txt

# RUN pip3 install -r extensions-builtin/sd_forge_controlnet/requirements.txt && \
#     pip3 install -r extensions-builtin/forge_legacy_preprocessors/requirements.txt && \
#     pip3 install insightface && \
#     pip3 uninstall -y onnxruntime && \
#     pip3 install onnxruntime-gpu && \
#     pip3 install pydantic==1.10.15

# RUN python3 -c "from launch import prepare_environment; prepare_environment()" --skip-torch-cuda-test

COPY --chmod=755 ./install.sh ./
RUN ./install.sh

WORKDIR /app
COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]