import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Data Quality Analyzer", layout="wide")

st.title("📊 Data Quality Analyzer & Cleaner")
st.write("Upload your CSV file to automatically analyze, clean, and score your data quality.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Use session_state to persist data across rerenders during cleaning actions
    if 'df' not in st.session_state:
        st.session_state.df = pd.read_csv(uploaded_file)
    
    df = st.session_state.df

    # 1. DATA QUALITY SCORE CALCULATION (0-100)
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    
    # Calculate penalties
    missing_penalty = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
    duplicate_penalty = (duplicate_rows / df.shape[0]) * 100 if df.shape[0] > 0 else 0
    
    # Final Score (Ensuring it stays between 0 and 100)
    quality_score = max(0, min(100, round(100 - (missing_penalty + duplicate_penalty))))

    # Layout: Two columns (Left for analysis, Right for cleaning actions)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🧐 General Overview")
        
        # Display Metrics including the new Quality Score
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Rows", df.shape[0])
        kpi2.metric("Columns", df.shape[1])
        kpi3.metric("Duplicate Rows", duplicate_rows)
        
        # Color-coded Quality Score display
        if quality_score >= 80:
            kpi4.metric("Quality Score", f"{quality_score}%", delta="Good", delta_color="normal")
        elif quality_score >= 50:
            kpi4.metric("Quality Score", f"{quality_score}%", delta="Warning", delta_color="off")
        else:
            kpi4.metric("Quality Score", f"{quality_score}%", delta="Critical", delta_color="inverse")
        
        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(5))

        st.subheader("🔍 Missing Data Analysis")
        missing = pd.DataFrame({
            "Column": df.columns,
            "Missing Count": df.isnull().sum().values,
            "Missing Percentage (%)": (df.isnull().sum().values / len(df) * 100).round(2)
        })
        
        # Show only columns with missing data if they exist, otherwise show all
        st.dataframe(missing[missing["Missing Count"] > 0] if df.isnull().sum().sum() > 0 else missing)

        st.subheader("📊 Missing Data Chart")
        fig, ax = plt.subplots(figsize=(10, 3))
        missing_filtered = missing[missing["Missing Count"] > 0]
        if len(missing_filtered) > 0:
            sns.barplot(x="Column", y="Missing Percentage (%)", data=missing_filtered, ax=ax, palette="vlag")
            plt.xticks(rotation=45, ha="right")
            st.pyplot(fig)
        else:
            st.success("Perfect! No missing values detected in the dataset.")

        st.subheader("📈 Column Distribution Analysis")
        column = st.selectbox("Select a column to view distribution", df.columns)
        fig2, ax2 = plt.subplots(figsize=(10, 4))
        if df[column].dtype in ["int64", "float64"]:
            sns.histplot(df[column].dropna(), bins=30, kde=True, ax=ax2, color="skyblue")
        else:
            df[column].value_counts().head(10).plot(kind="bar", ax=ax2, color="salmon")
        ax2.set_title(f"{column} Distribution")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig2)

    with col2:
        st.subheader("🛠️ Data Cleaning Wizard")
        
        # Action 1: Remove Duplicates
        if duplicate_rows > 0:
            if st.button("Remove Duplicate Rows"):
                st.session_state.df = df.drop_duplicates()
                st.success("Duplicate rows removed successfully!")
                st.rerun()
        else:
            st.info("No duplicate rows found.")

        # Action 2: Handle Missing Values
        st.markdown("---")
        st.write("**Missing Data Actions:**")
        missing_cols = [col for col in df.columns if df[col].isnull().sum() > 0]
        
        if missing_cols:
            selected_missing_col = st.selectbox("Select column with missing values", missing_cols)
            action = st.radio("Choose Action", ["Drop Rows", "Fill with Mean (Numeric)", "Fill with Median (Numeric)", "Fill with Mode (Categorical)"])
            
            if st.button("Apply Action"):
                if action == "Drop Rows":
                    st.session_state.df = df.dropna(subset=[selected_missing_col])
                elif action == "Fill with Mean (Numeric)" and df[selected_missing_col].dtype in ["int64", "float64"]:
                    st.session_state.df[selected_missing_col] = df[selected_missing_col].fillna(df[selected_missing_col].mean())
                elif action == "Fill with Median (Numeric)" and df[selected_missing_col].dtype in ["int64", "float64"]:
                    st.session_state.df[selected_missing_col] = df[selected_missing_col].fillna(df[selected_missing_col].median())
                elif action == "Fill with Mode (Categorical)":
                    st.session_state.df[selected_missing_col] = df[selected_missing_col].fillna(df[selected_missing_col].mode()[0])
                
                st.success(f"Action applied to {selected_missing_col}!")
                st.rerun()
        else:
            st.info("No missing values left to clean.")

        # Action 3: DOWNLOAD BUTTON FOR CLEAN CSV
        st.markdown("---")
        st.subheader("💾 Export Clean Data")
        
        # Prepare the clean data for download
        csv_buffer = st.session_state.df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned CSV",
            data=csv_buffer,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )