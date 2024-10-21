ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG OMOST_COMMIT

RUN apt-get update && \
    apt-get install -y wget git libglib2.0-0 libgl1 curl

RUN git clone https://github.com/lllyasviel/Omost.git
WORKDIR /app/Omost
RUN git checkout ${OMOST_COMMIT}
RUN pip install -r requirements.txt && \
    pip cache purge

WORKDIR /app

COPY --chmod=755 ./start.sh ./

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]