# Task 22 – A B Test Analysis

## Overview

This project analyzes an A/B test comparing a Control group and a Treatment group to determine whether the observed difference in conversion rate is statistically meaningful.

The analysis demonstrates how statistical testing and effect-size measurement can be used to support data-driven business decisions.

## Objective

The main objectives of this task are:

* Compare Control and Treatment groups.
* Calculate descriptive statistics.
* Compare conversion rates.
* Calculate effect size.
* Perform an appropriate statistical test.
* Interpret the p-value.
* Make a final recommendation based on statistical evidence.

## Tools Used

* Python
* Pandas
* NumPy
* SciPy
* Matplotlib
* Jupyter Notebook

## Dataset

The dataset contains user-level A/B testing information with the following columns:

| Column      | Description                         |
| ----------- | ----------------------------------- |
| `user_id`   | Unique identifier for each user     |
| `group`     | Control or Treatment group          |
| `converted` | Whether the user converted (0 or 1) |

## Methodology

### 1. Data Preparation

The dataset was loaded and checked for structure, data types, missing values, and group distribution.

### 2. Group Definition

* **Control:** Existing or standard version.
* **Treatment:** New version being tested.

### 3. Conversion Rate

Conversion rate was calculated as:

```text
Conversion Rate = Number of Conversions / Total Users
```

### 4. Effect Size

Both absolute improvement and relative improvement were calculated.

### 5. Statistical Testing

A two-proportion statistical test was used to compare conversion rates between the Control and Treatment groups.

The significance level was set to:

```text
α = 0.05
```

## Results

| Metric                    |                 Result |
| ------------------------- | ---------------------: |
| Control Conversion Rate   |                 11.22% |
| Treatment Conversion Rate |                 15.45% |
| Absolute Improvement      | 4.23 percentage points |
| Relative Improvement      |                 37.67% |
| Z-statistic               |                 2.7829 |
| P-value                   |                 0.0054 |

## Interpretation

The Treatment group achieved a higher conversion rate than the Control group.

The relative improvement was **37.67%**, indicating a substantial difference in conversion performance.

The p-value was **0.0054**, which is lower than the significance level of 0.05. Therefore, the null hypothesis was rejected, providing statistically significant evidence of a difference between the two groups.

## Final Recommendation

Based on the statistical evidence and effect size, the Treatment version can be recommended for implementation.

However, business factors such as implementation cost, user experience, technical feasibility, and other performance metrics should also be considered before full deployment.

## Key Learnings

* Understanding A/B testing and experimentation.
* Defining Control and Treatment groups.
* Calculating conversion rates.
* Measuring effect size.
* Performing statistical hypothesis testing.
* Interpreting p-values.
* Understanding statistical vs. practical significance.
* Making data-driven recommendations.

## Interview Questions

### What is A/B testing?

A/B testing is an experimental method used to compare two versions and determine which performs better based on a selected metric.

### What is the Control group?

The Control group receives the existing or standard version and acts as the baseline for comparison.

### Why should effect size be considered alongside statistical significance?

Statistical significance indicates whether the observed difference is likely to be due to something other than random variation, while effect size indicates the magnitude of that difference. Both are important for making meaningful business decisions.

## Conclusion

This project demonstrates how A/B testing can be used to evaluate changes using both statistical evidence and practical impact. The Treatment group showed a statistically significant improvement in conversion rate compared with the Control group.
