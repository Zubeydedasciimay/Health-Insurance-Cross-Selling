

import pandas as pd
import streamlit as st
from PIL import Image


         
image4=Image.open('portfolio2.jpg')

st.image(image4, caption='Customer Portfolio', width=900)

