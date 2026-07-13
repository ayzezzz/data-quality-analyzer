import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Quality Analyzer")
st.write("CSV dosyanı yükle, otomatik analiz edelim.")

uploaded_file = st.file_uploader("CSV dosyası seç", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Genel Bilgiler")
    st.write(f"Satır sayısı: {df.shape[0]}")
    st.write(f"Sütun sayısı: {df.shape[1]}")
    st.write(f"Yinelenen kayıt sayısı: {df.duplicated().sum()}")
    
    st.subheader("Sütun Tipleri")
    col_types = pd.DataFrame({
        "Sütun": df.columns,
        "Tip": df.dtypes.values,
        "Tür": ["Sayısal" if df[col].dtype in ["int64","float64"] else "Kategorik" for col in df.columns]
    })
    st.dataframe(col_types)
    
    st.subheader("Eksik Veri Analizi")
    missing = pd.DataFrame({
        "Sütun": df.columns,
        "Eksik Sayısı": df.isnull().sum().values,
        "Eksik Yüzdesi (%)": (df.isnull().sum().values / len(df) * 100).round(2)
    })
    st.dataframe(missing)
    
    st.subheader("Eksik Veri Grafiği")
    fig, ax = plt.subplots(figsize=(10, 4))
    missing_filtered = missing[missing["Eksik Sayısı"] > 0]
    if len(missing_filtered) > 0:
        ax.bar(missing_filtered["Sütun"], missing_filtered["Eksik Yüzdesi (%)"])
        ax.set_xlabel("Sütun")
        ax.set_ylabel("Eksik Yüzdesi (%)")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig)
    else:
        st.write("Hiç eksik veri yok!")
    
    st.subheader("Temel İstatistikler")
    st.dataframe(df.describe())