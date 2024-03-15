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

### [Company Bankruptcy Prediction](https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction)

  

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


### Oversampling & Undersampling

![](https://i.imgur.com/IXz5Spf.png)


#### Oversampling

- 소수 클래스의 샘플 수를 인위적으로 늘려서 클래스 간의 불균형을 해소하는 방법

- SMOTE (Synthetic Minority Over-sampling Technique): 소수 클래스 데이터 포인트 사이를 보간하여 새로운 데이터 포인트를 생성

##### SMOTE(Synthetic Minority Over-sampling Technique) 개념

- 대표적인 OverSampling 기법
- **낮은 비율 클래스 데이터들의 최근접 이웃을 이용**하여 새로운 데이터를 생성
- 완전히 똑같은 특성을 가진 데이터를 복사하는 것이 아님


근접해 있는 데이터들과 일정한 거리를 떨어진 위치에 데이터를 생성 하는 과정

![](https://blog.kakaocdn.net/dn/GaITt/btqGmTl4AeX/qkrQ3yl4LjsNyDorwyr5Gk/img.png)

출처: https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets

주의 사항:
- [재현율과 정밀도](https://hwi-doc.tistory.com/entry/%EB%AA%A8%EB%8D%B8-%ED%8F%89%EA%B0%80%ED%95%98%EA%B8%B0-%EC%A0%95%ED%99%95%EB%8F%84%EB%A7%8C-%EB%86%92%EC%9C%BC%EB%A9%B4-%EC%A2%8B%EC%9D%80-%EB%AA%A8%EB%8D%B8?category=910648)
	- 양성 데이터가 음성 데이터보다 훨씬 부족한 데이터로 예를 들었을때,
	- 오버 샘플링을 하게 되면 양성으로 예측하는 비율이 높아지기 때문에 정밀도가 감소하게 된다 (반대로 재현율은 증가하게 된다).
	- 따라서 정밀도의 감소율을 낮추고 재현율의 증가율은 높이는 방법에 유의하며 SMOTE 패키지를 사용해야 한다
  
```python
# imbalanced-learn 패키지 
from imlearn.over_sampling import SMOTE 
# 검증 데이터나 테스트 데이터가 아닌 학습데이터에서만 오버샘플링 사용할 것 
smote = SMOTE(random_state=11) 
X_train_over, y_train_over = smote.fit_sample(X_train, y_train)
```
#### Undersampling

- 다수 클래스의 샘플 수를 줄여서 불균형을 해소
- 정보 손실이 발생할 수 있기 때문에 데이터의 양이 많지 않을 때 주의해서 사용해야 한다
- 계산 비용을 줄이고 싶을 때 유용

## 방법론

### Supervised Anomaly Detection

- 주어진 학습 데이터 셋에 정상 sample과 비정상 sample의 Data와 Label이 모두 존재하는 경우
- 다른 방법 대비 **정확도가 높음**
-  비정상 sample을 다양하게 보유할수록 더 높은 성능을 달성 가능

- 문제점:
- 일반적인 산업 현장에서는 정상 sample보다 비정상 sample의 발생 빈도가 현저히 적기 때문에 **Class-Imbalance(불균형)** 문제
- 해결 시도 방안:
- Data Augmentation(증강), Loss function 재설계, Batch Sampling 등 다양한 연구가 수행중

#### 장단점
- 장점: 양/불
- 판정 정확도가 높다
- 단점:
- 비정상 sample을 취득하는데 시간과 비용이 많이 든다
- Class-Imbalance 문제를 해결해야 한다

### Semi-supervised (One-Class) Anomaly Detection

- Class-Imbalance가 매우 심한 경우 정상 sample만 이용해서 모델을 학습
- 핵심 아이디어:
1. 정상 sample들을 둘러싸는 discriminative boundary를 설정
2. boundary를 최대한 좁혀 boundary 밖에 있는 sample들을 모두 비정상으로 간주

 [**One-Class SVM**](http://www.jmlr.org/papers/volume2/manevitz01a/manevitz01a.pdf) 이 One-Class Classification을 사용하는 대표적인 방법론으로 잘 알려져 있으며, 이 아이디어에서 확장해 Deep Learning을 기반으로 One-Class Classification 방법론을 사용하는 [**Deep SVDD**](http://data.bit.uni-bonn.de/publications/ICML2018.pdf) 논문이 잘 알려져 있다

  
  

![Deep SVDD 방법론 모식도](https://i.imgur.com/2xcDa9N.png)

  

- 다양한 시도:
- Energy-based 방법론 [**“Deep structured energy based models for anomaly detection, 2016 
- Deep Autoencoding Gaussian Mixture Model 방법론 [**“Deep autoencoding gaussian mixture model for unsupervised anomaly detection, 2018 ICLR”**](https://sites.cs.ucsb.edu/~bzong/doc/iclr18-dagmm.pdf) 
- Generative Adversarial Network 기반 방법론 [**“Anomaly detection with generative adversarial networks, 2018 arXiv”**](https://arxiv.org/pdf/1809.04758.pdf) 
- Self-Supervised Learning 기반 [**“Deep Anomaly Detection Using Geometric Transformations, 2018 NeurIPS”**](https://papers.nips.cc/paper/8183-deep-anomaly-detection-using-geometric-transformations.pdf)

  

#### 장단점
- 장점:
- 비교적 활발하게 연구가 진행되고 있으며, 정상 sample만 있어도 학습이 가능하다
- 단점:
- Supervised Anomaly Detection 방법론과 비교했을 때 상대적으로 정확도가 떨어진다

  

### Unsupervised Anomaly Detection

-  대부분의 데이터가 정상 sample이라는 가정을 하여 Label 취득 없이 학습을 시키는 방법론

  

#### 방식

- Principal Component Analysis(PCA, 주성분 분석)를 이용하여 차원을 축소하고 복원을 하는 과정을 통해 비정상 sample을 검출

- Neural Network 기반으로는 대표적으로 Autoencoder 기반의 방법론 주로 사용

1. 입력을 code 혹은 latent variable로 압축하는 Encoding

2. 다시 원본과 가깝게 복원해내는 Decoding 과정

- 데이터의 중요한 정보들만 압축적으로 배울 수 있다는 점에서 데이터의 주성분을 배울 수 있는 PCA와 유사한 동작을 한다

  

![autoencoder 기반 unsupervised anomaly detection](https://i.imgur.com/ON4BC4F.png)

  
  

- 정확도가 Supervised Anomaly Detection에 비해 다소 불안정

- 성능 좌우 요소:

- code size (= latent variable의 dimension) 같은 hyper-parameter

- autoencoder에 넣어주는 input과 output의 차이를 어떻게 정의할 것인지(= 어떤 방식으로 difference map을 계산할지)

- loss function

#### 논문

- [**Improving Unsupervised Defect Segmentation by Applying Structural Similarity to Autoencoders**](https://arxiv.org/pdf/1807.02011.pdf)

- [**Deep Autoencoding Models for Unsupervised Anomaly Segmentation in Brain MR Images**](https://arxiv.org/pdf/1804.04488.pdf)

- [**MVTec AD – A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection**](https://www.mvtec.com/fileadmin/Redaktion/mvtec.com/company/research/mvtec_ad.pdf)

  

#### 장단점

- 장점: Labeling 과정이 필요하지 않다.

- 단점: 양/불 판정 정확도가 높지 않고 hyper parameter에 매우 민감하다.

  

![Anomaly Detection 관련 3가지 용어의 분류 방법 정리](https://i.imgur.com/C947qx3.png)

  

## 최신 모델

### Variational Autoencoders (VAEs).

  

### UniTs

- [**Project Page**](https://zitniklab.hms.harvard.edu/projects/UniTS/)

- https://github.com/mims-harvard/UniTS

- [**Paper link**](https://arxiv.org/pdf/2403.00131.pdf)