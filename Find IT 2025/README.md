# Find IT 2025: COPPA Risk Prediction

## Project Overview
This repository contains the solution for the **Find IT 2025 Data Science Competition**. The project focuses on predicting the **COPPA (Children's Online Privacy Protection Act) risk** of mobile applications based on their metadata. Ensuring privacy compliance is critical in the digital age, especially for applications targeting or accessible to children.

## Problem Statement
The objective is to build a binary classification model that determines whether an application poses a high risk of COPPA non-compliance (`coppaRisk = True`) or is low risk (`coppaRisk = False`). The prediction is based on various attributes such as developer country, genre, user ratings, app age, and the presence of privacy links.

## Dataset Description
The dataset consists of 7,000 application records with the following features:
- **developerCountry**: The country where the app developer is based.
- **countryCode**: The ISO country code.
- **userRatingCount**: The total number of ratings received by the app.
- **primaryGenreName**: The main category of the application (e.g., Entertainment, Business).
- **deviceType**: The primary device the app is designed for (e.g., Global, Tablet).
- **hasPrivacyLink**: Boolean indicating if a privacy policy link is provided.
- **appAge**: The age of the application in months.
- **appDescriptionBrandSafetyRating**: Safety rating of the app description (Low, Medium, High).
- **mfaRating**: Made-for-Advertising (MFA) rating.
- **Target Variable**: `coppaRisk` (Binary: True/False).

## Methodology

### 1. Exploratory Data Analysis (EDA)
- Analyzed feature distributions and correlation with the target variable.
- Identified significant class imbalance in the `coppaRisk` labels.

### 2. Preprocessing & Feature Engineering
- **Handling Missing Values**: Categorical imputation for unknown countries and genres.
- **Encoding**: Label Encoding for categorical variables and Ordinal Mapping for risk ratings.
- **Balancing**: Addressed class imbalance using **Random Resampling (Upsampling)** to ensure the model does not bias towards the majority class.

### 3. Machine Learning Model
- **Algorithm**: `RandomForestClassifier`.
- **Logic**: An ensemble of decision trees used to capture complex non-linear relationships between app metadata and compliance risk.
- **Validation**: Evaluated using metrics suitable for imbalanced datasets, primarily focusing on **AUC (Area Under Curve)**.

## Repository Structure
```text
.
├── Benchmark Model.ipynb     # Main notebook for EDA, Preprocessing, and Modeling
├── Description.txt           # Official competition task description
└── README.md                 # Project documentation
```

## Getting Started
### Dependencies
- Python 3.x
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

### Usage
1. Open `Benchmark Model.ipynb` in a Jupyter environment or Google Colab.
2. Ensure the dataset files are placed in the appropriate directory.
3. Run the cells to execute the preprocessing and training pipeline.

---
*Developed as part of the Find IT 2025 Data Science Competition.*
