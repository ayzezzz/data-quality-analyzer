import streamlit as st
import pandas as pd

st.title("Data Quality Analyzer")
st.write("CSV dosyanı yükle, otomatik analiz edelim.")

uploaded_file = st.file_uploader("CSV dosyası seç", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Genel Bilgiler")
    st.write(f"Satır sayısı: {df.shape[0]}")
    st.write(f"Sütun sayısı: {df.shape[1]}")
    
    st.subheader("İlk 5 Satır")
    st.dataframe(df.head())
    
    st.subheader("Eksik Veriler")
    st.dataframe(df.isnull().sum().reset_index().rename(columns={0: "Eksik Sayısı", "index": "Sütun"}))
    
    st.subheader("Temel İstatistikler")
    st.dataframe(df.describe())