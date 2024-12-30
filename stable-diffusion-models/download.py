#!/usr/bin/env python
# coding: utf-8
from IPython import get_ipython

# # Download Model

# ## Create a sub-directory

# In[ ]:


import os
import shutil

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{path} created")
    else:
        print(f"{path} already exists")

ckpt_dir = ['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d', 'upscale']
clip_dir=['sd3', 'sd35_medium', 'sd35_large']
controlnet_dir=['sd15', 'sd2', 'sdxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']
diffusers_dir = ['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d', 'flux1']
embedding_dir=['sd15', 'sd2', 'sdxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']
facerestore_model_dir=['CodeFormer', 'GFPGAN', 'RestoreFormer']
hypernetwork_dir=['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']
lora_dir=['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']
onnx_model_dir=['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']
ultralytics_dir=['bbox', 'segm']
unet_model_dir=['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']
upscale_model_dir=['ESRGAN', 'RealESRGAN', 'LDSR', 'SwinIR']
vae_dir=['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']

[makedirs(os.path.join("./models/checkpoints", dir)) for dir in ckpt_dir]
[makedirs(os.path.join("./models/clip", dir)) for dir in clip_dir]
makedirs("./models/clip_vision")
makedirs("./models/configs")
[makedirs(os.path.join("./models/controlnet", dir)) for dir in controlnet_dir]
makedirs("./models/deepbooru")
[makedirs(os.path.join("./models/diffusers", dir)) for dir in diffusers_dir]
[makedirs(os.path.join("./models/embeddings", dir)) for dir in embedding_dir]
[makedirs(os.path.join('./models/facerestore_models', dir)) for dir in facerestore_model_dir]
makedirs("./models/gligen")
[makedirs(os.path.join("./models/hypernetworks", dir)) for dir in hypernetwork_dir]
makedirs("./models/inpaint")
makedirs("./models/karlo")
[makedirs(os.path.join("./models/loras", dir)) for dir in lora_dir]
makedirs("./models/mmdets")
[makedirs(os.path.join('./models/onnx', dir)) for dir in onnx_model_dir]
makedirs("./models/photomaker")
makedirs("./models/prompt_expansion")
makedirs("./models/safety_ckecker")
makedirs("./models/sams")
makedirs("./models/style_models")
[makedirs(os.path.join('./models/ultralytics', dir)) for dir in ultralytics_dir]
[makedirs(os.path.join('./models/unet', dir)) for dir in unet_model_dir]
[makedirs(os.path.join('./models/upscale_models', dir)) for dir in upscale_model_dir]
[makedirs(os.path.join("./models/vae", dir)) for dir in vae_dir]
makedirs("./models/vae_approx")


# ## Login to huggingface

# In[2]:


from huggingface_hub import notebook_login, hf_hub_download, snapshot_download

notebook_login(new_session=False)


# ## Login to CivitAI with API token

# In[ ]:


from civitai_downloader import login, civitai_download, advanced_download

token=login()


# ## Download Model

# In[4]:


models_dir='./models'
model_types=['checkpoints', 'clip', 'clip_vision', 'configs', 'controlnet', 'deepbooru', 'diffusers', 'embeddings', 'facerestore_models', 'gligen', 'hypernetworks', 'inpaint', 'karlo', 'loras', 'mmdets', 'onnx', 'photomaker', 'prompt_expansion', 'safety_ckecker', 'sams', 'style_models', 'ultralytics', 'unet', 'upscale_models', 'vae', 'vae_approx']
model_versions=['sd15', 'sd2', 'sdxl', 'pony', 'ilxl', 'sd3', 'sd35_medium', 'sd35_large', 'flux1_s', 'flux1_d']

class ModelDirs:
    def __init__(self, model_versions):
        self.dirs={}
        for ver in model_versions:
            dirs_for_ver={}
            for model_type in model_types:
                dir_path=os.path.join(models_dir, model_type, ver)
                attr_name=model_type
                dirs_for_ver[attr_name]=dir_path
            self.dirs[ver]=dirs_for_ver
    
model_dirs=ModelDirs(model_versions)


# ### Download Stable Diffusion 1.5 Model

# In[5]:


# Set Stable Diffusion 1.5 Model Path

sd15_ckpt_dir=model_dirs.dirs['sd15']['checkpoints']
sd15_vae_dir=model_dirs.dirs['sd15']['vae']
sd15_lora_dir=model_dirs.dirs['sd15']['loras']
sd15_controlnet_dir=model_dirs.dirs['sd15']['controlnet']
sd15_embedding_dir=model_dirs.dirs['sd15']['embeddings']


# #### Checkpoint

# In[ ]:


# Download Stable Diffusion 1.5 Model
hf_hub_download(repo_id="runwayml/stable-diffusion-v1-5", filename="v1-5-pruned-emaonly.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Stable Diffusion 1.5 Inpaint Model
hf_hub_download(repo_id="runwayml/stable-diffusion-inpainting", filename="sd-v1-5-inpainting.ckpt", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Anything V3 Model
civitai_download(model_version_id=34373, local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Anything V5 Model
civitai_download(model_version_id=30163, local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Anything Ink Model
civitai_download(model_version_id=90854, local_dir=sd15_ckpt_dir)


# In[ ]:


# Download AbyssOrangeMix3 Model
if os.path.exists(f"{sd15_ckpt_dir}/AOM3A1B_orangemixs.safetensors"):
    pass
else:
    hf_hub_download(repo_id="WarriorMama777/OrangeMixs", filename="AOM3A1B_orangemixs.safetensors", subfolder='Models/AbyssOrangeMix3', local_dir=sd15_ckpt_dir)
    filename="AOM3A1B_orangemixs.safetensors"
    src=os.path.join(sd15_ckpt_dir, "Models/AbyssOrangeMix3")
    dst=sd15_ckpt_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    shutil.rmtree(os.path.join(sd15_ckpt_dir, "Models"))


# In[ ]:


# Download Counterfeit-V3.0 fp32 Model
hf_hub_download(repo_id="gsdf/Counterfeit-V3.0", filename="Counterfeit-V3.0_fp32.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Counterfeit-V3.0 fp16 fix Model
hf_hub_download(repo_id="gsdf/Counterfeit-V3.0", filename="Counterfeit-V3.0_fix_fp16.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download ChilloutMix Ni pruned fp32 fix Model
civitai_download(model_version_id=11745, local_dir=sd15_ckpt_dir)


# In[ ]:


# Download ChilloutMix Ni pruned fp16 fix Model
civitai_download(model_version_id=11732, local_dir=sd15_ckpt_dir)


# In[ ]:


# Download DreamShaper 8 pruned Model
hf_hub_download(repo_id="Lykon/DreamShaper", filename="DreamShaper_8_pruned.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download DreamShaper 8 Inpainting Model
hf_hub_download(repo_id="Lykon/DreamShaper", filename="DreamShaper_8_INPAINTING.inpainting.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download MeinaMix Model
civitai_download(model_version_id=948574, local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Waifu Diffusion v1.4 Model
hf_hub_download(repo_id="hakurei/waifu-diffusion-v1-4", filename="wd-1-4-anime_e2.ckpt", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download AAM AnyLora Anime Mix Model
hf_hub_download(repo_id="Lykon/AnyLoRA", filename="AAM_Anylora_AnimeMix.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Blue Pencil Model
hf_hub_download(repo_id="bluepen5805/blue_pencil", filename="blue_pencil-v10.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download Blue Pencil Realistic Model
hf_hub_download(repo_id="bluepen5805/blue_pencil_realistic", filename="blue_pencil_realistic-v1.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download XpucT Reliberate Model
hf_hub_download(repo_id="XpucT/Reliberate", filename="Reliberate_v3.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download XpucT Reliberate Inpainting Model
hf_hub_download(repo_id="XpucT/Reliberate", filename="Reliberate_v3-inpainting.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download XpucT Anime Model
hf_hub_download(repo_id="XpucT/Anime", filename="Anime_v2.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download XpucT Anime Inpainting Model
hf_hub_download(repo_id="XpucT/Anime", filename="Anime_v2-inpainting.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download XpucT Deliberate Model
hf_hub_download(repo_id="XpucT/Deliberate", filename="Deliberate_v6.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download XpucT Deliberate Inpainting Model
hf_hub_download(repo_id="XpucT/Deliberate", filename="Deliberate_v6-inpainting.safetensors", local_dir=sd15_ckpt_dir)


# In[ ]:


# Download AnyLoRA BakedVae Blessed FP16 Model
hf_hub_download(repo_id="Lykon/AnyLoRA", filename="AnyLoRA_bakedVae_blessed_fp16.safetensors", local_dir=sd15_ckpt_dir)


# In[30]:


# Delete cache
get_ipython().system('rm -rf {sd15_ckpt_dir}/.cache')
get_ipython().system('rm -rf {sd15_ckpt_dir}/.civitai')


# #### VAE

# In[ ]:


# Download Stable Diffusion 1.5 VAE
hf_hub_download(repo_id="stabilityai/sd-vae-ft-mse-original", filename="vae-ft-mse-840000-ema-pruned.safetensors", local_dir=sd15_vae_dir)


# In[ ]:


# Download Waifu Diffusion v1.4 kl-f8-anime2 VAE
if os.path.exists(f"{sd15_vae_dir}/kl-f8-anime2.ckpt"):
    pass
else:
    hf_hub_download(repo_id="hakurei/waifu-diffusion-v1-4", filename="kl-f8-anime2.ckpt", subfolder='vae', local_dir=sd15_vae_dir)
    filename="kl-f8-anime2.ckpt"
    src=os.path.join(sd15_vae_dir, "vae")
    dst=sd15_vae_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download OrangeMix VAE
if os.path.exists(f"{sd15_vae_dir}/orangemix.vae.pt"):
    pass
else:
    hf_hub_download(repo_id="WarriorMama777/OrangeMixs", filename="orangemix.vae.pt", subfolder='VAEs', local_dir=sd15_vae_dir)
    filename="orangemix.vae.pt"
    src=os.path.join(sd15_vae_dir, "VAEs")
    dst=sd15_vae_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Anything VAE
civitai_download(model_version_id=119279, local_dir=sd15_vae_dir)


# In[ ]:


# Download ClearVAE
civitai_download(model_version_id=88156, local_dir=sd15_vae_dir)


# In[36]:


# Delete cache
get_ipython().system('rm -rf {sd15_vae_dir}/.cache')
get_ipython().system('rm -rf {sd15_vae_dir}/.civitai')


# #### LoRA

# In[ ]:


# Download Stable Diffusion 1.5 LCM LoRA
if os.path.exists(f"{sd15_lora_dir}/lcm-lora-sdv1-5.safetensors"):
    pass
else:
    hf_hub_download(repo_id="latent-consistency/lcm-lora-sdv1-5", filename="pytorch_lora_weights.safetensors", local_dir=sd15_lora_dir)
    filepath=sd15_lora_dir
    src=os.path.join(filepath, "pytorch_lora_weights.safetensors")
    dst=os.path.join(filepath, "lcm-lora-sdv1-5.safetensors")
    os.rename(src, dst)


# In[ ]:


# Download ShortBang Concept LoRA
civitai_download(model_version_id=122064, local_dir=sd15_lora_dir)


# In[ ]:


# Download Disembodied Head V2 LoRA
civitai_download(model_version_id=100482, local_dir=sd15_lora_dir)


# In[ ]:


# Download Dullahan LoRA
civitai_download(model_version_id=186885, local_dir=sd15_lora_dir)


# In[ ]:


# Download HeadinJar LoRA
civitai_download(model_version_id=77230, local_dir=sd15_lora_dir)


# In[ ]:


# Download Kirito LoRA
civitai_download(model_version_id=141405, local_dir=sd15_lora_dir)


# In[ ]:


# Download Eugeo LoRA
civitai_download(model_version_id=158391, local_dir=sd15_lora_dir)


# In[ ]:


# Download Tomboy LoRA
civitai_download(model_version_id=120588, local_dir=sd15_lora_dir)


# In[ ]:


# Download TomboyBuzzcut1-2-0805 LoRA
civitai_download(model_version_id=91509, local_dir=sd15_lora_dir)


# In[ ]:


# Download Princess Carry LoRA
civitai_download(model_version_id=112975, local_dir=sd15_lora_dir)


# In[ ]:


# Download Shima920 V2 LoRA
civitai_download(model_version_id=92833, local_dir=sd15_lora_dir)


# In[ ]:


# Download Anime Enhancer Midrange LoRA
civitai_download(model_version_id=215522, local_dir=sd15_lora_dir)


# In[49]:


# Delete cache
get_ipython().system('rm -rf {sd15_lora_dir}/.cache')
get_ipython().system('rm -rf {sd15_lora_dir}/.civitai')


# #### Embedding

# In[ ]:


# Download EasyNegative
hf_hub_download(repo_id="gsdf/EasyNegative", repo_type="dataset", filename="EasyNegative.safetensors", local_dir=sd15_embedding_dir)


# In[ ]:


# Download EasyNegativeV2
if os.path.exists(f"{sd15_embedding_dir}/EasyNegativeV2.safetensors"):
    pass
else:
    hf_hub_download(repo_id="gsdf/Counterfeit-V3.0", filename="EasyNegativeV2.safetensors", subfolder='embedding', local_dir=sd15_embedding_dir)
    filename="EasyNegativeV2.safetensors"
    src=os.path.join(sd15_embedding_dir, "embedding")
    dst=os.path.join(sd15_embedding_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download bad-hand-v4
civitai_download(model_version_id=230261, local_dir=sd15_embedding_dir)


# In[ ]:


# Download bad-hands-v5
hf_hub_download(repo_id="Kajise/bad-hands", filename="bad-hands-5.safetensors", local_dir=sd15_embedding_dir)


# In[ ]:


# Download bad_prompt_version2
hf_hub_download(repo_id="Nerfgun3/bad_prompt", repo_type="dataset", filename="bad_prompt_version2.pt", local_dir=sd15_embedding_dir)


# In[ ]:


# Download bad-artist-anime
hf_hub_download(repo_id="nick-x-hacker/bad-artist", filename="bad-artist-anime.pt", local_dir=sd15_embedding_dir)


# In[ ]:


# Download bad-artist
hf_hub_download(repo_id="nick-x-hacker/bad-artist", filename="bad-artist.pt", local_dir=sd15_embedding_dir)


# In[ ]:


# Download Deep Negative V1 75 T
civitai_download(model_version_id=5637, local_dir=sd15_embedding_dir)


# In[ ]:


# Download veryBadImageNegative
civitai_download(model_version_id=25820, local_dir=sd15_embedding_dir)


# In[ ]:


# Download GS-Boyish
civitai_download(model_version_id=95611, local_dir=sd15_embedding_dir)


# In[60]:


# Delete cache
get_ipython().system('rm -rf {sd15_embedding_dir}/.cache')
get_ipython().system('rm -rf {sd15_embedding_dir}/.civitai')


# #### ControlNet

# In[ ]:


# Download ControlNet SD15 ip2p Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11e_sd15_ip2p_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Shuffle Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11e_sd15_shuffle_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Tile Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11f1e_sd15_tile_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Depth Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11f1p_sd15_depth_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Canny Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_canny_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Inpaint Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_inpaint_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Lineart Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_lineart_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 MLSD Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_mlsd_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet NormalBae Canny Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_normalbae_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 OpenPose Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_openpose_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Scribble Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_scribble_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Seg Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_seg_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Softedge Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15_softedge_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[ ]:


# Download ControlNet SD15 Lineart Anime Model
hf_hub_download(repo_id="comfyanonymous/ControlNet-v1-1_fp16_safetensors", filename="control_v11p_sd15s2_lineart_anime_fp16.safetensors", local_dir=sd15_controlnet_dir)


# In[75]:


# Delete cache
get_ipython().system('rm -rf {sd15_controlnet_dir}/.cache')


# ### Download Stable Diffusion 2.x Model

# In[76]:


# Set Stable Diffusion 2.x Model Path

sd2_ckpt_dir=model_dirs.dirs['sd2']['checkpoints']
sd2_controlnet_dir=model_dirs.dirs['sd2']['controlnet']


# #### Checkpoint

# In[ ]:


# Download Stable Diffusion 2.0 768 Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-2", filename="768-v-ema.safetensors", local_dir=sd2_ckpt_dir)


# In[ ]:


# Download Stable Diffusion 2.0 512 Base Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-2-base", filename="512-base-ema.safetensors", local_dir=sd2_ckpt_dir)


# In[ ]:


# Download Stable Diffusion 2.0 512 Depth Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-2-depth", filename="512-depth-ema.safetensors", local_dir=sd2_ckpt_dir)


# In[ ]:


# Download Stable Diffusion 2.0 512 Inpainting Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-2-inpainting", filename="512-inpainting-ema.safetensors", local_dir=sd2_ckpt_dir)


# In[ ]:


# Download Stable Diffusion 2.1 Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-2-1", filename="v2-1_768-ema-pruned.safetensors", local_dir=sd2_ckpt_dir)


# In[ ]:


# Download Stable Diffusion 2.1 Base Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-2-1-base", filename="v2-1_512-ema-pruned.safetensors", local_dir=sd2_ckpt_dir)


# In[83]:


# Delete cache
get_ipython().system('rm -rf {sd2_ckpt_dir}/.cache')


# #### ControlNet

# In[ ]:


# Download Stable Diffusion 2.1 ControlNet
snapshot_download(repo_id="thibaud/controlnet-sd21", allow_patterns="*.safetensors", local_dir=sd2_controlnet_dir)


# In[85]:


# Delete cache
get_ipython().system('rm -rf {sd2_controlnet_dir}/.cache')


# ### Download Stable Diffusion XL Model

# In[6]:


sdxl_ckpt_dir=model_dirs.dirs['sdxl']['checkpoints']
sdxl_vae_dir=model_dirs.dirs['sdxl']['vae']
sdxl_lora_dir=model_dirs.dirs['sdxl']['loras']
sdxl_controlnet_dir=model_dirs.dirs['sdxl']['controlnet']
sdxl_embedding_dir=model_dirs.dirs['sdxl']['embeddings']


# #### Checkpoint

# In[ ]:


# Download Stable Diffusion XL 1.0 Base Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-xl-base-1.0", filename="sd_xl_base_1.0.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Stable Diffusion XL 1.0 Refiner Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-xl-refiner-1.0", filename="sd_xl_refiner_1.0.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Anything XL Model
civitai_download(model_version_id=384264, local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download AnimagineXL 3.1 Model
hf_hub_download(repo_id="cagliostrolab/animagine-xl-3.1", filename="animagine-xl-3.1.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Gamma XL NSFW for Anything XL Model
civitai_download(model_version_id=412021, local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Kohaku XL Epsilon Model
civitai_download(model_version_id=546178, local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download CounterfeitXL V2.5 Model
hf_hub_download(repo_id="gsdf/CounterfeitXL-V2.0", filename="CounterfeitXL-V2.5.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Juggernaut XL Model
hf_hub_download(repo_id="RunDiffusion/Juggernaut-XI-v11", filename="Juggernaut-XI-byRunDiffusion.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download NoobAI XL Model
civitai_download(model_version_id=968495, local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download AAM XL Anime Mix Model
hf_hub_download(repo_id="Lykon/AnyLoRA", filename="AAM_XL_Anime_Mix.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Blue Pencil XL Model
hf_hub_download(repo_id="bluepen5805/blue_pencil-XL", filename="blue_pencil-XL-v7.0.0.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download Anima Pencil XL Model
hf_hub_download(repo_id="bluepen5805/anima_pencil-XL", filename="anima_pencil-XL-v5.0.0.safetensors", local_dir=sdxl_ckpt_dir)


# In[ ]:


# Download DreamShaper XL Model
hf_hub_download(repo_id="Lykon/DreamShaper", filename="DreamShaperXL1.0Alpha2_fixedVae_half_00001_.safetensors", local_dir=sdxl_ckpt_dir)


# In[100]:


# Delete cache
get_ipython().system('rm -rf {sdxl_ckpt_dir}/.cache')
get_ipython().system('rm -rf {sdxl_ckpt_dir}/.civitai')


# #### VAE

# In[ ]:


# Download Stable Diffusion XL 1.0 VAE
hf_hub_download(repo_id="madebyollin/sdxl-vae-fp16-fix", filename="sdxl_vae.safetensors", local_dir=sdxl_vae_dir)


# In[102]:


# Delete cache
get_ipython().system('rm -rf {sdxl_vae_dir}/.cache')


# #### LoRA

# In[ ]:


# Download Stable Diffusion XL LCM LoRA
if os.path.exists(f"{sdxl_lora_dir}/lcm-lora-sdxl.safetensors"):
    pass
else:
    hf_hub_download(repo_id="latent-consistency/lcm-lora-sdxl", filename="pytorch_lora_weights.safetensors", local_dir=sdxl_lora_dir)
    filepath=sdxl_lora_dir
    src=os.path.join(filepath,"pytorch_lora_weights.safetensors")
    dst=os.path.join(filepath, "lcm-lora-sdxl.safetensors")
    os.rename(src, dst)


# In[ ]:


# Download Envy Tomboy Slider XL LoRA
civitai_download(model_version_id=251963, local_dir=sdxl_lora_dir)


# In[ ]:


# Download SAO Kirito SDXL Satu LoRA
civitai_download(model_version_id=489270, local_dir=sdxl_lora_dir)


# In[ ]:


# Download XL Eugeo SAO Animagine XL 3.1 LoRA
civitai_download(model_version_id=437049, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Sailorboy XL LoRA
civitai_download(model_version_id=134460, local_dir=sdxl_lora_dir)


# In[ ]:


# Download SDXL Disembodied head Headless LoRA
civitai_download(model_version_id=515553, local_dir=sdxl_lora_dir)


# In[ ]:


# Download [Yue] Paintingboys SDXL LoRA
civitai_download(model_version_id=144865, local_dir=sdxl_lora_dir)


# In[ ]:


# Download A Short cut v3 SDXL LoRA
civitai_download(model_version_id=298618, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Breasts Slider LoRA
civitai_download(model_version_id=173866, local_dir=sdxl_lora_dir)


# In[ ]:


# Download SDXL Dark Knight LoRA
civitai_download(model_version_id=570644, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Enhancer V4 XL LoRA
civitai_download(model_version_id=497695, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Add Details XL LoRA
civitai_download(model_version_id=436121, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Head Swap (Male Head on Female Body) Animagine XL 3.1 LoRA
civitai_download(model_version_id=513742, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Head Swap (Female Head on Male Body) Animagine XL 3.1 LoRA
civitai_download(model_version_id=429832, local_dir=sdxl_lora_dir)


# In[ ]:


# Download Original Character - 南飛鳥(Minami Asuka) XL for Animagine XL 3.1 LoRA
hf_hub_download(repo_id="bean980310/minami-asuka-xl-animagine", filename="minami-asuka-xl-animagine.safetensors", local_dir=sdxl_lora_dir)


# In[ ]:


# Download Tomboy XL for Animagine XL 3.1 LoRA
hf_hub_download(repo_id="bean980310/tomboy-xl-animagine", filename="tomboy-xl-animagine.safetensors", local_dir=sdxl_lora_dir)


# In[ ]:


# Download headswap XL for Animagine XL 3.1 LoRA
hf_hub_download(repo_id="bean980310/headswap_xl_animagine", filename="headswap_xl_animagine.safetensors", local_dir=sdxl_lora_dir)


# In[120]:


# Delete cache
get_ipython().system('rm -rf {sdxl_lora_dir}/.cache')
get_ipython().system('rm -rf {sdxl_lora_dir}/.civitai')


# #### Embedding

# In[ ]:


# Download NegativeXL A
if os.path.exists(f"{sdxl_embedding_dir}/negativeXL_A.safetensors"):
    pass
else:
    hf_hub_download(repo_id="gsdf/CounterfeitXL", filename="negativeXL_A.safetensors", subfolder='embeddings', local_dir=sdxl_embedding_dir)
    filename="negativeXL_A.safetensors"
    src=os.path.join(sdxl_embedding_dir, "embeddings")
    dst=sdxl_embedding_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download NegativeXL B
if os.path.exists(f"{sdxl_embedding_dir}/negativeXL_B.safetensors"):
    pass
else:
    hf_hub_download(repo_id="gsdf/CounterfeitXL", filename="negativeXL_B.safetensors", subfolder='embeddings', local_dir=sdxl_embedding_dir)
    filename="negativeXL_B.safetensors"
    src=os.path.join(sdxl_embedding_dir, "embeddings")
    dst=sdxl_embedding_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download NegativeXL C
if os.path.exists(f"{sdxl_embedding_dir}/negativeXL_C.safetensors"):
    pass
else:
    hf_hub_download(repo_id="gsdf/CounterfeitXL", filename="negativeXL_C.safetensors", subfolder='embeddings', local_dir=sdxl_embedding_dir)
    filename="negativeXL_C.safetensors"
    src=os.path.join(sdxl_embedding_dir, "embeddings")
    dst=sdxl_embedding_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download NegativeXL D
if os.path.exists(f"{sdxl_embedding_dir}/negativeXL_D.safetensors"):
    pass
else:
    hf_hub_download(repo_id="gsdf/CounterfeitXL", filename="negativeXL_D.safetensors", subfolder='embeddings', local_dir=sdxl_embedding_dir)
    filename="negativeXL_D.safetensors"
    src=os.path.join(sdxl_embedding_dir, "embeddings")
    dst=sdxl_embedding_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download DeepNegative XL
civitai_download(model_version_id=454217, local_dir=sdxl_embedding_dir)


# In[ ]:


# Download Negative XL
civitai_download(model_version_id=261856, local_dir=sdxl_embedding_dir)


# In[ ]:


# Download Negative XL V2
civitai_download(model_version_id=264111, local_dir=sdxl_embedding_dir)


# In[ ]:


# Download Negative XL Color_Balance_Calibration_0.8
civitai_download(model_version_id=431425, local_dir=sdxl_embedding_dir)


# In[129]:


# Delete cache
get_ipython().system('rm -rf {sdxl_embedding_dir}/.cache')
get_ipython().system('rm -rf {sdxl_embedding_dir}/.civitai')


# #### ControlNet

# **Stability AI**

# In[ ]:


# Download Stability AI ControlNet XL Canny
if os.path.exists(f"{sdxl_controlnet_dir}/control-lora-canny-rank256.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/control-lora", filename="control-lora-canny-rank256.safetensors", subfolder='control-LoRAs-rank256', local_dir=sdxl_controlnet_dir)
    filename='control-lora-canny-rank256.safetensors'
    src=os.path.join(sdxl_controlnet_dir, 'control-LoRAs-rank256')
    dst=sdxl_controlnet_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Stability AI ControlNet XL Depth
if os.path.exists(f"{sdxl_controlnet_dir}/control-lora-depth-rank256.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/control-lora", filename="control-lora-depth-rank256.safetensors", subfolder='control-LoRAs-rank256', local_dir=sdxl_controlnet_dir)
    filename='control-lora-depth-rank256.safetensors'
    src=os.path.join(sdxl_controlnet_dir, 'control-LoRAs-rank256')
    dst=sdxl_controlnet_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Stability AI ControlNet XL Recolor
if os.path.exists(f"{sdxl_controlnet_dir}/control-lora-recolor-rank256.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/control-lora", filename="control-lora-recolor-rank256.safetensors", subfolder='control-LoRAs-rank256', local_dir=sdxl_controlnet_dir)
    filename='control-lora-recolor-rank256.safetensors'
    src=os.path.join(sdxl_controlnet_dir, 'control-LoRAs-rank256')
    dst=sdxl_controlnet_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Stability AI ControlNet XL Sketch
if os.path.exists(f"{sdxl_controlnet_dir}/control-lora-sketch-rank256.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/control-lora", filename="control-lora-sketch-rank256.safetensors", subfolder='control-LoRAs-rank256', local_dir=sdxl_controlnet_dir)
    filename='control-lora-sketch-rank256.safetensors'
    src=os.path.join(sdxl_controlnet_dir, 'control-LoRAs-rank256')
    dst=sdxl_controlnet_dir
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# **Diffusers**

# In[ ]:


# Download Diffusers ControlNet XL Canny
if os.path.exists(f"{sdxl_controlnet_dir}/controlnet-canny-sdxl-1.0.safetensors"):
    pass
else:
    hf_hub_download(repo_id="diffusers/controlnet-canny-sdxl-1.0", filename="diffusion_pytorch_model.fp16.safetensors", local_dir=sdxl_controlnet_dir)
    filepath=sdxl_controlnet_dir
    src=os.path.join(filepath,"diffusion_pytorch_model.fp16.safetensors")
    dst=os.path.join(filepath, "controlnet-canny-sdxl-1.0.safetensors")
    os.rename(src, dst)


# In[ ]:


# Download Diffusers ControlNet XL Depth
if os.path.exists(f"{sdxl_controlnet_dir}/controlnet-depth-sdxl-1.0.safetensors"):
    pass
else:
    hf_hub_download(repo_id="diffusers/controlnet-depth-sdxl-1.0", filename="diffusion_pytorch_model.fp16.safetensors", local_dir=sdxl_controlnet_dir)
    src=os.path.join(filepath,"diffusion_pytorch_model.fp16.safetensors")
    dst=os.path.join(filepath, "controlnet-depth-sdxl-1.0.safetensors")
    os.rename(src, dst)


# **Kataragi**

# In[ ]:


# Download Kataragi ControlNet XL Canny
hf_hub_download(repo_id="kataragi/controlnet_canny", filename="Kataragi_cannyXL-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL Flatline
hf_hub_download(repo_id="kataragi/flatline", filename="diffusers_xl_flatline_testXL-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL Inpaint
hf_hub_download(repo_id="kataragi/controlnetXL_inpaint", filename="Kataragi_inpaintXL-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL Line2Color
hf_hub_download(repo_id="kataragi/controlnetXL_line2color", filename="controlnetXL_line2colorV2-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL LineArt
hf_hub_download(repo_id="kataragi/ControlNet-LineartXL", filename="Katarag_lineartXL-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL ReColor
hf_hub_download(repo_id="kataragi/ControlNet-recolorXL", filename="diffusers_xl_recolor_testXL-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL Tori29 Blur
hf_hub_download(repo_id="kataragi/ControlNet_tori29_blur", filename="ControlNet_tori29_blur-fp16.safetensors", local_dir=sdxl_controlnet_dir)


# In[ ]:


# Download Kataragi ControlNet XL Routh Coating
hf_hub_download(repo_id="kataragi/controlnetXL-rough-coating", filename="rough-coatingV1.safetensors", local_dir=sdxl_controlnet_dir)


# **Thibaud**

# In[ ]:


# Download Thibaud ControlNet XL OpenPose
hf_hub_download(repo_id="thibaud/controlnet-openpose-sdxl-1.0", filename="control-lora-openposeXL2-rank256.safetensors", local_dir=sdxl_controlnet_dir)


# **xinsir**

# In[ ]:


# Download Xinsir ControlNet XL Union
if os.path.exists(f"{sdxl_controlnet_dir}/controlnet-union-sdxl-1.0-promax.safetensors"):
    pass
else:
    hf_hub_download(repo_id="xinsir/controlnet-union-sdxl-1.0", filename="diffusion_pytorch_model_promax.safetensors", local_dir=sdxl_controlnet_dir)
    src=os.path.join(sdxl_controlnet_dir,"diffusion_pytorch_model_promax.safetensors")
    dst=os.path.join(sdxl_controlnet_dir, "controlnet-union-sdxl-1.0-promax.safetensors")
    os.rename(src, dst)


# In[146]:


# Delete cache
get_ipython().system('rm -rf {sdxl_controlnet_dir}/.cache')


# ### Download Pony Diffusion Model

# In[147]:


pony_ckpt_dir=model_dirs.dirs['pony']['checkpoints']
pony_vae_dir=model_dirs.dirs['pony']['vae']
pony_lora_dir=model_dirs.dirs['pony']['loras']


# #### Checkpoint

# In[ ]:


# Download Pony Diffusion XL V6 Model
civitai_download(model_version_id=290640, local_dir=pony_ckpt_dir)


# In[ ]:


# Download AutismMix Pony Model
civitai_download(model_version_id=324619, local_dir=pony_ckpt_dir)


# In[ ]:


# Download 7th Anime XL Pony Model
civitai_download(model_version_id=441236, local_dir=pony_ckpt_dir)


# In[ ]:


# Download Hassaku XL (Pony) Model
civitai_download(model_version_id=575495, local_dir=pony_ckpt_dir)


# In[ ]:


# Download Pony Pencil XL Model
hf_hub_download(repo_id="bluepen5805/pony_pencil-XL", filename="pony_pencil-XL-v2.0.0.safetensors", local_dir=pony_ckpt_dir)


# In[ ]:


# Download T-ponynai3 Model
civitai_download(model_version_id=814910, local_dir=pony_ckpt_dir)


# In[154]:


# Delete cache
get_ipython().system('rm -rf {pony_ckpt_dir}/.cache')
get_ipython().system('rm -rf {pony_ckpt_dir}/.civitai')


# #### VAE

# In[ ]:


# Download Pony Standard VAE
civitai_download(model_version_id=739304, local_dir=pony_vae_dir)


# In[ ]:


# Download Pony Enhanced VAE Pastels
civitai_download(model_version_id=739267, local_dir=pony_vae_dir)


# In[157]:


# Delete cache
get_ipython().system('rm -rf {pony_vae_dir}/.civitai')


# #### LoRA

# In[ ]:


# Download Head Swap (Male Head on Female Body) Pony
civitai_download(model_version_id=528192, local_dir=pony_lora_dir)


# In[ ]:


# Download Head Swap (Female Head on Male Body) Pony
civitai_download(model_version_id=528196, local_dir=pony_lora_dir)


# In[ ]:


# Download SDXL Pony Headless
civitai_download(model_version_id=357744, local_dir=pony_lora_dir)


# In[ ]:


# Download SDXL Pony Disembodied Head
civitai_download(model_version_id=360519, local_dir=pony_lora_dir)


# In[ ]:


# Download Tomboy Style Pony
advanced_download(model_version_id=647477, local_dir=pony_lora_dir, type_filter='Model', format_filter='SafeTensor', size_filter=None, fp_filter=None)


# In[163]:


# Delete cache
get_ipython().system('rm -rf {pony_lora_dir}/.civitai')


# ### Download Illustrious XL Model

# In[164]:


ilxi_ckpt_dir=model_dirs.dirs['ilxl']['checkpoints']


# #### Checkpoint

# In[ ]:


# Download Illustrious XL Model
hf_hub_download(repo_id="OnomaAIResearch/Illustrious-xl-early-release-v0", filename="Illustrious-XL-v0.1.safetensors", local_dir=ilxi_ckpt_dir)


# In[ ]:


# Download Illustrious Pencil XL Model
hf_hub_download(repo_id="bluepen5805/illustrious_pencil-XL", filename="illustrious_pencil-XL-v1.2.0.safetensors", local_dir=ilxi_ckpt_dir)


# In[168]:


# Delete cache
get_ipython().system('rm -rf {ilxl_ckpt_dir}/.cache')


# ### Download Stable Diffusion 3.x Model

# In[169]:


sd3_ckpt_dir=model_dirs.dirs['sd3']['checkpoints']
sd35_medium_ckpt_dir=model_dirs.dirs['sd35_medium']['checkpoints']
sd35_large_ckpt_dir=model_dirs.dirs['sd35_large']['checkpoints']
sd3_clip_dir=model_dirs.dirs['sd3']['clip']
sd35_medium_clip_dir=model_dirs.dirs['sd35_medium']['clip']
sd35_large_clip_dir=model_dirs.dirs['sd35_large']['clip']


# #### Checkpoint

# **Stable Diffusion 3 Medium**

# In[ ]:


# Download Stable Diffusion 3 Medium Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-3-medium", filename="sd3_medium.safetensors", local_dir=sd3_ckpt_dir)


# **Stable Diffusion 3.5 Medium**

# In[ ]:


# Download Stable Diffusion 3.5 Medium Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-medium", filename="sd3.5_medium.safetensors", local_dir=sd35_medium_ckpt_dir)


# In[ ]:


# Download Intermediate(SD 3.5 medium) Model
civitai_download(model_version_id=1019118, local_dir=sd35_medium_ckpt_dir)


# **Stable Diffusion 3.5 Large**

# In[ ]:


# Download Stable Diffusion 3.5 Large Model
hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-large", filename="sd3.5_large.safetensors", local_dir=sd35_large_ckpt_dir)


# In[174]:


# Delete cache
get_ipython().system('rm -rf {sd3_ckpt_dir}/.cache')
get_ipython().system('rm -rf {sd35_medium_ckpt_dir}/.cache')
get_ipython().system('rm -rf {sd35_medium_ckpt_dir}/.civitai')
get_ipython().system('rm -rf {sd35_large_ckpt_dir}/.cache')


# #### Clip

# **Stable Diffusion 3**

# In[ ]:


# Download Clip L
if os.path.exists(f"{sd3_clip_dir}/clip_l.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3-medium", filename="clip_l.safetensors", subfolder='text_encoders', local_dir=sd3_clip_dir)
    filename='clip_l.safetensors'
    src=os.path.join(sd3_clip_dir, 'text_encoders')
    dst=os.path.join(sd3_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Clip G
if os.path.exists(f"{sd3_clip_dir}/clip_g.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3-medium", filename="clip_g.safetensors", subfolder='text_encoders', local_dir=sd3_clip_dir)
    filename='clip_g.safetensors'
    src=os.path.join(sd3_clip_dir, 'text_encoders')
    dst=os.path.join(sd3_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download T5 XXL FP8
if os.path.exists(f"{sd3_clip_dir}/t5xxl_fp8_e4m3fn.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3-medium", filename="t5xxl_fp8_e4m3fn.safetensors", subfolder='text_encoders', local_dir=sd3_clip_dir)
    filename='t5xxl_fp8_e4m3fn.safetensors'
    src=os.path.join(sd3_clip_dir, 'text_encoders')
    dst=os.path.join(sd3_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download T5 XXL FP16
if os.path.exists(f"{sd3_clip_dir}/t5xxl_fp16.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3-medium", filename="t5xxl_fp16.safetensors", subfolder='text_encoders', local_dir=sd3_clip_dir)
    filename='t5xxl_fp16.safetensors'
    src=os.path.join(sd3_clip_dir, 'text_encoders')
    dst=os.path.join(sd3_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Delete cache
get_ipython().system('rm -rf {sd3_clip_dir}/.cache')


# **Stable Diffusion 3.5 Medium**

# In[ ]:


# Download Clip L
if os.path.exists(f"{sd35_medium_clip_dir}/clip_l.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-medium", filename="clip_l.safetensors", subfolder='text_encoders', local_dir=sd35_medium_clip_dir)
    filename='clip_l.safetensors'
    src=os.path.join(sd35_medium_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_medium_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Clip G
if os.path.exists(f"{sd35_medium_clip_dir}/clip_g.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-medium", filename="clip_g.safetensors", subfolder='text_encoders', local_dir=sd35_medium_clip_dir)
    filename='clip_g.safetensors'
    src=os.path.join(sd35_medium_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_medium_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download T5 XXL FP8
if os.path.exists(f"{sd35_medium_clip_dir}/t5xxl_fp8_e4m3fn.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-medium", filename="t5xxl_fp8_e4m3fn.safetensors", subfolder='text_encoders', local_dir=sd35_medium_clip_dir)
    filename='t5xxl_fp8_e4m3fn.safetensors'
    src=os.path.join(sd35_medium_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_medium_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download T5 XXL FP16
if os.path.exists(f"{sd35_medium_clip_dir}/t5xxl_fp16.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-medium", filename="t5xxl_fp16.safetensors", subfolder='text_encoders', local_dir=sd35_medium_clip_dir)
    filename='t5xxl_fp16.safetensors'
    src=os.path.join(sd35_medium_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_medium_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Delete cache
get_ipython().system('rm -rf {sd35_medium_clip_dir}/.cache')


# **Stable Diffusion 3.5 Large**

# In[ ]:


# Download Clip L
if os.path.exists(f"{sd35_large_clip_dir}/clip_l.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-large", filename="clip_l.safetensors", subfolder='text_encoders', local_dir=sd35_large_clip_dir)
    filename='clip_l.safetensors'
    src=os.path.join(sd35_large_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_large_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download Clip G
if os.path.exists(f"{sd35_large_clip_dir}/clip_g.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-large", filename="clip_g.safetensors", subfolder='text_encoders', local_dir=sd35_large_clip_dir)
    filename='clip_g.safetensors'
    src=os.path.join(sd35_large_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_large_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download T5 XXL FP8
if os.path.exists(f"{sd35_large_clip_dir}/t5xxl_fp8_e4m3fn.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-large", filename="t5xxl_fp8_e4m3fn.safetensors", subfolder='text_encoders', local_dir=sd35_large_clip_dir)
    filename='t5xxl_fp8_e4m3fn.safetensors'
    src=os.path.join(sd35_large_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_large_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[ ]:


# Download T5 XXL FP16
if os.path.exists(f"{sd35_large_clip_dir}/t5xxl_fp16.safetensors"):
    pass
else:
    hf_hub_download(repo_id="stabilityai/stable-diffusion-3.5-large", filename="t5xxl_fp16.safetensors", subfolder='text_encoders', local_dir=sd35_large_clip_dir)
    filename='t5xxl_fp16.safetensors'
    src=os.path.join(sd35_large_clip_dir, 'text_encoders')
    dst=os.path.join(sd35_large_clip_dir)
    shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
    os.rmdir(src)


# In[179]:


# Delete cache
get_ipython().system('rm -rf {sd35_large_clip_dir}/.cache')


# ### Download Flux.1 Dev Model

# In[6]:


flux_dev_ckpt_dir=model_dirs.dirs['flux1_d']['checkpoints']
flux_dev_vae_dir=model_dirs.dirs['flux1_d']['vae']
flux_dev_lora_dir=model_dirs.dirs['flux1_d']['loras']


# #### Checkpoint

# In[ ]:


# Download Flux.1 Dev Model
hf_hub_download(repo_id="black-forest-labs/FLUX.1-dev", filename="flux1-dev.safetensors", local_dir=flux_dev_ckpt_dir)


# In[ ]:


# Download Blue Pencil Flux 1 Model
hf_hub_download(repo_id="bluepen5805/blue_pencil-flux1", filename="blue_pencil-flux1-v0.2.1-bf16.safetensors", local_dir=flux_dev_ckpt_dir)


# In[9]:


# Delete cache
get_ipython().system('rm -rf {flux_dev_ckpt_dir}/.cache')


# #### VAE

# In[ ]:


# Download Flux.1 Dev VAE
hf_hub_download(repo_id="black-forest-labs/FLUX.1-dev", filename="ae.safetensors", local_dir=flux_dev_vae_dir)


# In[11]:


# Delete cache
get_ipython().system('rm -rf {flux_dev_vae_dir}/.cache')


# #### LoRA

# In[ ]:


# Download Flux.1 Dev AntiBlur LoRA
hf_hub_download(repo_id="Shakker-Labs/FLUX.1-dev-LoRA-AntiBlur", filename="FLUX-dev-lora-AntiBlur.safetensors", local_dir=flux_dev_lora_dir)


# In[ ]:


# Download Flux.1 Dev Add Details LoRA
hf_hub_download(repo_id="Shakker-Labs/FLUX.1-dev-LoRA-add-details", filename="FLUX-dev-lora-add_details.safetensors", local_dir=flux_dev_lora_dir)


# In[ ]:


# Download Tomboy for Flux LoRA
civitai_download(model_version_id=797322, local_dir=flux_dev_lora_dir)


# In[15]:


# Delete cache
get_ipython().system('rm -rf {flux_dev_lora_dir}/.cache')
get_ipython().system('rm -rf {flux_dev_lora_dir}/.civitai')


# ### Download Upscale Model

# #### ESRGAN

# In[ ]:


# Download 4x AnimeSharp Model
hf_hub_download(repo_id="Kim2091/AnimeSharp", filename="4x-AnimeSharp.pth", local_dir="./models/upscale_models/ESRGAN")


# In[ ]:


# Download 4x UltraSharp Model
hf_hub_download(repo_id="Kim2091/UltraSharp", filename="4x-UltraSharp.pth", local_dir="./models/upscale_models/ESRGAN")


# In[182]:


# Delete cache
get_ipython().system('rm -rf ./models/upscale_models/ESRGAN/.cache')


# #### RealESRGAN

# In[183]:


from requests import get
from urllib.parse import urljoin

def git_download(repo_id: str, filename: str, tag: str, local_dir: str):
    repo_url=urljoin('https://github.com', repo_id, 'releases/download')
    src=urljoin(repo_url, tag, filename)
    filepath=os.path.join(local_dir, filename)
    download(src, filepath)
    return src, filepath

def download(url, filename):
    with open(filename, 'wb') as f:
        response = get(url)
        f.write(response.content)

realesrgan_dir="./models/upscale_models/RealESRGAN"


# In[ ]:


# Download RealESRGAN x4 Plus Model
git_download(repo_id='xinntao/Real-ESRGAN', filename='RealESRGAN_x4plus.pth', tag='v0.1.0', local_dir=realesrgan_dir)


# In[ ]:


# Download RealESRGAN x4 Plus Anime 6B Model
git_download(repo_id="xinntao/Real-ESRGAN", filename="RealESRGAN_x4plus_anime_6B.pth", tag='v0.2.2.4', local_dir=realesrgan_dir)


# #### LDSR

# In[186]:


# Download LDSR Model
ldsr_dir='./models/upscale_models/LDSR'
download("https://heibox.uni-heidelberg.de/f/31a76 db13ea27482981b4/?dl=1", f"{ldsr_dir}/2021-11-02T06-24-44-project.yaml")
download("https://heibox.uni-heidelberg.de/f/578df07c8fc04ffbadf3/?dl=1", f"{ldsr_dir}/last.ckpt")


# #### Stable Diffusion x4 Upscale Model

# In[ ]:


#download Stable Diffusion x4 Upscale model
hf_hub_download(repo_id="stabilityai/stable-diffusion-x4-upscaler", filename="x4-upscaler-ema.safetensors", local_dir="./models/checkpoints/upscale")


# In[188]:


# Delete cache
get_ipython().system('rm -rf ./models/checkpoints/upscale/.cache')


# ### Download Face Restore Model

# In[ ]:


# Download GFPGAN Model
git_download(repo_id="TencentARC/GFPGAN", filename="GFPGANv1.4.pth", tag='v1.3.4', local_dir='./models/facerestore_models/GFPGAN')


# In[ ]:


# Download Code Former Model
git_download(repo_id="TencentARC/GFPGAN", filename="CodeFormer.pth", tag='v1.3.4', local_dir="./models/facerestore_models/Codeformer")


# In[ ]:


# Download Restore Former Model
git_download(repo_id='TencentARC/GFPGAN', filename='RestoreFormer.pth', tag='v1,3,4', local_dir='./models/facerestore_models/Codeformer')


# ### Download UltraLytics Model

# In[ ]:


# Download UltraLytics BBOX Model
snapshot_download(repo_id="Bingsu/adetailer", allow_patterns="*.pt", ignore_patterns="*-seg.pt", local_dir="./models/ultralytics/bbox")


# In[ ]:


# Download UltraLytics SEGM Model
snapshot_download(repo_id="Bingsu/adetailer", allow_patterns="*-seg.pt", local_dir="./models/ultralytics/segm")


# In[191]:


# Delete cache
get_ipython().system('rm -rf ./models/ultralytics/bbox/.cache')
get_ipython().system('rm -rf ./models/ultralytics/segm/.cache')


# ### Download Segment Anything Model

# #### SAMS

# In[192]:


# Download SAM Vit H Model
download("https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth", "./models/sams/sam_vit_h_4b8939.pth")


# In[193]:


# Download SAM Vit L Model
download("https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth", "./models/sams/sam_vit_l_0b3195.pth")


# In[194]:


# Download SAM Vit B Model
download("https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth", "./models/sams/sam_vit_b_01ec64.pth")


# #### SAMS HQ

# In[195]:


sams_dir='./models/sams'


# In[ ]:


# Download SAM HQ Vit H Model
hf_hub_download(repo_id='lkeab/hq-sam', filename='sam_hq_vit_h.pth', local_dir=sams_dir)


# In[ ]:


# Download SAM HQ Vit L Model
hf_hub_download(repo_id='lkeab/hq-sam', filename='sam_hq_vit_l.pth', local_dir=sams_dir)


# In[ ]:


# Download SAM HQ Vit B Model
hf_hub_download(repo_id='lkeab/hq-sam', filename='sam_hq_vit_b.pth', local_dir=sams_dir)


# In[ ]:


# Download SAM HQ Vit Tiny Model
hf_hub_download(repo_id='lkeab/hq-sam', filename='sam_hq_vit_tiny.pth', local_dir=sams_dir)


# In[200]:


# Delete cache
get_ipython().system('rm -rf {sams_dir}/.cache')


# ### Download Clip Vision Model

# In[201]:


clip_vision_dir='./models/clip_vision'


# In[ ]:


# Download OpenAI Clip Vit Large Patch14
if os.path.exists(f"{clip_vision_dir}/clip-vit-large-patch14.safetensors"):
    pass
else:
    hf_hub_download(repo_id="openai/clip-vit-large-patch14", filename="model.safetensors", local_dir=clip_vision_dir)
    src=os.path.join(clip_vision_dir,"model.safetensors")
    dst=os.path.join(clip_vision_dir, "clip-vit-large-patch14.safetensors")
    os.rename(src, dst)


# In[ ]:


# Download Laion CLIP-ViT-H-14-laion2B-s32B-b79K
if os.path.exists(f"{clip_vision_dir}/CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors"):
    pass
else:
    hf_hub_download(repo_id="laion/CLIP-ViT-H-14-laion2B-s32B-b79K", filename="open_clip_pytorch_model.safetensors", local_dir=clip_vision_dir)
    src=os.path.join(clip_vision_dir,"open_clip_pytorch_model.safetensors")
    dst=os.path.join(clip_vision_dir, "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors")
    os.rename(src, dst)


# In[ ]:


# Download Laion CLIP-ViT-bigG-14-laion2B-39B-b160k
if os.path.exists(f"{clip_vision_dir}/CLIP-ViT-bigG-14-laion2B-39B-b160k.safetensors"):
    pass
else:
    hf_hub_download(repo_id="laion/CLIP-ViT-bigG-14-laion2B-39B-b160k", filename="open_clip_pytorch_model.safetensors", local_dir=clip_vision_dir)
    src=os.path.join(clip_vision_dir,"open_clip_pytorch_model.safetensors")
    dst=os.path.join(clip_vision_dir, "CLIP-ViT-bigG-14-laion2B-39B-b160k.safetensors")
    os.rename(src, dst)


# In[205]:


# Delete cache
get_ipython().system('rm -rf {clip_vision_dir}/.cache')

