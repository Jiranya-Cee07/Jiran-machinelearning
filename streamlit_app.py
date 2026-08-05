import streamlit as st
import streamlit as st
import pandas as pd

st.title('Heart Disease Predictions')

st.info('ข้อมูลสำหรับทำนาย')

with st.expander('ข้อมูลทั้งหมด'):
  data = pd.read_csv('/kaggle/input/heart-disease/heart.csv')
  print('Shape of the data is ', data.shape)
  st.dataframe(dt, use_container_width=True, height=300)

