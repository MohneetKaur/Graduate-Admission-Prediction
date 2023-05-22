import streamlit as st
import home
import graduate_prediction
import EDA

PAGES = {
    "Home": home,
    "Graduate Prediction": graduate_prediction,
    "Exploratory Data Analysis": EDA
}

st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run the app
PAGES[page].run()
