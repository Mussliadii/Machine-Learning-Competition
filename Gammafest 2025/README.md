# Gammafest 2025: Research Paper Citation Prediction

## Overview
This repository contains the implementation for the **Gammafest 2025** machine learning competition. The task is a **Graph-Based Link Prediction** problem where the goal is to predict whether a research paper cites another paper based on their metadata, content, and structural relationships.

## Problem Statement
In the vast landscape of academic research, identifying relevant citations is crucial for knowledge discovery. This competition challenges participants to build a model that can accurately predict citation links (citations) between pairs of papers. This is a binary classification task on a graph, where papers are nodes and citations are directed edges.

## Dataset
The dataset consists of multiple components:
- `train.csv`: Training set containing pairs of papers (`paper`, `referenced_paper`) and the ground truth label `is_referenced` (1 if a citation exists, 0 otherwise).
- `test.csv`: Test set for which predictions need to be made.
- `papers_metadata.csv`: Detailed metadata for 4,356 papers, including:
  - `paper_id`: Unique identifier.
  - `title`: Title of the paper.
  - `authors`: List of authors.
  - `concepts`: Scientific concepts/keywords associated with the paper.
  - `publication_year`: Year of publication.
  - `cited_by_count`: Number of times the paper has been cited.
  - `type`: Type of publication (e.g., article, review).
- `Paper Database/`: A directory containing individual `.txt` files for each paper, providing the full text content.

## Methodology
The solution leverages a hybrid approach combining Natural Language Processing (NLP) and Graph Machine Learning:

### 1. Feature Engineering
- **Textual Features**: Paper titles and concepts are processed using pre-trained Transformer models (e.g., BERT or SciBERT) to generate high-dimensional embeddings.
- **Metadata Features**: Features such as publication year differences and author overlap are calculated.
- **Graph-Based Features**: Structural features are extracted from the citation network, including:
  - Common Neighbors
  - Jaccard Coefficient
  - Adamic-Adar Index
  - Preferential Attachment

### 2. Model Architecture
The benchmark model follows a standard pipeline for link prediction:
- **Embedding Layer**: Uses a pre-trained NLP model to represent the semantic content of each paper.
- **Link Predictor**: A classification head (e.g., CatBoost or a Neural Network) that takes the concatenated features of the paper pair and predicts the likelihood of a citation.

## Repository Structure
```text
.
├── Paper Database/           # Full text of research papers
├── Benchmark Model.ipynb     # Main development and training notebook
├── papers_metadata.csv       # Metadata for all papers
├── train.csv                 # Training data
├── test.csv                  # Test data
├── sample_submission.csv     # Template for submission
└── README.md                 # Project documentation
```

## Getting Started
### Prerequisites
- Python 3.8+
- PyTorch / TensorFlow
- Transformers (Hugging Face)
- NetworkX (for graph features)
- Pandas, NumPy, Scikit-learn

### Setup
1. Clone this repository.
2. Ensure the `Paper Database` is extracted in the root directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the `Benchmark Model.ipynb` to train the model and generate predictions.

## Evaluation
The model performance is evaluated using the **Area Under the ROC Curve (AUC-ROC)**, which measures the ability of the model to distinguish between positive citation links and negative ones.
