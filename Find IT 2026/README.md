# Find IT 2026 - Face Anti-Spoofing

## Problem Statement
The "Find IT 2026" competition focuses on the critical security task of **Face Anti-Spoofing**. The goal is to distinguish between "live" faces (real human presence) and "spoof" attacks (e.g., photos, videos, or masks presented to a camera). This technology is essential for securing biometric authentication systems against fraudulent access attempts.

## Technical Methodology
The solution employs a hybrid Computer Vision approach, combining advanced feature extraction from Transformer-based models with high-speed object detection architectures.

### Machine Learning Pipeline:
1.  **Feature Extraction**:
    *   **ConvNeXt-Base**: Utilized as a powerful backbone for deep feature extraction. ConvNeXt architectures modernize standard CNNs with Transformer-like design choices, offering exceptional accuracy in image classification tasks.
2.  **Detection Framework**:
    *   **YOLOv8-Nano**: Integrated for efficient face detection and real-time processing capabilities. This lightweight model ensures that the system can quickly localize faces before performing anti-spoofing verification.
3.  **Preprocessing & Augmentation**:
    *   Dynamic resizing and normalization of input frames.
    *   Augmentation techniques (brightness adjustment, rotation, noise injection) to improve model robustness against varying environmental conditions.
4.  **Model Training**:
    *   Fine-tuning the ConvNeXt-Base model on a specialized dataset containing both live and spoofed samples.
    *   Optimization using weighted loss functions to handle potential class imbalances.
5.  **Performance Evaluation**:
    *   Evaluated using metrics such as EER (Equal Error Rate) and HTER (Half Total Error Rate) to minimize both false acceptances and false rejections.
