from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sdxl-turbo",
    torch_dtype=torch.float16
).to("cuda")

image = pipe("a cat in space", num_inference_steps=4, guidance_scale=0.0).images[0]
image.save("image.png")
