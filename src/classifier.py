## A simplified Multimodal Classifier logic.

import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer
import clip
class MultimodalABSA(nn.Module):
    def __init__(self, text_model_name="bert-base-uncased", device='cuda'):
        super().__init__()
        self.device = device
        self.text_encoder = AutoModel.from_pretrained(text_model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(text_model_name)
        self.clip_model, _ = clip.load("ViT-B/32", device=device)
        self.fc = nn.Linear(768 + 512, 3)
    def forward(self, text, image):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(self.device)
        text_emb = self.text_encoder(**inputs).last_hidden_state[:, 0, :]
        image_emb = self.clip_model.encode_image(image).float()
        combined = torch.cat((text_emb, image_emb), dim=1)
        output = self.fc(combined)
        return output
