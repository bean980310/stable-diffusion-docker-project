ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app/svd-webui
RUN git clone https://github.com/Stability-AI/generative-models.git

WORKDIR /app.svd-webui/generative-models
RUN pip3 install -r requirements/pt2.txt && \
    pip3 install . && \
    pip3 install -e git+https://github.com/Stability-AI/datapipelines.git@main#egg=sdata

WORKDIR /app/svd-webui
RUN mkdir -p ./scripts/util/detection
RUN ln -s ./generative-models/scripts/util/detection/p_head_v1.npz ./scripts/util/detection/p_head_v1.npz
RUN ln -s ./generative-models/scripts/util/detection/w_head_v1.npz ./scripts/util/detection/w_head_v1.npz

RUN mkdir -p ./scripts/sampling
COPY ./scripts/sampling/simple_video_sample.py ./scripts/sampling/simple_video_sample.py

RUN mkdir -p ./scripts/sampling/configs
RUN ln -s ./generative-models/scripts/sampling/configs/svd.yaml ./scripts/scripts/sampling/configs/svd.yaml
RUN ln -s ./generative-models/scripts/sampling/configs/svd_xt.yaml ./scripts/scripts/sampling/configs/svd_xt.yaml
RUN ln -s ./generative-models/scripts/sampling/configs/svd_xt_1_1.yaml ./scripts/scripts/sampling/configs/svd_xt_1_1.yaml
RUN ln -s ./generative-models/scripts/sampling/configs/svd_image_decoder.yaml ./scripts/scripts/sampling/configs/svd_image_decoder.yaml
RUN ln -s ./generative-models/scripts/sampling/configs/svd_xt_image_decoder.yaml ./scripts/scripts/sampling/configs/svd_xt_image_decoder.yaml
RUN ln -s ./generative-models/scripts/sampling/configs/sv3d_u.yaml ./scripts/sampling/configs/sv3d_u.yaml
RUN ln -s ./generative-models/scripts/sampling/configs/sv3d_p.yaml ./scripts/sampling/configs/sv3d_p.yaml

# RUN mkdir -p ./sgm
# RUN ln -s ./generative-models/sgm ./sgm

RUN mkdir -p ./configs/interface
RUN ln -s ./generative-models/configs/interface/svd.yaml ./configs/interface/svd.yaml
RUN ln -s ./generative-models/configs/interface/svd_image_decoder.yaml ./configs/interface/svd_image_decoder.yaml
RUN ls -s ./generative-models/configs/interface/sv3d_u.yaml ./configs/interface/sv3d_u.yaml
RUN ls -s ./generative-models/configs/interface/sv3d_p.yaml ./configs/interface/sv3d_p.yaml

RUN mkdir -p ./models/checkpoints