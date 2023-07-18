import streamlit as st

from PIL import Image

image4=Image.open('portfolio.jpg')

st.image(image4, caption='Customer Portfolio', width=900)