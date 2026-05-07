# DAC ITS - Sentiment Analysis

## Problem Statement
The objective of this project is to perform sentiment analysis on Indonesian text data. Sentiment analysis is a crucial task in Natural Language Processing (NLP) that involves determining the emotional tone behind a body of text. In this competition, the goal was to accurately classify sentiments from various social media or review platforms into specific categories (e.g., Positive, Neutral, Negative).

## Technical Methodology
The solution leverages state-of-the-art Transformer architectures specifically optimized for multilingual and Indonesian contexts.

### Machine Learning Pipeline:
1.  **Data Preprocessing**:
    *   Text cleaning: Removing special characters, URLs, and emojis.
    *   Normalization: Converting text to lowercase and handling informal Indonesian slang.
    *   Tokenization: Utilizing the specialized tokenizer associated with the XLM-RoBERTa model.
2.  **Model Architecture**:
    *   **XLM-RoBERTa**: A large-scale multilingual model that provides superior performance for Indonesian sentiment tasks due to its extensive pre-training on diverse datasets.
    *   Fine-tuning: The model was fine-tuned on the competition's training dataset to adapt to the specific sentiment labels.
3.  **Training Strategy**:
    *   Loss Function: Cross-Entropy Loss for multi-class classification.
    *   Optimizer: AdamW with a learning rate scheduler.
    *   Evaluation Metrics: Accuracy and F1-Score to ensure balanced performance across all sentiment classes.
4.  **Inference**:
    *   Generating predictions on the benchmark/test model for final submission.
