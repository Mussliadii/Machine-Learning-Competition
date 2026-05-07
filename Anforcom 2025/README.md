# 🇮🇩 Astacita Pillar Tweet Classification: Towards Indonesia Emas 2045

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![IndoBERT](https://img.shields.io/badge/Model-IndoBERT-green.svg)](https://huggingface.co/indobenchmark/indobert-base-p1)
[![Anforcom](https://img.shields.io/badge/Competition-Anforcom%202025-orange.svg)]()

This repository contains the solution for the **Anforcom 2025** competition, focusing on automated text classification (Natural Language Processing) to categorize public interactions on social media (Tweets) into the 8 pillars of **Astacita**.

## 👥 Team Information
- **Team Name**: Heisenberg
- **Affiliation**: Universitas Syiah Kuala (USK)

## 📋 Problem Statement
The primary goal of this project is to build a machine learning model capable of classifying public tweets regarding the "Indonesia Emas 2045" vision into the appropriate Astacita pillar categories.

**Key Challenges:**
- Significant **class imbalance** across different pillars.
- Usage of non-standard language, slang, and informal Indonesian in tweets.
- Comparative analysis between classical statistical models and Transformer-based models.

## 📊 Dataset & Categories
The model is trained to recognize 8 labels corresponding to the Astacita pillars, including:
1. Ideology
2. Defense & Security
3. Downstreaming (Hilirisasi)
4. *...and other pillars as defined by the competition data.*

## 🧠 Methodology
We employed two primary approaches:

### 1. Baseline Model
- **Feature Extraction**: TF-IDF Vectorizer.
- **Classifier**: Random Forest.
- **Purpose**: To provide a performance benchmark before implementing complex models.

### 2. Main Model (Transformer)
- **Model**: IndoBERT (Base version).
- **Optimization**: Class Weights (to handle class imbalance).
- **Metric**: Balanced Accuracy.
- **Library**: Hugging Face Transformers & Datasets.

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: 
  - `transformers`, `torch`, `datasets` (Deep Learning)
  - `scikit-learn` (Evaluation & Baseline)
  - `pandas`, `numpy` (Data Processing)
  - `matplotlib`, `seaborn`, `wordcloud` (Visualization)
  - `emoji`, `re` (Preprocessing)

## 🚀 Getting Started

### Prerequisites
- Google Colab (recommended) or a local Python environment with GPU support.

### Installation
```bash
pip install transformers datasets scikit-learn emoji imblearn accelerate wordcloud
```

### Run the Notebook
Open the `Heisenberg_UniversitasSyiahKuala.ipynb` file in a Jupyter environment or Google Colab and run each cell sequentially.

## 📈 Results
The IndoBERT model optimized with class weights showed a significant performance boost compared to the baseline model, especially in handling minority categories such as the "Hilirisasi" pillar.

---
*Developed for Anforcom 2025 Competition by Team Heisenberg.*
