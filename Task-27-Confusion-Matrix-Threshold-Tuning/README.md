# Task 27 – Confusion Matrix and Threshold Tuning

## Objective

Analyze classification predictions using a confusion matrix and investigate how changing the probability threshold affects precision and recall.

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

## Dataset

The Breast Cancer Wisconsin dataset available through Scikit-learn was used.

## Tasks Performed

* Loaded and explored the dataset
* Split the data into training and testing sets
* Standardized numerical features
* Trained a Logistic Regression model
* Generated predicted probabilities using `predict_proba()`
* Created a confusion matrix using the default threshold of 0.5
* Tested multiple probability thresholds
* Compared Precision, Recall, and F1-score
* Visualized Precision vs Recall
* Selected a threshold based on the highest F1-score among the tested thresholds
* Created a final confusion matrix using the selected threshold

## Confusion Matrix

A confusion matrix shows:

* True Positive
* True Negative
* False Positive
* False Negative

It helps understand the types of errors made by a classification model.

## Threshold Tuning

The following probability thresholds were tested:

* 0.3
* 0.4
* 0.5
* 0.6
* 0.7

Changing the threshold changes how the model converts predicted probabilities into class predictions.

A lower threshold generally classifies more observations as positive, which can increase recall but may also increase false positives.

A higher threshold makes the model more selective about positive predictions, which can increase precision but may reduce recall.

## Threshold Recommendation

The threshold with the highest F1-score among the tested thresholds was selected as the recommended threshold.

This provides a balance between precision and recall.

However, in a real-world application, the threshold should ultimately be selected based on the practical cost of false positives and false negatives.

## Conclusion

This task provided practical experience with confusion matrices, predicted probabilities, probability thresholds, precision, recall, and F1-score.

It demonstrated that the default 0.5 threshold is not always optimal and that threshold selection should consider the requirements of the specific classification problem.
