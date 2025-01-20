FROM bean980310/conda:cu124 AS base
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Seoul \
    PYTHONUNBUFFERED=1 \
    SHELL=/bin/bash

RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

RUN apt-get update && \
    apt-get install -y --no-install-recommends git git-lfs wget curl build-essential pandoc gcc g++ netcat-openbsd jq && \
    apt-get install -y --no-install-recommends python3-dev python3-launchpadlib python3-pip python3-tk && \
    apt-get install -y --no-install-recommends ffmpeg libsm6 libxext6 && \
    apt-get install -y --no-install-recommends libgl1 libglib2.0-0 libxrender1 libnvrtc11.2 libgoogle-perftools4 libtcmalloc-minimal4 libcairo2 libcairo2-dev libgl1-mesa-glx && \
    apt-get install -y openssh-server nginx rsync && \
    update-ca-certificates && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/lists/* && \
    echo "ko_KR.UTF-8 UTF-8" > /etc/locale.gen

RUN pip install --no-cache-dir jupyter jupyterlab jupyterlab_widgets ipython ipykernel ipywidgets

# Start the container
CMD ["bin/bash"]