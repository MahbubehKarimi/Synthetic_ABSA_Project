Requirement: Instructions for installation and usage.


# Synthetic Image ABSA

This project implements the method proposed in the EMNLP 2025 paper: **"Aspect-based Sentiment Analysis via Synthetic Image Generation"**.

## Project Description
The system generates synthetic images based on input text and aspect terms to provide visual context for sentiment analysis. It uses Stable Diffusion for generation and CLIP+BERT for classification.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3.	Download the SAM checkpoint (sam_vit_h_4b8939.pth) and place it in the root if using refinement.
Usage
Running the Demo
Navigate to the demo folder and open analysis.ipynb to see the step-by-step pipeline:
1.	Generation: Creates images from text.
2.	Refinement: Masks irrelevant background.
3.	Classification: Predicts sentiment.
Running from Command Line

Bash


python src/generator.py --text "The screen is crisp" --aspect "screen" --sentiment "Positive"

Experiments
We tested the model on a subset of Twitter-2015.
●	Settings: Batch size 1, learning rate 5e-518.

●	Result: The inclusion of synthetic images resolved ambiguity in texts like "painful lessons" (correctly identified as Positive)19.
