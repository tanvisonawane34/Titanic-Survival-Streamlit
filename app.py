import joblib
import pandas as pd
import streamlit as st

st.title("🚢 Titanic Survival Prediction")

# Load saved files with basic exception handling
try:
    model = joblib.load("titanic_model.pkl")
    scaler = joblib.load("scaler.pkl")
    columns = joblib.load("columns.pkl")
except Exception as e:
    st.error("Error loading files! Make sure all .pkl files are in the folder.")
    st.stop()

# Inputs from user
pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0)
sibsp = st.number_input("Number of Siblings/Spouses", min_value=0, value=0)
parch = st.number_input("Number of Parents/Children", min_value=0, value=0)
fare = st.number_input("Fare", min_value=0.0, value=32.0)

sex = st.selectbox("Sex", ["male", "female"])
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Predict button
if st.button("Predict"):
    try:
        # Convert text inputs to numbers
        sex_male = 1 if sex == "male" else 0
        embarked_Q = 1 if embarked == "Q" else 0
        embarked_S = 1 if embarked == "S" else 0

        # Prepare input data
        input_data = pd.DataFrame(
            [
                {
                    "Pclass": pclass,
                    "Age": age,
                    "SibSp": sibsp,
                    "Parch": parch,
                    "Fare": fare,
                    "Sex_male": sex_male,
                    "Embarked_Q": embarked_Q,
                    "Embarked_S": embarked_S,
                }
            ]
        )

        # Match training column structure
        input_data = input_data.reindex(columns=columns, fill_value=0)

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)

        # Show result
        if prediction[0] == 1:
            st.success("Survived: Yes 🚢")
        else:
            st.error("Survived: No ❌")

    except Exception as e:
        st.error("Something went wrong during prediction!")