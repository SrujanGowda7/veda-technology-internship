# Veda Technology - Task 2
## Data Cleaning and Preprocessing

### Project Overview

This project was completed as part of the Veda Technology Data Science Internship.

The objective of this task was to clean and preprocess a raw Titanic dataset by identifying and resolving common data quality issues such as missing values, duplicate records, inconsistent categorical values, and incorrect data types.

### Tools Used

- Python
- Pandas
- NumPy
- Google Colab
- GitHub

### Dataset

Titanic Dataset containing passenger information such as passenger ID, survival status, passenger class, name, sex, age, family information, ticket, fare, and embarkation port.

### Data Cleaning Steps

1. Inspected the dataset using `df.info()`.
2. Identified missing values using `df.isnull().sum()`.
3. Checked duplicate records using `df.duplicated().sum()`.
4. Filled missing Age values using the median.
5. Filled missing Embarked values using the mode.
6. Removed the Cabin column because it contained excessive missing values.
7. Standardized categorical values in the Sex and Embarked columns.
8. Verified and corrected numerical data types.
9. Performed a final data-quality check.
10. Exported the cleaned dataset as `titanic_cleaned.csv`.

### Data Quality Improvements

| Issue | Action |
|---|---|
| Missing Age values | Median imputation |
| Missing Embarked values | Mode imputation |
| Excessive Cabin missing values | Column removed |
| Duplicate records | Checked and removed |
| Inconsistent Sex values | Standardized |
| Inconsistent Embarked values | Standardized |
| Data types | Verified and corrected |

### Final Result

The cleaned dataset contains:

- 891 rows
- 11 columns
- 0 missing values
- 0 duplicate rows
- Appropriate data types

### Deliverables

- `Veda_Technology_Task_2_Data_Cleaning.ipynb` - Data cleaning notebook
- `titanic_cleaned.csv` - Cleaned dataset

### Conclusion

The raw Titanic dataset was successfully cleaned and prepared for further data analysis and machine learning. The cleaning process improved data consistency, completeness, and reliability.

### Deployment and Rollback

This task focuses on data cleaning and preprocessing using Python and Pandas. It does not involve deploying an application or service. Therefore, deployment configuration and application rollback evidence are not applicable to this project.

The cleaned dataset and notebook are version-controlled in this public GitHub repository, allowing previous project versions to be reviewed through Git history if required.
