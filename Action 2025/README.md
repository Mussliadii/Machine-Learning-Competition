# 🍱 Data Mining Action 2025: Indonesian Food Object Detection

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8-green.svg)](https://github.com/ultralytics/ultralytics)
[![Competition](https://img.shields.io/badge/Competition-Data%20Mining%20Action-orange.svg)]()

This repository contains the implementation of a high-performance object detection model for identifying various types of Indonesian traditional cuisine. Developed for the **Data Mining Action 2025** competition, the project leverages state-of-the-art computer vision techniques to automate the classification and localization of food items in images.

## 🚀 Overview

Indonesian cuisine is diverse and visually rich. This project aims to build a robust model capable of detecting 15 distinct classes of popular Indonesian dishes. We utilized the **YOLOv8 (You Only Look Once)** architecture by Ultralytics, known for its exceptional balance between speed and accuracy.

### Key Features
- **Real-time Detection**: Optimized for fast inference without compromising precision.
- **Data Augmentation**: Robust training pipeline including mosaic, blur, and geometric transformations.
- **Indonesian Cuisine Focus**: Specially trained on a curated dataset of traditional dishes.
- **Cloud Ready**: Designed for seamless execution on Google Colab or local GPU environments.

## 📊 Dataset & Classes

The model is trained to recognize the following **15 classes**:

| Category | Food Item | Category | Food Item |
| :--- | :--- | :--- | :--- |
| 🍗 | Ayam Bakar | 🍜 | Bakso |
| 🍗 | Ayam Betutu | 🥘 | Coto Makassar |
| 🍗 | Ayam Goreng | 🥗 | Gado-Gado |
| 🍗 | Ayam Pop | 🍲 | Gudeg |
| 🍚 | Nasi Goreng | 🍡 | Pempek |
| 🥩 | Rawon | 🥩 | Rendang |
| 🍢 | Sate Madura | 🍢 | Sate Padang |
| 🍲 | Soto | | |

## 🏗️ Model Architecture

We employed **YOLOv8 Nano (yolov8n)** as the base architecture to ensure lightweight deployment while maintaining competitive accuracy.

- **Framework**: `ultralytics`
- **Training Epochs**: 200
- **Image Size**: 640x640
- **Optimizations**: Automatic Mixed Precision (AMP), AdamW Optimizer, and Albumentations-based augmentation.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10+
- CUDA-enabled GPU (recommended for training)

### Installation
```bash
# Clone the repository
git clone https://github.com/username/data-mining-action-2025.git

# Install dependencies
pip install ultralytics albumentations
```

## 💻 Usage

### Training
The training process is automated in the `Benchmark Model.ipynb` notebook. To start training manually:
```python
from ultralytics import YOLO

# Load a pretrained model
model = YOLO('yolov8n.pt')

# Train the model
results = model.train(
    data='data.yaml',
    epochs=200,
    imgsz=640,
    batch=32,
    name='action_model_augmented'
)
```

### Inference
```python
# Load the best trained model
model = YOLO('runs/detect/action_model_augmented/weights/best.pt')

# Run inference on an image
results = model.predict('test_image.jpg', conf=0.25)

# Show results
results[0].show()
```

## 📈 Performance

The model shows strong performance across the evaluation metrics:
- **mAP50**: High precision in localized food detection.
- **Inference Speed**: ~8-15ms per image on a Tesla T4 GPU.

## 📝 License

This project is part of a submission for the Data Mining Action 2025 Competition. All rights reserved by the development team.

---
*Built with ❤️ for Indonesian Culinary Heritage.*
