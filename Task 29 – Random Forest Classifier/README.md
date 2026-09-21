# Task 29 – Random Forest Classifier

## Level 2 – Day 29 | Data Science Track

## 📌 Overview

This task focuses on building a **Random Forest Classification model** and comparing its performance with a **Decision Tree Classifier**.

The main goal is to understand **ensemble learning** and how combining multiple decision trees can improve model generalization.

## 🎯 Objectives

* Build a Decision Tree classification model.
* Build a Random Forest classification model.
* Compare training and testing performance.
* Experiment with different numbers of trees using `n_estimators`.
* Analyze feature importance.
* Understand ensemble learning.

## 🛠️ Tools & Technologies

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Jupyter Notebook

## 📊 Dataset

**Breast Cancer Wisconsin Dataset**

The dataset is available directly through `scikit-learn`.

It contains medical measurements that are used to classify tumors into two categories.

## 🔍 Methodology

### 1. Data Loading

Loaded the Breast Cancer Wisconsin dataset using `sklearn.datasets`.

### 2. Data Splitting

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

### 3. Decision Tree

A Decision Tree Classifier was trained as the baseline model.

### 4. Random Forest

A Random Forest Classifier was trained using multiple decision trees.

The model was tested with different values of `n_estimators` such as:

* 10
* 50
* 100
* 200

### 5. Performance Comparison

Training and testing accuracy were compared between the Decision Tree and Random Forest models.

### 6. Feature Importance

The `feature_importances_` attribute was used to identify the features that contributed most to the predictions.

## 📈 Evaluation

The models were evaluated using:

* Training Accuracy
* Testing Accuracy
* Classification Report
* Confusion Matrix

## 🌲 Decision Tree vs Random Forest

| Decision Tree                | Random Forest               |
| ---------------------------- | --------------------------- |
| Uses a single tree           | Uses multiple trees         |
| Can easily overfit           | Usually reduces overfitting |
| Simple and easy to interpret | More robust                 |
| Faster to train              | Requires more computation   |
| Less stable                  | More stable predictions     |

## 💡 Key Learnings

* Random Forest is an **ensemble learning algorithm**.
* It combines predictions from multiple decision trees.
* Using multiple trees can improve generalization.
* `n_estimators` controls the number of trees in the forest.
* Feature importance helps identify important input features.
* Comparing training and testing accuracy helps identify overfitting.

## 🧠 Interview Questions

### What is Random Forest?

Random Forest is an ensemble learning algorithm that combines multiple decision trees to make predictions.

### Why does Random Forest usually generalize better than a single Decision Tree?

A single Decision Tree can overfit the training data. Random Forest combines multiple trees, which helps reduce overfitting and produces more stable predictions.

### What is Ensemble Learning?

Ensemble learning is a technique where multiple machine-learning models are combined to improve the overall prediction.

### What is `n_estimators`?

`n_estimators` specifies the number of decision trees used in the Random Forest.

### What is `feature_importances_`?

It shows the relative importance of each feature in making predictions.

## ✅ Conclusion

In this task, a **Decision Tree** and **Random Forest** classifier were built using the Breast Cancer Wisconsin dataset.

Their training and testing performance was compared, different numbers of trees were experimented with, and feature importance was analyzed.

This task provided practical understanding of **ensemble learning, model comparison, overfitting, and feature importance**.
