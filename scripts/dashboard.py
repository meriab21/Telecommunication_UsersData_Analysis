import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("TellCo user data analysis")
st.subheader("user overview analysis")

def main():

    df = pd.read_csv('../data/')

    page = st.sidebar.selectbox("Choose a page", ['Homepage', 'Exploration', 'Prediction'])
