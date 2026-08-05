import streamlit as st
import pandas as pd

# -------------------------------
# ตั้งค่าหน้าเว็บ
# -------------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# -------------------------------
# โหลดข้อมูล
# -------------------------------
dt = pd.read_csv("./data/heart.csv")

# -------------------------------
# ส่วนหัว
# -------------------------------
st.title("❤️ Heart Disease Prediction")

st.info(
    """
    **Dataset : Heart Disease**

    ชุดข้อมูลนี้ใช้สำหรับฝึกโมเดล Machine Learning เพื่อทำนายความเสี่ยงของโรคหัวใจ
    """
)

# -------------------------------
# Tabs
# -------------------------------
tab1, tab2 = st.tabs(["📋 ข้อมูล Dataset", "📖 ความหมายตัวแปร"])

# -------------------------------
# Tab 1
# -------------------------------
with tab1:

    st.subheader("ข้อมูลทั้งหมด")

    st.dataframe(
        dt,
        use_container_width=True,
        height=400
    )

    st.caption(f"จำนวนข้อมูลทั้งหมด : {len(dt)} แถว   |   จำนวนตัวแปร : {len(dt.columns)} คอลัมน์")

# -------------------------------
# Tab 2
# -------------------------------
with tab2:

    st.markdown("""
| **ชื่อตัวแปร** | **ความหมาย** |
|:---|:---|
| **age** | อายุ (ปี) |
| **sex** | เพศ<br>**1 = ชาย**<br>**0 = หญิง** |
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
| **thal** | 0 = Error<br>1 = Fixed Defect<br>2 = Normal<br>3 = Reversible Defect |
| **target** | **0 = ไม่เป็นโรคหัวใจ**<br>**1 = เป็นโรคหัวใจ** |
""", unsafe_allow_html=True)
