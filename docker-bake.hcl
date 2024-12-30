variable "BASE_IMAGE" {
    default = "bean980310/ubuntu-docker-conda:cu124"
}

variable "RELEASE" {
    default = "runpod"
}

variable "TORCH_VERSION" {
    default = "2.5.1"
}

variable "CUDA_VERSION" {
    default = "cu124"
}

variable "INDEX_URL" {
    default = "https://download.pytorch.org/whl/cu124"
}

variable "XFORMERS_VERSION" {
    default = "0.0.28.post3"
}
group "default" {
    targets=[
        "base",
        "stable-diffusion-webui",
        "kohya_ss",
        "comfyui",
        "invokeai",
        "fooocus",
        "sdnext",
        "swarmui",
        "facefusion"
    ]
}

target "base" {
    dockerfile="runpod/base/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
        logo = "container-template"
    }
    args={
        BASE_IMAGE="nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04"
        TORCH_VERSION="${TORCH_VERSION}"
        REQUIRED_CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/ubuntu-docker-conda:cu124-${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "stable-diffusion-webui" {
    dockerfile="runpod/a1111-sdwebui/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        WEBUI_VERSION="v1.10.1"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/stable-diffusion-webui:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "kohya_ss" {
    dockerfile="runpod/kohya_ss/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        KOHYA_VERSION="v24.1.4"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/kohya-ss:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "comfyui" {
    dockerfile="runpod/comfyui/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        COMFYUI_VERSION="v0.3.10"
        WEBUI_VERSION="v1.10.1"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/comfyui:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "invokeai" {
    dockerfile="runpod/invokeai/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        INVOKEAI_VERSION="v4.2.4"
        TORCH_VERSION="2.4.1"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="0.0.28.post1"
    }
    tags=["bean980310/invokeai:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "fooocus" {
    dockerfile="runpod/fooocus/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        FOOOCUS_VERSION="v2.5.5"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/fooocus:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "sdnext" {
    dockerfile="runpod/vladmandic-sdnext/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        SDNEXT_COMMIT="master"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/sd-next:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "swarmui" {
    dockerfile="runpod/swarmui/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        SWARMUI_VERSION="0.9.4-Beta"
        COMFYUI_VERSION="v0.3.10"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/swarmui:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "facefusion" {
    dockerfile="runpod/facefusion/Dockerfile"
    contexts = {
        scripts = "container-template"
        proxy = "container-template/proxy"
    }
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        FACEFUSION_VERSION="3.1.0"
        TORCH_VERSION="${TORCH_VERSION}"
        CUDA_VERSION="${CUDA_VERSION}"
        INDEX_URL="${INDEX_URL}"
        XFORMERS_VERSION="${XFORMERS_VERSION}"
    }
    tags=["bean980310/facefusion:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}