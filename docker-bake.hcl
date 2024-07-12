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
        "invokeai"
    ]
}

target "stable-diffusion-webui" {
    context="./"
    dockerfile="Dockerfile.a1111"
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
        COMFYUI_COMMIT="8e012043a9d0af3979bbe2cea8dc1ec7768f9d88"
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
