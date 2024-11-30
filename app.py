import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model (update the path if needed)
model = joblib.load(r"E:\preforintren\logistic_regression_model.pkl")  # Ensure correct path

# Function to predict depression
def predict_depression(input_data):
    input_df = pd.DataFrame(input_data)
    input_df = input_df[['Gender', 'Age', 'Academic Pressure', 'Study Satisfaction', 
                          'Sleep Duration', 'Dietary Habits', 'Have you ever had suicidal thoughts ?',
                          'Study Hours', 'Financial Stress', 'Family History of Mental Illness']]
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        return "The prediction indicates a higher likelihood of depression."
    else:
        return "The prediction indicates a lower likelihood of depression."

# Streamlit app with light theme and styling
def main():
    # Set page layout, theme and style
    st.set_page_config(page_title="Depression Prediction App", page_icon=":guardsman:", layout="wide", initial_sidebar_state="expanded")
    st.markdown(
        """
        <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
        }
        h1, h2, h3 {
            color: #3E6C63;
        }
        .stButton>button {
            background-color: #3E6C63;
            color: white;
            border-radius: 5px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #4B8F72;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Header section
    st.title("🧠 Depression Prediction Dashboard")
    st.markdown("""
        This app predicts the likelihood of depression based on various factors such as gender, age, academic pressure, and more. 
        Fill in the details below to get the prediction.
    """)

    # Sidebar for navigation and inputs
    st.sidebar.header("User Input")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    gender = 1 if gender == "Female" else 0  # Convert to numeric format

    age = st.sidebar.number_input("Age", min_value=1, max_value=100, value=18)  # Age range for context
    academic_pressure = st.sidebar.slider("Academic Pressure (1-5)", 1, 5, value=3)
    study_satisfaction = st.sidebar.slider("Study Satisfaction (1-5)", 1, 5, value=3)
    sleep_duration = st.sidebar.number_input("Sleep Duration (hours)", min_value=0.0, value=7.0)
    dietary_habits = st.sidebar.slider("Dietary Habits (1-5)", 1, 5, value=3)

    # Suicidal thoughts as a radio button
    suicidal_thoughts = st.sidebar.radio("Have you ever had suicidal thoughts?", ["No", "Yes"])
    suicidal_thoughts = 1 if suicidal_thoughts == "Yes" else 0

    study_hours = st.sidebar.number_input("Study Hours", min_value=0, value=4)
    financial_stress = st.sidebar.slider("Financial Stress (1-5)", 1, 5, value=3)

    # Family history of mental illness as a selectbox
    family_history = st.sidebar.selectbox("Family History of Mental Illness", ["No", "Yes"])
    family_history = 1 if family_history == "Yes" else 0

    # Display a brief summary of user inputs
    st.sidebar.markdown("### Your Inputs Summary:")
    st.sidebar.markdown(f"**Gender:** {'Female' if gender == 1 else 'Male'}")
    st.sidebar.markdown(f"**Age:** {age}")
    st.sidebar.markdown(f"**Academic Pressure:** {academic_pressure}")
    st.sidebar.markdown(f"**Study Satisfaction:** {study_satisfaction}")
    st.sidebar.markdown(f"**Sleep Duration:** {sleep_duration} hours")
    st.sidebar.markdown(f"**Dietary Habits:** {dietary_habits}")
    st.sidebar.markdown(f"**Suicidal Thoughts:** {'Yes' if suicidal_thoughts == 1 else 'No'}")
    st.sidebar.markdown(f"**Study Hours:** {study_hours} hours")
    st.sidebar.markdown(f"**Financial Stress:** {financial_stress}")
    st.sidebar.markdown(f"**Family History:** {'Yes' if family_history == 1 else 'No'}")

    # Prediction Button
    st.markdown("---")
    if st.button("🔮 Predict Depression Likelihood"):
        input_data = {
            'Gender': [gender],
            'Age': [age],
            'Academic Pressure': [academic_pressure],
            'Study Satisfaction': [study_satisfaction],
            'Sleep Duration': [sleep_duration],
            'Dietary Habits': [dietary_habits],
            'Have you ever had suicidal thoughts ?': [suicidal_thoughts],
            'Study Hours': [study_hours],
            'Financial Stress': [financial_stress],
            'Family History of Mental Illness': [family_history]
        }
        result = predict_depression(input_data)
        
        # Display the prediction result
        st.markdown(f"### Prediction Result:")
        st.write(result)

    # Footer Section with additional resources
    st.markdown("---")
    st.markdown("### Need help?")
    st.markdown("""
        If you're feeling depressed or in need of help, please contact a healthcare professional or reach out to a helpline.
        - **National Helpline:** [Link to national helpline]
        - **Mental Health Resources:** [Link to mental health resources]
    """)

if __name__ == '__main__':
    main()
