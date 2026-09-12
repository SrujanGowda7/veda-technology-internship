# Task 20 – Chi-Square Test of Independence

## Objective

To perform a Chi-Square Test of Independence to determine whether two categorical variables are statistically associated.

## Tools Used

- Python
- Pandas
- NumPy
- SciPy
- Jupyter Notebook / Google Colab

## Dataset

A sample categorical dataset containing **Gender** and **Survival** variables was used for the analysis.

## Tasks Performed

1. Created a categorical dataset using Pandas.
2. Created a contingency table using `pd.crosstab()`.
3. Formulated the null and alternative hypotheses.
4. Performed the Chi-Square Test of Independence using SciPy.
5. Calculated the Chi-Square statistic, degrees of freedom, and p-value.
6. Calculated and analyzed expected frequencies.
7. Interpreted the statistical significance using a significance level of 0.05.

## Hypotheses

**Null Hypothesis (H0):** Gender and Survival are statistically independent.

**Alternative Hypothesis (H1):** Gender and Survival are statistically associated.

## Significance Level

The significance level used for the test was **0.05**.

## Contingency Table

A contingency table was created to show the observed frequency of each combination of Gender and Survival.

## Expected Frequencies

Expected frequencies were calculated using the Chi-Square test. These values represent the expected counts when the two categorical variables are assumed to be independent.

## Result Interpretation

The calculated p-value was compared with the significance level of 0.05.

- If **p-value < 0.05**, the null hypothesis is rejected and there is a statistically significant association between the variables.
- If **p-value ≥ 0.05**, the null hypothesis is not rejected because there is insufficient evidence to conclude that the variables are associated.

## Conclusion

The Chi-Square Test of Independence is useful for determining whether two categorical variables have a statistically significant relationship. This task helped strengthen my understanding of contingency tables, expected frequencies, hypothesis testing, and statistical interpretation using Python.
