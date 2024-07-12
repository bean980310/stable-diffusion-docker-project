variable "REGISTRY" {
    default = "docker.io"
}

variable "REGISTRY_USER" {
    default = "bean980310"
}

variable "RELEASE" {
    default = "1.1.0"
}

variable "CU_VERSION" {
    default = "121"
}

variable "BASE_IMAGE_REPOSITORY" {
    default = "bean980310/ubuntu-docker"
}

variable "BASE_IMAGE_VERSION" {
    default = "1.0.0"
}

variable "CUDA_VERSION" {
    default = "12.1.1"
}

variable "TORCH_VERSION" {
    default = "2.3.1"
}

target "default" {
    dockerfile = "Dockerfile"
    tags = ["${REGISTRY}/${REGISTRY_USER}/stable-diffusion-docker-base:${RELEASE}-cuda${CUDA_VERSION}-torch${TORCH_VERSION}"]
    args = {
        RELEASE = "${RELEASE}"
        BASE_IMAGE = "${BASE_IMAGE_REPOSITORY}:${BASE_IMAGE_VERSION}-cuda${CUDA_VERSION}-torch${TORCH_VERSION}"
    }
}
