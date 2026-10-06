import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Page title
st.title("🎓 Student Performance Prediction")

st.write("Enter the student details to predict the next exam marks.")

# Input fields
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance Percent",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

assignment_marks = st.number_input(
    "Assignment Marks",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

internal_marks = st.number_input(
    "Internal Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

# Prediction button
if st.button("Predict Marks"):

    student = pd.DataFrame([{
        "Study Hours": study_hours,
        "Attendance Percent": attendance,
        "Assignment Marks": assignment_marks,
        "Internal Marks": internal_marks,
        "Previous Marks": previous_marks,
        "Sleep Hours": sleep_hours
    }])

    prediction = model.predict(student)[0]

    st.success(f"Predicted Next Exam Marks: {prediction:.2f}")