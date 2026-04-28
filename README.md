# Credit Risk Prediction & Interactive Dash Dashboard

An end-to-end Python data analytics project that cleans and encodes a credit risk dataset, trains a Decision Tree classifier, evaluates model performance, and delivers findings through an interactive web dashboard built with Dash by Plotly. The dashboard was shared live during class using ngrok to create a secure public tunnel from a local server - demonstrating deployment awareness without requiring cloud infrastructure.

<p align="center">
  <a href="Presentation PDF.pdf">View Project Presentation</a> · <a href="Jupyter Notebook.ipynb">View Jupyter Notebook</a>
</p>

<p align="center">
  <img src="images/project overview .png" width="680" alt="Project overview slide showing pipeline and objectives"/>
</p>

<p align="center"><em>Project overview - end-to-end pipeline from raw Excel data through Decision Tree modeling to interactive Dash dashboard.</em></p>

---

## Overview

Credit risk assessment is one of the most consequential analytical problems in financial services. Misclassifying a high-risk customer as low-risk exposes a lender to default losses. Misclassifying a low-risk customer as high-risk means losing a creditworthy borrower. Both errors have real financial and human costs.

This project builds a classification pipeline to predict customer credit risk from demographic and financial features, then makes those predictions interpretable through an interactive dashboard. The dashboard is designed for non-technical stakeholders - loan officers, risk managers, and business analysts - who need to understand which customer profiles are associated with higher risk without reading a model summary table.

The honest finding from this project is that a Decision Tree model achieved 46% accuracy on this dataset. Rather than hiding that result, this README treats it the same way a rigorous analyst would - as a finding that reveals something important about the data and points toward what a more robust model would need. The feature importance chart, confusion matrix, and demographic breakdowns in the dashboard exist precisely to understand where the model succeeds and where it fails.

---

## The Dataset

| | |
|---|---|
| File | Credit Risk Data.xlsx |
| Features | Age, gender, marital status, home ownership, income, savings, credit history, employment status, loan purpose |
| Target Variable | Credit Risk (High / Low) |
| Tool | Python, Jupyter Notebook, Dash by Plotly |

---

## Pipeline Walkthrough

### Stage 1 - Data Cleaning and Encoding

The raw Excel dataset was loaded into a Jupyter Notebook using pandas. Cleaning steps included identifying and handling missing values, standardizing categorical variable formats, and encoding string categories into numeric representations compatible with scikit-learn.

Label encoding was applied to binary categorical variables - gender, marital status, home ownership. The target variable credit risk was encoded as 0 (Low) and 1 (High) to enable binary classification. Feature selection focused on variables with genuine predictive relevance, removing identifier columns before model training to prevent data leakage.

---

### Stage 2 - Decision Tree Model Building

<p align="center">
  <img src="images/model building decision tree .png" width="620" alt="Decision Tree model building code in Jupyter Notebook"/>
</p>

<p align="center"><em>Model building in Jupyter Notebook - Decision Tree classifier trained on encoded credit risk features with an 80/20 train-test split.</em></p>

A Decision Tree classifier was trained using scikit-learn with an 80/20 train-test split. Decision Tree was selected as the initial model because its structure is directly interpretable - the feature importance scores it produces show exactly which variables the model weighted most heavily, which is essential for communicating risk drivers to non-technical stakeholders.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

<p align="center">
  <img src="images/decision tree model .png" width="620" alt="Trained Decision Tree model structure visualization"/>
</p>

<p align="center"><em>The trained Decision Tree structure - each node shows the split condition, Gini impurity, and sample count that guided the model's classification decisions.</em></p>

---

### Stage 3 - Model Evaluation

<p align="center">
  <img src="images/model evaluation .png" width="620" alt="Model evaluation metrics including accuracy score"/>
</p>

<p align="center"><em>Model evaluation output - 46% accuracy on the held-out test set, with full classification report showing precision, recall, and F1-score per class.</em></p>

**Model accuracy: 46%**

This result is below the 50% random baseline for a balanced binary classification problem, which is the most important analytical finding in the project. When a Decision Tree performs at or below random baseline, it indicates that the available features do not contain sufficient signal to predict the target reliably, or that the model's hyperparameters need tuning. The confusion matrix and feature importance analysis were built specifically to diagnose which factors are driving the poor performance.

<p align="center">
  <img src="images/confusion matrix .png" width="560" alt="Confusion matrix heatmap showing true vs predicted classifications"/>
</p>

<p align="center"><em>Confusion matrix heatmap - breaking down correct and incorrect classifications by type. False negatives - high-risk customers classified as low-risk - are the highest-cost error in a lending context and are tracked separately from overall accuracy.</em></p>

---

### Stage 4 - Interactive Dash Dashboard

The dashboard was built using Dash by Plotly and assembled from six interactive visualizations covering model performance and customer demographic breakdowns.

<p align="center">
  <img src="images/dash by ploty dashboard .png" width="640" alt="Full Dash by Plotly dashboard view"/>
</p>

<p align="center"><em>The complete Dash dashboard - feature importance, confusion matrix, and demographic breakdown charts assembled into a single interactive web application.</em></p>

<p align="center">
  <img src="images/dashboard charts .png" width="620" alt="Dashboard charts showing feature importance and demographic breakdowns"/>
</p>

<p align="center"><em>Feature importance bar chart (top) ranking all input variables by predictive contribution. Income and savings emerge as the strongest available predictors of credit risk.</em></p>

<p align="center">
  <img src="images/age and contribution dashboard charts .png" width="620" alt="Age distribution and contribution charts by demographic group"/>
</p>

<p align="center"><em>Age distribution and contribution charts segmented by demographic group - surfaces which customer profiles cluster in high-risk segments.</em></p>

The dashboard was shared live using ngrok, which creates a secure tunnel from a local Dash server to a public URL. This allowed the dashboard to be demonstrated to professors and classmates directly in a browser without requiring cloud deployment or any recipient installation.

<p align="center">
  <img src="images/dashboard link via ngrok .jpg" width="580" alt="ngrok secure tunnel generating a public URL for the local Dash app"/>
</p>

<p align="center"><em>ngrok generating a secure public URL from the local Dash server - a lightweight deployment approach that made the dashboard accessible to any browser without cloud infrastructure.</em></p>

```bash
# Run the dashboard locally
python credit_dashboard.py
# Open http://localhost:8050 in your browser
```

---

### Stage 5 - Notebook Visualizations

<p align="center">
  <img src="images/notebook charts gender .png" width="620" alt="Notebook charts showing credit risk distribution by gender"/>
</p>

<p align="center"><em>Credit risk distribution by gender from the Jupyter Notebook EDA - checking whether the model's predictions are proportionally distributed across demographic groups, a compliance requirement in regulated lending under fair lending laws.</em></p>

---

## Key Findings

**The 46% accuracy is a diagnostic finding.** A Decision Tree at below-random baseline on binary classification signals that the available demographic and basic financial features do not contain sufficient predictive signal on their own. This is consistent with what the credit scoring literature shows: static demographic features are weak predictors compared to dynamic behavioral data like payment history and credit utilization.

**Income and savings are the strongest available predictors.** The feature importance chart confirms that liquidity variables outperform demographic ones in predicting credit risk, even in a model that is overall underperforming. A more feature-rich dataset incorporating payment history and credit utilization would give the model the signal it currently lacks.

**False negatives carry the highest cost in this context.** The confusion matrix shows the rate at which high-risk customers were classified as low-risk. In a real lending context, each false negative represents an approved loan likely to default - a more costly error than a false positive.

**Demographic breakdowns surface potential bias.** The gender and age distribution charts allow stakeholders to check whether predictions are proportionally distributed across demographic groups - a compliance requirement under fair lending regulations.

---

## What a Production Model Would Need

A richer feature set is the most important change. Payment history, credit utilization ratio, number of open accounts, and length of credit history are the variables that drive performance in deployed credit scoring models like FICO. Adding even one or two behavioral features would likely push accuracy substantially above the random baseline.

Ensemble methods would outperform a single Decision Tree. Random Forest or Gradient Boosting would reduce the variance that causes a single tree to overfit on small datasets. The feature importance analysis done here would carry over directly to inform feature selection for an ensemble model.

Cross-validation rather than a single train-test split would give a more reliable accuracy estimate. K-fold cross-validation averages performance across multiple splits and produces a more stable estimate on smaller datasets.

---

## Repository Structure

```
Credit-Risk-Prediction-Dash-Dashboard/
│
├── images/
│   ├── project overview .png
│   ├── model building decision tree .png
│   ├── decision tree model .png
│   ├── model evaluation .png
│   ├── confusion matrix .png
│   ├── dash by ploty dashboard .png
│   ├── dashboard charts .png
│   ├── age and contribution dashboard charts .png
│   ├── dashboard link via ngrok .jpg
│   └── notebook charts gender .png
│
├── Jupyter Notebook.ipynb            # Full pipeline - cleaning, encoding, modeling, evaluation
├── credit_dashboard.py               # Dash web application - all interactive visualizations
├── Credit Risk Data.xlsx             # Raw credit risk dataset
├── Presentation PDF.pdf              # Project presentation with outcomes and recommendations
└── README.md
```

---

## Getting Started

```bash
# Install dependencies
pip install pandas scikit-learn plotly dash openpyxl

# Run the Dash dashboard
python credit_dashboard.py

# Open your browser and go to:
# http://localhost:8050
```

To explore the full modeling pipeline, open `Jupyter Notebook.ipynb` in Jupyter and run all cells sequentially.

---

## Looker Studio vs Python Dash - Same Data, Two Tools

This project and the [companion Looker Studio project](https://github.com/TejashwiniSaravanan/Credit-Risk-Looker-Studio-Dashboard) use the exact same 425-record credit risk dataset but approach it with completely different tools for completely different audiences.

| | Python Dash | Looker Studio |
|---|---|---|
| **Code required** | Full Python pipeline | None |
| **Primary audience** | Data teams, technical reviewers | Business stakeholders, executives |
| **Build time** | Slower - coded from scratch | Fast - drag and drop |
| **Customization** | Unlimited with Plotly | Limited to built-in chart types |
| **Data connection** | Static Excel file loaded in pandas | Live via Google Sheets |
| **Deployment** | Required ngrok tunnel | Instant public URL |
| **ML integration** | Decision Tree classifier built in | None |
| **Best for** | Building and evaluating predictive models | Exploring and communicating patterns |

**What the comparison reveals:** The Dash project adds a layer that Looker Studio cannot provide - a trained model, feature importance ranking, and confusion matrix that quantify which variables actually predict risk and where the model fails. Looker Studio surfaces the demographic and behavioral patterns faster with no code - the Sankey diagram and funnel chart immediately showed marital status and age-gender risk patterns without writing a single line.

In a real business setting, both tools would be used together: Looker Studio for the executive dashboard that refreshes automatically, Python Dash for the data science team that needs to understand model behavior and iterate on predictions. Building both on the same dataset demonstrates exactly that end-to-end capability.

---

## Limitations and What I Would Do Next

The dataset size limits the model's ability to generalize. A larger dataset with more records would give the Decision Tree more examples to learn from and reduce prediction variance.

Hyperparameter tuning - adjusting max depth, minimum samples per leaf, and split criteria - was not performed in this iteration. A grid search over these parameters would likely improve accuracy by preventing the tree from overfitting to noise in the training data.

Deploying the dashboard to a cloud platform like Heroku or Render would make it permanently accessible without requiring ngrok, converting this from a class demonstration into a live portfolio piece.

---

## Tools and Technologies

Python · Pandas · Scikit-Learn · Plotly · Dash · Jupyter Notebook · ngrok · Microsoft Excel

---

## Related Projects

- **[Healthcare Analytics - PySpark ML & GCP Strategy](https://github.com/TejashwiniSaravanan/Healthcare-Analytics-PySpark-ML-GCP-Strategy)** - End-to-end ML pipeline with GCP cloud deployment strategy
- **[Clinical Trial Patient Selection](https://github.com/TejashwiniSaravanan/Clinical-Trial-Patient-Selection-Optimization)** - Classification modeling for patient screening using Orange Data Mining
- **[Global Affordability Dashboard](https://github.com/TejashwiniSaravanan/global-affordability-dashboard-tableau-ml)** - Random Forest regression with interactive Tableau dashboards

---

## About Me

**Tejashwini Saravanan** - Master's student in Data Analytics at Seattle Pacific University, focused on healthcare data engineering, predictive analytics, and interactive data applications.

[LinkedIn](https://www.linkedin.com/in/tejashwinisaravanan/) · [GitHub](https://github.com/TejashwiniSaravanan)

---

*Dataset: Credit Risk Data · Tools: Python, Dash by Plotly, Scikit-Learn · Seattle Pacific University*
