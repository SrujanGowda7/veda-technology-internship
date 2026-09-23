# Task 31 – K-Means Clustering

## 📌 Overview

This task focuses on applying **K-Means Clustering**, an unsupervised machine learning algorithm, to the Iris dataset.

The objective is to group similar observations into clusters based on their numerical features.

## 🎯 Objective

* Understand unsupervised learning
* Apply K-Means clustering
* Preprocess and scale numerical features
* Determine a suitable number of clusters
* Visualize the resulting clusters
* Analyze cluster centers

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

## 📊 Dataset

The **Iris dataset** from Scikit-learn was used.

It contains four numerical features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The dataset contains **150 observations**.

## 🔄 Methodology

1. Loaded the Iris dataset.
2. Converted the data into a Pandas DataFrame.
3. Selected numerical features.
4. Standardized the features using `StandardScaler`.
5. Used the Elbow Method to analyze different values of K.
6. Applied K-Means with **3 clusters**.
7. Added cluster labels to the dataset.
8. Calculated the Silhouette Score.
9. Analyzed cluster centers.
10. Visualized the clusters using Matplotlib.

## 📈 Results

The K-Means algorithm successfully divided the observations into **3 clusters** based on their feature similarity.

The cluster centers were analyzed to understand the characteristics of each group.

The **Silhouette Score** was also calculated to evaluate the quality of the clustering.

## 💡 Key Learning

This task helped me understand:

* Unsupervised learning
* K-Means clustering
* Feature scaling
* Cluster centers
* Elbow Method
* Silhouette Score
* Cluster visualization

## 🎤 Interview Questions

### What is clustering?

Clustering is an unsupervised learning technique used to group similar data points together without predefined labels.

### How does K-Means work?

K-Means selects K cluster centers, assigns data points to their nearest center, recalculates the centers, and repeats the process until the clusters become stable.

### Why do we need to choose K?

K represents the number of clusters we want to create. Methods such as the Elbow Method and Silhouette Score can help select a suitable value of K.

## ✅ Conclusion

K-Means clustering was successfully applied to the Iris dataset. The features were standardized before clustering, and the observations were grouped into three clusters. This task provided practical understanding of unsupervised machine learning and clustering techniques.
