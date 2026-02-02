##This script implements the Image Generation logic using a pre-trained Stable Diffusion model (simulating the fine-tuned version for the assignment constraint).

import torch
from diffusers import StableDiffusionPipeline

import torch
from diffusers import StableDiffusionPipeline
class SyntheticGenerator:
    def __init__(self, device='cuda' if torch.cuda.is_available() else 'cpu'):
        self.device = device
        self.pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
        self.pipe.to(self.device)
    def generate(self, text, aspect, sentiment, output_path):
        prompt = f"A photo of {aspect} showing {sentiment} sentiment. Context: {text}"
        image = self.pipe(prompt).images[0]
        image.save(output_path)
        return image
