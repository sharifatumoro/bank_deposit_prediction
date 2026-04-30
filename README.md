# Bank Deposit Subscription Prediction

## Overview

This project builds a binary classification solution to predict whether a bank customer will subscribe to a term deposit. The model is based on logistic regression and is framed as a post-contact analysis, meaning campaign interaction variables such as contact duration, contact channel, campaign frequency, and previous campaign outcome are treated as valid predictors.

## Business Problem

Banks run marketing campaigns to promote term deposit products, but not every contacted customer is equally likely to subscribe. A prediction system can help analysts and campaign teams understand which factors are associated with subscription and which models perform best for this classification task.

## Project Objective

The objective of this project is to build and compare multiple classification models that predict deposit subscription using customer information, financial variables, and campaign-related features.

## Project Framing

This project is framed as a **post-contact analysis**. That means variables such as:

- `duration`
- `contact`
- `campaign`
- `pdays`
- `previous`
- `poutcome`

are considered valid predictors because they are available in the analysis setting being modeled.

## Dataset

The dataset used is a bank marketing dataset stored as `bank.csv`.

### Dataset summary

- Number of rows: 11,162
- Number of columns: 17
- Target variable: `deposit`
- Target classes:
  - `yes`
  - `no`

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
- Previous campaign history appeared to be important, especially `poutcome`, `pdays`, and `previous`.
- Campaign timing, especially `month`, showed a strong relationship with deposit subscription.

## Preprocessing

The preprocessing workflow was designed to prepare the data for logistic regression modeling in a clean and reusable way.

### Steps performed

- Loaded the dataset from CSV
- Manually encoded the target variable:
  - `no = 0`
  - `yes = 1`
- Split the data into features (`X`) and target (`y`)
- Identified categorical and numerical columns
- Applied one-hot encoding to categorical features
- Applied standard scaling to numerical features
- Performed a train test split using stratification to preserve class balance
- Built a model pipeline
- Performed hyperparameter tunning
- Saved the model

## Modeling Approach

A logistic regression model was trained using a Scikit-learn pipeline that combined preprocessing and classification into a single workflow.

### Why logistic regression

Logistic regression was selected because it is:

- suitable for binary classification
- efficient and fast on tabular data
- easy to interpret
- a strong baseline model for industrial machine learning workflows

## Model Evaluation

The logistic regression model was evaluated using the test set.

### Evaluation metrics

- Accuracy: **0.8253**
- Precision: **0.8275**
- Recall: **0.7977**
- F1 Score: **0.8123**
- ROC AUC: **0.9072**

### Interpretation of results

The model achieved strong predictive performance. It correctly classified about 82.5% of observations overall and showed a good balance between precision and recall. The ROC AUC score of 0.9072 indicates excellent class separability, meaning the model is highly effective at distinguishing subscribers from non-subscribers.

## Confusion Matrix Interpretation

The confusion matrix showed the following:

- True negatives: **999**
- True positives: **844**
- False positives: **176**
- False negatives: **214**

This indicates that the model performs well on both classes, but it misses some actual subscribers. This is consistent with recall being slightly lower than precision.

## ROC Curve Interpretation

The ROC curve stayed well above the diagonal reference line and approached the top-left corner. This supports the strong ROC AUC score and shows that the model has excellent discriminative ability across probability thresholds.

## Feature Importance and Coefficient Analysis

Since logistic regression is an interpretable model, feature importance was examined using model coefficients.

Because categorical variables were one-hot encoded, two levels of interpretation were used:

1. Encoded feature level coefficients
2. Original variable level importance by grouping encoded categories back to their source variable

### Variable-level importance based on summed absolute coefficients

| Variable   | Sum Absolute Coefficient |
|------------|---------------------------|
| month      | 9.988471 |
| job        | 3.865241 |
| poutcome   | 2.729840 |
| duration   | 1.887458 |
| contact    | 1.540865 |
| education  | 1.098738 |
| housing    | 0.677671 |
| loan       | 0.548744 |
| campaign   | 0.243834 |
| marital    | 0.211365 |
| balance    | 0.118910 |
| previous   | 0.038243 |
| pdays      | 0.024848 |
| age        | 0.007672 |
| default    | 0.000000 |

### Interpretation

The strongest variables in the model were mostly campaign-related rather than demographic. In particular:

- `month`
- `job`
- `poutcome`
- `duration`
- `contact`

had the largest overall influence on prediction.

This suggests that deposit subscription is shaped more strongly by campaign timing, interaction context, and prior campaign outcome than by variables such as age or balance alone.

### Maximum absolute coefficient by variable

| Variable   | Max Absolute Coefficient | Mean Coefficient |
|------------|--------------------------|------------------|
| age        | 0.007672 | -0.007672 |
| balance    | 0.118910 | 0.118910 |
| campaign   | 0.243834 | -0.243834 |
| contact    | 1.489416 | -0.770433 |
| default    | 0.000000 | 0.000000 |
| duration   | 1.887458 | 1.887458 |
| education  | 0.548958 | 0.366246 |
| housing    | 0.677671 | -0.677671 |
| job        | 0.737351 | -0.164326 |
| loan       | 0.548744 | -0.548744 |
| marital    | 0.120687 | -0.015004 |
| month      | 1.794813 | -0.018604 |
| pdays      | 0.024848 | -0.024848 |
| poutcome   | 2.237093 | 0.730824 |
| previous   | 0.038243 | 0.038243 |

### Coefficient insights

- `poutcome` had the strongest single effect among all variables.
- `duration` had a large positive coefficient, indicating that longer calls were associated with higher odds of subscription.
- `campaign` had a negative coefficient, suggesting that more frequent contact during the campaign was associated with lower odds of subscription.
- `housing` and `loan` were negatively associated with deposit subscription.
- `balance` had a small positive effect.
- `age`, `pdays`, and `previous` had relatively weak effects.
- `default` contributed no meaningful predictive value in the fitted model.

## Current Conclusion

The model results show that logistic regression provides a strong and interpretable baseline for predicting deposit subscription in a post-contact setting. Campaign-related variables, especially `month`, `poutcome`, `duration`, and `contact`, appear to be the most influential drivers of subscription behavior.

Overall, the findings suggest that customer response is shaped more by campaign context and previous campaign outcomes than by basic demographic variables alone.

## Repository Structure

```bash
bank-deposit-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── bank.csv
│   └──test_data.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_train.ipynb
│   └── 03_evaluation.ipynb
│
├── model/
│   └── log_model.pkl
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

## 👤 Author

**Sharifatu Moro**
Aspiring Data Scientist & Machine Learning Engineer 
Background: Economics & Applied Data Analysis

🔗 *Actively building projects in Machine Learning*

---

## Acknowledgement

This project is inspired by real-world bank marketing campaigns and is built for learning and portfolio development.

---

## 📎 Note

This repository is actively being updated as the project progresses. Stay tuned for model development and results 🚀





# Bank Deposit Subscription Prediction

## Overview

This project builds and evaluates machine learning models to predict whether a bank customer will subscribe to a term deposit. The work is framed as a post-contact analysis, so campaign interaction variables such as contact duration, contact type, campaign frequency, and previous campaign outcome are treated as valid predictors.

The project is designed as an industry-style portfolio project that demonstrates a full tabular machine learning workflow, from exploratory analysis and preprocessing to model training, evaluation, comparison, and interpretation.

## Business Problem

Banks run marketing campaigns to promote term deposit products, but not every contacted customer is equally likely to subscribe. A prediction system can help analysts and campaign teams understand which factors are associated with subscription and which models perform best for this classification task.

## Project Objective

The objective of this project is to build and compare multiple classification models that predict deposit subscription using customer information, financial variables, and campaign-related features.

## Project Framing

This project is treated as a **post-contact** prediction problem. That means variables such as:

- `duration`
- `contact`
- `campaign`
- `pdays`
- `previous`
- `poutcome`

are considered valid because they are available in the analysis setting being modeled.

## Dataset

The dataset used is a bank marketing dataset stored as `bank.csv` and later processed into `cleaned_bank.csv`.

### Dataset summary

- Rows: 11,162
- Columns: 17
- Target: `deposit`
- Target classes:
  - `yes`
  - `no`

### Target variable

- `deposit = yes` means the customer subscribed to a term deposit
- `deposit = no` means the customer did not subscribe

### Feature groups

**Customer profile**
- `age`
- `job`
- `marital`
- `education`

**Financial information**
- `default`
- `balance`
- `housing`
- `loan`

**Campaign and contact information**
- `contact`
- `day`
- `month`
- `duration`
- `campaign`
- `pdays`
- `previous`
- `poutcome`

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Scikit-learn

## Exploratory Data Analysis

Exploratory analysis was used to understand the structure of the data and the relationship between features and the target.

### Visualizations created

- segmented bar chart for `default` vs `deposit`
- mosaic plot for `month` vs `deposit`
- KDE plot for `balance` vs `deposit`
- line plot of deposit rate by `day`
- duration distribution analysis against `deposit`
- mean campaign bar chart by `deposit`
- grouped `pdays` vs `deposit` chart
- grouped `previous` vs `deposit` chart

### Key EDA findings

- Education level appears to matter, with tertiary education showing a higher subscription rate than primary education.
- Higher account balances are slightly associated with subscription, although the two classes overlap a lot.
- Subscription rate varies across days of the month.
- Customers who subscribed were contacted fewer times on average than those who did not.
- Previous campaign history appears important, especially `poutcome`, `pdays`, and `previous`.
- Campaign timing, especially `month`, appears strongly related to deposit subscription.

## Preprocessing

The preprocessing workflow was built to support reusable and clean modeling.

### Steps performed

- loaded the dataset from CSV
- removed duplicate rows
- encoded the target variable manually:
  - `no = 0`
  - `yes = 1`
- split the data into features (`X`) and target (`y`)
- identified categorical and numerical columns
- applied one-hot encoding to categorical variables
- applied standard scaling to numerical features for linear and distance-based models
- used a train-test split with stratification

### Target encoding

The target was encoded manually because logistic regression and other binary classifiers work naturally with a numeric binary outcome.

### Encoding note

Categorical variables were encoded using `OneHotEncoder(handle_unknown="ignore")`.

This parameter does **not** remove literal categories called `"unknown"`. It simply prevents errors when unseen categories appear at prediction time.

## Modeling Approach

Several classification models were trained and compared:

- Logistic Regression
- Support Vector Machine
- K-Nearest Neighbors
- Decision Tree
- Random Forest

This allows comparison between:

- linear models
- margin-based models
- instance-based models
- tree-based models
- ensemble models

## Baseline Model Results

The following baseline results were obtained on the test set.

| Model | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|------|---------:|----------:|-------:|---------:|--------:|
| Logistic Regression | 0.8253 | 0.8275 | 0.7977 | 0.8123 | 0.9072 |
| SVM | 0.8470 | 0.8200 | 0.8700 | 0.8430 | 0.9110 |
| KNN | 0.8227 | 0.8195 | 0.8025 | 0.8109 | 0.8923 |
| Decision Tree | 0.8050 | 0.7860 | 0.8080 | 0.7970 | 0.8770 |
| Random Forest | 0.8580 | 0.8260 | 0.8880 | 0.8560 | 0.9150 |

## Baseline Result Interpretation

Among the baseline models, **Random Forest** performed best overall, achieving the highest accuracy, recall, F1 score, and ROC AUC. **SVM** ranked second and also showed strong classification ability. **Logistic Regression** performed slightly below Random Forest and SVM, but remained valuable because it offers strong interpretability. **KNN** produced balanced but weaker performance, while the **Decision Tree** was the weakest of the five baseline models.

## Logistic Regression Evaluation

The initial logistic regression model achieved:

- Accuracy: **0.8253**
- Precision: **0.8275**
- Recall: **0.7977**
- F1 Score: **0.8123**
- ROC AUC: **0.9072**

### Confusion matrix interpretation

- True negatives: 999
- True positives: 844
- False positives: 176
- False negatives: 214

This shows that the model performs well on both classes, although it misses some actual subscribers.

### ROC interpretation

The ROC curve stayed well above the diagonal reference line, and the AUC of 0.9072 indicates strong class separability.

## Feature Importance and Coefficient Analysis

Because logistic regression is interpretable, variable importance was examined using the model coefficients.

### Variable-level importance from grouped coefficients

| Variable | Sum Absolute Coefficient |
|---------|--------------------------:|
| month | 9.988471 |
| job | 3.865241 |
| poutcome | 2.729840 |
| duration | 1.887458 |
| contact | 1.540865 |
| education | 1.098738 |
| housing | 0.677671 |
| loan | 0.548744 |
| campaign | 0.243834 |
| marital | 0.211365 |
| balance | 0.118910 |
| previous | 0.038243 |
| pdays | 0.024848 |
| age | 0.007672 |
| default | 0.000000 |

### Maximum coefficient view

| Variable | Max Absolute Coefficient | Mean Coefficient |
|---------|--------------------------:|-----------------:|
| age | 0.007672 | -0.007672 |
| balance | 0.118910 | 0.118910 |
| campaign | 0.243834 | -0.243834 |
| contact | 1.489416 | -0.770433 |
| default | 0.000000 | 0.000000 |
| duration | 1.887458 | 1.887458 |
| education | 0.548958 | 0.366246 |
| housing | 0.677671 | -0.677671 |
| job | 0.737351 | -0.164326 |
| loan | 0.548744 | -0.548744 |
| marital | 0.120687 | -0.015004 |
| month | 1.794813 | -0.018604 |
| pdays | 0.024848 | -0.024848 |
| poutcome | 2.237093 | 0.730824 |
| previous | 0.038243 | 0.038243 |

### Coefficient insights

- `poutcome`, `duration`, `month`, and `contact` are the strongest drivers in the model.
- `duration` has a strong positive relationship with subscription in the post-contact setting.
- `campaign`, `housing`, and `loan` are negatively associated with subscription.
- `balance` has a small positive effect.
- `age`, `pdays`, `previous`, and `default` contribute relatively little.

Overall, the coefficient analysis suggests that campaign context and prior campaign outcomes matter more than basic demographic variables.

## Hyperparameter Tuning

Hyperparameter tuning has been started for:

- Logistic Regression
- SVM
- Random Forest

Cross-validation was used with ROC AUC as the scoring metric.

### Current status

One tuned logistic regression run produced near-perfect performance on the cleaned dataset:

- Best parameters:
  - `C = 3`
  - `penalty = l1`
  - `solver = liblinear`
  - `class_weight = None`
- Best cross-validated ROC AUC: **1.0**
- Test Accuracy: **0.9978**
- Test Precision: **0.9991**
- Test Recall: **0.9962**
- Test F1 Score: **0.9976**
- Test ROC AUC: **1.0**

A shuffled-target sanity test was also run and produced:

- Sanity Accuracy: **0.5316**
- Sanity ROC AUC: **0.5325**

This suggests that the pipeline is not trivially leaking target information, but the near-perfect tuned results are still being treated as **under validation** until further model-by-model checks are completed.

## Current Conclusion

At the current stage of the project:

- Random Forest is the strongest baseline model
- SVM is the second strongest baseline model
- Logistic Regression remains the most interpretable model
- Campaign-related features are more influential than basic demographic features
- Hyperparameter tuning is underway, and some tuned results are being validated before they are treated as final

## Repository Structure

```bash
bank-deposit-prediction/
│
├── data/
│   ├── bank.csv
│   └── cleaned_bank.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_logistic_regression.ipynb
│   ├── 04_model_comparison.ipynb
│   ├── 05_feature_importance.ipynb
│   └── 06_hyperparameter_tuning.ipynb
│
├── outputs/
│   ├── figures/
│   └── results/
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── README.md
└── requirements.txt