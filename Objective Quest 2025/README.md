# Objective Quest 2025: Dataquest

## Project Overview
This repository contains the machine learning solution for **Objective Quest**, a data science competition held as part of **DATAQUEST 2025**. The event is organized by the Data Science Technology Student Association (Himpunan Mahasiswa Teknologi Sains Data) of the Faculty of Advanced Technology and Multidisciplinary at **Universitas Airlangga**.

The challenge focuses on the application of **Natural Language Processing (NLP)** and **Regression** techniques to the legal domain in Indonesia.

## Problem Statement
Indonesia follows a civil law system where written statutes are the primary source of law, but judicial precedents (jurisprudence) play a vital role in ensuring consistency. With approximately 100,000 new court decisions added every month, manually analyzing these documents to understand sentencing trends is highly labor-intensive.

**Task:** Build a predictive model that can estimate the length of imprisonment (in months) for a criminal case based solely on the text narrative of the court decision.

## Dataset
- `train.csv`: Training metadata including document IDs and the target variable (`lama hukuman (bulan)`).
- `test.csv`: Metadata for the test set.
- `file_putusan/`: A collection of text files containing the raw judicial decisions.
- `sample_submission.csv`: Example format for final predictions.

## Methodology
The technical pipeline implemented in this project includes:

### 1. Data Preprocessing & NLP Cleaning
- **Boilerplate Removal:** Identifying and stripping standard judicial headers, footers, and disclaimer text using regex.
- **Text Normalization:** Lowercasing and removing non-alphabetic characters (numbers/symbols) to focus on judicial language.
- **Vektorization:** Converting cleaned text into numerical format using **TF-IDF (Term Frequency-Inverse Document Frequency)** with:
  - `max_features`: 15,000
  - `ngram_range`: (1, 2)

### 2. Modeling
Multiple regression algorithms were evaluated to find the best fit for the judicial text data:
- **LightGBM Regressor** (Best performing baseline)
- **XGBoost Regressor**
- **Random Forest Regressor**
- **Ridge Regression**

### 3. Evaluation
Model performance is measured using **Root Mean Squared Error (RMSE)**. The goal is to minimize the deviation between predicted and actual sentence lengths.

## Directory Structure
- `Benchmark Model.ipynb`: Comprehensive notebook for data loading, preprocessing, model training, and evaluation.
- `file_putusan/`: Folder containing the raw text documents.
- `Description.txt`: Official competition overview and context.

## Getting Started
To run the analysis:
1. Ensure the dataset files are placed according to the paths in the notebook.
2. Install the necessary libraries:
   ```bash
   pip install pandas numpy scikit-learn lightgbm xgboost tqdm
   ```
3. Open `Benchmark Model.ipynb` and execute the cells to preprocess the raw text and train the regressor.

---
*Developed for the DATAQUEST 2025 Competition by Universitas Airlangga.*
