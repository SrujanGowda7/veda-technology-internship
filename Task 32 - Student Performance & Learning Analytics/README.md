# Student Performance & Learning Analytics

## 📌 Project Overview

**Student Performance & Learning Analytics** is a Data Science project focused on analyzing academic and learning-related factors that may be associated with student performance.

The project covers the basic Data Science workflow, including **data generation, data cleaning, exploratory data analysis (EDA), visualization, correlation analysis, feature engineering, and introductory predictive modeling**.

The project uses a **synthetic student dataset** created with Python for learning and demonstration purposes.

---

## 🎯 Objectives

* Analyze student academic performance.
* Study attendance and study-hour patterns.
* Compare performance across subjects.
* Explore relationships between learning factors and final scores.
* Perform data cleaning and validation.
* Create meaningful visualizations.
* Perform correlation analysis.
* Create additional features through feature engineering.
* Build a basic machine-learning model in the next stage.
* Document the complete workflow for reproducibility.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Jupyter Notebook / Google Colab**
* **Excel**
* **Git & GitHub**

---

## 📊 Dataset

A synthetic dataset containing **500 student records** was created using Python and NumPy.

The dataset contains academic, attendance, study, and demographic information.

### Original Features

| Feature          | Description               |
| ---------------- | ------------------------- |
| `Student_ID`     | Unique student identifier |
| `Gender`         | Student gender            |
| `Age`            | Student age               |
| `Study_Hours`    | Average study hours       |
| `Attendance`     | Attendance percentage     |
| `Math_Score`     | Mathematics score         |
| `Science_Score`  | Science score             |
| `English_Score`  | English score             |
| `Previous_Score` | Previous academic score   |
| `Final_Score`    | Final academic score      |

---

## 🧪 Synthetic Dataset Provenance

The dataset is **synthetically generated** and does not contain real student records.

The dataset was created using Python, Pandas, and NumPy with a fixed random seed:

```python
np.random.seed(42)
```

Using a fixed seed makes the dataset generation **reproducible**, meaning the same code can be used to generate the same dataset again.

### Data Generation

The main input variables were generated within predefined ranges:

* Age: 17–22 years
* Study Hours: approximately 1–10 hours
* Attendance: approximately 50–100%
* Subject Scores: 35–100
* Previous Score: 35–100

The `Final_Score` was generated using a weighted combination of:

* Mathematics score
* Science score
* English score
* Previous score
* Attendance
* Study hours

A small amount of random noise was added to the final score to introduce natural variation.

Therefore, some relationships between these variables and `Final_Score` are **expected by design**.

---

## ⚠️ Important Interpretation Note

Because the dataset is synthetic, correlations and patterns observed in the analysis should **not be interpreted as real-world evidence about student behavior**.

For example, because attendance, study hours, previous score, and subject scores were included in the formula used to generate `Final_Score`, relationships between these variables and final performance are partly a result of the data-generation process.

The project is therefore intended to demonstrate the **Data Science workflow and analytical techniques**, rather than make claims about real students.

---

## ⚖️ Performance Categories & Class Balance

Students were categorized according to their final score:

| Category          | Final Score |
| ----------------- | ----------: |
| Excellent         |        ≥ 80 |
| Good              |       60–79 |
| Average           |       40–59 |
| Needs Improvement |        < 40 |

The class distribution was examined before using these categories for any classification task.

Class balance is important because a highly uneven distribution can affect classification-model performance and evaluation metrics.

The exact class counts and percentages should be calculated directly from the generated dataset before model training.

Example:

```python
df["Performance_Category"].value_counts()
```

```python
df["Performance_Category"].value_counts(normalize=True) * 100
```

---

## 🧹 Data Cleaning & Validation

The following data-quality checks were performed:

* Checked dataset dimensions.
* Inspected column names and data types.
* Checked for missing values.
* Checked for duplicate records.
* Validated attendance values.
* Validated score ranges.
* Removed duplicate records where applicable.
* Generated descriptive statistics.

These steps helped prepare the dataset for further analysis.

---

## 🔍 Exploratory Data Analysis

EDA was performed to understand the structure and distribution of the data.

The analysis included:

* Dataset inspection
* Descriptive statistics
* Final-score distribution
* Attendance distribution
* Study-hours analysis
* Subject-wise performance
* Performance-category distribution
* Relationships between learning factors and final score

---

## 📈 Attendance Analysis

Attendance was analyzed to understand its relationship with student performance.

A scatter plot was created to compare:

**Attendance → Final Score**

Correlation analysis was also performed to measure the strength and direction of the relationship.

However, because the dataset is synthetic and attendance contributes to the generated final score, this relationship should be interpreted as a **synthetic-data pattern rather than a causal finding**.

---

## 📚 Study Hours Analysis

Study hours were compared with final scores using a scatter plot.

The analysis helps demonstrate how numerical variables can be explored visually and statistically.

Pearson correlation was used to measure the linear association between study hours and final score.

---

## 📖 Subject-wise Performance

Average scores were calculated for:

* Mathematics
* Science
* English

A bar chart was created to compare the average performance across subjects.

This helps identify differences in average subject performance within the synthetic dataset.

---

## 🔗 Correlation Analysis

A correlation matrix and heatmap were created to examine relationships between numerical variables.

Variables analyzed include:

* Study Hours
* Attendance
* Math Score
* Science Score
* English Score
* Previous Score
* Final Score

Correlation helps identify the **direction and strength of linear association** between variables.

### Important Consideration

The correlations involving `Final_Score` are partly expected because the final score was generated using several of these variables.

Therefore:

> Correlation in this project represents association within the synthetic dataset and should not be interpreted as proof of causation.

---

## ⚙️ Feature Engineering

Additional features were created to improve analysis and prepare the dataset for machine learning.

### 1. Average Subject Score

Calculated using the average of:

* Math Score
* Science Score
* English Score

### 2. Attendance Category

Attendance was grouped into:

* Low
* Moderate
* Good
* Excellent

### 3. Study Level

Study hours were grouped into:

* Low
* Moderate
* High
* Very High

### 4. Performance Category

Final scores were converted into:

* Excellent
* Good
* Average
* Needs Improvement

---

## 📊 Visualizations

The project includes the following visualizations:

* Final Score Distribution
* Attendance Distribution
* Attendance vs Final Score
* Study Hours vs Final Score
* Average Subject Performance
* Performance Category Distribution
* Correlation Heatmap

These visualizations make it easier to identify patterns and relationships within the dataset.

---

## 🔄 Project Workflow

```text
Synthetic Dataset Generation
          ↓
Data Inspection
          ↓
Data Cleaning & Validation
          ↓
Exploratory Data Analysis
          ↓
Data Visualization
          ↓
Correlation Analysis
          ↓
Feature Engineering
          ↓
Predictive Modeling
          ↓
Model Evaluation
          ↓
Final Documentation
```

---

## 🤖 Predictive Modeling

Predictive modeling is planned as the next stage of the project.

The planned workflow includes:

1. Selecting relevant features.
2. Selecting the target variable.
3. Splitting the dataset into training and testing sets.
4. Training a basic machine-learning model.
5. Generating predictions.
6. Evaluating model performance.
7. Comparing predicted and actual values.

Possible approaches include **Linear Regression** for score prediction or a **classification model** for predicting performance categories.

Model results will be documented separately after training and evaluation.

---

## 📁 Project Structure

```text
Student-Performance-Learning-Analytics/
│
├── README.md
│
├── Student_Performance_Learning_Analytics.ipynb
│
├── student_performance.csv
│
├── cleaned_student_performance.csv
│
├── visualizations/
│   ├── final_score_distribution.png
│   ├── attendance_distribution.png
│   ├── attendance_vs_score.png
│   ├── study_hours_vs_score.png
│   ├── subject_performance.png
│   └── correlation_heatmap.png
│
└── report/
    └── final_report.pdf
```

---

## ✅ Day 1 Work Completed

The following activities were completed during Day 1:

* ✅ Synthetic dataset generation
* ✅ Dataset inspection
* ✅ Data cleaning and validation
* ✅ Missing-value checking
* ✅ Duplicate checking
* ✅ Descriptive statistics
* ✅ Exploratory Data Analysis
* ✅ Attendance analysis
* ✅ Study-hours analysis
* ✅ Subject-wise performance analysis
* ✅ Correlation analysis
* ✅ Data visualizations
* ✅ Performance categorization
* ✅ Feature engineering
* ✅ Cleaned dataset creation

---

## 🔁 Reproducibility

The project uses a fixed random seed to make synthetic-data generation reproducible.

```python
np.random.seed(42)
```

To reproduce the analysis:

1. Open the Jupyter Notebook or Google Colab notebook.
2. Run the dataset-generation cells.
3. Run the data-cleaning cells.
4. Run the EDA and visualization cells.
5. Run the feature-engineering cells.
6. The cleaned dataset can then be used for predictive modeling.

---

## 📌 Limitations

* The dataset is synthetic rather than collected from real students.
* Relationships between variables may reflect the formula used during data generation.
* Correlation does not imply causation.
* Synthetic class distributions may differ from real-world student populations.
* Model performance on this dataset should not be assumed to represent performance on real educational data.

---

## 🚀 Future Improvements

Future versions of the project could include:

* Using a real-world educational dataset.
* More detailed attendance analysis.
* Additional student behavioral features.
* Multiple machine-learning algorithms.
* Hyperparameter tuning.
* Cross-validation.
* Model comparison.
* Feature-importance analysis.
* Interactive dashboards using Power BI or Tableau.
* Deployment of the final model as a simple application.

---

## 📝 Conclusion

The **Student Performance & Learning Analytics** project demonstrates a complete introductory Data Science workflow starting from synthetic data generation and progressing through data cleaning, exploratory analysis, visualization, correlation analysis, and feature engineering.

The project also documents the **provenance and limitations of the synthetic dataset**, making it clearer which patterns are intentionally introduced during data generation and which are discovered during analysis.

The cleaned and engineered dataset provides a foundation for the next stage: **predictive modeling and model evaluation**.

---

## 👨‍💻 Author

**Srujan Gowda**

BE – Information Science & Engineering
APS College of Engineering, Bengaluru

**Areas of Interest:**
Data Science • Data Analytics • Machine Learning • AI/ML

---

## ⚠️ Dataset Disclaimer

This project is created for **educational and demonstration purposes**. The synthetic dataset does not represent real students, institutions, or academic records. Any patterns, correlations, or model results should be interpreted within the context of the synthetic data-generation process.
