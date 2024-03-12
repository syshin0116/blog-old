---
layout: post
title: Anomaly Detection
date: 2024-03-12 22:43 +0900
categories:
  - Deep-Learning
  - 기법
tags: 
math: true
---

## Dataset

## [Company Bankruptcy Prediction](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction)



## 참고 Git repo

### [INM701_CW](https://github.com/Saurabhraj5162/INM701_CW)
#### Company Bankruptcy Prediction
#### Problem:

It is a classification problem. As bankruptcy due to business failure can negatively affect the enterprise as well as the global economy, it is crucial to understand and predict whether a company is showing symptoms of getting bankrupt or not. The problem statement is to develop a prediction model which will predict whether a company can go bankrupt or not. This will help the company to take appropriate decisions.

#### Dataset:

The data is collected from Taiwan Economic Journal for the years 1999 to 2009. Company bankruptcy was defined based on the business regulations of the Taiwan Stock Exchange. The dataset consists of multiple financial ratio columns such as:

- Return on Assets (ROAs)
- Gross Profits
- Operating & Net income and Expenses
- Cash flows
- Taxes
- Growth rate
- Debt
- Turnover, Revenue, Liability, etc.

All the features are normalized in the range 0 to 1.

The target column is “Bankrupt?” (0: No, 1: Yes).

It is a highly imabalanced data.

Source : [https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction](https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction)

#### Data Preparation

1. Oversampled (SMOTE)
2. Undersampled (Bring down the count of majority class data)
3. Resampled (created multiple datasets containing all samples of minority class).



## 정리

