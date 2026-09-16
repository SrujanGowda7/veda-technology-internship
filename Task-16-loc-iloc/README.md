# Task 16 – Selecting Rows and Columns with loc and iloc

## Objective

Practice selecting rows and columns from Pandas DataFrames using `loc[]` and `iloc[]` and understand the difference between label-based and position-based selection.

## Tools Used

* Python
* Pandas
* Jupyter Notebook / Google Colab

## Dataset

A sample student DataFrame was created containing:

* Name
* Age
* Marks
* Department

Custom row labels (`S1` to `S5`) were used to demonstrate label-based selection.

## Tasks Performed

### Using `loc[]`

Five examples were performed:

1. Selecting a single row using its label.
2. Selecting multiple rows using labels.
3. Selecting a specific row and column.
4. Selecting multiple rows and columns using labels.
5. Selecting rows based on a condition and specific columns.

### Using `iloc[]`

Five examples were performed:

1. Selecting the first row using its position.
2. Selecting multiple rows using integer positions.
3. Selecting a specific value using row and column positions.
4. Selecting multiple rows and columns using positions.
5. Selecting a range of rows and columns.

## loc[] vs iloc[]

| Feature               | `loc[]`      | `iloc[]`                     |
| --------------------- | ------------ | ---------------------------- |
| Selection type        | Label-based  | Position-based               |
| Row selection         | Row labels   | Integer positions            |
| Column selection      | Column names | Integer positions            |
| Can use column names? | Yes          | No                           |
| Can use conditions?   | Yes          | Not directly in the same way |

## Key Learning

`loc[]` is useful when working with row labels, column names, and conditional selections.

`iloc[]` is useful when selecting data based on integer positions.

## Conclusion

This task provided practical experience in selecting rows and columns using Pandas `loc[]` and `iloc[]`. Understanding the difference between label-based and position-based indexing is important for accurate and efficient data manipulation.
