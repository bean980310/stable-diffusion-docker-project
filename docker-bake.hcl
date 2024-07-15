variable "BASE_IMAGE" {
    default = "bean980310/ubuntu-docker:1.0.2-cuda12.1.1-torch2.3.1"
}

variable "WEBUI_VERSION" {
    default = "v1.9.4"
}

variable "RELEASE" {
    default = "latest"
}

group "default" {
    targets=[
        "stable-diffusion-webui",
        "kohya_ss",
        "comfyui",
        "invokeai",
        "fooocus",
        "stable-diffusion-webui-forge"
    ]
}

target "stable-diffusion-webui" {
    context="build/a1111-sdwebui"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/stable-diffusion-webui:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "kohya_ss" {
    context="build/kohya_ss"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        KOHYA_VERSION="v24.1.4"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/kohya-ss:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "comfyui" {
    context="build/comfyui"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        COMFYUI_COMMIT="4ca9b9cc29fefaa899cba67d61a8252ae9f16c0d"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/comfyui:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "invokeai" {
    context="build/invokeai"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        INVOKEAI_VERSION="v4.2.4"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/invokeai:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "fooocus" {
    context="build/fooocus"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        FOOOCUS_VERSION="v2.4.3"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/fooocus:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "stable-diffusion-webui-forge" {
    context="build/sdwebui-forge"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        FORGE_COMMIT="bfee03d8d9415a925616f40ede030fe7a51cbcfd"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/stable-diffusion-webui-forge:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}

target "sdnext" {
    context="build/vladmandic-sdnext"
    dockerfile="Dockerfile"
    args={
        BASE_IMAGE="${BASE_IMAGE}"
        SDNEXT_COMMIT="2ec6e9eec481223b8abe50cb5165d5fd9be2d086"
        WEBUI_VERSION="${WEBUI_VERSION}"
    }
    tags=["bean980310/sd-next:${RELEASE}"]
    platforms=["linux/amd64"]
    annotations=["org.opencontainers.image.authors=bean980310"]
}