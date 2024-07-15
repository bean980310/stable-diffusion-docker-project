ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG SDNEXT_COMMIT

COPY --chmod=755 ./install.sh /
COPY --chmod=755 ./install.py /

# RUN git clone https://github.com/vladmandic/automatic
# COPY --chmod=755 ./install.py /automatic
# WORKDIR /app/automatic
# RUN git checkout ${SDNEXT_COMMIT}

# RUN git submodule --quiet update --init --recursive
# RUN git submodule --quiet sync --recursive

# RUN python3 install.py
# RUN rm /install.py

RUN /install.sh

WORKDIR /app

COPY --chmod=755 ./start.sh /

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "/start.sh" ]