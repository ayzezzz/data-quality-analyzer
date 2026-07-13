# 📊 Data Quality Analyzer & Cleaner

A Streamlit application for analyzing, assessing, and cleaning CSV datasets. The tool helps identify common data quality issues and provides interactive options to clean and export the processed dataset.

---

## 🚀 Features

- Calculate an overall data quality score based on missing values and duplicate records.
- Display dataset summary, including rows, columns, duplicates, and a data preview.
- Analyze missing values with counts, percentages, and visualizations.
- Explore column distributions using histograms or bar charts.
- Remove duplicate rows.
- Handle missing values using:
  - Drop rows
  - Mean or median (numeric columns)
  - Mode (categorical columns)
- Export the cleaned dataset as a CSV file.

---

## 🛠️ Tech Stack

- Python
- Pandas
- Streamlit
- Matplotlib
- Seaborn

---
## 💻 Run Locally

```bash
# Clone the repository and navigate to the project folder
git clone [https://github.com/ayzezzz/data-quality-analyzer.git](https://github.com/ayzezzz/data-quality-analyzer.git)
cd data-quality-analyzer

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment:
# On macOS / Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install requirements and run the application
pip install -r requirements.txt
python -m streamlit run app.py
