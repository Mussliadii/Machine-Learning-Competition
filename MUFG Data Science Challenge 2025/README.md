# MUFG Data Science Challenge 2025: Small Business Loan Default Prediction

## Project Overview
This repository contains the solution for the **MUFG Data Science Challenge 2025**, an exclusive competition for students hosted on **SIGNATE**. The task involves analyzing loan data for small and medium-sized enterprises (SMEs) to predict whether they will successfully repay their loans or default.

## Problem Statement
The objective is to build a robust binary classification model to determine the risk of default. This is a critical task in financial services, where accurate risk assessment helps in maintaining a healthy lending portfolio while supporting enterprise growth.

## Dataset Description
The dataset includes various features related to loan conditions and enterprise attributes:
- **Loan Terms**: `GrossApproval` (Total loan amount), `SBAGuaranteedApproval` (Guaranteed portion), `InitialInterestRate`, `TermInMonths`, `FixedOrVariableInterestInd`.
- **Enterprise Attributes**: `NaicsSector` (Industry sector), `BusinessType` (Corporation, Individual, etc.), `BusinessAge`, `JobsSupported`.
- **Target Variable**: `LoanStatus` (Binary: 1 for Default, 0 for Rejection/Success - *Note: Based on the tutorial, it targets the risk of non-payment*).

## Technical Methodology

### 1. Exploratory Data Analysis (EDA)
- Visualized data distributions using `matplotlib` and `seaborn`.
- Analyzed correlations between interest rates, loan terms, and default rates.
- Checked for missing values (none found in this specific dataset).

### 2. Preprocessing & Feature Engineering
- **Dummy Encoding**: Converted categorical variables like `NaicsSector`, `BusinessType`, and `BusinessAge` into numerical format using one-hot encoding.
- **Handling Inconsistencies**: Ensured feature alignment between training and test sets by removing columns that appeared in one but not the other (e.g., specific rare industry sectors).

### 3. Machine Learning Model
- **Algorithm**: **LightGBM** (Gradient Boosting Decision Tree).
- **Validation Strategy**: **Stratified K-Fold Cross-Validation** (5 Folds) to ensure model stability and generalization across different data splits.
- **Metric**: **F1 Score (Binary)**, which balances precision and recall for the minority class (default).

## Repository Structure
```text
.
├── Benchmark Model.ipynb     # LightGBM training and cross-validation pipeline
├── Desc Competition.txt      # Official competition description (Japanese)
└── README.md                 # Project documentation
```

## Setup & Requirements
- **Environment**: Python 3.x, Google Colab (recommended).
- **Libraries**:
  - `pandas`, `numpy`
  - `lightgbm`
  - `scikit-learn`
  - `matplotlib`, `seaborn`

## How to Run
1. Open `Benchmark Model.ipynb` in Google Colab.
2. Mount your Google Drive to access the dataset files.
3. Run the cells sequentially to perform data loading, preprocessing, model training, and inference.
4. The final predictions will be saved in a submission format.

---
*Developed for the MUFG Data Science Challenge 2025.*
