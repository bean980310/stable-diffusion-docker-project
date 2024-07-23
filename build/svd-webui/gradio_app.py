# Adding this at the very top of app.py to make 'generative-models' directory discoverable
import argparse
import os
import sys

import math
import random
import uuid
from glob import glob
from pathlib import Path
from typing import Optional

import cv2
import gradio as gr
import numpy as np
import torch
from einops import rearrange, repeat
from fire import Fire
from huggingface_hub import hf_hub_download
from omegaconf import OmegaConf
from PIL import Image
from torchvision.transforms import ToTensor
from torchvision.transforms import functional as TF

from scripts.sampling.simple_video_sample import (
    get_batch,
    get_unique_embedder_keys_from_conditioner,
    load_model,
)
sys.path.append("generative-models")
# from scripts.util.detection.nsfw_and_watermark_dectection import DeepFloydDataFiltering
# from sgm.inference.helpers import embed_watermark
from sgm.util import default, instantiate_from_config

# To download all svd models
# hf_hub_download(repo_id="stabilityai/stable-video-diffusion-img2vid-xt", filename="svd_xt.safetensors", local_dir="checkpoints")
# hf_hub_download(repo_id="stabilityai/stable-video-diffusion-img2vid", filename="svd.safetensors", local_dir="checkpoints")
# hf_hub_download(repo_id="stabilityai/stable-video-diffusion-img2vid-xt-1-1", filename="svd_xt_1_1.safetensors", local_dir="checkpoints")

ckpt_dir="./models/ckeckpoints"

TYPE2PATH={
    "svd": ["stabilityai/stable-video-diffusion-img2vid", "svd.safetensors", ckpt_dir],
    "svd_xt": ["stabilityai/stable-video-diffusion-img2vid-xt", "svd_xt.safetensors", ckpt_dir],
    "svd_xt_1_1": ["stabilityai/stable-video-diffusion-img2vid-xt-1-1", "svd_xt_1_1.safetensors", ckpt_dir],
    "svd_image_decoder": ["stabilityai/stable-video-diffusion-img2vid", "svd_image_decoder.safetensors", ckpt_dir],
    "svd_xt_image_decoder": ["stabilityai/stable-video-diffusion-img2vid-xt", "svd_xt_image_decoder.safetensors", ckpt_dir],
    # "sv3d_u": ["stabilityai/sv3d", "sv3d_u.safetensors", ckpt_dir],
    # "sv3d_p": ["stabilityai/sv3d", "sv3d_p.safetensors", ckpt_dir]
}
repo_id, filename, local_dir=TYPE2PATH[version]

# Define the repo, local directory and filename
local_file_path = os.path.join(local_dir, filename)

os.makedirs("checkpoints", exist_ok=True)

# Check if the file already exists
if not os.path.exists(local_file_path):
    # If the file doesn't exist, download it
    hf_hub_download(repo_id=repo_id, filename=filename, local_dir=local_dir)
    print("File downloaded.")
else:
    print("File already exists. No need to download.")
    
parser=argparse.ArgumentParser()
parser.add_argument("--model_path", help="Specifies the model path.")
parser.add_argument("--outputs", help="Directory to save segmentation image.")
parser.add_argument("--port", help="Specifies the server port, default is 7860.", default=7860)
# parser.add_argument("--listen", help="Listen a IP Address, default is 0.0.0.0.", default="0.0.0.0")
args=parser.parse_args()

version = os.path.basename(args.model_path).split(".")[0]

if version == "svd":
    num_frames = 14
    num_steps = 25
    model_config = "scripts/sampling/configs/svd.yaml"
elif version == "svd_xt":
    num_frames = 25
    num_steps = 30
    model_config = "scripts/sampling/configs/svd_xt.yaml"
elif version == "svd_xt_1_1":
    num_frames = 25
    num_steps = 30
    model_config = "scripts/sampling/configs/svd_xt_1_1.yaml"
elif version == "svd_image_decoder":
    num_frames = 14
    num_steps = 25
    model_config = "scripts/sampling/configs/svd_image_decoder.yaml"
elif version == "svd_xt_image_decoder":
    num_frames = 25
    num_steps = 30
    model_config = "scripts/sampling/configs/svd_xt_image_decoder.yaml"
# elif version == "sv3d_u":
#     num_frames = 21
#     num_steps = 50
#     model_config = "scripts/sampling/configs/sv3d_u.yaml"
#     cond_aug = 1e-5
# elif version == "sv3d_p":
#     num_frames = 21
#     num_steps = 50
#     model_config = "scripts/sampling/configs/sv3d_p.yaml"
#     cond_aug = 1e-5
#     if isinstance(elevations_deg, float) or isinstance(elevations_deg, int):
#         elevations_deg = [elevations_deg] * num_frames
#     assert (
#         len(elevations_deg) == num_frames
#     ), f"Please provide 1 value, or a list of {num_frames} values for elevations_deg! Given {len(elevations_deg)}"
#     polars_rad = [np.deg2rad(90 - e) for e in elevations_deg]
#     if azimuths_deg is None:
#         azimuths_deg = np.linspace(0, 360, num_frames + 1)[1:] % 360
#     assert (
#         len(azimuths_deg) == num_frames
#     ), f"Please provide a list of {num_frames} values for azimuths_deg! Given {len(azimuths_deg)}"
#     azimuths_rad = [np.deg2rad((a - azimuths_deg[-1]) % 360) for a in azimuths_deg]
#     azimuths_rad[:-1].sort()
else:
    raise ValueError(f"Version {version} does not exist.")
device = "cuda" if torch.cuda.is_available() else "cpu"
max_64_bit_int = 2**63 - 1

model = load_model(
    model_config,
    device,
    num_frames,
    num_steps,
)

model.conditioner.cpu()
model.first_stage_model.cpu()
model.model.to(dtype=torch.float16)
torch.cuda.empty_cache()
model=model.requires_grad_(False)

def get_ckpt_dir():
    return os.environ.get("SVD_CKPT_PATH", ckpt_dir)

def sample(
    input_path: str = "assets/test_image.png",  # Can either be image file or folder with image files
    seed: Optional[int] = None,
    randomize_seed: bool = True,
    motion_bucket_id: int = 127,
    fps_id: int = 6,
    num_frames: Optional[int] = None,
    num_steps: Optional[int] = None,
    cond_aug: float = 0.02,
    resize_image: bool = False,
    decoding_t: int = 2,  # Number of frames decoded at a time! This eats most VRAM. Reduce if necessary.
    device: str = "cuda",
    output_folder: Optional[str] = "outputs",
    progress=gr.Progress(track_tqdm=True),
):
    """
    Simple script to generate a single sample conditioned on an image `input_path` or multiple images, one for each
    image file in folder `input_path`. If you run out of VRAM, try decreasing `decoding_t`.
    """
    fps_id = int(fps_id)  # casting float slider values to int)
    if randomize_seed:
        seed = random.randint(0, max_64_bit_int)

    torch.manual_seed(seed)

    path = Path(input_path)
    all_img_paths = []
    if path.is_file():
        if any([input_path.endswith(x) for x in ["jpg", "jpeg", "png"]]):
            all_img_paths = [input_path]
        else:
            raise ValueError("Path is not valid image file.")
    elif path.is_dir():
        all_img_paths = sorted(
            [
                f
                for f in path.iterdir()
                if f.is_file() and f.suffix.lower() in [".jpg", ".jpeg", ".png"]
            ]
        )
        if len(all_img_paths) == 0:
            raise ValueError("Folder does not contain any images.")
    else:
        raise ValueError

    for input_img_path in all_img_paths:
        with Image.open(input_img_path) as image:
            if image.mode == "RGBA":
                image = image.convert("RGB")
            w, h = image.size

            if h % 64 != 0 or w % 64 != 0:
                width, height = map(lambda x: x - x % 64, (w, h))
                image = image.resize((width, height))
                print(
                    f"WARNING: Your image is of size {h}x{w} which is not divisible by 64. We are resizing to {height}x{width}!"
                )

            image = ToTensor()(image)
            image = image * 2.0 - 1.0

        image = image.unsqueeze(0).to(device)
        H, W = image.shape[2:]
        assert image.shape[1] == 3
        F = 8
        C = 4
        shape = (num_frames, C, H // F, W // F)
        if (H, W) != (576, 1024):
            print(
                "WARNING: The conditioning frame you provided is not 576x1024. This leads to suboptimal performance as model was only trained on 576x1024. Consider increasing `cond_aug`."
            )
        if motion_bucket_id > 255:
            print(
                "WARNING: High motion bucket! This may lead to suboptimal performance."
            )

        if fps_id < 5:
            print("WARNING: Small fps value! This may lead to suboptimal performance.")

        if fps_id > 30:
            print("WARNING: Large fps value! This may lead to suboptimal performance.")

        value_dict = {}
        value_dict["motion_bucket_id"] = motion_bucket_id
        value_dict["fps_id"] = fps_id
        value_dict["cond_aug"] = cond_aug
        value_dict["cond_frames_without_noise"] = image
        value_dict["cond_frames"] = image + cond_aug * torch.randn_like(image)
        value_dict["cond_aug"] = cond_aug
        
        model.conditioner.cpu()
        model.first_stage_model.cpu()
        torch.cuda.empty_cache()
        model.sampler.verbose=True

        with torch.no_grad():
            with torch.autocast(device):
                batch, batch_uc = get_batch(
                    get_unique_embedder_keys_from_conditioner(model.conditioner),
                    value_dict,
                    [1, num_frames],
                    T=num_frames,
                    device=device,
                )
                c, uc = model.conditioner.get_unconditional_conditioning(
                    batch,
                    batch_uc=batch_uc,
                    force_uc_zero_embeddings=[
                        "cond_frames",
                        "cond_frames_without_noise",
                    ],
                )
                model.conditioner.cpu()
                torch.cuda.empty_cache()

                for k in ["crossattn", "concat"]:
                    uc[k] = repeat(uc[k], "b ... -> b t ...", t=num_frames)
                    uc[k] = rearrange(uc[k], "b t ... -> (b t) ...", t=num_frames)
                    c[k] = repeat(c[k], "b ... -> b t ...", t=num_frames)
                    c[k] = rearrange(c[k], "b t ... -> (b t) ...", t=num_frames)
                for k in uc.keys():
                    uc[k]=uc[k].to(dtype=torch.float16)
                    c[k]=c[k].to(dtype=torch.float16)

                randn = torch.randn(shape, device=device)

                additional_model_inputs = {}
                additional_model_inputs["image_only_indicator"] = torch.zeros(
                    2, num_frames
                ).to(device)
                additional_model_inputs["num_video_frames"] = batch["num_video_frames"]
                
                for k in additional_model_inputs:
                    if isinstance(additional_model_inputs[k]. torch.Tensor):
                        additional_model_inputs[k]=additional_model_inputs[k].to(
                            dtype=torch.float16
                        )

                def denoiser(input, sigma, c):
                    return model.denoiser(
                        model.model, input, sigma, c, **additional_model_inputs
                    )

                samples_z = model.sampler(denoiser, randn, cond=c, uc=uc)
                samples_z.to(dtype=model.first_stage_model.dtype)
                model.en_and_decode_n_samples_a_time = decoding_t
                model.first_stage_model.to(device)
                samples_x = model.decode_first_stage(samples_z)
                samples = torch.clamp((samples_x + 1.0) / 2.0, min=0.0, max=1.0)

                os.makedirs(output_folder, exist_ok=True)
                base_count = len(glob(os.path.join(output_folder, "*.mp4")))
                video_path = os.path.join(output_folder, f"{base_count:06d}.mp4")
                writer = cv2.VideoWriter(
                    video_path,
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    fps_id + 1,
                    (samples.shape[-1], samples.shape[-2]),
                )

                vid = (
                    (rearrange(samples, "t c h w -> t h w c") * 255)
                    .cpu()
                    .numpy()
                    .astype(np.uint8)
                )
                for frame in vid:
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    writer.write(frame)
                writer.release()

        return video_path, seed

def resize_image(image_path, output_size=(1024, 576)):
    image = Image.open(image_path)
    # Calculate aspect ratios
    target_aspect = output_size[0] / output_size[1]  # Aspect ratio of the desired size
    image_aspect = image.width / image.height  # Aspect ratio of the original image

    # Resize then crop if the original image is larger
    if image_aspect > target_aspect:
        # Resize the image to match the target height, maintaining aspect ratio
        new_height = output_size[1]
        new_width = int(new_height * image_aspect)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        # Calculate coordinates for cropping
        left = (new_width - output_size[0]) / 2
        top = 0
        right = (new_width + output_size[0]) / 2
        bottom = output_size[1]
    else:
        # Resize the image to match the target width, maintaining aspect ratio
        new_width = output_size[0]
        new_height = int(new_width / image_aspect)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        # Calculate coordinates for cropping
        left = 0
        top = (new_height - output_size[1]) / 2
        right = output_size[0]
        bottom = (new_height + output_size[1]) / 2

    # Crop the image
    cropped_image = resized_image.crop((left, top, right, bottom))

    return cropped_image

with gr.Blocks() as demo:
    gr.Markdown(
        """# Community demo for Stable Video Diffusion - Img2Vid - XT ([model](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt), [paper](https://stability.ai/research/stable-video-diffusion-scaling-latent-video-diffusion-models-to-large-datasets))
#### Research release ([_non-commercial_](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/main/LICENSE)): generate `4s` vid from a single image at (`25 frames` at `6 fps`). Generation takes ~60s in an A100. [Join the waitlist for Stability's upcoming web experience](https://stability.ai/contact).
  """
    )
    with gr.Row():
        with gr.Column():
            image = gr.Image(label="Upload your image", type="filepath")
            resize_image=gr.Checkbox(label="Enter Your custom size", value=True)
            generate_btn = gr.Button("Generate")
        video = gr.Video()
    with gr.Accordion("Advanced options", open=False):
        num_frames = gr.Slider(
            label="Frames",
            value=25,
            minimum=14,
            maximum=240,
        )
        num_steps=gr.Slider(
            label="Steps",
            value=25,
            minimum=1,
            maximum=100,
        )
        decoding_t=gr.Slider(
            label="Frames decoded at a time",
            value=2,
            minimum=1,
            maximum=10,
        )
        seed = gr.Slider(
            label="Seed",
            value=42,
            randomize=True,
            minimum=0,
            maximum=max_64_bit_int,
            step=1,
        )
        randomize_seed = gr.Checkbox(label="Randomize seed", value=True)
        motion_bucket_id = gr.Slider(
            label="Motion bucket id",
            info="Controls how much motion to add/remove from the image",
            value=127,
            minimum=1,
            maximum=255,
        )
        fps_id = gr.Slider(
            label="Frames per second",
            info="The length of your video in seconds will be 25/fps",
            value=6,
            minimum=5,
            maximum=30,
        )

    image.upload(fn=resize_image, inputs=image, outputs=image, queue=False)
    generate_btn.click(
        fn=sample,
        inputs=[image, seed, randomize_seed, motion_bucket_id, fps_id],
        outputs=[video, seed],
        api_name="video",
    )

if __name__ == "__main__":
    demo.queue(max_size=20)
    demo.launch(share=True)
