ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG FOOOCUS_VERSION

# RUN git clone https://github.com/lllyasviel/Fooocus.git && \
#     cd /Fooocus && \
#     git checkout ${FOOOCUS_VERSION}

# WORKDIR /app/Fooocus

# RUN pip3 install -r requirements_versions.txt --extra-index-url https://download.pytorch.org/whl/cu121 && \
#     sed '$d' launch.py > setup.py && \
#     python3 -m setup

COPY --chmod=755 ./install.sh ./
RUN ./install.sh

WORKDIR /app

COPY --chmod=755 ./start.sh ./

# RUN export HF_HOME="/app"

SHELL ["/bin/bash", "--login", "-c"]
# CMD ["nohup", "python3", "entry_with_update.py", "--listen", "--port", "7860", ">", "/app/fooocus.log", "2>&1", "&"]
CMD [ "./start.sh" ]