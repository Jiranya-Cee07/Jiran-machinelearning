import streamlit as st
import streamlit as st
import pandas as pd

st.title('Heart Disease Predictions')

st.info('ข้อมูลสำหรับทำนาย')

with st.expander('ข้อมูล Heart Disease Predictions'):
  st.write('ข้อมูลทั้งหมด')
  dt = pd.read_csv("./data/heart.csv")
  st.dataframe(dt, use_container_width=True, height=300)
  st.write('หมายเหตุ')
  st.markdown("""
| **ชื่อตัวแปร** | **ความหมาย** |
|:---|:---|
| **age** | อายุ (ปี) |
| **sex** | เพศ<br>1 = ชาย<br>0 = หญิง |
| **cp** | ประเภทของอาการเจ็บหน้าอก<br>0 = Typical Angina<br>1 = Atypical Angina<br>2 = Non-anginal Pain<br>3 = Asymptomatic |
| **trestbps** | ความดันโลหิตขณะพัก (mmHg) |
| **chol** | ระดับคอเลสเตอรอลในเลือด (mg/dL) |
| **fbs** | ระดับน้ำตาลในเลือดหลังอดอาหาร<br>1 = มากกว่า 120 mg/dL<br>0 = ไม่เกิน 120 mg/dL |
| **restecg** | ผลตรวจคลื่นไฟฟ้าหัวใจขณะพัก |
| **thalach** | อัตราการเต้นของหัวใจสูงสุด |
| **exang** | อาการเจ็บหน้าอกจากการออกกำลังกาย<br>1 = มี<br>0 = ไม่มี |
| **oldpeak** | ระดับ ST Depression จากการออกกำลังกาย |
| **slope** | ความชันของช่วง ST<br>0 = Upsloping<br>1 = Flat<br>2 = Downsloping |
| **ca** | จำนวนหลอดเลือดหัวใจหลัก (0–3) |
| **thal** | 0 = Error, 1 = Fixed Defect, 2 = Normal, 3 = Reversible Defect |
| **target** | 0 = ไม่เป็นโรคหัวใจ<br>1 = เป็นโรคหัวใจ |
""", unsafe_allow_html=True)
