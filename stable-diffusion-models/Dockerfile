ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /data

RUN pip3 install -U huggingface huggingface_hub[cli]

COPY --chmod=755 . .

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]