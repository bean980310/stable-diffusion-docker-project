ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG SDNEXT_COMMIT

RUN git clone https://github.com/vladmandic/automatic
WORKDIR /app/automatic
RUN git checkout ${SDNEXT_COMMIT}

RUN git submodule --quiet update --init --recursive
RUN git submodule --quiet sync --recursive

COPY --chmod=755 ./install.py /
RUN python3 install.py

WORKDIR /app

COPY --chmod=755 ./start.sh /

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]