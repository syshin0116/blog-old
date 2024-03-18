---
layout: post
title: Imbalanced Data Prediction(Anomaly Detection)
date: 2024-03-18 21:07 +0900
categories:
  - Deep-Learning
  - 기법
tags: 
math: true
---

# 이상치 탐지 모델 성능 비교

## 차원 축소 및 클러스터링(Dimension Reduction and Clustering)

## 모델 성능 비교 평가
### 지도학습 분류 모델(Supervised Classification Model)



평가 방식

- PyCaret 모델 테스트 후 Top 3모델 선정

- Stratified K Fold: 5 교차검증 평가 점수

  

평가 모델 리스트

1. Random Forest Classifier

2. Extra Trees Classifier

3. Extreme Gradient Boosting

4. CatBoost Classifier

5. Linear Discriminant Analysis

6. Logistic Regression

7. Ada Boost Classifier

8. Decision Tree Classifier

9. Gradient Boosting Classifier

10. Ridge Classifier

11. K Neighbors Classifier

12. Dummy Classifier

13. SVM - Linear Kernel

14. Light Gradient Boosting Machine

15. Naive Bayes

16. Quadratic Discriminant Analysis

#### CatBoost - Base vs UnderSampling vs OverSampling 비교

PyCaret에서 가장 성능이 좋았던 CatBoost 모델로 Sampling 비교
### 비지도학습 이상 탐지 모델(UnSupervised Outlier Detection Models)

![Scaled minmax threshold estimation](https://i.imgur.com/JlLa3Ms.png)

### PyOD

### DeepOD

### PyThresh

