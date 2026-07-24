# 🚢 Titanic Survival Prediction System

## 📌 Project Description
This project predicts whether a passenger survived the Titanic disaster based on demographic and ticket details using Machine Learning. The trained model is deployed interactively using Streamlit.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-Learn
- Streamlit
- Joblib / Pickle

## 🤖 Machine Learning Algorithm
- Random Forest Classifier (or Logistic Regression)

## 📊 Dataset
- Titanic: Machine Learning from Disaster
- Dataset Link: https://www.kaggle.com/c/titanic/data

## 🔑 Features Used
- Pclass (Ticket Class)
- Sex (Gender)
- Age
- SibSp (Siblings / Spouses Aboard)
- Parch (Parents / Children Aboard)
- Fare
- Embarked (Port of Embarkation)

## ⚙️ Project Workflow
1. Data Loading & Cleaning
2. Exploratory Data Analysis (EDA)
3. Missing Value Imputation
4. Feature Encoding & Scaling
5. Train-Test Split & Model Training
6. Model Evaluation & Saving (`.pkl`)
7. Streamlit Frontend Development
8. GitHub Deployment

## 🎯 Accuracy
- Model Accuracy: 82%+ (may vary slightly)

## 📂 Project Structure
Titanic-Survival-Prediction-Streamlit/
│── app.py
│── titanic_model.pkl
│── scaler.pkl
│── columns.pkl
│── requirements.txt
└── README.md

## 🚀 Run Locally
1. Clone repository:
   git clone https://github.com/tanvisonawane34/Titanic-Survival-Prediction-Streamlit.git
   cd Titanic-Survival-Prediction-Streamlit

2. Install requirements:
   pip install -r requirements.txt

3. Run Streamlit App:
   streamlit run app.py

## 👩‍💻 Author
Tanvi Sonawane
