# Customer Segmentation & Service Recommendation System

## 📌 Project Overview

This project was developed as part of the **Veda Technology Data Science Internship**.

The project focuses on analyzing customer behavior and dividing customers into meaningful groups using **K-Means Clustering**. Based on customer interests, engagement, spending, and interactions, the system also provides suitable **service recommendations**.

The final solution includes data preprocessing, feature engineering, clustering, PCA visualization, service recommendation, business insights, and an interactive **Streamlit dashboard**.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze customer behavior and interaction data.
- Identify different customer segments.
- Apply K-Means clustering for customer segmentation.
- Use PCA for visualization of customer clusters.
- Understand the characteristics of each customer group.
- Recommend suitable services to customers.
- Build an interactive dashboard for business users.
- Generate useful business insights from customer data.

---

## 📊 Dataset

A **synthetic customer dataset** containing **500 customer records** was created for this project.

The dataset contains information such as:

- Customer ID
- Age
- Website Visits
- Service Inquiries
- Training Interest
- Internship Interest
- Engagement Score
- Monthly Spending
- Previous Purchases
- Support Interactions
- Days Since Last Interaction

### Feature Engineering

Additional features were created from the original data:

- **Total Interest** = Training Interest + Internship Interest
- **Total Interactions** = Website Visits + Service Inquiries + Support Interactions
- **Customer Value** = Monthly Spending × Previous Purchases

These features helped provide a better representation of customer behavior.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook / Google Colab
- GitHub

---

## 🔄 Project Workflow

The project follows these major steps:

```text
Customer Dataset
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Feature Scaling
       ↓
K-Means Clustering
       ↓
Cluster Evaluation
       ↓
PCA Visualization
       ↓
Customer Segmentation
       ↓
Service Recommendation
       ↓
Business Insights
       ↓
Streamlit Dashboard
```

---

## 🤖 Customer Segmentation

K-Means clustering was used to group customers based on their behavior and characteristics.

Different values of K were evaluated using the **Silhouette Score**.

The best result obtained in the final dataset was:

- **Number of clusters (K): 2**
- **Silhouette Score: 0.1264**

The final customer groups were:

| Customer Segment | Number of Customers |
|---|---:|
| Highly Engaged Customers | 257 |
| Training-Focused Customers | 243 |

### Segment Interpretation

#### 1. Highly Engaged Customers

These customers showed relatively higher overall interactions and engagement with the business.

They can be targeted with:

- Premium digital services
- IT & digital solutions
- Personalized offers
- Additional services

#### 2. Training-Focused Customers

These customers showed strong interest in training-related offerings.

They can be targeted with:

- Data Analytics training
- Python training
- Beginner training programs
- Industry-oriented training

---

## 🎯 Service Recommendation System

A rule-based recommendation system was developed using customer behavior and interests.

The system recommends services such as:

- Data Analytics & Python Training
- Beginner Training & Orientation
- Industry Internship Program
- IT & Digital Services
- Premium Digital Solutions

### Recommendation Results

| Recommended Service | Customers |
|---|---:|
| Data Analytics & Python Training | 172 |
| Beginner Training & Orientation | 138 |
| Industry Internship Program | 117 |
| IT & Digital Services | 43 |
| Premium Digital Solutions | 30 |

The recommendations help demonstrate how customer analytics can be converted into practical business actions.

---

## 📈 PCA Visualization

**Principal Component Analysis (PCA)** was used to reduce the dimensionality of the customer data and visualize customer clusters in a two-dimensional space.

PCA makes it easier to understand how the identified customer groups are distributed.

---

## 📊 Project Visualizations

The project generates several visualizations:

- Elbow Method
- Silhouette Scores
- PCA Customer Clusters
- Customer Segment Distribution
- Service Recommendation Distribution

These visualizations help understand the clustering process and final results.

---

## 🖥️ Streamlit Dashboard

A Streamlit dashboard was developed as the final application of the project.

The dashboard provides:

### KPI Cards

- Total Customers
- Average Engagement
- Average Monthly Spending
- Average Website Visits

### Interactive Filters

Users can filter customers based on:

- Customer Segment
- Recommended Service

### Dashboard Sections

- Customer Data
- Customer Segment Distribution
- Recommended Services
- Business Insights
- Project Information

The dashboard makes the analytical results easier for business users to understand and explore.

---

## 💡 Key Business Insights

The analysis provides the following business insights:

- Customers can be grouped according to their behavior and interests.
- Highly engaged customers can be targeted with premium and personalized services.
- Training-focused customers represent an important target group for training programs.
- Data Analytics & Python Training received the highest number of recommendations.
- Customer engagement and interaction data can support targeted marketing.
- Customer segmentation can help businesses move from general marketing to more personalized strategies.

---

## 📁 Project Structure

```text
Veda_Day4_Customer_Segmentation/
│
├── app.py
├── customer_dataset.csv
├── customer_segmentation_final.csv
├── cluster_profiles.csv
├── segment_summary.csv
├── recommendation_summary.csv
├── business_recommendations.txt
├── PROJECT_SUMMARY.txt
├── requirements.txt
│
├── elbow_method.png
├── silhouette_scores.png
├── pca_clusters.png
├── segment_distribution.png
├── recommendations.png
│
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the Project Folder

```bash
cd Veda_Day4_Customer_Segmentation
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in the browser.

---

## 📦 Requirements

The main Python libraries required are:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```

---

## ⚠️ Dataset Note

The dataset used in this project is **synthetically generated for educational and internship purposes**.

It does not represent real customers or real business transactions.

Therefore, the results should be considered as a demonstration of a customer analytics workflow rather than actual business performance.

---

## 🚀 Future Improvements

The project can be improved further by:

- Using real customer data.
- Testing additional clustering algorithms such as DBSCAN and Hierarchical Clustering.
- Improving cluster separation through better feature selection.
- Developing a machine-learning-based recommendation system.
- Adding customer lifetime value prediction.
- Adding real-time data sources.
- Connecting the dashboard to a SQL database.
- Adding Power BI/Tableau reporting.
- Deploying the Streamlit application online.

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing
- Feature engineering
- Exploratory data analysis
- Feature scaling
- K-Means clustering
- Silhouette Score
- PCA
- Customer segmentation
- Rule-based recommendation systems
- Data visualization
- Streamlit dashboard development
- Business-oriented data interpretation

---

## 👨‍💻 Internship Project

**Organization:** Veda Technology  
**Internship Domain:** Data Science  
**Project:** Customer Segmentation & Service Recommendation System  
**Project Duration:** 4 Days

---

## ⭐ Conclusion

This project demonstrates how data science can be used to understand customer behavior, identify customer segments, recommend suitable services, and generate actionable business insights.

The final Streamlit dashboard provides an interactive way to explore the results and demonstrates how a data science model can be converted into a simple business application.
