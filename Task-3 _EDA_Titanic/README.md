# Veda Technology - Task 3

## Exploratory Data Analysis - Titanic Dataset

### Project Overview

This project was completed as part of the Veda Technology Data Science Internship.

The objective of this task was to perform Exploratory Data Analysis (EDA) on the Titanic dataset to understand passenger characteristics, survival patterns, distributions, and relationships between different variables using statistical analysis and data visualization.

### Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab
* GitHub

### Dataset

The Titanic dataset contains passenger information such as passenger ID, survival status, passenger class, name, sex, age, family information, ticket, fare, and embarkation port.

The dataset contains **891 passenger records and 11 columns**.

### Exploratory Data Analysis

The following analyses were performed:

1. Inspected the dataset shape and structure.
2. Examined data types of all variables.
3. Checked for missing values.
4. Reviewed summary statistics of numerical variables.
5. Analyzed overall passenger survival.
6. Analyzed survival based on gender.
7. Analyzed survival based on passenger class.
8. Studied the age distribution of passengers.
9. Examined the fare distribution.
10. Analyzed correlations between numerical variables.
11. Compared age distribution by survival status.
12. Compared fare distribution across passenger classes.
13. Analyzed survival rate by passenger class and gender.

### Visualizations

The following visualizations were created:

* Passenger Survival Count
* Survival Count by Gender
* Survival Count by Passenger Class
* Age Distribution
* Age Distribution and Outliers
* Fare Distribution
* Fare Distribution and Potential Outliers
* Correlation Heatmap
* Age Distribution by Survival Status
* Fare Distribution by Passenger Class
* Survival Rate by Passenger Class and Gender

These visualizations were used to identify patterns and relationships within the dataset.

### Key Findings

1. **Overall Survival:** Out of 891 passengers, 342 survived and 549 did not survive. The overall survival rate was **38.38%**.

2. **Gender and Survival:** Female passengers had a substantially higher survival rate of **74.2%**, compared with **18.9%** for male passengers.

3. **Passenger Class and Survival:** Survival rate decreased with passenger class. First-class passengers had the highest survival rate at **63.0%**, followed by second class at **47.3%**, while third-class passengers had the lowest at **24.2%**.

4. **Fare Distribution:** Fare values were right-skewed, with most passengers paying relatively low fares and a small number paying very high fares.

5. **Gender and Class:** Female passengers had higher survival rates than male passengers across all three passenger classes.

### Data Quality Verification

The final dataset was verified after the analysis.

* **Total records:** 891
* **Total columns:** 11
* **Missing values:** 0
* **Duplicate rows:** 0
* **Data types:** Numeric and categorical variables were appropriately represented.
* **Dataset status:** Clean and ready for further analysis or machine learning applications.

### Deliverables

* `Veda_Technology_Task_3_EDA_Titanic.ipynb` - Exploratory Data Analysis notebook
* `titanic_cleaned_final.csv` - Final cleaned Titanic dataset
* `README.md` - Project documentation

### Conclusion

The Exploratory Data Analysis of the Titanic dataset provided useful insights into passenger survival patterns. The analysis showed that gender and passenger class had strong relationships with survival outcomes. Female passengers had a much higher survival rate than male passengers, while first-class passengers had a higher survival rate than second- and third-class passengers.

The analysis also highlighted the distribution of passenger ages and fares and helped identify relationships between numerical variables through correlation analysis.

Overall, the project demonstrates how Python-based data analysis and visualization can be used to explore datasets, identify patterns, and generate meaningful analytical insights.

### Deployment and Rollback

This task focuses on Exploratory Data Analysis using Python, Pandas, NumPy, Matplotlib, and Seaborn. It does not involve deploying an application or service. Therefore, deployment configuration and application rollback evidence are not applicable to this project.

The notebook, cleaned dataset, and project documentation are version-controlled in this public GitHub repository, allowing previous project versions to be reviewed through Git history if required.
