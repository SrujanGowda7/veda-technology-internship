# Veda Technology Business & Service Analytics

## Project Overview

This project analyzes simulated business and service data representing the operations of Veda Technology.

The objective is to understand how data science can support business decision-making through website visitor analysis, internship and training analysis, service demand analysis, marketing analysis, customer segmentation, KPI tracking, predictive analysis, and visualization.

> Note: This project uses completely synthetic data created for educational purposes. No private or confidential Veda Technology data is used.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab
- SQL
- Excel
- Power BI
- Git & GitHub

---

# Day 1 – Data Creation, Cleaning & Initial Analysis

## Dataset

A synthetic dataset containing 1,000 business records was generated to represent different areas of Veda Technology.

The dataset includes information related to:

- Website visitors
- Marketing channels
- Internships
- Training programs
- IT services
- Digital services
- Customer types
- Locations
- Inquiries
- Applications
- Conversions
- Revenue
- Response time
- Customer satisfaction

## Data Cleaning

The following preprocessing steps were performed:

- Checked dataset structure and data types
- Checked missing values
- Checked duplicate records
- Converted Date to datetime format
- Verified numerical and categorical columns
- Added a Month feature for monthly analysis
- Exported the cleaned dataset

Final dataset:

- Records: 1,000
- Missing values: 0
- Duplicate rows: 0

## Business KPIs

| KPI | Result |
|---|---:|
| Unique Visitors | 1,000 |
| Website Visits | 7,438 |
| Applications | 426 |
| Inquiries | 668 |
| Conversions | 308 |
| Conversion Rate | 30.80% |
| Simulated Revenue | ₹7,545,313 |
| Average Satisfaction | 2.95 / 5 |
| Average Response Time | 24.09 hours |

## Initial Analysis

### Business Area

Internship showed the highest activity with 354 records, followed by Training, IT Services and Digital Services.

### Service Demand

Data Analytics Training recorded the highest service demand with 143 records.

### Marketing Channels

LinkedIn generated the highest number of records with 181.

College Referral achieved the highest simulated conversion rate at 34.48%.

### Customer Analysis

Students represented the largest customer group with 501 records.

### Revenue Analysis

Internship generated the highest simulated revenue at ₹3,094,855.

## Correlation Analysis

A correlation matrix was created to study relationships between numerical business variables.

Converted and Revenue showed a strong positive correlation of approximately 0.83. This relationship is expected because revenue in the synthetic dataset is assigned only to converted records.

Most other variables showed weak correlations because the synthetic dataset was primarily generated using independent random sampling.

## Day 1 Visualizations

The initial analysis includes visualizations for:

- Business area demand
- Marketing channel distribution
- Service demand
- Customer type distribution
- Location distribution
- Conversion rate by marketing channel
- Revenue by business area
- Monthly business activity
- Correlation matrix

## Day 1 Conclusion

Day 1 established the foundation for the project by creating, cleaning and exploring a realistic synthetic business dataset.

The initial analysis identified patterns in business areas, service demand, marketing channels, customer groups, conversions and simulated revenue.

The cleaned dataset will be used in the next stages for deeper business analytics, segmentation, predictive analysis and dashboard development.

---

## Project Progress

- [x] Day 1 – Dataset Creation, Cleaning & Initial Analysis
- [ ] Day 2 – Detailed Business & Service Analysis
- [ ] Day 3 – Customer Segmentation & Predictive Analysis
- [ ] Day 4 – Power BI Dashboard, Recommendations & Final Report
