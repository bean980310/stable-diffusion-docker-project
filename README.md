# stable-diffusion-docker-project
Stable Diffusion WebUI and KohyaSS, ComfyUI, InvokeAI, and Fooocus on Docker
## Setup
You need NVIDIA GPU and CUDA 12.1, Docker and NVIDIA Container toolkit, if you are using Windows 10/11, you also need enable WSL2. it is recommanded on Amazon Web Services, Microsoft Azure, Google Cloud Platform.
### How to install
```bash
git clone https://github.com/bean980310/stable-diffusion-docker-project.git
```
You must put models in directory stable-diffusion-models/models.

```bash
cd <your_path_of_dir>/stable-diffusion-docker-project
docker compose --profile <service_name> pull
docker compose --profile <service_name> up -d
```

## Usage
## Features
### [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
### [KohyaSS](https://github.com/bmaltais/kohya_ss)
### [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
### [InvokeAI](https://github.com/invoke-ai/InvokeAI)
### [Fooocus](https://github.com/lllyasviel/Fooocus)
## Contributing
