from huggingface_hub import hf_hub_download
import os
import shutil

sd15_ckpt_dir="/app/stable-diffusion-webui/models/Stable-diffusion/sd15"
sdxl_ckpt_dir="/app/stable-diffusion-webui/models/Stable-diffusion/sdxl"

hf_hub_download(repo_id="runwayml/stable-diffusion-v1-5", filename="v1-5-pruned-emaonly.safetensors", local_dir=sd15_ckpt_dir)
hf_hub_download(repo_id="runwayml/stable-diffusion-inpainting", filename="sd-v1-5-inpainting.ckpt", local_dir=sd15_ckpt_dir)
hf_hub_download(repo_id="WarriorMama777/OrangeMixs", filename="AOM3A1B_orangemixs.safetensors", subfolder="Models/AbyssOrangeMix3", local_dir=sd15_ckpt_dir)
if os.path.exists(f"{sd15_ckpt_dir}/AOM3A1B_orangemixs.safetensors"):
    pass
else:
    filename="AOM3A1B_orangemixs.safetensors"
    src=os.path.join(sd15_ckpt_dir, "Models/AbyssOrangeMix3")
    dst=sd15_ckpt_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    shutil.rmtree(os.path.join(sd15_ckpt_dir, "Models"))

hf_hub_download(repo_id="stabilityai/stable-diffusion-xl-base-1.0", filename="sd_xl_base_1.0.safetensors", local_dir=sdxl_ckpt_dir)
hf_hub_download(repo_id="stabilityai/stable-diffusion-xl-refiner-1.0", filename="sd_xl_refiner_1.0.safetensors", local_dir=sdxl_ckpt_dir)
hf_hub_download(repo_id="cagliostrolab/animagine-xl-3.1", filename="animagine-xl-3.1.safetensors", local_dir=sdxl_ckpt_dir)
shutil.rmtree(os.path.join(sdxl_ckpt_dir, ".cache"))