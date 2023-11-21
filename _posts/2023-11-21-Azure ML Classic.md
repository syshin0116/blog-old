---
layout: post
title: Azure ML Classic
date: 2023-11-21 14:58 +0900
categories:
  - SeSAC
  - Computer-Vision
tags: 
math: true
---
## Azure ml classic

- No Coding Tool 이 아닌 Low Coding Tool이라 부른다
- `Python`이나 `R` 코드를 사용할 수 있기 때문

### 접속
1. https://studio.azureml.net/ 접속
2. 회원가입 & 로그인

### Blank Experiments 생성

1. Experiments > Blank Experiment

![](https://i.imgur.com/ZdmzErL.png)

### 데이터 불러오기

1. https://gallery.azure.ai/Experiment/Titanic-1-2

![](https://i.imgur.com/e9ZU1iz.png)

2. Open in Studio(classic) 클릭

> Azure ML Classic에 로그인 되어있어야 한다

![](https://i.imgur.com/JQpcdfL.png)



### 데이터 확인
1. Titanic Dataset 우클릭해서 Visualize 선택
![](https://i.imgur.com/mDCeXBe.png)
![](https://i.imgur.com/bsAI5j7.png)


### Select Columns in Dataset

1. `Select Columns in Dataset` 클릭
2. 우측에 `Launch column selector` 클릭

![](https://i.imgur.com/5PRc9lX.png)
### Edit Metadata

![](https://i.imgur.com/tFwupI5.png)
![](https://i.imgur.com/BcPKYWv.png)
![](https://i.imgur.com/vP97C6Z.png)

### Missing Values Scrubber

![](https://i.imgur.com/hb5AxF4.png)

- `For missing values`: 결측치 처리 방법

### Missing Values Scrubber2

![](https://i.imgur.com/ddlu8vj.png)

- 위에서 한번 결측치 처리를 했음에도 남아있다면 Remove entire row


### Edit Metadata

![](https://i.imgur.com/D4LAMJr.png)


### Split Data


![](https://i.imgur.com/FCdv785.png)


### Train Model


![](https://i.imgur.com/Cb8NCBx.png)


#### 모델 추가
- 좌측 Machine Learning - Iitialize Model - Classification - Two-Class Decision Tree 드래그

![](https://i.imgur.com/S4ZARmf.png)

### Run Model

1. 하단에 `Run` 클릭

![](https://i.imgur.com/iHFweKv.png)


### Score Model


![](https://i.imgur.com/qRra6XT.png)


![](https://i.imgur.com/lRwz7Ww.png)

- `Scored Labels` 선택 후 compare to Survived

![](https://i.imgur.com/dTB5R7G.png)
