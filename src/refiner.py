## This implements the Visual Refinement (SAM + CLIP).

import torch
from segment_anything import sam_model_registry, SamPredictor
import clip
from PIL import Image
import numpy as np
class VisualRefiner:
    def __init__(self, device='cuda' if torch.cuda.is_available() else 'cpu'):
        self.device = device
        self.clip_model, self.preprocess = clip.load("ViT-B/32", device=device)
        self.sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h_4b8939.pth")
        self.sam.to(device=device)
        self.predictor = SamPredictor(self.sam)
    def refine(self, image_path, aspect_text):
        image = Image.open(image_path).convert("RGB")
        img_np = np.array(image)
        self.predictor.set_image(img_np)
        masks, _, _ = self.predictor.predict(multimask_output=False)
        mask = masks[0]
        refined_img = img_np * mask[:, :, None]
        return Image.fromarray(refined_img)
