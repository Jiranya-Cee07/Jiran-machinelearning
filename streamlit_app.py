import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

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

    with st.expander("📝 ดูคำอธิบายตัวแปร"):
        st.write("""
    - Age: อายุ
    - Sex: เพศ
    - cp: อาการเจ็บหน้าอก
    - trestbps: ความดันโลหิตขณะพัก (mmHg) 
    - chol: ระดับคอเลสเตอรอลในเลือด (mg/dL)
    - fbs: ระดับน้ำตาลในเลือดหลังอดอาหาร
    - restecg: ผลการตรวจคลื่นไฟฟ้าหัวใจขณะพัก
    - thalach: อัตราการเต้นของหัวใจสูงสุดที่วัดได้ 
    - exang: อาการเจ็บหน้าอกจากการออกกำลังกาย
    - oldpeak: ระดับการลดลงของช่วง ST ที่เกิดจากการออกกำลังกายเมื่อเทียบกับขณะพัก
    - slope: ลักษณะความชันของช่วง ST ขณะออกกำลังกายสูงสุด
    - ca: จำนวนหลอดเลือดหัวใจหลัก ที่ตรวจพบด้วยการฉีดสี มีค่า 0–3
    - thal: ผลการตรวจ Thalassemia/Thallium Stress Test
    - target: ตัวแปรเป้าหมาย สำหรับการทำนาย
    """)

# สถิติพื้นฐาน
st.subheader("📈 สถิติพื้นฐานของข้อมูล")
st.write(dt.describe())

with st.sidebar:
    st.header('รับข้อมูล')
    Age = st.slider('อายุ(Age)', 1, 100, 1)
    Sex = st.selectbox('เพศ(Sex)',('ชาย','หญิง'))
    cp = st.selectbox('อาการเจ็บหน้าอก(cp)',('เจ็บหน้าอกปกติ','เจ็บหน้าอกผิดปกติ','เจ็บหน้าอกที่ไม่ได้เกิดจากโรคหลอดเลือดหัวใจ','ไม่มีอาการ'))
    trestbps =  st.slider('ความดันโลหิตขณะพัก(mmHg)(trestbps)', 1, 200, 50)
    chol = st.slider('ระดับคอเลสเตอรอลในเลือด(mg/dL)(chol)', 1, 500, 150)
    fbs = st.selectbox('ระดับน้ำตาลในเลือดหลังอดอาหาร(fbs)',('มากกว่า 12ไม่เกิน 120 mg/dL','ไม่เกิน 120 mg/dL'))
    restecg = st.selectbox('ผลการตรวจคลื่นไฟฟ้าหัวใจขณะพัก(restecg)',('ปกติ','มีความผิดปกติของคลื่น ST-T','มีภาวะหัวใจห้องล่างซ้ายโต ตามเกณฑ์ของ Estes'))
    thalach = st.slider('อัตราการเต้นของหัวใจสูงสุดที่วัดได้(thalach)', 1, 250, 100)
    exang = st.selectbox('อาการเจ็บหน้าอกจากการออกกำลังกาย(exang)',('มี','ไม่มี'))
    oldpeak = st.slider('ระดับการลดลงของช่วง ST ที่เกิดจากการออกกำลังกายเมื่อเทียบกับขณะพัก(oldpeak)', 0.0, 10.00, 6.0)
    slope =  st.selectbox('ลักษณะความชันของช่วง ST ขณะออกกำลังกายสูงสุด(slope)',('ชันขึ้น (Upsloping)','ราบ (Flat)','ชันลง (Downsloping)'))
    ca = st.selectbox('จำนวนหลอดเลือดหัวใจหลัก ที่ตรวจพบด้วยการฉีดสี มีค่า 0–3(ca)',('0','1','2','3'))
    thal = st.selectbox('ผลการตรวจ Thalassemia/Thallium Stress Test(thal)',('ข้อมูลผิดพลาดหรือไม่มีข้อมูล','ผิดปกติแบบคงที่','ปกติ (Normal)','ผิดปกติที่สามารถกลับคืนได้ (Reversible Defect)'))
    

    predict_btn = st.button("❤️ ทำนายผล"):



Sex = 1 if Sex == "ชาย" else 0


cp = {
    'เจ็บหน้าอกปกติ': 0,
    'เจ็บหน้าอกผิดปกติ': 1,
    'เจ็บหน้าอกที่ไม่ได้เกิดจากโรคหลอดเลือดหัวใจ': 2,
    'ไม่มีอาการ': 3
}[cp]


fbs = 1 if fbs == 'มากกว่า 120 mg/dL' else 0


restecg = {
    'ปกติ': 0,
    'มีความผิดปกติของคลื่น ST-T': 1,
    'มีภาวะหัวใจห้องล่างซ้ายโต ตามเกณฑ์ของ Estes': 2
}[restecg]


exang = 1 if exang == 'มี' else 0


slope = {
    'ชันขึ้น (Upsloping)': 0,
    'ราบ (Flat)': 1,
    'ชันลง (Downsloping)': 2
}[slope]


thal = {
    'ข้อมูลผิดพลาดหรือไม่มีข้อมูล': 0,
    'ผิดปกติแบบคงที่': 1,
    'ปกติ (Normal)': 2,
    'ผิดปกติที่สามารถกลับคืนได้ (Reversible Defect)': 3
}[thal]
    
    # -------------------------------
# สร้าง DataFrame สำหรับส่งเข้าโมเดล
# -------------------------------

data = {
    'age': Age,
    'sex': Sex,
    'cp': cp,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs,
    'restecg': restecg,
    'thalach': thalach,
    'exang': exang,
    'oldpeak': oldpeak,
    'slope': slope,
    'ca': int(ca),
    'thal': thal
}

if predict_btn:

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ มีความเสี่ยงโรคหัวใจ")
    else:
        st.success("✅ ไม่มีความเสี่ยงโรคหัวใจ")
















