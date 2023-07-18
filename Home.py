import numpy as np
import pandas as pd
import streamlit as st
import pickle


st.set_page_config(layout="wide")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Fantasy:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Fantasy', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.write("# Welcome to the Insurance Cross-Selling Prediction Web App!")

st.write("""
# 
This app predicts if the existing customers will buy vehicle insurance!
Data obtained from the [kaggle](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction).

""")

from PIL import Image

with st.sidebar.container():
    image = Image.open('black.jpg')
st.image(image, width= None)

import streamlit as st













