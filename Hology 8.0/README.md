# Hology 8.0 - Crowd Counting via Density Map Estimation

## Problem Statement
Crowd counting is a significant challenge in Computer Vision, with applications ranging from public safety and urban planning to retail analytics. The objective of the Hology 8.0 competition is to accurately estimate the number of people in highly congested images where individual head detection is difficult due to occlusion and perspective distortion.

## Technical Methodology
The approach moves beyond simple object detection by employing **Density Map Estimation**, which treats crowd counting as a regression problem over the spatial domain of the image.

### Machine Learning Pipeline:
1.  **Density Map Generation**:
    *   Transforming point annotations (head coordinates) into continuous density maps using Gaussian kernels.
2.  **Model Architecture**:
    *   **Convolutional Neural Networks (CNN)**: Customized architectures designed to handle multi-scale features, ensuring that both small heads in the background and larger heads in the foreground are counted accurately.
    *   Dilated Convolutions: Used to expand the receptive field without losing spatial resolution, which is critical for dense crowd scenarios.
3.  **Data Augmentation**:
    *   Random cropping, horizontal flipping, and gamma correction to improve the model's robustness to different lighting and density levels.
4.  **Training Strategy**:
    *   Loss Function: Euclidean Loss (MSE) between the predicted and ground-truth density maps.
5.  **Performance Metric**:
    *   **Mean Absolute Error (MAE)**: The primary metric used to evaluate the average difference between the predicted count and the actual count.
    *   **Root Mean Squared Error (RMSE)**: Used to measure the variance and sensitivity to outliers in the predictions.
