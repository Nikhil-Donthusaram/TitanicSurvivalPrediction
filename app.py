import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load saved model and column names
model = pickle.load(open("titanic_model.pkl", "rb"))
columns = pickle.load(open("titanic_columns.pkl", "rb"))

st.set_page_config(page_title="Titanic Survival Prediction")

st.title("🚢 Titanic Survival Prediction App")

# Input fields
pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.slider("Age", 0, 100, 30)
sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, step=1)
parch = st.number_input("Parents/Children Aboard", 0, 10, step=1)
fare = st.number_input("Ticket Fare", 0.0, 600.0, step=1.0)
sex = st.selectbox("Sex", ['male', 'female'])
embarked = st.selectbox("Port of Embarkation", ['C', 'Q', 'S'])

# Convert categorical inputs to match trained data
sex_male = 1 if sex == 'male' else 0
embarked_Q = 1 if embarked == 'Q' else 0
embarked_S = 1 if embarked == 'S' else 0

# Prepare input DataFrame
input_data = np.array([[pclass, age, sibsp, parch, fare, sex_male, embarked_Q, embarked_S]])
input_df = pd.DataFrame(input_data, columns=columns)

# Predict on button click
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][prediction]

    if prediction == 1:
        st.success(f"🎉 Passenger would have SURVIVED! (Confidence: {probability:.2f})")
    else:
        st.error(f" Passenger would NOT have survived. (Confidence: {probability:.2f})")
