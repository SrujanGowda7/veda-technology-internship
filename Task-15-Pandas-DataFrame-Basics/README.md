# Task 15 – Pandas DataFrame Basics

## Objective

Learn the fundamentals of Pandas DataFrames and understand how tabular data can be created, loaded, inspected, and summarized using Python.

## Tools Used

* Python
* Pandas
* Scikit-learn
* Jupyter Notebook / Google Colab

## Tasks Performed

### 1. Created a DataFrame Manually

A Pandas DataFrame was created using a Python dictionary containing student information such as:

* Name
* Age
* Marks
* Department

### 2. Loaded a Real Dataset

The Iris dataset was loaded using Scikit-learn and converted into a Pandas DataFrame.

The dataset contains:

* 150 rows
* 5 columns
* 4 numerical features
* 1 categorical species column

### 3. Data Inspection

The following Pandas functions and properties were used:

* `head()` – view the first rows
* `info()` – inspect DataFrame structure
* `shape` – find rows and columns
* `columns` – display column names
* `dtypes` – identify data types
* `size` – find total number of elements
* `describe()` – generate summary statistics

## Key Concepts

### DataFrame

A DataFrame is a two-dimensional labeled data structure consisting of rows and columns.

### Shape

The `shape` property returns the number of rows and columns.

For the Iris dataset:

`(150, 5)`

### Size

The `size` property returns the total number of elements.

For the Iris dataset:

`150 × 5 = 750`

### Summary Statistics

The `describe()` function provides statistical information such as count, mean, standard deviation, minimum, maximum, and percentiles.

## Conclusion

This task provided practical experience with Pandas DataFrames and basic data exploration. It strengthened understanding of creating DataFrames, loading datasets, inspecting data structure, and generating summary statistics using Python.
