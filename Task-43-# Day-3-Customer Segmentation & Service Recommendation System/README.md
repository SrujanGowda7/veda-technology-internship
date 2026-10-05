# Customer Segmentation & Service Recommendation System

## Veda Technology – Day 3 Data Science Internship Project

### 📌 Project Overview

This project develops a **Customer Segmentation and Service Recommendation System** for Veda Technology.

The system analyzes customer behavior, interests, engagement, spending, service inquiries, and interaction patterns to divide customers into meaningful groups using **K-Means Clustering**.

Based on customer characteristics, the system also recommends suitable **Veda Technology services and learning programs** using a rule-based recommendation approach.

The project uses **synthetic customer data** created for learning and demonstration purposes.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze customer behavior and interaction patterns.
- Perform data preprocessing and feature engineering.
- Segment customers using **K-Means clustering**.
- Identify the optimal number of customer clusters.
- Evaluate clustering using the **Elbow Method and Silhouette Score**.
- Visualize customer clusters using **PCA**.
- Create meaningful customer segment profiles.
- Develop a rule-based service recommendation system.
- Generate business insights from customer segments.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- K-Means Clustering
- PCA
- Google Colab / Jupyter Notebook
- CSV

---

## 📊 Dataset

A synthetic dataset containing **500 customers** was generated using Python.

### Main Features

| Feature | Description |
|---|---|
| Customer_ID | Unique customer identifier |
| Age | Customer age |
| Website_Visits | Number of website visits |
| Service_Inquiries | Number of service-related inquiries |
| Training_Interest | Interest in training programs |
| Internship_Interest | Interest in internship programs |
| Engagement_Score | Overall customer engagement |
| Monthly_Spending | Estimated monthly spending |
| Previous_Purchases | Number of previous purchases |
| Support_Interactions | Customer support interactions |
| Days_Since_Last_Interaction | Days since last interaction |

### Engineered Features

Additional features were created to improve customer analysis:

- **Total_Interest**
- **Total_Interactions**
- **Customer_Value**

---

## 🔄 Project Workflow

```text
Synthetic Customer Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Feature Standardization
        ↓
Elbow Method
        ↓
Silhouette Score
        ↓
K-Means Clustering
        ↓
Customer Segment Profiles
        ↓
PCA Visualization
        ↓
Service Recommendation
        ↓
Business Insights
```

---

## 🧹 Data Preprocessing

The dataset was checked for:

- Missing values
- Duplicate records
- Numerical data consistency

Missing numerical values were handled using the **median**, and duplicate records were removed.

Since K-Means is distance-based, the numerical features were standardized using **StandardScaler** before clustering.

---

## 🔍 Exploratory Data Analysis

Customer behavior was analyzed using:

- Engagement score distribution
- Website visits
- Monthly spending
- Service inquiries
- Training interest
- Internship interest
- Customer interactions

Visualizations were created using **Matplotlib and Seaborn**.

---

## 🤖 Customer Segmentation

### K-Means Clustering

K-Means clustering was used to group customers according to their behavioral characteristics.

The optimal number of clusters was evaluated using:

### 1. Elbow Method

The Elbow Method compares the clustering inertia for different values of K.

### 2. Silhouette Score

Silhouette Score was used to evaluate how well customers fit within their assigned clusters.

The K value with the highest silhouette score was selected for the final clustering model.

---

## 📈 PCA Visualization

**Principal Component Analysis (PCA)** was used to reduce the customer feature space to two dimensions.

This allowed the customer clusters to be visualized in a 2D scatter plot.

```text
Customer Features
       ↓
StandardScaler
       ↓
K-Means
       ↓
PCA
       ↓
2D Cluster Visualization
```

---

## 👥 Customer Segments

The resulting clusters were given meaningful business names based on their characteristics.

Possible segments include:

### Highly Engaged Customers

Customers showing higher engagement and spending.

**Recommended:**  
Premium Digital Solutions and IT Services.

### Training-Focused Customers

Customers showing strong interest in training and learning programs.

**Recommended:**  
Data Analytics, Python and Machine Learning Training.

### Internship-Focused Customers

Customers showing higher interest in internship opportunities.

**Recommended:**  
Industry Internship Programs.

### Occasional Customers

Customers with comparatively lower interaction or engagement.

**Recommended:**  
Beginner Training and Orientation Programs.

> Segment names are assigned after analyzing the actual cluster characteristics rather than assuming them beforehand.

---

## 🎯 Service Recommendation System

A simple **rule-based recommendation system** was developed.

Recommendations are generated using customer characteristics such as:

- Training interest
- Internship interest
- Service inquiries
- Engagement score
- Monthly spending

### Example

```text
High Training Interest
        ↓
Data Analytics & Python Training
```

```text
High Internship Interest
        ↓
Industry Internship Program
```

```text
High Service Inquiries
        ↓
IT & Digital Services
```

```text
High Engagement + High Spending
        ↓
Premium Digital Solutions
```

```text
Low Engagement
        ↓
Beginner Training & Orientation
```

---

## 💡 Business Insights

The segmentation system can help Veda Technology:

- Understand different types of customers.
- Identify highly engaged customers.
- Identify customers interested in training.
- Identify potential internship candidates.
- Personalize service recommendations.
- Improve customer engagement.
- Target premium services toward high-value customers.
- Promote suitable learning programs to interested customers.
- Support data-driven marketing decisions.

---

## 📁 Project Files

```text
Day-3-Customer-Segmentation/
│
├── Customer_Segmentation.ipynb
│
├── Veda_Day3_Customer_Segmentation.csv
│
├── Veda_Day3_Cluster_Profile.csv
│
├── Veda_Day3_Segment_Summary.csv
│
├── screenshots/
│   ├── dataset.png
│   ├── customer_analysis.png
│   ├── elbow_method.png
│   ├── cluster_visualization.png
│   ├── segment_summary.png
│   └── recommendations.png
│
└── README.md
```

---

## 📌 Key Learning Outcomes

Through this project, I gained practical experience in:

- Customer analytics
- Exploratory Data Analysis
- Data preprocessing
- Feature engineering
- Feature standardization
- Unsupervised Machine Learning
- K-Means clustering
- Elbow Method
- Silhouette Score
- PCA
- Customer segmentation
- Rule-based recommendation systems
- Business insight generation

---

## 🚀 Future Improvements

The project can be further improved by:

- Using real-world customer datasets.
- Building an interactive **Streamlit dashboard**.
- Adding more advanced recommendation techniques.
- Using DBSCAN or hierarchical clustering.
- Implementing collaborative filtering.
- Connecting the system to a real customer database.
- Adding real-time customer recommendations.

---

## 👨‍💻 Author

**Srujan Gowda**

Data Science / Data Analytics Enthusiast

### Internship

**Veda Technology – Data Science Internship**

**Project:** Customer Segmentation & Service Recommendation System

**Day:** 3 of 4
