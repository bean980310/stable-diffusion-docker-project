ARG BASE_IMAGE
FROM ${BASE_IMAGE} AS base

WORKDIR /app
ARG EASYDIFF_VERSION
RUN wget https://github.com/easydiffusion/easydiffusion/releases/download/${EASYDIFF_VERSION}/Easy-Diffusion-Linux.zip
RUN unzip Easy-Diffusion-Linux.zip
RUN rm Easy-Diffusion-Linux.zip

WORKDIR /app/easy-diffusion
RUN sed -i 's/exec .\/scripts\/on_sd_start.sh/#exec .\/scripts\/on_sd_start.sh/g' /app/easy-diffusion/scripts/on_env_start.sh
RUN ./start.sh
RUN sed -i 's/#exec .\/scripts\/on_sd_start.sh/#exec .\/scripts\/on_sd_start.sh/g' /app/easy-diffusion/scripts/on_env_start.sh
RUN cp /app/easy-diffusion/scripts/on_sd_start.sh /app/easy-diffusion/scripts/on_sd_start.sh.ori
RUN cp /app/easy-diffusion/scripts/on_env_start.sh /app/easy-diffusion/scripts/on_sd_start.sh.ori
RUN head -n -5 /app/easy-diffusion/scripts/on_sd_start.sh.ori > /app/easy-diffusion/scripts/on_sd_start.sh
RUN sed -i '11,43d' /app/easy-diffusion/scripts/on_env_start.sh
RUN ./start.sh
RUN mv /app/easy-diffusion/scripts/on_sd_start.sh.ori /app/easy-diffusion/scripts/on_sd_start.sh
RUN mv /app/easy-diffusion/scripts/on_env_start.sh.ori /app/easy-diffusion/scripts/on_env_start.sh
RUN echo '{"render_devices": "auto", "update_branch": "main", "ui": {"open_browser_on_start": false}, "net": {"listen_port": 9000,"listen_to_network": true}}' > /app/easy-diffusion/scripts/config.json 

SHELL ["/bin/bash", "--login", "-c"]
CMD [ "./start.sh" ]