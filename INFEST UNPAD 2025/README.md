# Ifest Unpad 2025 - Movie Genre Recommendation System

## Problem Statement
The goal of this project is to build an intelligent recommendation engine that suggests movie genres based on textual descriptions or plot summaries. In a world with an overwhelming amount of content, providing accurate and personalized recommendations is key to user retention on streaming platforms.

## Technical Methodology
The solution employs a hybrid semantic approach, combining deep learning text embeddings with similarity-based ranking.

### Machine Learning Pipeline:
1.  **Semantic Embedding**:
    *   **BERT (Bidirectional Encoder Representations from Transformers)**: Utilized to extract high-dimensional semantic vectors from movie plot summaries. BERT's ability to understand context ensures that the subtle nuances of a movie's theme are captured.
2.  **Vector Similarity**:
    *   **Cosine Similarity**: After generating embeddings for all movies in the database, Cosine Similarity is used to calculate the distance between the input movie/user profile and potential recommendations.
3.  **Genre Classification**:
    *   A classification head is added on top of the BERT encoder to categorize movies into predefined genres (e.g., Sci-Fi, Drama, Thriller).
4.  **Recommendation Logic**:
    *   The system ranks movies based on their semantic proximity to the user's preferred genres or past viewing history.
5.  **Evaluation**:
    *   Accuracy and Recall@K metrics are used to measure how often the system's top suggestions match the user's actual interests.
