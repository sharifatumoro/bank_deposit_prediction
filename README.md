# Bank Deposit Subscription Prediction

## Overview

This project builds and evaluates machine learning models to predict whether a bank customer will subscribe to a term deposit. The project is designed as an industry-style portfolio project that demonstrates a full tabular machine learning workflow, from exploratory analysis and preprocessing to model training, evaluation, comparison, interpretation and deployment.

## Business Problem

Banks run marketing campaigns to promote term deposit products, but not every contacted customer is equally likely to subscribe. A prediction system can help analysts and campaign teams understand which factors are associated with subscription and which models perform best for this classification task.

## Project Objective

The objective of this project is to build and compare multiple classification models that predict deposit subscription using customer information, financial variables, and campaign-related features, then deploy the strongest final model in a Streamlit app.

## Project Framing

This project is framed as a **post-contact analysis**. That means variables such as:

- `duration`
- `contact`
- `campaign`
- `previous`
- `poutcome`

are considered valid predictors because they are available in the analysis setting being modeled.

## Dataset

The dataset used is a bank marketing dataset stored as `bank.csv`.

### Dataset summary

- Number of rows: 11,162
- Number of columns: 17

### Target variable

- `deposit = yes` means the customer subscribed to a term deposit
- `deposit = no` means the customer did not subscribe

### Feature groups

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
- `contact` = contact communication type
- `day` = last contact day of the week
- `month` = last contact month of year
- `duration` = last contact duration, in seconds
- `campaign` = number of contacts performed during this campaign
- `pdays` =  number of days that passed by after the client was last contacted from a previous campaign 
- `previous` =   number of contacts performed before this campaign and for this customer
- `poutcome` =  outcome of the previous marketing campaign

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Scikit-learn
- Streamlit
- Joblib

## Exploratory Data Analysis

Exploratory data analysis was carried out to understand the structure of the data and the relationships between customer and campaign variables and the deposit outcome.

### Visualizations created

Below are some of the visualizations used during analysis:

- Distribution of contact
- Educational  status distribution 
- segmented bar chart for `default` vs `deposit`
- mosaic plot for `month` vs `deposit`
- KDE plot for `balance` vs `deposit`
- boxplot and distribution analysis for `duration` vs `deposit`
- mean bar chart for `campaign` vs `deposit`
- heatmap of numerical features

### Key EDA findings

- Customers with tertiary education appeared more likely to subscribe than those with primary education.
- The distribution of `balance` suggested that subscribers tend to have slightly higher balances on average, although the two groups overlap considerably.
- Customers with longer duration are more likely to suscribe than otherwise. 
- Previous campaign history appeared to be important, especially `poutcome` and `previous`.
- Campaign timing, especially `month`, showed a strong relationship with deposit subscription.

## Preprocessing

The preprocessing workflow included:
- dropping `day` and `pdays`
- encoding the target variable manually
- identifying categorical and numerical columns
- one-hot encoding categorical variables
- scaling numerical variables for linear and distance-based models
- stratified train-test split

## Models Trained

The following models were trained and evaluated:

- Logistic Regression
- Support Vector Classifier
- K-Nearest Neighbors
- Decision Tree
- Random Forest

## Baseline Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.825 | 0.827 | 0.798 | 0.812 | 0.907 |
| SVC | 0.847 | 0.818 | 0.870 | 0.843 | 0.911 |
| KNN | 0.823 | 0.820 | 0.802 | 0.811 | 0.892 |
| Decision Tree | 0.780 | 0.773 | 0.759 | 0.766 | 0.779 |
| Random Forest | 0.855 | 0.824 | 0.883 | 0.852 | 0.915 |

## Hyperparameter Tuning Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|---|---:|---:|---:|---:|---:|
| Tuned Logistic Regression | 0.829 | 0.822 | 0.818 | 0.820 | 0.907 |
| Tuned SVC | 0.849 | 0.814 | 0.882 | 0.849 | 0.916 |
| Tuned Random Forest | 0.854 | 0.819 | 0.887 | 0.858 | 0.918 |

## Model Comparison

### Key takeaways
- **Tuned Random Forest** was the strongest final model overall
- **Tuned SVM** performed very strongly and ranked second
- **Logistic Regression** remained the most interpretable model
- **KNN** performed reasonably well but did not outperform the top models
- **Decision Tree** was the weakest model in this project

### Final ranking by predictive performance
1. Tuned Random Forest  
2. Tuned SVM  
3. Untuned Random Forest  
4. Untuned SVM  
5. Tuned Logistic Regression  
6. Untuned Logistic Regression  
7. KNN  
8. Decision Tree  

## Feature Importance Insights

Coefficient analysis from Random Forest showed that the most influential variables were mainly campaign-related:

- `duration`
- `month`
- `poutcome`

This suggests that campaign timing, interaction context, and prior campaign outcomes matter more than basic demographic variables alone.

## Final Model

The final selected model for deployment is:

**Tuned Random Forest**

It was chosen because it achieved the strongest overall balance of:
- recall
- F1 score
- ROC AUC

## Streamlit Deployment

The final model was deployed using Streamlit.

### App features
- input customer and campaign details
- generate a deposit subscription prediction
- display probability of subscription

## Project Structure

```bash
bank-deposit-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── bank.csv
│   └── cleaned_bank.csv
│   └──test_data.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_train.ipynb
│   └── 03_evaluation.ipynb
│
├── model/
│   └── log_model.pkl
│   └── knn__model.pkl
│   └── dt__model.pkl
│   └── svc__model.pkl
│   └── rf__model.pkl
│   └── tuned__rf.pkl
│
├── README.md
├── .gitignore
└── requirements.txt
```

## Portfolio Value

This project demonstrates:

- Strong EDA and analytical thinking
- Ability to connect data insights to business problems
- End-to-end machine learning workflow
- Practical skills in feature engineering, tuning, and deployment
- Clean and structured project organization suitable for production

## How to Run Locally

```bash
git clone https://github.com/sharifatumoro/bank_deposit_prediction.git
cd bank-deposit-prediction
pip install -r requirements.txt
streamlit run app/app.py
```

## 👤 Author

**Sharifatu Moro**
Aspiring Data Scientist & Machine Learning Engineer 
Background: Economics

🔗 *Actively building projects in Machine Learning*

