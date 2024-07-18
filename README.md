# stable-diffusion-docker-project
Stable Diffusion WebUI and KohyaSS, ComfyUI, InvokeAI, and Fooocus on Docker
## Setup
You need NVIDIA GPU and CUDA 12.1, Docker and NVIDIA Container toolkit, if you are using Windows 10/11, you also need enable WSL2. it is recommanded on Amazon Web Services, Microsoft Azure, Google Cloud Platform.
### How to install
```bash
git clone https://github.com/bean980310/stable-diffusion-docker-project.git
```

First, run the docker-compose.download.yml
```bash
cd <your_path_of_dir>/stable-diffusion-docker-project
docker compose -f docker-compose.download.yml up
```
And you must put models in directory stable-diffusion-models/models.

```bash
cd <your_path_of_dir>/stable-diffusion-docker-project
docker compose -f docker-compose.pull.yml up -d <service_name>
```

| Service list                  | Port |
|-------------------------------|------|
| stable-diffusion-webui        | 3010 |
| kohya_ss                      | 3020 |
| comfyui                       | 3030 |
| invokeai                      | 9090 |
| fooocus                       | 3040 |
| stable-diffusion-webui-forge  | 3050 |
| sdnext                        | 3060 |
| open-webui                    | 3000 |
| easy-diffusion                | 9000 |
| swarmui                       | 7801 |
| facefusion                    | 3070 |

example:
```bash
cd ~/stable-diffusion-docker-project
docker compose -f docker-compose.pull.yml up -d stable-diffusion-webui 
```

How to install extension of stable-diffusion-webui:
```bash
cd <your_path_of_dir>/stable-diffusion-docker-project/workspace/stable-diffusion-webui/extensions
git clone <stable-diffusion-webui_extension>
```
How to install ComfyUI Manager:
```bash
cd <your_path_of_dir>/stable-diffusion-docker-project/workspace/ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
```

## Usage
```bash
docker compose -f docker-compose.pull.yml up -d
```
or
```bash
docker compose -f docker-compose.pull.yml up -d <service_name>
```
## Features
### [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
### [KohyaSS](https://github.com/bmaltais/kohya_ss)
### [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
### [InvokeAI](https://github.com/invoke-ai/InvokeAI)
### [Fooocus](https://github.com/lllyasviel/Fooocus)
### [Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)
### [SD.Next](https://github.com/vladmandic/automatic)
### [Open-WebUI](https://github.com/open-webui/open-webui)
### [EasyDiffusion](https://github.com/easydiffusion/easydiffusion)
### [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI)
### [FaceFusion](https://github.com/facefusion/facefusion)
## Contributing
