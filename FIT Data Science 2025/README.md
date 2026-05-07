# FIT Data Science 2025 - Global Air Pollution Prediction

## Problem Statement
The FIT Data Science 2025 competition focuses on analyzing and predicting global air pollution levels. With increasing urbanization and industrialization, air quality has become a critical environmental concern. The goal of this project is to develop a predictive model that can estimate the Air Quality Index (AQI) based on various environmental and geographical factors, helping policymakers and citizens understand and mitigate health risks.

## Technical Methodology
The project utilizes a robust tabular data science pipeline, ranging from exploratory data analysis to complex ensemble modeling.

### Machine Learning Pipeline:
1.  **Exploratory Data Analysis (EDA)**:
    *   Analyzing the distribution of pollutants such as CO, NO2, O3, and PM2.5.
    *   Identifying geographical trends and correlations between industrial activity and AQI levels.
2.  **Data Preprocessing**:
    *   Handling missing values through median imputation.
    *   Feature scaling using `StandardScaler` to ensure uniform influence across numerical variables.
    *   Categorical encoding for country and city-level data.
3.  **Model Selection**:
    *   **Linear Regression**: Used as a baseline to establish fundamental linear relationships.
    *   **Random Forest Regressor**: Employed to capture non-linear patterns and complex interactions between pollutants.
4.  **Hyperparameter Tuning**:
    *   Utilizing `GridSearchCV` to optimize parameters such as the number of trees and maximum depth for the Random Forest model.
5.  **Evaluation**:
    *   Measured using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess the accuracy of AQI predictions.
