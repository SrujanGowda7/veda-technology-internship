# Student Performance & Learning Analytics

## 📌 Project Overview

Student Performance & Learning Analytics is a data science project that analyzes academic and learning-related factors to identify student performance patterns.

The project examines attendance, study hours, subject scores, previous performance, and final scores. It also uses exploratory data analysis, visualization, correlation analysis, feature engineering, and a basic machine learning model to predict final student scores.

> **Note:** The dataset used in this project is synthetic and was created for educational purposes. The relationships identified in the analysis should not be interpreted as causal evidence about real-world students.

---

## 🎯 Objectives

* Analyze student academic performance
* Study attendance and study-hour patterns
* Compare subject-wise performance
* Identify relationships between learning factors and final scores
* Perform data cleaning and preprocessing
* Create useful features from existing data
* Build a basic predictive model
* Evaluate model performance using standard metrics
* Document the complete data science workflow

---

## 🛠️ Technologies & Tools

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook / Google Colab
* Excel
* Git & GitHub

---

## 📊 Dataset

The project uses a synthetic dataset containing **500 student records**.

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
| Final_Score    | Final examination score   |

Additional engineered features include:

* `Average_Subject_Score`
* `Attendance_Category`
* `Study_Level`
* `Performance_Category`

---

## 🔄 Project Workflow

```text
Dataset Creation
       ↓
Data Understanding
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Attendance Analysis
       ↓
Subject-wise Analysis
       ↓
Study Hours Analysis
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
Error Analysis
       ↓
Feature Coefficient Analysis
```

---

## 🧹 Data Cleaning

The dataset was checked for:

* Missing values
* Duplicate records
* Invalid attendance values
* Invalid final scores
* Basic statistical consistency

Duplicate records were removed where applicable.

---

## 📈 Exploratory Data Analysis

The analysis includes:

### Subject-wise Performance

Average scores were calculated for:

* Mathematics
* Science
* English

### Attendance Analysis

Attendance distribution was visualized and its relationship with final score was examined.

### Study Hours Analysis

The relationship between study hours and final score was visualized.

### Performance Categories

Students were categorized as:

* Excellent
* Good
* Average
* Needs Improvement

based on their final scores.

---

## 🔗 Correlation Analysis

A correlation matrix and heatmap were created to examine relationships between numerical variables.

The analysis helps identify how variables such as:

* Study Hours
* Attendance
* Subject Scores
* Previous Score

are associated with Final Score.

Correlation represents association and does not establish causation.

---

## 🤖 Machine Learning

### Model Used

**Linear Regression**

The model uses the following features:

```text
Study_Hours
Attendance
Math_Score
Science_Score
English_Score
Previous_Score
```

### Train-Test Split

The dataset was divided into:

* **80% training data — 400 students**
* **20% testing data — 100 students**

A `random_state` of 42 was used for reproducibility.

---

## 📊 Model Results

| Metric   | Result |
| -------- | -----: |
| MAE      |  3.623 |
| MSE      | 20.133 |
| RMSE     |  4.487 |
| R² Score |  0.760 |

The R² value of **0.760** indicates that the model explains approximately 76% of the variation in Final Score within this synthetic dataset.

The MAE indicates an average absolute prediction error of approximately **3.62 score points** on the test set.

---

## 🔍 Feature Coefficients

The Linear Regression coefficients were:

| Feature        | Coefficient |
| -------------- | ----------: |
| Study_Hours    |       0.434 |
| Math_Score     |       0.304 |
| Science_Score  |       0.261 |
| English_Score  |       0.183 |
| Previous_Score |       0.114 |
| Attendance     |       0.085 |

All features had positive coefficients in this particular model.

These coefficients describe the fitted linear model and should not be interpreted as proof that one factor causes higher academic performance.

---

## 📌 Key Findings

* Student performance was analyzed using academic and learning-related variables.
* Subject-wise averages were calculated to identify performance patterns.
* Attendance and study hours were examined in relation to final scores.
* Correlation analysis was used to understand relationships between numerical variables.
* Feature engineering created additional performance and attendance categories.
* Linear Regression was used to predict Final Score.
* The model achieved an R² score of **0.760** on the test data.
* Prediction errors were analyzed using MAE, MSE and RMSE.

---

## ⚠️ Limitations

* The dataset is synthetic rather than collected from real students.
* The generated relationships may not represent real-world educational behavior.
* The project uses a basic Linear Regression model.
* The model does not include other potentially relevant factors such as socioeconomic background, teaching quality, sleep, learning environment, or extracurricular activities.
* Correlation and regression coefficients do not establish causation.

---

## 📁 Project Structure

```text
Student-Performance-Learning-Analytics/
│
├── Student_Performance_Learning_Analytics.ipynb
│
├── cleaned_student_performance.csv
│
├── README.md
│
└── report/
    └── Student_Performance_Analytics_Report.pdf
```

---

## 🚀 Future Improvements

* Test additional regression models
* Perform cross-validation
* Apply hyperparameter tuning
* Add more real-world student features
* Compare multiple machine learning algorithms
* Build an interactive dashboard using Power BI or Tableau
* Use a real-world public student dataset
* Deploy the model as a simple web application

---

## 👨‍💻 Author

**Srujan Gowda**

BE – Information Science & Engineering

Interested in Data Science, Data Analytics and AI/ML.
