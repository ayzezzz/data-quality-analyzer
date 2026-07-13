# 📊 Data Quality Analyzer & Cleaner

An interactive, user-friendly web application built with Streamlit and Pandas designed to automatically analyze, evaluate, and clean CSV datasets instantly. 

This tool serves as an essential utility for data analysts to accelerate the data-pre-processing phase.

## Key Features
- **Data Quality Scoring:** Dynamically calculates an overall data quality score (0-100%) based on total missing cells and duplicate rows.
- **Data Overview:** Instantly displays total rows, columns, duplicate records, and a neat dataset preview.
- **Missing Data Analysis:** Identifies columns containing missing data with exact counts and percentages, coupled with a visual bar chart representation.
- **Column Distribution Analysis:** Interactive visualization allowing users to select any column and instantly view its distribution (Histogram with KDE for numerical data, Bar chart for categorical data).
- **Interactive Data Cleaning Wizard:** - One-click removal of all duplicate records.
  - Advanced missing value imputation choices (Drop rows, Fill with Mean/Median for numeric data, or Fill with Mode for categorical data).
- **Export Refined Data:** Download the completely cleaned dataset as a fresh CSV file with a single click.

## 🛠️ Tech Stack
- **Core:** Python
- **Data Manipulation:** Pandas
- **Web Framework:** Streamlit
- **Data Visualization:** Matplotlib, Seaborn

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>