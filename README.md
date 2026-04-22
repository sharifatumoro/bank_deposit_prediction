# 📊 Bank Marketing Deposit Prediction

### Logistic Regression | End-to-End Data Science Project

---

## 📌 Project Overview

This project aims to predict whether a client will subscribe to a **term deposit** using a bank marketing dataset. It follows a structured, real-world data science workflow—from data exploration to model development, evaluation and deployment.

At the current stage, the focus is on **Exploratory Data Analysis (EDA)** to uncover patterns, detect anomalies, and build strong intuition before modeling.

---

## 🎯 Business Problem

Banks run marketing campaigns to promote deposit products, but not every customer is equally likely to convert. Contacting all customers the same way can be inefficient and costly.

This project addresses that problem by predicting the likelihood that a customer will subscribe to a deposit product. The resulting model can support:

- customer targeting
- campaign prioritization
- probability-based lead scoring
- better allocation of marketing effort

---

## 🧠 Project Objectives
## Project Objective

The main objective of this project is to build an interpretable binary classification model that predicts deposit subscription using customer profile, financial, and campaign-related features.

## Dataset

The dataset used in this project is a bank marketing dataset stored as `bank.csv`.

### Target variable
- `deposit`
  - `yes` = customer subscribed
  - `no` = customer did not subscribe

### Feature categories

**Customer profile**
- `age` = age of the customer
- `job` = type of job
- `marital` = marital status
- `education`

**Financial information**
- `default` = has credit in default?
- `balance` 
- `housing` = has housing loan?
- `loan` = has personal loan?

**Campaign and contact information**
- `contact` = last contact month of year
- `day` = last contact day of the week
- `month` = last contact month of year
- `duration` = last contact duration, in seconds
- `campaign` = number of contacts performed during this campaign
- `pdays` =  number of days that passed by after the client was last contacted from a previous campaign 
- `previous` =   number of contacts performed before this campaign and for this customer
- `poutcome` =  outcome of the previous marketing campaign

## Project Scope

This project includes:

- exploratory data analysis
- univariate and bivariate visualizations
- preprocessing for mixed feature types
- logistic regression modeling
- model evaluation using classification metrics
- interpretation of feature relationships with deposit subscription
- deployment using streamlit

---

## Why Logistic Regression

Logistic regression was chosen because it is:

- suitable for binary classification
- fast and efficient for tabular data
- easy to interpret
- useful as a strong baseline model in real-world ML workflows

This makes it a good choice for demonstrating both machine learning fundamentals and business-facing model interpretation.

---

## 🔍 Exploratory Data Analysis (EDA)

### ✅ Univariate Analysis

* Analyzed distributions of individual variables
* Used normalized proportions to understand category dominance

### ✅ Bivariate Analysis

* Explored relationships between features and target variable
* Visualized patterns using:

  * Grouped bar charts
  * Stacked bar charts
  * KDE plot
  * Mosaic plots
  * Box plot 
  * Line chart

### ⏳ Multivariate Analysis *(In Progress)*

* Investigating combined feature interactions
* Identifying deeper patterns for segmentation

---

## 📊 Key Insights

-  Most clients do not have loans, which may affect subscription likelihood
- customers with tertiary education appear more likely to subscribe than those with primary education
- higher account balances are slightly associated with subscription, although the distributions overlap considerably
- subscription rate varies across the day of the month
- customers who subscribed were contacted fewer times on average during the campaign
- previous contact history appears strongly associated with higher subscription rates
- recency of previous contact also seems to matter

---

## Project Workflow

The workflow for this project is structured as follows:

1. Load and inspect the dataset
2. Perform exploratory data analysis
3. Clean and preprocess the data
4. Encode categorical features
5. Split data into training and test sets
6. Train a logistic regression model
7. Evaluate model performance
8. Deploy using streamlit

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels


---

## 🚧 Current Progress

| Stage                 | Status        |
| --------------------- | ------------- |
| Data Understanding    | ✅ Completed   |
| Data Cleaning         | ✅ Completed   |
| Univariate Analysis   | ✅ Completed   |
| Bivariate Analysis    | ✅ Completed   |
| Multivariate Analysis | ⏳ In Progress |
| Preprocessing         | ⏳ Not Started |
| Modeling              | ⏳ Not Started |
| Evaluation             | ⏳ Not Started |
| Deployment             | ⏳ Not Started |

---

## 🔜 Next Steps

* Complete multivariate analysis
* Handle categorical encoding (One-Hot / Label Encoding)
* Feature scaling (if necessary)
* Train-test split
* Build Logistic Regression model
* Hyperparameter tuning
* Evaluate using:

  * Accuracy
  * Precision & Recall
  * ROC-AUC Curve
* Interpret model coefficients
* Deploy  the model

---

## Repository Structure

```bash
bank-deposit-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── bank.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
│
├── model/
│   └── model.pkl
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 💼 Portfolio Value

This project demonstrates:

- Strong EDA and analytical thinking
- Ability to connect data insights to business problems
- End-to-end machine learning workflow
- Practical skills in feature engineering, tuning, and deployment
- Clean and structured project organization suitable for production

---

## 👤 Author

**Sharifatu Moro**
Aspiring Data Scientist

🔗 *Actively building projects in Machine Learning*

---

## ⭐ Acknowledgement

This project is inspired by real-world **bank marketing campaigns** and is built for learning and portfolio development.

---

## 📎 Note

This repository is actively being updated as the project progresses. Stay tuned for model development and results 🚀


