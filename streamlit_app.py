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
    <style>
    .note-table{
        width:75%;
        margin:auto;
        border-collapse:collapse;
        font-size:14px;
    }

    .note-table th{
        background:#f2f2f2;
        text-align:center;
        padding:10px;
        border:1px solid #ddd;
    }

    .note-table td{
        padding:10px;
        border:1px solid #ddd;
        vertical-align:top;
    }

    .note-table td:first-child{
        width:120px;
        font-weight:bold;
    }
    </style>

    <table class="note-table">
        <tr>
            <th>ชื่อตัวแปร</th>
            <th>ความหมาย</th>
        </tr>

        <tr>
            <td>age</td>
            <td>อายุ (ปี)</td>
        </tr>

        <tr>
            <td>sex</td>
            <td>
                เพศ<br>
                1 = ชาย<br>
                0 = หญิง
            </td>
        </tr>

        <tr>
            <td>cp</td>
            <td>
                ประเภทของอาการเจ็บหน้าอก<br>
                0 = Typical Angina<br>
                1 = Atypical Angina<br>
                2 = Non-anginal Pain<br>
                3 = Asymptomatic
            </td>
        </tr>

        <!-- เพิ่มแถวอื่น ๆ ต่อได้ -->

    </table>
    """, unsafe_allow_html=True)
