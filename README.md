# Corporate Financial Intelligence Platform (CFIP)

> An end-to-end financial analytics platform built with Python, Streamlit, Plotly, Pandas, NumPy, and the Yahoo Finance API that transforms raw financial statements into actionable insights through financial ratio analysis, Altman Z-Score, the Corporate Financial Health Index (CFHI), interactive visualizations, and executive financial summaries.


## 🚀 Live Demo

> ## 🚀 Live Demo

**Try the live application here:**
https://corporate-financial-intelligence-platform-nnbvpdwvvysuuzvow8hw.streamlit.app/

---

##  Overview

The **Corporate Financial Intelligence Platform (CFIP)** is an interactive web application that simplifies corporate financial analysis by converting complex financial statements into meaningful business insights.

Using real-time financial data from **Yahoo Finance**, the platform automatically evaluates a company's financial health through financial ratios, bankruptcy risk assessment, a proprietary financial scoring model (**CFHI**), and interactive dashboards.

The goal of this project is to provide an intuitive financial analysis tool that enables students, analysts, investors, and finance professionals to understand corporate financial performance without manually interpreting extensive financial statements.

---

# Project Objectives

* Automate financial statement analysis.
* Evaluate corporate financial health using standardized financial ratios.
* Assess bankruptcy risk using the Altman Z-Score.
* Develop a proprietary Corporate Financial Health Index (CFHI).
* Present financial insights through an interactive dashboard.
* Make financial analysis more accessible through data visualization.

---

# Features

### Financial Statement Analysis

* Income Statement
* Balance Sheet
* Key Financial Metrics

### Financial Ratio Analysis

The platform automatically calculates **13 financial ratios** across four major categories:

#### Profitability

* Gross Margin
* Operating Margin
* Net Margin
* Return on Assets (ROA)
* Return on Equity (ROE)

#### Liquidity

* Current Ratio
* Quick Ratio
* Cash Ratio

#### Solvency

* Debt-to-Assets Ratio
* Debt-to-Equity Ratio
* Equity Ratio
* Interest Coverage Ratio

#### Efficiency

* Asset Turnover Ratio

---

# Corporate Financial Health Index (CFHI)

The **Corporate Financial Health Index (CFHI)** is a proprietary financial scoring model developed specifically for this project.

The model combines financial ratios into four weighted dimensions:

* Profitability
* Liquidity
* Solvency
* Efficiency

Each category is benchmarked and scored to generate an overall **Financial Health Score (0–100)**, allowing users to evaluate corporate financial strength through a single comprehensive metric.

---

# Bankruptcy Risk Assessment

The dashboard incorporates the **Altman Z-Score** model to estimate bankruptcy risk and classify companies into:

* 🟢 Safe Zone
* 🟡 Grey Zone
* 🔴 Distress Zone

---

# Interactive Dashboard

The application includes interactive visualizations built using **Plotly**:

* Financial Health Radar Chart
* Revenue Trend Analysis
* Net Income Trend Analysis
* Multi-Year CFHI Trend

These visualizations enable users to quickly identify financial trends and evaluate company performance over multiple reporting periods.

---

# Executive Financial Summary

Based on the calculated financial metrics, CFHI score, and Altman Z-Score, the platform automatically generates an executive financial summary highlighting:

* Overall Financial Health
* Profitability
* Liquidity
* Solvency
* Operational Efficiency
* Bankruptcy Risk

This allows users to interpret financial performance without manually reviewing individual ratios.

---

# Technology Stack

| Category             | Technologies                 |
| -------------------- | ---------------------------- |
| Programming Language | Python                       |
| Web Framework        | Streamlit                    |
| Data Processing      | Pandas, NumPy                |
| Data Visualization   | Plotly                       |
| Financial Data       | Yahoo Finance API (yFinance) |

---

#  Project Structure

```text
Corporate_Financial_Health_Index/

├── app.py
├── altman.py
├── cfhi.py
├── data_fetcher.py
├── financial_metrics.py
├── industry_mapping.py
├── ratio_calculator.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Installation

```bash
git clone https://github.com/YOUR_USERNAME/Corporate-Financial-Intelligence-Platform.git

cd Corporate_Financial_Health_Index

pip install -r requirements.txt

streamlit run app.py
```

---

# Current Scope

The current version focuses on **non-financial companies**.

Financial institutions such as banks and insurance companies use specialized accounting standards and financial ratios, and therefore are outside the scope of the current CFHI model.

---

#  Future Enhancements

* Company Comparison Dashboard
* AI-Powered Financial Insights
* PDF Financial Report Generation
* Historical Stock Price Visualization
* Discounted Cash Flow (DCF) Valuation
* Peer Company Benchmarking
* Industry-Level Comparative Analysis

---

# Application Preview

Dashboard screenshots will be added after deployment.

---

# Data Source

Financial statement data is retrieved using the **Yahoo Finance API** through the **yFinance** Python library.

---

#  Author

**AMAR KUMAR**
Bachelor of Management Studies (BMS)
UNIVERSITY OF DELHI

Finance • Business Analytics • Python

---

## ⭐ If you found this project useful, consider giving it a star.
