import streamlit as st
import streamlit as st
import pandas as pd

st.title('Heart Disease Predictions')

st.info('ข้อมูลสำหรับทำนาย')

with st.expander('ข้อมูลทั้งหมด'):
  dt = pd.read_csv("./data/Heart3.csv")
  st.dataframe(dt, use_container_width=True, height=300)

pt_age = st.number_input("กรุณาเลือกข้อมูล Age")
pt_sex = st.number_input("กรุณาเลือกข้อมูล Sex")
sp_ChestPainType = st.number_input("กรุณาเลือกข้อมูล ChestPainType")
sp_RestingBP = st.number_input("กรุณาเลือกข้อมูล RestingBP")
pt_Cholesterol = st.number_input("กรุณาเลือกข้อมูล Cholesterol")
pt_FastingBS = st.number_input("กรุณาเลือกข้อมูล FastingBS")
sp_RestingECG = st.number_input("กรุณาเลือกข้อมูล RestingECG")
sp_MaxHR = st.number_input("กรุณาเลือกข้อมูล MaxHR")
sp_ExerciseAngina = st.number_input("กรุณาเลือกข้อมูล ExerciseAngina")
sp_Oldpeak = st.number_input("กรุณาเลือกข้อมูล Oldpeak")
sp_ST_Slope = st.number_input("กรุณาเลือกข้อมูล ST_Slope")

if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/Heart3.csv") 
   X = dt.drop('HeartDisease', axis=1)
   y = dt.HeartDisease  

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)  
    
   x_input = np.array([[pt_age, pt_sex, sp_ChestPainType, sp_RestingBP, pt_Cholesterol, pt_FastingBS, sp_RestingECG, sp_MaxHR, sp_ExerciseAngina,
                        sp_Oldpeak, sp_ST_Slope]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == '1':
    st.write("เป็นโรคหัวใจ")
   
   else:
    st.write("ไม่เป็นโรคหัวใจ")
    
else:
    st.write("ไม่ทำนาย")
