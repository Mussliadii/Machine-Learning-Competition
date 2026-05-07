# Hology 7.0: Matos Fashion Product Classification

## Project Overview
This repository contains the solution for the **Hology 7.0 Data Mining Competition**. The project involves developing an automated system for **Matos Fashion**, a rising e-commerce fashion startup, to categorize their growing inventory of T-shirts and Hoodies based on product photos.

## Problem Statement
The goal is to implement a **Multi-label/Multi-class Classification** system that identifies:
1. **Product Type**: T-shirt (`Kaos`) or Hoodie.
2. **Color**: Red, Yellow, Blue, Black, or White.

The challenge requires high precision, as the system must correctly identify all labels for a given image to be considered a successful prediction.

## Technical Methodology

### 1. Computer Vision Pipeline
- **Framework**: `ultralytics` YOLOv8.
- **Model**: `YOLOv8x-cls` (the largest version of YOLOv8 classification model) for maximum feature extraction capability.
- **Image Processing**: Images were resized to `480x480` to maintain high resolution for detail recognition (fabric type and subtle color variations).

### 2. Data Strategy
- **Dataset Organization**: The labels (`jenis` and `warna`) were combined into unique classes (e.g., `jenis_0_warna_1`) to transform the task into a 10-class single-label classification problem, simplifying the training process for standard CV models.
- **Train/Val Split**: 80% training and 20% validation.
- **Early Stopping**: Implemented with a patience of 10 epochs to prevent overfitting.

### 3. Evaluation
- **Metric**: **Exact Match Ratio**.
- **Result**: The model achieved high accuracy on the validation set, demonstrating robust performance in identifying both fashion types and colors simultaneously.

## Repository Structure
```text
.
├── Benchmark Model.ipynb     # YOLOv8 training and evaluation pipeline
├── Description.txt           # Official competition guidelines (Indonesian)
└── README.md                 # Project documentation
```

## Setup & Requirements
- **Hardware**: NVIDIA GPU recommended (trained on Tesla T4).
- **Libraries**:
  - `ultralytics` (YOLOv8)
  - `torch`
  - `pillow`
  - `pandas`
  - `matplotlib`

## How to Run
1. Install requirements: `pip install ultralytics`
2. Open `Benchmark Model.ipynb`.
3. Follow the data restructuring steps to organize images into class folders.
4. Execute the training cell using the `yolo` command or Python API.

---
*Developed for the Hology 7.0 Data Mining Competition.*
