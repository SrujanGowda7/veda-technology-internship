# Day 3 – Customer Segmentation & Predictive Analysis

## Overview

Day 3 focused on customer segmentation, predictive analysis, service-demand analysis, customer engagement, and business recommendations using the synthetic Veda Technology dataset.

## Customer Segmentation

K-Means clustering was used to group records based on:

- Website Visits
- Application Submitted
- Inquiry Submitted
- Revenue
- Response Time
- Satisfaction Score

Three customer clusters were created and analyzed.

Cluster 2 showed a 100% conversion rate. However, this result is influenced by the synthetic dataset design because Revenue was included in clustering and revenue is assigned only to converted records. Therefore, this should not be interpreted as a perfect real-world customer segment.

## Predictive Analysis

Logistic Regression was used to predict customer conversion.

Revenue was excluded from the prediction model to avoid target leakage.

### Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 69.0% |
| Precision | 0.0% |
| Recall | 0.0% |
| F1 Score | 0.0% |

Although accuracy was 69%, the model failed to correctly identify converted customers.

This indicates that the current synthetic features contain limited predictive information about conversion. Accuracy alone is therefore not sufficient to evaluate this model.

## Key Findings

- Highest demand service: **Data Analytics Training – 143 records**
- Highest converting service: **Digital Marketing – 37.69%**
- Highest revenue service: **Digital Marketing – ₹1,134,155**
- Highest converting customer cluster: **Cluster 2 – 100%**
- Highest converting engagement group: **Medium – 32.02%**

## Business Recommendations

- Give additional attention to Data Analytics Training due to its high demand.
- Study Digital Marketing because it achieved the highest service conversion rate and simulated revenue.
- Use customer segmentation to develop different engagement strategies.
- Track response time together with customer satisfaction.
- Use marketing-channel analysis to understand stronger channels.
- Continue monitoring monthly applications, inquiries, conversions and revenue.

## Day 3 Output Files

- `veda_business_analytics_day3.csv`
- `day3_customer_cluster_profile.csv`
- `day3_cluster_business_performance.csv`
- `day3_conversion_model_coefficients.csv`
- `day3_service_analysis.csv`
- `day3_engagement_conversion.csv`

## Day 3 Conclusion

Day 3 introduced customer segmentation and predictive analytics into the project.

The analysis also demonstrated that model accuracy should not be considered alone. Precision, recall and F1-score showed that the current Logistic Regression model was unable to identify converted customers effectively.

These findings and limitations will be considered during the final dashboard, recommendations and executive reporting stage.

> Note: All results are based on synthetic data created for educational purposes and do not represent actual Veda Technology business performance.
