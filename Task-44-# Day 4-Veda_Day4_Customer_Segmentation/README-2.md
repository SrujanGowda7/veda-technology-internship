# Veda Technology - Customer Segmentation & Service Recommendation System

## Overview

This project was developed as part of the Veda Technology
Data Science Internship.

The objective is to analyze customer behaviour and group
customers into meaningful segments using K-Means clustering.

A rule-based recommendation system is also developed to
recommend suitable services to different customer groups.

## Dataset

The project contains 500 synthetic customers.

Features include:

- Age
- Website Visits
- Service Inquiries
- Training Interest
- Internship Interest
- Engagement Score
- Monthly Spending
- Previous Purchases
- Support Interactions
- Days Since Last Interaction

## Feature Engineering

Additional features:

- Total Interest
- Total Interactions
- Customer Value

## Machine Learning

K-Means clustering was used.

The number of clusters was evaluated using:

- Elbow Method
- Silhouette Score

Selected K: 2

Best Silhouette Score: 0.1264

## Customer Segmentation

The project creates customer groups such as:

- Highly Engaged Customers
- Training-Focused Customers
- Internship-Focused Customers
- Occasional Customers

## Service Recommendation

Services are recommended based on customer behaviour.

Examples:

- Data Analytics & Python Training
- Industry Internship Program
- IT & Digital Services
- Premium Digital Solutions
- Beginner Training & Orientation

## Dashboard

A Streamlit dashboard was created to:

- View customer data
- Filter customer segments
- Filter recommended services
- View KPIs
- View customer segment distribution
- View recommended services
- View business insights

## Technologies

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Google Colab

## Business Benefits

This solution can help businesses:

- Understand customer behaviour
- Improve customer targeting
- Personalize marketing
- Recommend suitable services
- Improve engagement
- Identify valuable customer groups

## Disclaimer

The dataset is synthetic and created for educational
and internship purposes.