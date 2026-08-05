import streamlit as st
import streamlit as st
import pandas as pd

st.title('Heart Disease Predictions')

st.info('ข้อมูลสำหรับทำนาย')

with st.expander('ข้อมูล Heart Disease Predictions'):
  st.white('ข้อมูลทั้งหมด')
  dt = pd.read_csv("./data/heart.csv")
  st.dataframe(dt, use_container_width=True, height=300)

