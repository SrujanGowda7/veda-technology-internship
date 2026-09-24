# Student Performance & Learning Analytics

A beginner-friendly Data Science project that analyzes student academic and learning data to identify performance patterns, subject-wise strengths and weaknesses, attendance trends, and relationships between learning factors and academic performance.

## 📌 Project Overview

This project follows a basic end-to-end Data Science workflow, starting from dataset creation and data cleaning to exploratory data analysis, visualization, correlation analysis, and feature engineering.

The project uses a **synthetic dataset containing 500 student records** created for educational and analytical purposes.

## 🎯 Objectives

* Analyze student academic performance
* Study attendance and study-hour patterns
* Compare subject-wise performance
* Explore relationships between learning factors and final scores
* Create meaningful visualizations
* Perform correlation analysis
* Engineer useful features for predictive modeling
* Build a basic prediction model in the next stage

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook / Google Colab
* Excel
* Git & GitHub

## 📊 Dataset

The dataset contains 500 synthetic student records with features including:

* Student ID
* Gender
* Age
* Study Hours
* Attendance
* Mathematics Score
* Science Score
* English Score
* Previous Score
* Final Score

Additional features were created during analysis, including:

* Average Subject Score
* Attendance Category
* Study Level
* Performance Category

## 🔍 Data Science Workflow

### 1. Dataset Creation

A synthetic student performance dataset was generated with academic and learning-related attributes.

### 2. Data Cleaning

* Checked for missing values
* Checked for duplicate records
* Validated attendance and score ranges
* Removed duplicate records where applicable

### 3. Exploratory Data Analysis

Analyzed:

* Dataset structure
* Statistical summary
* Average student performance
* Attendance patterns
* Study-hour patterns
* Subject-wise performance

### 4. Visualization

The project includes visualizations such as:

* Final Score Distribution
* Attendance Distribution
* Attendance vs Final Score
* Study Hours vs Final Score
* Average Subject Performance
* Performance Category Distribution
* Correlation Heatmap

### 5. Correlation Analysis

Correlation analysis was performed to examine linear relationships between numerical variables, particularly:

* Attendance and Final Score
* Study Hours and Final Score
* Previous Score and Final Score
* Subject scores and Final Score

Correlation indicates association between variables and does not by itself establish causation.

### 6. Feature Engineering

Additional features were created to make the dataset more useful for further analysis and predictive modeling.

Examples:

```python
df["Average_Subject_Score"] = df[
    ["Math_Score", "Science_Score", "English_Score"]
].mean(axis=1)
```

Performance categories were also created based on final scores.

## 📈 Key Analysis Areas

The project focuses on understanding:

* How student attendance varies across the dataset
* How study hours relate to final performance
* Differences in average performance across subjects
* Distribution of student performance categories
* Relationships among academic and learning-related variables

## 🤖 Predictive Modeling

Predictive modeling will be implemented in the next stage of the project.

The planned workflow includes:

1. Feature selection
2. Train-test split
3. Model training
4. Prediction
5. Model evaluation
6. Interpretation of results

Possible models include Linear Regression or a classification model depending on the selected target variable.

## 📁 Project Structure

```text
Student-Performance-Learning-Analytics/
│
├── data/
│   ├── student_performance.csv
│   └── cleaned_student_performance.csv
│
├── notebooks/
│   └── Student_Performance_Learning_Analytics.ipynb
│
├── visualizations/
│   ├── final_score_distribution.png
│   ├── attendance_distribution.png
│   ├── attendance_vs_score.png
│   ├── study_hours_vs_score.png
│   ├── subject_performance.png
│   └── correlation_heatmap.png
│
├── report/
│   └── final_report.pdf
│
└── README.md
```

## 🚀 Current Progress

### Day 1 — Completed ✅

* Dataset creation
* Data understanding
* Data cleaning
* Exploratory Data Analysis
* Attendance analysis
* Study-hours analysis
* Subject-wise performance analysis
* Correlation analysis
* Data visualization
* Feature engineering
* Cleaned dataset generation

### Day 2 — Planned 🔄

* Feature selection
* Train-test split
* Predictive model
* Model training
* Predictions

### Day 3 — Planned 🔄

* Model evaluation
* Final analysis
* Project report
* GitHub documentation
* Project presentation

## 📌 Note

This project is created for educational purposes. The dataset used in the project is synthetic and does not represent real individual students or real academic records.
