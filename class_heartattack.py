import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('heart_attack.sav', 'rb'))

st.title('Prediksi Serangan Jantung')
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Umur Pasien')
    cp = st.number_input('Tipe dari nyeri dada')
    chol = st.number_input('Kolestoral dalam mg/dl diambil melalui sensor BMI')
    restecg = st.number_input('Hasil Elektrokardiografi Istirahat')
    exng = st.number_input('olahraga untuk induksi angina')
    slp = st.number_input('Perubahan Kemampuan Bicara')
    thall = st.number_input('Kecacatan')

with col2:
    sex = st.number_input('Gender Pasien')
    trtbps = st.number_input('Tekanan darah pasien (mm Hg)')
    fbs = st.number_input('Gula Darah ketika Puasa')
    thalachh = st.number_input('Denyut Jantung Maksimum')
    oldpeak = st.number_input('Penurunan ST saat Istirahat')
    caa = st.number_input('Jumlah Pembuluh Darah')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])

    if(predik[0] == 1):
        predik = 'Kemungkinan Besar Pasien terkena Serangan Jantung'
    else:
        predik = 'Kemungkinan Kecil Pasien terkena Serangan Jantung'
st.success(predik)