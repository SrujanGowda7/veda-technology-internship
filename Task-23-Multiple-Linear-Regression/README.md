# Task 23 – Multiple Linear Regression

## Objective

Build a Multiple Linear Regression model using several numerical predictors to estimate a continuous target variable.

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook / Google Colab

## Dataset

A sample house-price dataset was created for this task.

### Features

* Area_sqft
* Bedrooms
* Age_years
* Distance_km

### Target

* Price_lakhs

## Methodology

1. Created and explored the dataset.
2. Separated predictors and target variable.
3. Checked correlations between numerical variables.
4. Split the data into training and testing sets using an 80:20 ratio.
5. Built a Multiple Linear Regression model using Scikit-learn.
6. Calculated model coefficients and intercept.
7. Generated predictions on unseen test data.
8. Evaluated the model using MAE, MSE, RMSE, and R² score.
9. Interpreted the importance and direction of the model coefficients.

## Model

Multiple Linear Regression uses several independent variables to predict a continuous dependent variable.

The model estimates house price using area, number of bedrooms, house age, and distance.

## Evaluation Metrics

The model was evaluated using:

* **MAE:** Mean Absolute Error
* **MSE:** Mean Squared Error
* **RMSE:** Root Mean Squared Error
* **R² Score:** Measures how well the model explains variation in the target variable.

## Feature Interpretation

Each regression coefficient represents the expected change in predicted house price for a one-unit increase in that feature, while keeping the other features constant.

Positive coefficients indicate a positive relationship with the target, while negative coefficients indicate a negative relationship.

## Conclusion

This task provided practical experience with Multiple Linear Regression and multivariable prediction. It helped strengthen understanding of feature selection, train-test splitting, model coefficients, prediction, evaluation metrics, and feature interpretation using Python and Scikit-learn.
