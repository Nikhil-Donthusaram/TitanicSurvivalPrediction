# 🚢 Titanic Survival Prediction App

This is a Machine Learning web app that predicts whether a passenger would have survived the Titanic disaster. It uses **Logistic Regression** for classification and is built with **Python**, **scikit-learn**, and **Streamlit**.
[Click to Launch](https://titanicsurvivalprediction-s5oswswwnxujp7ubmpnfym.streamlit.app/)

---

## 📊 Project Overview

The Titanic dataset contains information on the fate of passengers on the Titanic. This project builds a logistic regression model using features like age, sex, class, fare, and family onboard to predict survival.

The app allows users to enter passenger details and see survival predictions interactively.

---

## 🧠 Machine Learning Details

- **Algorithm:** Logistic Regression
- **Input Features:**
  - Passenger Class (`Pclass`)
  - Age
  - Sex
  - Fare
  - Siblings/Spouses Aboard (`SibSp`)
  - Parents/Children Aboard (`Parch`)
  - Embarkation Port
- **Output:**  
  - `0`: Did not survive  
  - `1`: Survived

---

## 🛠️ Technologies Used

- Python
- pandas
- numpy
- scikit-learn
- Streamlit

---

## 📁 Project Structure

TitanicSurvivalPrediction/
│
├── app.py # Streamlit web app
├── titanic_model.pkl # Trained Logistic Regression model
├── titanic_columns.pkl # Feature columns used during training
├── titanic.csv # Dataset
├── requirements.txt # Required Python libraries
└── README.md # Project overview and instructions


## ▶️ How to Run This Project Locally

```bash
# 1. Clone the repository
git clone https://github.com/Nikhil-Donthusaram/TitanicSurvivalPrediction.git
cd TitanicSurvivalPrediction

# 2. Install required libraries
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

