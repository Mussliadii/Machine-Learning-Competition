# Sebelas Maret Statistics Data Science 2025 - Singapore Weather Analysis

## Problem Statement
The Sebelas Maret Statistics Data Science (SSDS) 2025 competition involves a large-scale analysis and prediction of weather patterns across multiple locations in Singapore. The challenge lies in integrating fragmented datasets from various meteorological stations and handling significant missing values to create a coherent regional weather model.

## Technical Methodology
The solution focuses on robust data engineering and statistical imputation to prepare a clean dataset for predictive modeling.

### Machine Learning Pipeline:
1.  **Data Integration**:
    *   Merging high-frequency data from over 40 meteorological stations (e.g., Changi, Jurong, Sentosa, etc.).
    *   Automated folder-based merging of CSV files for regional consistency.
2.  **Data Preprocessing & Cleaning**:
    *   Standardizing column names and handling encoding issues (UTF-8, ISO-8859-1).
    *   Replacing placeholder characters (e.g., '—') with NaN values.
    *   Converting data types to appropriate numerical and datetime formats.
3.  **Statistical Imputation**:
    *   **Monthly Median Imputation**: Filling missing values in rainfall, temperature, and wind speed based on the median value of the corresponding month and year for each specific location. This ensures that seasonal trends are preserved during imputation.
4.  **Feature Selection**:
    *   Focusing on key indicators: Rainfall (30/60/120 min), Mean/Max/Min Temperature, and Wind Speed.
5.  **Analytical Framework**:
    *   The cleaned dataset provides a foundation for complex time-series analysis and regional climate forecasting.
