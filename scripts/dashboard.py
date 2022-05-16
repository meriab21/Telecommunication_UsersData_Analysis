import streamlit as st
import numpy as np
import pandas as pd

# Add title
st.title("TellCo user data analysis")

# Add side bar
st.sidebar.selectbox(
    "User Analysis", ['User overview analysis', 'Engagment analysis', 'Satisfaction analysis'])
# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)
# # Upload csv file
# uploaded_file = st.sidebar.file_uploader(
#     label="Upload your clean data csv file", type=['csv', 'xlsx'])

# if uploaded_file is not None:
#     print(uploaded_file)
# else:
#     print("hel")

df = pd.read_csv('../data/analysis_data.csv')
st.write(df)
cdf = pd.read_csv('../data/clean_TellCo_data.csv')
st.write(cdf)
