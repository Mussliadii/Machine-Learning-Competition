# Rasio 9.0 - Daily CO2 Emission Prediction

## Problem Statement
The Rasio 9.0 competition focuses on environmental sustainability, specifically the task of predicting daily carbon dioxide ($CO_2$) emissions. By analyzing patterns in traffic, weather, and public transportation ridership, this project aims to create a predictive tool that can estimate the carbon footprint of urban activities.

## Technical Methodology
The project employs a multi-model ensemble approach to handle the high variance and complexity of environmental and urban data.

### Machine Learning Pipeline:
1.  **Feature Engineering**:
    *   Processing vehicle counts (Cars, Buses, Trucks) during peak and off-peak hours.
    *   Integrating weather conditions (Seasons, UV Index, Moon Phase) and holiday indicators.
    *   Analyzing public transportation ridership data.
2.  **Model Selection**:
    *   **XGBoost Regressor**: Selected as the final model for its efficiency and strong performance on structured datasets.
    *   **LightGBM & CatBoost**: Used for hyperparameter tuning and benchmarking.
    *   **Random Forest & SVR**: Implemented to provide diverse baseline comparisons.
3.  **Hyperparameter Optimization**:
    *   Utilizing `GridSearchCV` to fine-tune learning rates, depth, and estimators for LightGBM and CatBoost.
4.  **Data Preprocessing**:
    *   Dropping features with high missing value percentages (>75%).
    *   Handling categorical data through specialized boosters.
5.  **Evaluation**:
    *   Performance is assessed using Root Mean Squared Error (RMSE) to penalize larger prediction errors in $CO_2$ estimation.
