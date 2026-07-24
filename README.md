# Titanic Survival Prediction System

## Project Description
This project predicts whether a passenger survived the Titanic disaster based on demographic and ticket details using Machine Learning. The trained model is deployed interactively using Streamlit.

## Live Demo
https://titanic-survival-ml-app.streamlit.app/

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-Learn
- Streamlit
- Joblib

## Machine Learning Algorithm
- Logistic Regression

## Dataset
- Titanic: Machine Learning from Disaster
- Dataset Link: [https://www.kaggle.com/c/titanic/data](https://www.kaggle.com/c/titanic/data)

## Features Used
- Pclass (Ticket Class)
- Sex (Gender)
- Age
- SibSp (Siblings / Spouses Aboard)
- Parch (Parents / Children Aboard)
- Fare
- Embarked (Port of Embarkation)

## Project Workflow
1. Data Loading & Cleaning
2. Exploratory Data Analysis (EDA)
3. Missing Value Imputation
4. Feature Encoding & Scaling
5. Train-Test Split & Model Training
6. Model Evaluation & Saving (.pkl)
7. Streamlit Frontend Development
8. GitHub Deployment

## Accuracy
- Model Accuracy: 82%+ (may vary slightly)

## Project Structure
```text
Titanic-Survival-Prediction-Streamlit/
│── app.py
│── titanic.csv
│── titanic_model.pkl
│── scaler.pkl
│── columns.pkl
│── requirements.txt
└── README.md
```

## Run Locally
Install dependencies:
```bash
pip install -r requirements.txt
```

Run Streamlit App:
```bash
streamlit run app.py
```

## Author
Tanvi Sonawane
