# Statistics Explore 2024: Image Classification for Fire and Smoke Detection

## Project Overview
This repository contains the implementation for the **Statistics Explore 2024** competition, focusing on an image classification task. The primary objective is to detect and classify environmental conditions related to fire and smoke from image data, which is critical for early warning systems and disaster management.

## Problem Statement
The goal is to develop a robust deep learning model that can accurately categorize images into one of four distinct classes:
1.  **Fire**: Images containing active flames.
2.  **Smoke**: Images containing smoke without visible fire.
3.  **Smoke and Fire**: Images containing both active flames and smoke.
4.  **None**: Images with neither fire nor smoke (normal conditions).

## Dataset Description
The dataset is structured into training, validation, and testing sets, containing a total of several thousand images.
-   **Classes**: Fire, None, Smoke, Smoke and Fire.
-   **Distribution** (Approximate):
    -   **Fire**: ~1,230 images
    -   **None**: ~3,083 images
    -   **Smoke**: ~303 images
    -   **Smoke and Fire**: ~2,715 images
-   **Preprocessing**:
    -   Images are resized to **224x224** pixels.
    -   Pixel values are rescaled to the [0, 1] range.
    -   Data augmentation (Rotation, Shift, Shear, Zoom, Horizontal Flip) is applied to the training set to improve model generalization.

## Methodology
The solution leverages a Transfer Learning approach using the **EfficientNetB0** architecture, known for its efficiency and high performance in computer vision tasks.

### Technical Pipeline:
1.  **Base Model**: EfficientNetB0 (pre-trained on ImageNet, excluding the top layer).
2.  **Custom Head**:
    -   Global Average Pooling 2D layer.
    -   Dense layer with 1024 units and ReLU activation.
    -   Softmax Output layer with 4 units (corresponding to the classes).
3.  **Optimization**:
    -   **Optimizer**: Adam with a learning rate of 0.001.
    -   **Loss Function**: Categorical Crossentropy.
    -   **Metric**: Accuracy.

## Repository Structure
```text
.
├── Benchmark Model.ipynb      # Main notebook containing data pipeline and model training
└── README.md                  # Project documentation
```

## Getting Started
To run the notebook and reproduce the results, ensure you have the following dependencies installed:

```bash
pip install tensorflow matplotlib pandas pillow tqdm
```

### Usage
1.  Open `Benchmark Model.ipynb` in a Jupyter environment or Google Colab.
2.  Ensure the dataset is available in the expected directory structure (the notebook includes cells for dataset extraction and preparation).
3.  Run the cells sequentially to preprocess the data, build the model, and begin training.

## Evaluation
The model is evaluated based on its classification accuracy across the four categories. Detailed training logs and performance metrics (Accuracy/Loss curves) can be found within the `Benchmark Model.ipynb` file.
