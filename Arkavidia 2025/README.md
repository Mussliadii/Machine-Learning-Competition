# Arkavidia 2025: Datavidia - Commodity Price Prediction

## Project Overview
This repository contains the solution developed by **Team Heisenberg** for the **Datavidia** competition at **Arkavidia 9.0 (2025)**. The primary objective of this project is to predict food commodity prices in various regions across Indonesia using time-series forecasting techniques and external economic indicators.

## Problem Statement
Predicting commodity prices is crucial for economic stability and planning. This competition challenged participants to build robust models that can forecast price fluctuations in staple foods (e.g., rice, chili, meat, eggs) based on historical data and relevant external factors.

## Dataset
The project utilizes multiple datasets to enhance prediction accuracy:
- **Local Food Prices (Harga Bahan Pangan):** Historical price data for various commodities across different provinces/cities in Indonesia.
- **Global Commodity Prices:** Historical data for global futures such as Crude Oil (WTI), Natural Gas, Newcastle Coal, Palm Oil, Sugar, and Wheat.
- **Google Trends:** Search interest data for specific commodities, used as a proxy for market demand and sentiment.
- **Currency Exchange Rates (Mata Uang):** USD to IDR rates, reflecting the impact of global currency fluctuations on local prices.

## Repository Structure
- `Comodity Price Prediction/`
    - `Arkavidia9_Datavidia_Heisenberg/`: Main competition deliverables including the solution notebook (`.ipynb`), report (`.pdf`), and documentation (`.docx`).
    - `Global Commodity Price/`: External global market datasets.
    - `Google Trend/`: Search interest data for various food items.
    - `Harga Bahan Pangan/`: Primary training and testing data for food prices.
    - `Mata Uang/`: Currency exchange rate data.
- `Warmup/`: Initial exploration and warmup tasks for the competition.

## Methodology
The solution focuses on:
1. **Data Preprocessing:** Cleaning regional price data and handling missing values.
2. **Feature Engineering:** Integrating external datasets (Global Prices, Google Trends) to capture broader economic trends.
3. **Forecasting Model:** Implementation of Time Series models like **ARIMA** (AutoRegressive Integrated Moving Average) to capture historical price patterns.
4. **Validation:** Evaluating model performance against provided test datasets and sample submissions.

## Getting Started
To reproduce the results or explore the analysis:
1. Navigate to the `Comodity Price Prediction/Arkavidia9_Datavidia_Heisenberg/` directory.
2. Open and run the `Arkavidia9_Datavidia_Heisenberg.ipynb` notebook.
3. Ensure all data paths are correctly configured relative to the notebook's location.

## Technologies Used
- Python
- Pandas & NumPy (Data Manipulation)
- Matplotlib & Seaborn (Data Visualization)
- Statsmodels (ARIMA/Time Series Analysis)
- TQDM (Progress Monitoring)

---
*Developed by Team Heisenberg for Arkavidia 2025.*
