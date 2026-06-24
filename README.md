# Shopper Spectrum: Customer Segmentation & Product Recommendation System

## Project Overview

Shopper Spectrum is a machine learning-based retail analytics project designed to analyze customer purchasing behavior and generate personalized product recommendations. The project combines Customer Segmentation using RFM Analysis and K-Means Clustering with an Item-Based Collaborative Filtering Recommendation System to help businesses improve customer retention, customer engagement, and sales performance.

---

## Problem Statement

Retail businesses generate large amounts of transactional data, but extracting meaningful insights from this data can be challenging. This project aims to:

* Identify different customer segments based on purchasing behavior.
* Detect high-value and at-risk customers.
* Recommend similar products based on customer purchase history.
* Support data-driven marketing and sales strategies.

---

## Dataset Description

The dataset contains retail transaction records including:

* Invoice Number
* Customer ID
* Product Description
* Quantity
* Unit Price
* Invoice Date
* Country

---

## Project Workflow

### 1. Data Preprocessing

* Handled missing values
* Removed duplicate records
* Excluded cancelled invoices
* Removed invalid transactions
* Standardized date formats
* Treated outliers using IQR Method

### 2. Exploratory Data Analysis (EDA)

* Transaction Volume by Country
* Top Selling Products
* Purchase Trends Over Time
* Monetary Distribution Analysis
* Correlation Heatmap
* Pair Plot
* RFM Distributions
* Product Similarity Heatmap

### 3. Customer Segmentation

#### RFM Analysis

* Recency
* Frequency
* Monetary

#### Clustering

* Feature Scaling using StandardScaler
* K-Means Clustering
* Elbow Method
* Silhouette Score
* Cluster Profile Analysis

Customer Segments:

* VIP Customers
* High Value Customers
* Regular Customers
* At Risk Customers

### 4. Recommendation System

Implemented Item-Based Collaborative Filtering:

* Customer-Product Matrix
* Cosine Similarity
* Product Similarity Matrix
* Top 5 Product Recommendations

---

## Streamlit Application Features

### Customer Segmentation Module

Users can input:

* Recency
* Frequency
* Monetary

The application predicts the customer segment.

### Product Recommendation Module

Users can select a product and receive:

* Top 5 Similar Product Recommendations

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Joblib

---

## Project Structure

```text
Shopper Spectrum/
│
├── app.py
├── recommendation.py
├── segmentation.py
│
├── models/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│   └── product_similarity.pkl
│
├── data/
│   └── OnlineRetail.xlsx
│
└── README.md
```

---

## Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Business Impact

* Identifies valuable customers
* Detects at-risk customers
* Improves customer retention
* Enables personalized marketing
* Supports cross-selling and upselling
* Enhances customer experience
* Increases revenue opportunities

---

## Conclusion

Shopper Spectrum demonstrates how machine learning and data analytics can transform retail transaction data into actionable business insights. By combining customer segmentation and recommendation techniques, the project helps businesses improve customer engagement, optimize marketing strategies, and drive sales growth through personalized recommendations and data-driven decision-making.
