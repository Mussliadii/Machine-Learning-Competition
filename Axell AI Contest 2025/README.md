# Axell AI Contest 2025 - Product Detection

This repository contains the development environment and sample code for the **Axell AI Contest 2025**, focusing on object detection for retail products (beverages).

## 🚀 Overview
The goal of this competition is to accurately detect and classify various beverage products (cans, bottles, etc.) in different environments. The project utilizes the **YOLO (You Only Look Once)** architecture, specifically the latest versions supported by **Ultralytics**.

## 📊 Dataset Information
The dataset consists of multiple beverage categories, including:
- Various types of Coffee (Black, Latte, Sweet, Light Sugar)
- Teas (Green, Oolong, Barley)
- Soft Drinks (Cola, Soda, Ginger Ale, Juice)
- Energy Drinks and Water

The dataset is structured in the **Ultralytics YOLO format** within the `ultralytics_dataset` directory, containing:
- `images/`: Training and validation images.
- `labels/`: Annotation files in YOLO format.
- `data.yaml`: Dataset configuration file defining the 91 object classes.

## 📂 Project Structure
```text
Axell AI Contest 2025/
├── ultralytics_dataset/    # Dataset root (Images & YOLO Labels)
├── train_sample/           # Training scripts and notebooks
│   ├── train.py           # Python script for training
│   ├── train.ipynb        # Jupyter Notebook for local training
│   └── train_colab.ipynb  # Google Colab compatible notebook
├── sample_submit/          # Submission template structure
└── yolov8n.pt              # Pre-trained YOLOv8 nano model
```

## 🛠 Setup and Training
To get started with training:

### 1. Environment Setup
It is recommended to use a Conda environment:
```bash
conda create -n axell_ai python=3.12
conda activate axell_ai
pip install ultralytics torch torchvision
```

### 2. Training
You can run the training using the provided Python script or notebooks. 
Example using the script:
```bash
python train_sample/train.py \
    -c ultralytics_dataset/data.yaml \
    -m yolo11n \
    -o ./output
```

## 📈 Evaluation
Models are evaluated based on their detection accuracy. The best performing model weights (`best.pt`) should be used for the final submission.

## 📦 Submission Format
The final submission should be a ZIP file containing the following structure:
```text
submit/
├── model/
│   └── best.pt             # Your trained model weights
├── src/
│   └── predictor.py        # Prediction logic
└── requirements.txt        # Dependencies
```

---
*Note: This project is part of the Axell AI Contest 2025 competition.*
