ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app

ARG FACEFUSION_VERSION
# ENV GRADIO_SERVER_NAME=0.0.0.0

# RUN git clone https://github.com/facefusion/facefusion.git
# WORKDIR /app/facefusion
# RUN git checkout ${FACEFUSION_VERSION}

# RUN pip3 install -r requirements.txt
# RUN pip3 install -U onnxruntime-gpu
# RUN python3 install.py --skip-conda

COPY --chmod=755 ./install.sh ./
RUN ./install.sh

WORKDIR /app

COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]