# Credit-Card-Fraud-Detection-Analysis
Built a Python-based ETL pipeline using Pandas to process 284K+ credit card transactions and analyze fraud patterns. Developed an interactive Tableau dashboard to visualize fraud vs normal transactions, fraud spikes over time, and transaction amount anomalies to support fraud detection insights.
# Credit Card Fraud Detection Analysis

## 📊 Live Dashboard

Explore the interactive Tableau dashboard here:

🔗 https://public.tableau.com/app/profile/praneel.reddy.kanduri/viz/fraud_detection_dashboard_twbx/CreditCardFraudDetectionAnalysis?publish=yes

---

# 📌 Project Overview

This project analyzes credit card transactions to detect fraud patterns using **Python, Pandas, and Tableau**.
A simple **ETL pipeline** was implemented to extract, clean, and transform transaction data before visualizing it through an interactive dashboard.

The dataset contains **284,807 transactions**, of which **492 are fraudulent**, representing only **0.17% of total transactions**, making it a highly **imbalanced dataset**. ([riverml.xyz][1])

The goal of this project is to explore fraud behavior and uncover patterns that could help identify suspicious transactions.

---

# 🛠 Technologies Used

* **Python**
* **Pandas**
* **Tableau**
* **ETL Pipeline**
* **Data Visualization**

---

# 📂 Project Structure

```
credit-card-fraud-detection
│
├── data
│   └── creditcard.csv
│
├── scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── etl_pipeline.py
│
├── dashboard
│   └── fraud_detection_dashboard.twbx
│
└── README.md
```

---

# ⚙️ ETL Pipeline

The ETL pipeline consists of three stages:

### Extract

Loads the dataset using **Pandas**.

### Transform

Performs:

* Data inspection
* Fraud vs normal distribution analysis
* Feature exploration

### Load

Exports processed data for visualization in **Tableau**.

---

# 📈 Dashboard Insights

The dashboard includes three key analyses:

### 1️⃣ Fraud vs Normal Transactions

Shows the extreme **class imbalance** between legitimate and fraudulent transactions.

### 2️⃣ Fraud Transactions Over Time

Highlights **temporal spikes in fraud activity**, showing that fraudulent transactions occur in bursts rather than uniformly.

### 3️⃣ Transaction Amount Distribution

Displays how fraudulent transactions differ in **amount distribution compared to normal transactions**.

---

# 🔍 Key Findings

* Fraud transactions represent **only ~0.17% of total transactions**
* Fraud tends to occur in **clusters over time**
* Fraudulent transactions show **higher variability in transaction amounts**

---

# 🚀 How to Run the Project

Clone the repository:

```
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

Run the ETL pipeline:

```
python scripts/etl_pipeline.py
```

Open the Tableau dashboard:

```
dashboard/fraud_detection_dashboard.twbx
```

---

# 💼 Resume Description

**Credit Card Fraud Detection Analysis | Python, Pandas, Tableau**

* Built a Python **ETL pipeline** to process **284K+ credit card transactions**
* Performed **data cleaning and transformation using Pandas**
* Developed **interactive Tableau dashboards** to analyze fraud patterns
* Identified **temporal fraud spikes and anomalous transaction behavior**

---

# 📬 Author

**Praneel Reddy Kanduri**

Data Analyst | Python | SQL | Tableau

[1]: https://riverml.xyz/0.11.1/api/datasets/CreditCard/?utm_source=chatgpt.com "CreditCard - River"
