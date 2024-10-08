# -*- coding:utf-8 -*-

import streamlit as st 
import pandas as pd 

@st.cache_data
def load_data():
    data = pd.read_csv('data/cleaned_v2.2.csv')

    return data