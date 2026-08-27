# Task 4 – Data Visualization with Matplotlib & Seaborn

## Internship

**Veda Technology – Data Science Track**

**Task:** Task 4 – Level 1 Day 4
**Topic:** Data Visualization with Matplotlib & Seaborn

---

## 1. Project Overview

This project focuses on exploring and visualizing the Titanic dataset using Python, Matplotlib, and Seaborn.

The main objective of this task is to create meaningful charts that answer specific analytical questions and communicate patterns in the data clearly.

Different visualization techniques were selected based on the type of data and the analytical question being addressed.

---

## 2. Objective

The objectives of this task are:

* To understand the importance of data visualization in data science.
* To learn how to select an appropriate chart for an analytical question.
* To create different types of visualizations using Matplotlib and Seaborn.
* To identify patterns, distributions, relationships, and trends in the Titanic dataset.
* To communicate analytical findings using clear titles, labels, and takeaways.
* To avoid unnecessary visual clutter and maintain consistent formatting.

---

## 3. Dataset

The **Titanic dataset** was used for this project.

The dataset contains information about passengers who were aboard the Titanic, including:

* Passenger ID
* Survival status
* Passenger class
* Name
* Gender
* Age
* Number of siblings/spouses aboard
* Number of parents/children aboard
* Ticket
* Fare
* Cabin
* Port of embarkation

The dataset contains **891 passenger records and 12 columns** in its original form.

---

## 4. Technologies and Libraries Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Development Environment

* Google Colab

### Version Control

* GitHub

---

## 5. Visualizations Created

A total of **7 visualizations** were created in this project.

### 1. Bar Chart – Survival Distribution

**Analytical Question:**
How many passengers survived and how many did not?

**Why this chart was selected:**
A bar chart is suitable for comparing values across categorical groups.

**Key Takeaway:**
More passengers did not survive than survived the Titanic disaster.

---

### 2. Count Plot – Passenger Class Distribution

**Analytical Question:**
How were passengers distributed across the three passenger classes?

**Why this chart was selected:**
A count plot is useful for comparing the number of observations across categorical groups.

**Key Takeaway:**
Third-class passengers formed the largest passenger group.

---

### 3. Histogram – Age Distribution

**Analytical Question:**
What is the age distribution of Titanic passengers?

**Why this chart was selected:**
A histogram is appropriate for visualizing the distribution of a continuous numerical variable such as age.

**Key Takeaway:**
The passengers were mainly concentrated in the young-adult to middle-age range.

---

### 4. Box Plot – Fare Distribution by Passenger Class

**Analytical Question:**
How does fare vary across passenger classes?

**Why this chart was selected:**
A box plot shows the median, spread, and possible outliers of a numerical variable across different categories.

**Key Takeaway:**
First-class passengers generally paid substantially higher fares than second- and third-class passengers.

---

### 5. Scatter Plot – Age vs Fare

**Analytical Question:**
Is there a relationship between passenger age and fare?

**Why this chart was selected:**
A scatter plot is useful for examining the relationship between two numerical variables.

**Key Takeaway:**
Age and fare do not show a strong direct relationship, although some high-fare outliers are visible.

---

### 6. Correlation Heatmap

**Analytical Question:**
What relationships exist between the numerical variables?

**Why this chart was selected:**
A heatmap provides a compact visual representation of correlations between multiple numerical variables.

**Key Takeaway:**
Passenger class and fare show a noticeable relationship, while several other numerical variables have weaker correlations.

---

### 7. Count Plot – Survival by Gender

**Analytical Question:**
How did survival differ between male and female passengers?

**Why this chart was selected:**
A grouped count plot makes it easy to compare survival outcomes across gender categories.

**Key Takeaway:**
Female passengers had a much higher survival proportion than male passengers.

---

## 6. Key Findings

The visualizations helped identify several important patterns in the Titanic dataset:

1. The number of passengers who did not survive was higher than the number who survived.
2. Third-class passengers represented the largest passenger group.
3. Passenger ages were mainly concentrated among young and middle-aged adults.
4. First-class passengers generally paid higher fares.
5. Age and fare did not show a strong direct relationship.
6. Passenger class and fare showed a noticeable relationship.
7. Female passengers had a substantially higher survival proportion than male passengers.

---

## 7. Chart Selection Approach

Different charts were selected according to the analytical question:

| Analytical Purpose                                        | Visualization |
| --------------------------------------------------------- | ------------- |
| Compare categories                                        | Bar Chart     |
| Count categorical observations                            | Count Plot    |
| Understand numerical distribution                         | Histogram     |
| Compare spread and identify outliers                      | Box Plot      |
| Study relationship between two numerical variables        | Scatter Plot  |
| Analyze correlations between multiple numerical variables | Heatmap       |

The goal was to use the simplest visualization that clearly communicates the required information.

---

## 8. Data Visualization Best Practices Followed

The following practices were followed throughout the project:

* Meaningful titles were added to every visualization.
* X-axis and Y-axis labels were included.
* Appropriate chart types were selected according to the analytical question.
* Consistent formatting was maintained.
* Unnecessary visual clutter was avoided.
* Clear takeaways were provided for every visualization.
* Seaborn and Matplotlib were used appropriately.

---

## 9. Project Files

```text
Task-4-Data-Visualization/
│
├── Veda_Task_4_Data_Visualization.ipynb
├── titanic.csv
└── README.md
```

### File Description

**Veda_Task_4_Data_Visualization.ipynb**
Contains the complete Python code, visualizations, chart explanations, and analytical takeaways.

**titanic.csv**
Contains the Titanic dataset used for the visualizations.

**README.md**
Provides an overview of the project, methodology, visualizations, findings, and tools used.

---

## 10. How to Run the Project

1. Download or clone this repository.
2. Open `Veda_Task_4_Data_Visualization.ipynb` using Google Colab or Jupyter Notebook.
3. Install the required libraries if they are not already available.
4. Run the notebook cells from top to bottom.
5. The visualizations will be generated using Matplotlib and Seaborn.

The notebook can also be opened directly in Google Colab for execution.

---

## 11. Interview Questions

### Q1. When would you use a boxplot instead of a histogram?

A boxplot is useful when comparing the distribution of a numerical variable across different groups and when identifying the median, spread, and outliers is important. A histogram is more suitable when the main goal is to understand the overall distribution of a numerical variable.

### Q2. What is the difference between Matplotlib and Seaborn?

Matplotlib is a general-purpose Python visualization library that provides detailed control over plots. Seaborn is built on top of Matplotlib and provides a higher-level interface with convenient functions for statistical visualizations and attractive default formatting.

### Q3. How can you visualize three variables together?

Three variables can be visualized using techniques such as a scatter plot with color or size representing the third variable. For example, age can be shown on the X-axis, fare on the Y-axis, and passenger class can be represented using different colors.

---

## 12. Outcome

This project provided practical experience in selecting appropriate visualization techniques and communicating analytical insights through charts.

The Titanic dataset was explored using multiple visualization methods, including categorical comparisons, numerical distributions, relationships, and correlation analysis.

The task improved understanding of how visualization can be used to identify patterns and communicate data-driven findings effectively.

---

## 13. Conclusion

The project successfully demonstrates the use of Matplotlib and Seaborn for exploratory data visualization.

By selecting charts according to specific analytical questions, the visualizations make the Titanic dataset easier to understand and highlight important patterns related to survival, passenger class, gender, age, and fare.
