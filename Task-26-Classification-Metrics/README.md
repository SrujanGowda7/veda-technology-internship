# Task 26 – Classification Metrics Deep Dive

## Objective

Evaluate a classification model using Accuracy, Precision, Recall, F1-score, and Support, and understand when each metric is useful.

## Tools Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

## Dataset

The Breast Cancer Wisconsin dataset available through Scikit-learn was used.

## Tasks Performed

* Loaded and explored the dataset
* Split the data into training and testing sets
* Standardized numerical features
* Trained a Logistic Regression classification model
* Generated predictions on unseen test data
* Calculated Accuracy, Precision, Recall, and F1-score
* Generated a Classification Report
* Created a Confusion Matrix
* Analyzed False Positives and False Negatives
* Compared different classification metrics
* Studied practical use cases for each metric

## Classification Metrics

### Accuracy

Measures the overall proportion of correct predictions.

### Precision

Measures how many predicted positive cases were actually positive.

### Recall

Measures how many actual positive cases were correctly identified.

### F1-score

Provides a balance between Precision and Recall.

### Support

Represents the number of actual samples belonging to each class.

## Practical Interpretation

Accuracy is useful when different types of classification errors have similar importance.

Precision is useful when false positives are costly.

Recall is useful when false negatives are costly.

F1-score is useful when both precision and recall are important.

For medical screening, recall can be particularly important because missing a positive case may have serious consequences. However, the appropriate metric depends on the practical requirements and cost of errors.

## Conclusion

This task helped strengthen the understanding of classification model evaluation. It demonstrated that accuracy should not always be considered the best metric and that the choice of metric should depend on the practical problem and the cost of false positives and false negatives.
