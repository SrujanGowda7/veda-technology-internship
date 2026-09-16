# Task 24 – Regression Metrics

## Objective

Evaluate regression model predictions using MAE, MSE, RMSE, and R² and understand how each metric measures prediction performance.

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook / Google Colab

## Dataset

Sample actual and predicted values were created to demonstrate regression evaluation metrics.

## Metrics Calculated

### MAE – Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

Lower MAE indicates smaller average prediction errors.

### MSE – Mean Squared Error

Measures the average squared prediction error.

MSE gives greater penalty to larger errors.

### RMSE – Root Mean Squared Error

RMSE is the square root of MSE. It is expressed in the same units as the target variable and is sensitive to larger errors.

### R² – R-Squared

R² measures the proportion of variation in the target variable explained by the regression model.

## Methodology

1. Created actual and predicted values.
2. Calculated prediction errors.
3. Calculated MAE, MSE, RMSE, and R² using Scikit-learn and NumPy.
4. Created a comparison table.
5. Analyzed individual prediction errors.
6. Compared the interpretation of each metric.
7. Discussed the appropriate use of different regression metrics.

## Metric Comparison

| Metric | Measures                | Effect of Large Errors |
| ------ | ----------------------- | ---------------------- |
| MAE    | Average absolute error  | Lower sensitivity      |
| MSE    | Average squared error   | High sensitivity       |
| RMSE   | Error in original units | High sensitivity       |
| R²     | Variance explained      | Not an error metric    |

## Key Learning

Different regression metrics provide different perspectives on model performance. MAE is easy to interpret, while RMSE is useful when large errors need more attention. MSE is useful for mathematical optimization, and R² helps understand the amount of target variation explained by a model.

## Conclusion

This task provided practical experience in evaluating regression predictions using MAE, MSE, RMSE, and R². It demonstrated why multiple evaluation metrics should be considered rather than relying on R² alone.
