# Synthetic Image-Based Multimodal Aspect-Based Sentiment Analysis

This repository presents a **multimodal Aspect-Based Sentiment Analysis (ABSA) framework**
that integrates **synthetic image generation**, **visual refinement**, and
**joint vision–language classification**.

The proposed system is designed as a research-oriented pipeline
to investigate the role of synthetic visual data in multimodal ABSA tasks.

---

## Repository Structure
```text
Synthetic_ABSA_Project/
│
├── src/
│   ├── generator.py      # Synthetic image generation from text and aspects
│   ├── refiner.py        # Optional refinement of generated images
│   ├── classifier.py    # Aspect-based sentiment classifier
│
├── demo/
│   └── analysis.ipynb    # End-to-end training and testing pipeline
│
├── PresentationFiles/   # Presentation and supplementary materials
│
├── requirements.txt
└── README.md
```

---
## Baseline and Ablation Studies

We include a text-only ABSA baseline by nullifying the visual input,
allowing direct comparison between textual and multimodal settings.
This baseline is implemented by replacing the image tensor with a zero-valued tensor
while keeping the multimodal architecture unchanged.
Additionally, we perform a lightweight ablation study comparing
raw synthetic images and visually refined images to assess the impact
of visual refinement on sentiment prediction.
The ablation study is conducted at inference time only and does not
involve additional model training.

## Deviation from the Original Paper

The original EMNLP paper proposes supervised fine-tuning of diffusion models
and large-scale sentiment-aware dataset construction.
Due to the absence of public training code and limited computational resources,
this project focuses on a lightweight, executable prototype that demonstrates
the core ideas rather than reproducing the full training pipeline.

## Methodology Overview

The framework follows a **sequential processing pipeline** consisting of four stages:

1. Synthetic Image Generation  
2. Visual Refinement  
3. Multimodal Sentiment Classification  
4. Experimental Analysis  

Each stage depends on the outputs produced by the preceding stage.

---

## 1. Synthetic Image Generation

**File:** `src/generator.py`

This module generates synthetic images conditioned on:
- the input text,
- the target aspect term,
- the associated sentiment label.

A pre-trained **Stable Diffusion** model is employed to simulate
a controllable image generation process guided by textual prompts.

**Output:**  
A synthetic image stored on disk for subsequent processing.

---

## 2. Visual Refinement

**File:** `src/refiner.py`

This stage aims to enhance the relevance of the generated image
by isolating visually meaningful regions related to the target aspect.

The module utilizes:
- the **Segment Anything Model (SAM)** for image segmentation,
- **CLIP-based representations** to preserve semantic consistency.

**Input:**  
Synthetic image generated in Stage 1.

**Output:**  
A refined image emphasizing aspect-relevant visual content.

---

## 3. Multimodal ABSA Classification

**File:** `src/classifier.py`

This module performs sentiment classification using both textual
and visual modalities.

- Textual features are extracted using **BERT**.
- Visual features are extracted using **CLIP**.
- The fused representation is used for three-class sentiment prediction:
  *Positive*, *Neutral*, and *Negative*.

**Input:**  
- Text input  
- Refined image from Stage 2  

**Output:**  
Predicted sentiment label.

---

## 4. Demonstration and Analysis

**Location:** `demo/analysis.ipynb`

The notebook serves as the experimental and analytical component of the project.
It integrates the individual modules, executes the complete pipeline,
and presents qualitative and quantitative observations.

The notebook functions as the primary orchestration layer of the framework.

---

## Execution Procedure

To obtain valid outputs, the following execution order must be followed:

1. Environment setup and dependency installation  
2. Synthetic image generation (`generator.py`)  
3. Visual refinement (`refiner.py`)  
4. Multimodal sentiment classification (`classifier.py`)  
5. Execution of `demo/analysis.ipynb`

Deviation from this order may result in missing or invalid intermediate results.

---

## Dependencies and Requirements

Key dependencies include:
- PyTorch
- HuggingFace Transformers
- Diffusers
- CLIP
- Segment Anything Model (SAM)
- NumPy, PIL

Pre-trained model weights (e.g., SAM checkpoints) must be available prior to execution.

All required Python packages are listed in requirements.txt.
---

## Scope and Limitations

- The framework is intended for **research and experimental purposes**.
- The use of pre-trained models assumes access to adequate computational resources.
- The focus is on pipeline design and multimodal integration rather than deployment.

---

## Summary

This repository implements a coherent and logically ordered multimodal ABSA pipeline.
When executed in the specified order, the framework produces consistent intermediate
and final outputs, which are analyzed in the provided demonstration notebook.

## Presentation Materials

The `PresentationFiles` directory contains presentation slides and supplementary materials used to explain the project methodology and results.
