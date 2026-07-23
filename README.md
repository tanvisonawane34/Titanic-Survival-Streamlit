# 🚢 Titanic Survival Prediction App

An interactive Machine Learning web application built with **Streamlit** that predicts passenger survival on the Titanic based on demographic information, ticket details, and family background.

---

## 📌 Features

- 🎛️ **Interactive Inputs:** User-friendly dropdowns and numerical inputs to enter passenger details.
- ⚙️ **Preprocessing Pipeline:** Automatic handling of categorical variables (`Sex`, `Embarked`) and feature alignment matching model expectations.
- 📐 **Feature Scaling:** Seamless integration with standard scaling (`scaler.pkl`).
- ⚡ **Real-time Prediction:** Instant feedback with distinct survival/non-survival indicators.
- 🛡️ **Exception Handling:** Robust error catching to ensure app stability when loading assets.

---

## 📁 Repository Structure

```text
.
├── app.py                 # Streamlit web application code
├── titanic_model.pkl      # Pre-trained Classification Model
├── scaler.pkl             # Fitted Feature Scaler
├── columns.pkl            # Expected feature column layout
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Installation & Local Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Install Dependencies
Make sure you have a `requirements.txt` file containing:
```text
streamlit
pandas
joblib
scikit-learn
```

Then install the dependencies using pip:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

Launch the Streamlit app locally by executing:

```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 📊 Feature Reference Table

| Feature Name | Type | Options / Range | Description |
| :--- | :--- | :--- | :--- |
| **Pclass** | Categorical | `1`, `2`, `3` | Ticket class (1st, 2nd, or 3rd Class) |
| **Age** | Continuous | `0.0` - `100.0` | Age of passenger in years |
| **SibSp** | Discrete | `0+` | Number of siblings or spouses aboard |
| **Parch** | Discrete | `0+` | Number of parents or children aboard |
| **Fare** | Continuous | `0.0+` | Passenger fare amount |
| **Sex** | Categorical | `male`, `female` | Gender of the passenger |
| **Embarked** | Categorical | `C`, `Q`, `S` | Port of Embarkation (Cherbourg, Queenstown, Southampton) |

---

## ⚙️ Model & Feature Pipeline Details

1. **Categorical Mapping:** 
   - `Sex`: Converted to binary indicator (`Sex_male`).
   - `Embarked`: Transformed to dummy variables (`Embarked_Q`, `Embarked_S`).
2. **Column Alignment:** Reindexed against saved `columns.pkl` structure (`input_data.reindex(columns=columns, fill_value=0)`) to maintain feature order integrity.
3. **Scaling & Inference:** Transformed via `scaler.transform()` before predicting with `titanic_model.pkl`.
