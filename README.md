# Crypto Trader Sentiment & Behavior Analysis

This project analyzes the relationship between market sentiment (using the **Fear & Greed Index**) and trader behavior (using **Historical Trading Data**). It includes data processing pipelines, behavioral segmentation, actionable strategy generation, and an interactive Streamlit dashboard.

## 📂 Project Structure

```text
├── data/
│   ├── fear_greed_index.csv       # Market sentiment data (Required)
│   ├── historical_data.csv        # Trader execution data (Required)
├── notebooks/
│   ├── analysis_main.ipynb        # Jupyter Notebook containing Parts A, B, and C
├── dashboard/
│   ├── app.py                     # Streamlit Dashboard (Bonus Part)
├── README.md                      # Project documentation
└── requirements.txt               # List of dependencies
```

---

## 🚀 Setup & Installation

### 1. Prerequisites

Ensure you have **Python 3.8+** installed.

### 2. Install Dependencies

Create a virtual environment (recommended) and install the required libraries:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install libraries
pip install pandas numpy matplotlib seaborn scikit-learn streamlit plotly
```

**`requirements.txt` content:**

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
plotly
```

---

## 🏃‍♂️ How to Run

### Part 1: Data Analysis & Strategy (Jupyter Notebook)

To run the core analysis (Parts A, B, and C), use the provided Jupyter Notebook code.

1. Ensure `fear_greed_index.csv` and `historical_data.csv` are in your working directory.
2. Launch Jupyter:

```bash
jupyter notebook
```

3. Open the notebook and execute the cells sequentially:
   * **Part A:** Loads data, cleans timestamps, and calculates daily metrics.
   * **Part B:** Analyzes performance vs. sentiment and segments traders (Whales vs. Retail, etc.).
   * **Part C:** Outputs actionable trading rules (e.g., "Panic Filter").
   * **Bonus:** Runs the predictive model and clustering algorithms.

---

### Part 2: Interactive Dashboard (Streamlit)

To visualize the insights and play with the predictive model:

1. Save the dashboard code (provided in the Bonus section) as `app.py`.
2. Run the application from your terminal:

```bash
streamlit run app.py
```

3. The dashboard will open in your browser at `http://localhost:8501`.

---

## 📊 Features & Insights

### 1. Data Preparation

* **Alignment:** Merges trading data with daily sentiment scores using normalized timestamps.
* **Metrics:** Calculates Daily PnL, Win Rates, Average Trade Sizes, and Long/Short Ratios.

### 2. Analysis Modules

* **Sentiment Impact:** Compares trader performance during "Extreme Fear" vs. "Extreme Greed".
* **Segmentation:** Clusters traders into archetypes (e.g., "High-Freq Scalpers", "Risk-Takers").
* **Pattern Recognition:** Identifies over-trading behaviors during high volatility.

### 3. Actionable Strategies

The code generates specific rules based on the data, such as:

* **"Calm the Chaos":** Reduces position size by 50% when the Index is < 25 (Extreme Fear).
* **"Fade the Hype":** Shifts to short-selling strategies when the Index is > 70 (Greed).

### 4. Predictive Modeling

* **Next-Day Predictor:** A Random Forest model that predicts if the *next* trading day will be profitable based on current volume and sentiment.
* **Clustering:** K-Means algorithm to group traders based on trading frequency, size, and win rate.

---

## ⚠️ Notes on Data

* **Timestamps:** The code assumes `DD-MM-YYYY` format. If your CSVs use a different format, adjust the `pd.to_datetime` parameters in the loading cell.
* **Missing Values:** The pipeline handles missing sentiment days by left-joining; trades on days without sentiment data will have `NaN` classification.
