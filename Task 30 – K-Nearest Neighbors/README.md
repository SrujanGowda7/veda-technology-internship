# Task 30 – K-Nearest Neighbors (KNN)

## 📌 Overview

This task focuses on implementing the **K-Nearest Neighbors (KNN)** classification algorithm using the **Iris dataset**.

The main objective is to understand how KNN uses distance between data points for classification, why feature scaling is important, and how different values of **K** affect model performance.

---

## 🎯 Objectives

* Understand the K-Nearest Neighbors algorithm.
* Implement KNN classification using Python.
* Apply feature scaling before using KNN.
* Test multiple values of K.
* Compare training and testing performance.
* Select a suitable K value based on testing performance.
* Evaluate the final model using accuracy, classification report, and confusion matrix.

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

---

## 📊 Dataset

### Iris Dataset

The Iris dataset contains measurements of iris flowers and is commonly used for classification problems.

### Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

The dataset contains **150 observations and 4 input features**.

---

## 🔄 Workflow

```text
Load Iris Dataset
       ↓
Explore Dataset
       ↓
Separate Features and Target
       ↓
Train-Test Split
       ↓
Feature Scaling
       ↓
Build KNN Model
       ↓
Test Multiple K Values
       ↓
Compare Training & Testing Accuracy
       ↓
Select Best K
       ↓
Evaluate Final Model
```

---

## ⚙️ Feature Scaling

KNN is a **distance-based algorithm**, so feature scaling is important.

`StandardScaler` was used to standardize the features.

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

The scaler is fitted only on the training data and then applied to the testing data.

---

## 🤖 KNN Model

The KNN classifier was implemented using Scikit-learn:

```python
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train_scaled, y_train)
```

The model predicts the class of a new observation based on the majority class among its nearest neighbors.

---

## 🔍 Testing Different K Values

Multiple K values from **1 to 20** were tested.

```python
k_values = range(1, 21)
```

For each K value, both training and testing accuracy were calculated.

This helps understand how the choice of K affects model performance.

---

## 📈 Performance Comparison

Training and testing accuracy were compared for different K values.

The comparison was visualized using a line graph:

```python
plt.plot(k_values, train_accuracy, marker="o",
         label="Training Accuracy")

plt.plot(k_values, test_accuracy, marker="o",
         label="Testing Accuracy")
```

The K value with the highest testing accuracy was selected as the best K for this experiment.

---

## 🏆 Best K Selection

The best K was selected using the testing accuracy:

```python
best_index = np.argmax(test_accuracy)

best_k = list(k_values)[best_index]
```

The final KNN model was then trained using the selected K value.

> **Note:** The selected K depends on the particular train-test split used in this experiment.

---

## 📊 Model Evaluation

The final model was evaluated using:

### 1. Accuracy

Measures the proportion of correctly classified observations.

### 2. Classification Report

Provides:

* Precision
* Recall
* F1-score
* Support

### 3. Confusion Matrix

Shows the number of correct and incorrect predictions for each class.

---

## 💡 Key Learnings

* KNN is a supervised learning algorithm.
* KNN can be used for classification and regression.
* KNN uses distance to identify nearby observations.
* Feature scaling is important for distance-based algorithms.
* A very small K can make the model sensitive to noise.
* A very large K can make the model too generalized.
* Testing multiple K values helps identify a suitable value.
* Training and testing performance should both be considered when evaluating the model.

---

## 🎤 Interview Questions

### 1. What is KNN?

KNN stands for **K-Nearest Neighbors**. It is a supervised machine learning algorithm that predicts the class of a new observation based on the classes of its nearest neighbors.

### 2. How does KNN classify observations?

KNN calculates the distance between the new observation and the training observations, selects the K nearest observations, and uses majority voting to determine the predicted class.

### 3. Why is feature scaling important in KNN?

KNN uses distance calculations. If features have different scales, features with larger numerical values can have more influence on the distance. Scaling gives features a comparable influence.

### 4. What happens when K is too small?

A very small K can make the model sensitive to noise and outliers, which may lead to overfitting.

### 5. What happens when K is too large?

A very large K considers too many neighbors and can make the model too generalized, which may lead to underfitting.

### 6. Is KNN supervised or unsupervised?

KNN is a **supervised learning algorithm** because it learns from labelled training data.

### 7. Why is KNN called a lazy learning algorithm?

KNN does not build a complex model during the training phase. It stores the training data and performs distance calculations when making predictions.

---

## 📁 Project Structure

```text
Task-30-KNN/
│
├── Task_30_KNN.ipynb
│
└── README.md
```

---

## ✅ Conclusion

In this task, a **K-Nearest Neighbors classification model** was implemented using the Iris dataset. Feature scaling was applied because KNN is based on distance calculations. Multiple K values were tested and their training and testing performance was compared. A suitable K value was selected based on testing performance, and the final model was evaluated using accuracy, classification report, and confusion matrix.

This task helped strengthen the understanding of **distance-based classification, feature scaling, K selection, and model evaluation**.
