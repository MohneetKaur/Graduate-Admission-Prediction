import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the trained model
model = joblib.load('lr.pkl')  # Replace with the path to your trained model

# Define the web application
def run():
    # Set the title and description of the app
    st.title('Admission Chance Predictor')
    st.write('Enter the required details to predict your chance of admission.')

    # Create input fields for user to enter the data
    gre_score = st.number_input('GRE_Score')
    toefl_score = st.number_input('TOEFL_Score')
    university_rating = st.number_input('University_Rating')
    sop = st.number_input('SOP')
    lor = st.number_input('LOR')
    cgpa = st.number_input('CGPA')
    research = st.number_input('Research (0 for No, 1 for Yes)')

    # Create a button to trigger the prediction
    if st.button('Predict'):
        # Create a DataFrame with the user input
        data = pd.DataFrame({
            'GRE_Score': [gre_score],
            'TOEFL_Score': [toefl_score],
            'University_Rating': [university_rating],
            'SOP': [sop],
            'LOR': [lor],
            'CGPA': [cgpa],
            'Research': [research]
        })

        # Make the prediction
        prediction = model.predict(data)
        st.write('Predicted Chance of Admission:', round(prediction[0]*100,2),'%')

