
"group": {
    "default": {
      "targets": [
        "comfyui",
        "invokeai",
        "stable-diffusion-webui",
        "kohya_ss"
      ]
    }
  },
  "target": {
    "comfyui": {
      "context": "build/comfyui",
      "dockerfile": "Dockerfile",
      "args": {
        "BASE_IMAGE": "bean980310/ubuntu-docker:1.0.2-cuda-12.1.1-torch2.3.1",
        "COMFYUI_COMMIT": "8e012043a9d0af3979bbe2cea8dc1ec7768f9d88",
        "WEBUI_VERSION": "v1.9.4"
      },
      "tags": [
        "bean980310/comfyui:latest"
      ]
    },
    "invokeai": {
      "context": "build/invokeai",
      "dockerfile": "Dockerfile",
      "args": {
        "BASE_IMAGE": "bean980310/ubuntu-docker:1.0.2-cuda-12.1.1-torch2.3.1",
        "INVOKEAI_VERSION": "v4.2.4",
        "WEBUI_VERSION": "v1.9.4"
      },
      "tags": [
        "bean980310/invokeai:latest"
      ]
    },
    "kohya_ss": {
      "context": "build/kohya_ss",
      "dockerfile": "Dockerfile",
      "args": {
        "BASE_IMAGE": "bean980310/ubuntu-docker:1.0.2-cuda-12.1.1-torch2.3.1",
        "KOHYA_VERSION": "v24.1.4",
        "WEBUI_VERSION": "v1.9.4"
      },
      "tags": [
        "bean980310/kohya-ss:latest"
      ]
    },
    "stable-diffusion-webui": {
      "context": "build/a1111-sdwebui",
      "dockerfile": "Dockerfile",
      "args": {
        "BASE_IMAGE": "bean980310/ubuntu-docker:1.0.2-cuda-12.1.1-torch2.3.1",
        "WEBUI_VERSION": "v1.9.4"
      },
      "tags": [
        "bean980310/stable-diffusion-webui:latest"
      ]
    }
}
