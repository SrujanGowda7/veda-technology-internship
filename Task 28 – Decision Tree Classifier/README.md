# Task 28 – Decision Tree Classifier

## 📌 Description

This task focuses on building a **Decision Tree Classifier** and understanding how tree depth affects model performance and overfitting.

The **Iris dataset** was used to train and evaluate the classification model.

## 🎯 Objective

* Understand how Decision Tree classification works
* Train a Decision Tree model
* Visualize the decision tree
* Experiment with different `max_depth` values
* Compare training and testing performance
* Identify overfitting
* Analyze feature importance

## 🛠️ Tools & Technologies

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Jupyter Notebook

## 📊 Dataset

**Iris Dataset**

The dataset contains information about three species of Iris flowers:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

Features include:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

## 🔍 Methodology

1. Loaded the Iris dataset.
2. Split the data into training and testing sets.
3. Trained a Decision Tree Classifier.
4. Evaluated training and testing accuracy.
5. Visualized the decision tree.
6. Analyzed feature importance.
7. Tested different `max_depth` values.
8. Compared training and testing performance to identify overfitting.

## 🌳 Decision Tree

A Decision Tree makes predictions by applying a series of feature-based conditions.

For example:

```text
Is Petal Length ≤ threshold?
        |
   ┌────┴────┐
  Yes        No
   |          |
Class A    Next Decision
```

## 📈 Performance Analysis

Different tree depths were tested to understand the effect of model complexity.

As the tree depth increases:

* The model becomes more complex.
* Training accuracy generally increases.
* Very deep trees can learn the training data too closely.
* Testing performance may stop improving or decrease.

This helps demonstrate the concept of **overfitting**.

## ⭐ Feature Importance

Feature importance was calculated using the trained Decision Tree to understand which features contributed most to the classification decisions.

## 🧠 Key Learnings

* Decision Trees use a sequence of if-else conditions for classification.
* `max_depth` controls the complexity of the tree.
* A very shallow tree can underfit the data.
* A very deep tree can overfit the training data.
* Training and testing performance should be compared to evaluate generalization.
* Feature importance helps understand which features influence predictions.

## 🎤 Interview Questions

### 1. How does a Decision Tree make predictions?

It follows a sequence of decision rules from the root node to a leaf node, where the final class prediction is made.

### 2. What is overfitting in Decision Trees?

Overfitting happens when the tree becomes too complex and learns the training data too closely, resulting in poorer performance on unseen data.

### 3. What does `max_depth` control?

`max_depth` controls the maximum number of levels in the Decision Tree.

### 4. Why compare training and testing accuracy?

To check whether the model generalizes well to unseen data and to identify overfitting.

### 5. What is feature importance?

It shows how much each feature contributes to the decisions made by the Decision Tree.

## 📁 Project Structure

```text
Task-28-Decision-Tree-Classifier/
│
├── Decision_Tree_Classifier.ipynb
└── README.md
```

## ✅ Conclusion

This task provided practical experience with **Decision Tree classification, model complexity, tree visualization, feature importance, and overfitting analysis** using the Iris dataset.
