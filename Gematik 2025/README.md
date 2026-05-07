# Gematik 2025 - LinkedIn Job Post Popularity Prediction

## Problem Statement
The Gematik 2025 competition focuses on the digital job market, specifically predicting the popularity or demand of job postings on LinkedIn. Understanding what makes a job post "popular" (e.g., high application rates or visibility) is vital for both recruiters and job seekers. The task involves analyzing job metadata—such as title, description, company industry, and required skills—to predict engagement levels.

## Technical Methodology
The solution integrates Natural Language Processing (NLP) for text analysis with Gradient Boosting models for structured data processing.

### Machine Learning Pipeline:
1.  **Feature Engineering**:
    *   Extracting temporal features from posting dates.
    *   Quantifying company size and industry influence.
    *   Processing "Skills" tags to identify high-demand tech stacks.
2.  **Text Analysis**:
    *   Vectorizing job titles and descriptions using TF-IDF or Word Embeddings to capture semantic importance.
3.  **Model Implementation**:
    *   **CatBoost**: Utilized for its superior handling of categorical features (like Company, Industry, and Location) without the need for extensive manual encoding.
    *   **XGBoost/LightGBM**: Implemented as part of an ensemble to capture residual patterns in the data.
4.  **Training & Validation**:
    *   Cross-validation strategy to ensure the model generalizes well across different industries and time periods.
5.  **Evaluation Metrics**:
    *   Mean Squared Error (MSE) or R-Squared ($R^2$) to measure the accuracy of popularity score predictions.
