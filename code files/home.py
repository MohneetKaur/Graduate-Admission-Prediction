import streamlit as st
import pandas as pd
from PIL import Image
import base64
import os
#st.set_page_config(layout="wide")



df = pd.read_csv('Admission_Predict.csv')
df.drop('Serial No.',axis=1,inplace=True)

def run():

    st.title(":black[Graduate Admission Prediction]")
    image = Image.open('homepage.png')
    st.image(image, use_column_width=True)

    st.markdown("## :blue[About the Dataset]")
    st.markdown("###### Column Description")
    st.write('1.GRE Scores ( out of 340 )')
    st.write('2.TOEFL Scores ( out of 120 )')
    st.write('3.University Rating ( out of 5 )')
    st.write('4.Statement of Purpose and Letter of Recommendation Strength ( out of 5 )')
    st.write('5.Undergraduate CGPA ( out of 10 )')
    st.write('6.Research Experience ( either 0 or 1 )')
    st.write('7.Chance of Admit ( ranging from 0 to 1 )')


    st.markdown("###### Top Five Rows of Dataset")
    st.write(df.head())

    st.markdown("###### Total Numbers of Rows and Columns")
    st.write("Shape of Dataset:", df.shape)


    st.markdown("###### Null Values")
    st.write(df.isnull().sum())

    st.markdown('###### Data Description')
    st.write(df.describe())




    

