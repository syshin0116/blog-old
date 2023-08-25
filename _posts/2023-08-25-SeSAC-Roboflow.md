---
layout: post
title: "[SeSAC]Roboflow"
date: 2023-08-25 09:09 +0900
categories: [SeSAC, 머신러닝 데이터분석]
tags: []
math: true
---

## Roboflow

얀 르쿤(Yann LeCun): 
- Convolutional Neural Network 창시자, 페이스북 FAIR 설립자
- MNIST

> 특이점이 온다: 레이 커즈와일 책


## 딥러닝 영상처리

### AI Project Cycle
1. Problem Scoping
2. Data Acquisition
3. Data Exploration
4. Modeling
5. Evaluation
6. Deployment

YOLO의 가장 큰 장점:
- 빠르다

자율주행에서 YOLO를 쓰지 않는 이유: 
- 정확성이 떨어진다


![](https://i.imgur.com/GebX6VH.png)



Image Classification과 Object Detection의 차이: 
- Image Classification과는 다르게 Object Detection은 물체가 무엇인지에 대한 정보와 함께 위치정보도 제공한다


객체 인식과 객체 인지의 차이
- 객체 인식: 위치 + 라벨
- 객체 인지: 위치

ImageNet - 1000만장이 넘는 이미지에 1000개 class

Label과 Anotate의 차이:
- Label: 라벨(Classification)
- Anotate: 라벨 + 위치정보 (Object Detection)

Train_test_split 함수의 파라메터:
- stratify 

