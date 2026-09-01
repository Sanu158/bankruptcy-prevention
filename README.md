# Bankruptcy Prevention Using Machine Learning

A machine learning project that predicts the risk of company bankruptcy using financial and operational risk indicators. The project includes exploratory data analysis, model comparison, and a Streamlit web application for making predictions.

## Project Overview

This project analyzes company risk factors and predicts whether a company is likely to face bankruptcy.

The project compares multiple machine learning algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes

A Streamlit application is included so users can enter risk values and receive a bankruptcy-risk prediction with probability.

## Dataset

The dataset contains **250 company records** with six risk-related input features:

- Industrial Risk
- Management Risk
- Financial Flexibility
- Credibility
- Competitiveness
- Operating Risk

The target variable represents the bankruptcy status of the company.

## Model Performance

The models were evaluated using a test dataset.

| Model | Accuracy |
|---|---:|
| Logistic Regression | 100% |
| Decision Tree | 100% |
| Random Forest | 100% |
| Gradient Boosting | 100% |
| SVM | 100% |
| KNN | 100% |
| Naive Bayes | 98% |

Logistic Regression was selected as the final model because it provides a simple and interpretable classification approach.

## Streamlit Application

The Streamlit application allows users to enter values for:

- Industrial Risk
- Management Risk
- Financial Flexibility
- Credibility
- Competitiveness
- Operating Risk

The application returns:

- Predicted bankruptcy status
- Probability of bankruptcy
- Risk classification

## NLP / Machine Learning Workflow

The project workflow includes:

1. Data loading
2. Exploratory Data Analysis
3. Data preprocessing
4. Model training
5. Model comparison
6. Logistic Regression model selection
7. Model serialization using Pickle
8. Streamlit deployment

## Project Structure

```text
bankruptcy-prevention/
│
├── data/
│   └── bankruptcy-prevention.xlsx
│
├── models/
│   └── lr.pkl
│
├── notebooks/
│   ├── bankruptcy_EDA.ipynb
│   └── bankruptcy_model_building.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md