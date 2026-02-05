# Synthetic Image ABSA

This repository contains an implementation of an Aspect-Based Sentiment Analysis (ABSA) pipeline that leverages synthetic image generation to enrich textual sentiment understanding.

The project follows a modular design where the core functionalities are implemented as reusable Python modules, and the full pipeline is demonstrated in a Jupyter Notebook.

---

## Project Structure

Synthetic_ABSA_Project/
├── src/
│ ├── generator.py # Synthetic image generation from text and aspects
│ ├── refiner.py # Optional refinement of generated images
│ └── classifier.py # Aspect-based sentiment classifier
├── demo/
│ └── analysis.ipynb # End-to-end demo: training and testing pipeline
├── PresentationFiles/ # Presentation and supplementary materials
├── requirements.txt
└── README.md


---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MahbubehKarimi/Synthetic_ABSA_Project.git
   cd Synthetic_ABSA_Project

pip install -r requirements.txt

## Running the Demo

The main entry point of the project is a Jupyter Notebook that demonstrates the complete pipeline.

Important:
Jupyter Notebook must be launched from the project root directory to ensure correct module imports.

1. Start Jupyter Notebook
2. Open the notebook demo/analysis.ipynb
3. Run the cells sequentially to execute the pipeline.


## Pipeline Overview

The demo notebook performs the following steps:

1. Synthetic Image Generation
Images are generated from input text and aspect terms using the generation module.

2. Refinement (Optional)
Generated images can be refined to reduce irrelevant visual information.

3. Model Training and Testing
The classifier is trained and evaluated using the generated (and refined) data.

All core logic is implemented in the src directory and imported into the demo notebook.

Notes

This repository focuses on demonstrating the methodology and pipeline rather than large-scale training.

The implementation is designed to run on limited computational resources.

The notebook serves as both documentation and an executable example of the system.

## Requirements

All required Python packages are listed in requirements.txt.

## Presentation Materials

The `PresentationFiles` directory contains presentation slides and supplementary materials used to explain the project methodology and results.
