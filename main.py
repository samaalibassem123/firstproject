import streamlit as st
import pandas as pd
import numpy as np

st.write('# Churn Data')

df = pd.read_csv('ChurnData.csv')

st.write(df.head())

st.button("click me")


st.scatter_chart(df,x ='age' ,y ="churn")
st.scatter_chart(df,x ='address' ,y ="churn")

st.chat_input()

st.text_input("test")

st.radio("test", ['he','hello'])

st.number_input("test")

st.select_slider("test", options=[1,23,66,5,6])