# Credit Card Fraud Detection Analysis

This project analyzes credit card transaction data to identify fraud patterns using **Python, Pandas, and Tableau**.  
A Python-based **ETL (Extract, Transform, Load) pipeline** processes the dataset before building an interactive dashboard to explore fraud trends and anomalies.

🔗 **Live Dashboard:**  
https://public.tableau.com/app/profile/praneel.reddy.kanduri/viz/fraud_detection_dashboard_twbx/CreditCardFraudDetectionAnalysis

---

## Project Overview

The dataset contains **284,807 credit card transactions**, including **492 fraudulent transactions (~0.17%)**, making it a highly **imbalanced dataset**.  

This project focuses on analyzing transaction behavior to identify patterns associated with fraudulent activity.

Key objectives:

- Process raw transaction data using a **Python ETL pipeline**
- Perform **exploratory data analysis**
- Build a **Tableau dashboard** to visualize fraud patterns
- Identify anomalies in transaction amounts and time patterns

---

## Technologies Used

- **Python**
- **Pandas**
- **Tableau**
- **Git & GitHub**

---

## Project Structure


credit-card-fraud-detection
│
├── data
 └── creditcard.csv

├── scripts
 ├── extract.py
 ├── transform.py
 ├── load.py
 └── etl_pipeline.py

├── dashboard
 └── fraud_detection_dashboard.twbx

└── README.md


---

## ETL Pipeline

The ETL pipeline consists of three stages:

### Extract
Loads the dataset using **Pandas**.

### Transform
Performs:
- Data inspection
- Fraud vs normal transaction analysis
- Dataset structure exploration

### Load
Exports processed data for visualization in **Tableau**.

---

## Dashboard Insights

The Tableau dashboard includes three main analyses:

**Fraud vs Normal Transactions**  
Visualizes the class imbalance between legitimate and fraudulent transactions.

**Fraud Transactions Over Time**  
Shows temporal spikes in fraud activity.

**Transaction Amount Distribution**  
Highlights differences in transaction amounts between fraud and normal transactions.

---

## Key Findings

- Fraud transactions represent **~0.17% of the dataset**
- Fraud tends to occur in **short bursts over time**
- Fraudulent transactions show **greater variability in transaction amounts**

---


## Author

**Praneel Reddy Kanduri**  
Aspiring Data Analyst | Python | SQL | Tableau
