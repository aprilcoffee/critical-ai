from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
import torch

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt",
    torch_dtype=torch.float16
).to("cuda")

image = load_image("image.png").resize((1024, 576))
frames = pipe(image).frames[0]
export_to_video(frames, "video.mp4", fps=7)
