import streamlit as st
import streamlit as st
import pandas as pd

st.title('Heart Disease Predictions')

st.info('ข้อมูลสำหรับทำนาย')

st.subheader("ข้อมูลทั้งหมด")
dt = pd.read_csv("./data/Heart3.csv")
st.dataframe(dt, use_container_width=True, height=300)
