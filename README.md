Repository Structure

Create a folder named Synthetic_ABSA_Project and organize it like this:

Synthetic_ABSA_Project/
│
├── data/
│   ├── twitter15_sample.csv   # Create a small sample CSV
│   └── generated_images/      # Folder to save output images
│
├── src/
│   ├── __init__.py
│   ├── generator.py           # Handles Stable Diffusion
│   ├── refiner.py             # Handles SAM and CLIP masking
│   └── classifier.py          # The fusion model
│
├── demo/
│   ├── analysis.ipynb         # The main notebook for the assignment
│   └── new_data.csv           # Your custom data for testing
│
├── requirements.txt
└── README.md



Requirement: Instructions for installation and usage.


# Synthetic Image ABSA

This project implements the method proposed in the EMNLP 2025 paper: **"Aspect-based Sentiment Analysis via Synthetic Image Generation"**.

## Project Description
The system generates synthetic images based on input text and aspect terms to provide visual context for sentiment analysis. It uses Stable Diffusion for generation and CLIP+BERT for classification.

Since the paper does not explicitly link a public repository in the abstract, we will follow Category B (Implementation of Method) or Category A (Reproduction if code is assumed). Below is the file structure and code you should create.

Since the paper was asked to provide a minimal implementation of the paper's method (or the closest approximation possible in class time), even if it is simpler than the original version, the code was trained to run on small data sets due to lack of resources.

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
