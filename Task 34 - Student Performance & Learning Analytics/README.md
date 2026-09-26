# Student Performance & Learning Analytics

## 📌 Project Overview

The **Student Performance & Learning Analytics** project is a 3-day Data Science project that analyzes student academic and learning-related data to identify performance patterns, subject-wise performance, attendance trends, study habits, and factors associated with Final Score.

The project follows a complete basic Data Science workflow, from dataset creation and data cleaning to exploratory analysis, visualization, feature engineering, predictive modeling, model evaluation, and final insights.

> **Note:** The dataset used in this project is synthetic and was created for educational purposes. Therefore, the observed relationships should not be interpreted as real-world causal findings.

---

## 🎯 Objectives

* Perform data cleaning and preparation.
* Conduct Exploratory Data Analysis (EDA).
* Analyze subject-wise performance.
* Analyze attendance and study-hour patterns.
* Perform correlation analysis.
* Create useful engineered features.
* Build a basic Machine Learning prediction model.
* Evaluate model performance.
* Analyze prediction errors and model coefficients.
* Generate final project insights.
* Document the complete Data Science workflow.

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Google Colab / Jupyter Notebook
* Excel
* Git & GitHub

---

## 📊 Dataset

The project uses a **synthetically generated dataset containing 500 student records**.

### Main Features

| Feature        | Description               |
| -------------- | ------------------------- |
| Student_ID     | Unique student identifier |
| Gender         | Student gender            |
| Age            | Student age               |
| Study_Hours    | Daily study hours         |
| Attendance     | Attendance percentage     |
| Math_Score     | Mathematics score         |
| Science_Score  | Science score             |
| English_Score  | English score             |
| Previous_Score | Previous academic score   |
| Final_Score    | Final performance score   |

### Engineered Features

* Average Subject Score
* Performance Category
* Attendance Category
* Study Level

---

## 🔄 Complete Project Workflow

```text
Dataset Creation
       ↓
Data Inspection
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Data Visualization
       ↓
Correlation Analysis
       ↓
Feature Engineering
       ↓
Train-Test Split
       ↓
Linear Regression
       ↓
Prediction
       ↓
Model Evaluation
       ↓
Error & Coefficient Analysis
       ↓
Final Analysis & Insights
```

---

# 📅 Day 1 — Data Preparation & Exploratory Analysis

Day 1 focused on creating and preparing the student dataset.

### Activities Completed

* Dataset creation
* Data inspection
* Missing-value checking
* Duplicate checking
* Invalid-value checking
* Descriptive statistics
* Subject-wise performance analysis
* Final Score distribution
* Attendance analysis
* Study Hours analysis
* Correlation analysis
* Feature engineering

### Visualizations

* Subject-wise average scores
* Final Score distribution
* Attendance vs Final Score
* Study Hours vs Final Score
* Correlation heatmap

---

# 📅 Day 2 — Predictive Modeling

Day 2 focused on building a basic Machine Learning model.

## Model

**Linear Regression**

### Input Features

* Study Hours
* Attendance
* Math Score
* Science Score
* English Score
* Previous Score

### Target

`Final_Score`

### Train-Test Split

* Training: **400 records**
* Testing: **100 records**
* Test size: **20%**
* Random state: **42**

### Model Training Workflow

```text
Feature Selection
       ↓
Define X and y
       ↓
Train-Test Split
       ↓
Initialize Linear Regression
       ↓
Train Model
       ↓
Generate Predictions
       ↓
Evaluate Model
       ↓
Analyze Errors & Coefficients
```

---

## 📊 Model Results

| Metric   | Result |
| -------- | -----: |
| MAE      |  3.623 |
| MSE      | 20.133 |
| RMSE     |  4.487 |
| R² Score |  0.760 |

The Linear Regression model achieved an **R² score of 0.760** on the test dataset.

---

## 📉 Prediction Error Analysis

Prediction error was calculated as:

```text
Error = Actual Score − Predicted Score
```

Results:

* Average Prediction Error: **0.974**
* Minimum Error: **-11.254**
* Maximum Error: **10.494**

An Actual vs Predicted visualization was created to compare model predictions with actual Final Scores.

---

# 📅 Day 3 — Final Analysis & Insights

Day 3 focused on completing the project and generating final analytical insights.

### Activities Completed

* Performance category analysis
* Subject-wise strength analysis
* Attendance category analysis
* Study-level analysis
* Final correlation summary
* Model performance review
* Prediction error analysis
* Feature coefficient analysis
* Final project insights
* Final dataset export

### Performance Categories

Students were classified into:

* Excellent
* Good
* Average
* Needs Improvement

### Attendance Categories

* Low
* Moderate
* Good
* Excellent

### Study Levels

* Low
* Moderate
* High
* Very High

---

## 🔍 Feature Coefficients

| Feature        | Coefficient |
| -------------- | ----------: |
| Study Hours    |    0.433603 |
| Math Score     |    0.303717 |
| Science Score  |    0.261043 |
| English Score  |    0.182833 |
| Previous Score |    0.114416 |
| Attendance     |    0.084597 |

The coefficients are the values learned by the Linear Regression model.

Because the dataset is synthetic and the variables have different scales, these coefficients should not be interpreted as real-world causal effects or direct measures of practical feature importance.

---

## 💡 Key Insights

* Student academic and learning-related data was analyzed using a complete basic Data Science workflow.
* Subject-wise performance was compared across Mathematics, Science, and English.
* Attendance and study-hour patterns were analyzed against Final Score.
* Correlation analysis was used to examine associations between variables.
* Performance, attendance, and study-level categories were created through feature engineering.
* Linear Regression was used to predict Final Score.
* The model achieved an R² score of **0.760** and an RMSE of **4.487** on the test dataset.
* Prediction errors and model coefficients were analyzed to understand model behavior.

---

## ⚠️ Limitations

* The dataset is synthetic.
* It does not represent a real student population.
* The generated data may contain artificial relationships.
* The model uses a limited number of features.
* Only Linear Regression was implemented.
* The results should not be interpreted as causal relationships.
* Model performance may differ on real-world data.

---

## 🚀 Future Improvements

* Use real-world student datasets.
* Add more academic and behavioral features.
* Compare multiple Machine Learning models.
* Implement classification for performance categories.
* Perform cross-validation.
* Apply hyperparameter tuning.
* Build an interactive Power BI or Tableau dashboard.
* Deploy the model as a simple application.

---

## 📁 Project Structure

```text
Student-Performance-Learning-Analytics/
│
├── student_performance_analysis.ipynb
├── final_student_performance_analysis.csv
├── README.md
├── Day_2_Report.pdf
├── Day_3_Report.pdf
│
└── images/
    ├── subject_average.png
    ├── final_score_distribution.png
    ├── attendance_vs_final_score.png
    ├── study_hours_vs_final_score.png
    ├── correlation_heatmap.png
    ├── actual_vs_predicted.png
    └── feature_coefficients.png
```

---

## 📚 Learning Outcomes

This project provided practical experience in:

* Python programming
* Data cleaning
* Pandas and NumPy
* Exploratory Data Analysis
* Data visualization
* Correlation analysis
* Feature engineering
* Train-test splitting
* Linear Regression
* Model prediction
* Model evaluation
* Error analysis
* GitHub documentation

---

## 👨‍💻 Author

**Srujan Gowda**

BE – Information Science & Engineering
APS College of Engineering, Bengaluru

**Focus Areas:** Data Science | Data Analytics | Machine Learning | AI/ML
