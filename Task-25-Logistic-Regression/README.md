# Task 25 – Logistic Regression Classification

## Objective

Build a Logistic Regression model for binary classification and evaluate its predictions on unseen data.

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Dataset

The Breast Cancer Wisconsin dataset available through Scikit-learn was used.

The dataset contains numerical features describing breast cancer cases. The target variable contains two classes.

## Tasks Performed

1. Loaded the Breast Cancer Wisconsin dataset.
2. Created feature and target variables.
3. Checked for missing values and duplicate rows.
4. Split the data into training and testing sets.
5. Standardized numerical features using `StandardScaler`.
6. Built a Logistic Regression model.
7. Trained the model on the training data.
8. Generated predictions on unseen test data.
9. Used `predict_proba()` to examine class probabilities.
10. Evaluated the model using accuracy and a classification report.
11. Visualized the results using a confusion matrix.

## Logistic Regression

Logistic Regression is a supervised machine learning algorithm mainly used for classification problems.

It predicts the probability of an observation belonging to a particular class and then assigns a class based on the predicted probability.

## Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report
- Confusion Matrix

## Model Interpretation

Logistic Regression provided a simple baseline classification model for the binary classification problem.

Feature scaling was applied before training because the numerical features have different ranges.

The `predict_proba()` function was used to inspect the probability assigned to each class.

## Conclusion

This task helped strengthen my understanding of binary classification, Logistic Regression, feature scaling, probability prediction, and model evaluation using Python and Scikit-learn.
