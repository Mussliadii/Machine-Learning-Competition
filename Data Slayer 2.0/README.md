# Data Slayer 2.0: Motion Matters

## Project Overview
This repository contains the machine learning solution for **Data Slayer 2.0**, a national-level competition organized as part of **DINAMIKA 5.0** by the Data Science Study Program at **Telkom University Purwokerto**.

The competition theme, **"Motion Matters: Human Fall Detection Classification for Safety Insight,"** focuses on developing robust classification models to identify human falls, which is a critical safety concern for the elderly and high-risk workers.

## Objective
The goal is to build an accurate image classification model that can distinguish between various types of human falls and normal activities. Accurate detection is vital for providing rapid assistance and reducing the severity of injuries caused by falls.

## Dataset & Classes
The project classifies human motion into 12 distinct categories:
- **Fall Categories:** `backward_falls`, `forward_falls`, `left_falls`, `right_falls`, `sitting_falls`, `standing_falls`.
- **Other Activities:** `jumping`, `laying`, `picking`, `squat`, `stretching`, `walking`.

## Methodology
The solution leverages state-of-the-art computer vision models for image classification.

### 1. Model Architecture
- **Framework:** `ultralytics` (YOLO).
- **Base Model:** `yolo11m-cls.pt` (YOLOv11 medium classification model).
- **Why YOLOv11?** YOLOv11 provides an excellent balance between speed and accuracy, making it suitable for real-time safety monitoring applications.

### 2. Training Configuration
- **Epochs:** 20
- **Image Size:** 256x256 pixels
- **Batch Size:** 32
- **Data Splitting:** 80% Training, 20% Validation.

### 3. Evaluation Metric
The primary metric for this competition is **Accuracy**, measuring the percentage of correctly classified motions across the test dataset.

## Repository Structure
- `Notebook_Saran Nama Tim.ipynb`: The main Jupyter notebook containing data preprocessing, model training, and evaluation logic.
- `Competition Desc.txt`: Official competition overview and background details.
- `runs/`: (Generated after training) Contains training logs, model weights, and performance plots.

## Getting Started
To reproduce the training process:
1. Install the required dependencies:
   ```bash
   pip install ultralytics
   ```
2. Mount your dataset (e.g., via Google Drive if using Colab).
3. Open `Notebook_Saran Nama Tim.ipynb` and follow the cells to:
   - Extract and preprocess the dataset.
   - Initialize and train the YOLOv11 classifier.
   - Export the best weights for inference.

---
*Developed for the DINAMIKA 5.0 Competition.*
