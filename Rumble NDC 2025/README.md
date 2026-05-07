# Classification Rumble: Neurontara Data Clash 2025

## Project Overview
This repository contains the machine learning solution for the **Classification Rumble** competition, part of the **Neurontara Data Clash (NDC) 2025**. The goal of the competition is to build a classification model that predicts the quality grade of freshwater measurements collected globally.

## Problem Statement
Water quality monitoring is essential for environmental health. This challenge focuses on classifying records from the **UNEP GEMS/Water Global Freshwater Quality Archive (1906-2023)** into four quality categories:
- **Good**
- **Fair**
- **Unknown**
- **Pending Review**

The evaluation metric is the **Macro-averaged F1-score**, which requires strong performance across all classes, especially minority ones.

## Dataset
The dataset includes a wide range of features:
- **In-situ Readings:** Chemical and physical measurements (e.g., parameter codes, values).
- **Lab Workflow:** Analysis methods, laboratory information, and validation status.
- **Climate Data:** Temperature, rainfall, humidity, drought index, and extreme precipitation days.
- **Catchment & Ecology:** Land use percentages (urban, forest, agriculture, etc.) and landscape fragmentation.
- **Industrial Impact:** Proximity to industrial facilities and proxy scores for mercury/lead impacts.

## Methodology
The technical pipeline implemented in the project involves:

### 1. Data Preprocessing & Cleaning
- **Value Extraction:** Regex-based extraction of numeric values and units from the `value_with_unit` column.
- **Temporal Analysis:** Decomposition of the `time_season` column into distinct datetime and seasonal features.
- **Missing Value Imputation:** Advanced multivariate imputation using **IterativeImputer (MICE)** with Random Forest as the estimator for numeric and ordinal columns.

### 2. Feature Engineering
- **Ratios & Indices:** Creation of derived features such as `temp_humidity_ratio`, `climate_stress_index`, and `soil_buffer_ratio`.
- **Land Cover Grouping:** Aggregating granular land use data into broader categories like `green_cover` and `built_cover`.
- **Industrial Risk:** Composing a `total_industrial_risk` score from multiple impact proxies.

### 3. Model Development
- **Handling Imbalance:** Utilization of oversampling techniques (Resampling) to balance the target classes.
- **Algorithms:** Implementation and hyperparameter tuning of gradient boosting frameworks including:
    - **CatBoost**
    - **LightGBM**
    - **XGBoost**
- **Validation:** Extensive use of cross-validation and macro-F1 scoring to ensure robust generalization.

## Directory Structure
- `train.csv`: Labeled training data.
- `test.csv`: Test data for competition submission.
- `Benchmark Model.ipynb`: Main analysis and modeling notebook.
- `Compettition Desc.txt`: Detailed competition requirements and column guide.
- `sample_submission.csv`: Formatting guide for submissions.

## Getting Started
To run the solution:
1. Ensure you have the required libraries installed (`pandas`, `numpy`, `scikit-learn`, `catboost`, `lightgbm`, `xgboost`, `imblearn`).
2. Open `Benchmark Model.ipynb` in a Jupyter environment.
3. Update the data paths if necessary and execute the cells to preprocess data, train models, and generate predictions.

---
*Developed for the Neurontara Data Clash 2025.*
