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

#### Oversampling

- 소수 클래스의 샘플 수를 인위적으로 늘려서 클래스 간의 불균형을 해소하는 방법 
이를 통해 모델이 소수 클래스를 더 잘 학습할 수 있도록 돕습니다. 가장 널리 알려진 방법 중 하나는 SMOTE (Synthetic Minority Over-sampling Technique)로, 소수 클래스 데이터 포인트 사이를 보간하여 새로운 데이터 포인트를 생성합니다.

#### Undersampling

반면, Undersampling은 다수 클래스의 샘플 수를 줄여서 불균형을 해소합니다. 이 방법은 데이터의 양이 많지 않을 때 주의해서 사용해야 합니다. 정보 손실이 발생할 수 있기 때문입니다. 하지만, 계산 비용을 줄이고 싶을 때 유용할 수 있습니다.

두 기법은 각각 장단점이 있으며, 문제의 특성과 사용할 수 있는 데이터의 양, 모델의 성능 등을 고려하여 적절히 선택하여 사용해야 합니다.