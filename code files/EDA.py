import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import base64
import os
#st.set_page_config(layout="wide")



df = pd.read_csv('Admission_Predict.csv')

def run():

    st.title(":black[Exploratory Data Analysis]")


    st.markdown("###### Variable Importance")
    image = Image.open('variable_importance.png')
    st.image(image, use_column_width=True)


    st.markdown("###### Correlation between Variables")
    image = Image.open('heatmap.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Distribution of GRE Scores")
    image = Image.open('gre_dist.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Distribution of TOEFL Scores")
    image = Image.open('toefl_dist.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Distribution of CGPA")
    image = Image.open('cgpa_dist.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Distribution of SOP")
    image = Image.open('sop_dist.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Distribution of LOR")
    image = Image.open('lor_dist.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Distribution of Chance Of Admit")
    image = Image.open('admit_dist.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Countplot of University Rating")
    image = Image.open('university_count.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Countplot of Research")
    image = Image.open('research_count.png')
    st.image(image, use_column_width=True)

    st.markdown("###### GRE v/s Chance of Admit")
    image = Image.open('gre_admit.png')
    st.image(image, use_column_width=True)

    st.markdown("###### LOR v/s Chance of Admit")
    image = Image.open('lor_admit.png')
    st.image(image, use_column_width=True)

    st.markdown("###### TOEFL v/s Chance of Admit")
    image = Image.open('toefl_admit.png')
    st.image(image, use_column_width=True)

    st.markdown("###### CGPA v/s Chance of Admit")
    image = Image.open('cgpa_admit.png')
    st.image(image, use_column_width=True)

    st.markdown("###### SOP v/s Chance of Admit")
    image = Image.open('sop_admit.png')
    st.image(image, use_column_width=True)

    st.markdown("###### Research v/s Chance of Admit")
    image = Image.open('research_admit.png')
    st.image(image, use_column_width=True)

    st.markdown("###### University Rating v/s Chance of Admit")
    image = Image.open('ur_admit.png')
    st.image(image, use_column_width=True)

