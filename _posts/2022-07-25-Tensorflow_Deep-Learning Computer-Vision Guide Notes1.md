---
title: Deep-Learning Computer-Vision Guide Notes[1]
date: 2022-07-25 16:50:23 +0900
categories: [Deep-Learning, Computer-Vision]
tags: [ai, deep-learning, computer-vision]     # TAG names should always be lowercase
---
# Deep-Learning Computer-Vision Guide Notes[1]
[[2022-08-11-_Tensowflow_Deep-Learning Computer-Vision Guide Notes_2_]]

## 1. Object Detection, Segmentation에 대한 깊이 있는 이론 설명
## 2. 실습

### 구현패키지:
	
a) MMDetection
	
b) Ultralytics YOLO V3
	
c) AutoML EfficientDet
		
### 범용 인터페이스 API:

a) OpenCV
	
b) TensorFlow Hub

- Colab, Kaggle Kernel 사용


## Object Detection과 Segmentation 이해

* Object Detection - Deep learning 기반으로 발전
* 2012년에 AlexNet이 PASCAL VOC 대회에서 DeepLearning 기반의 CNN으로 우승하면서 발전이 가속화됨


* Localization / Detection / Segmentation
	* Classification > Localization > Detection > Segmentation

Detect할 대상: Object
	
* 하나의 Object가 하나의 Image에 있는 형태: Localization
* 여러 Object를 bounding box로 Detect: Detection
* Bounding box 가 아닌 정밀하게 Pixel 단위로 detect: Segmentation

2012년 기준으로:

* Traditional Detection Methods > 2012 > Deep Learning based Detection Methods

### Deep Learning based Detection Methods:

One-stage detector

* YOLO(2015), SSD, Retina-Net, EfficientDet

Two-stage detector: object의 대략적인 위치를 잡고 시작

* RCNN
* 실시간 적용이 어려움 (video)

### Object Detection의 주요 구성 요소:

1. Region Proposal 				
	* 영역추정
2. Feature Extraction & FPN & Network Prediction
	* Detection을 위한 Deep Learning 네트웍 구성
3.  IOU, NMS, mAP, Anchor box			
	* Detection을 구성하는 기타 요소

### 일반적인 Object Detection 모델:
- Backbone: ResNet
- Neck: FPN(Feature Pyramid Network)
- Head: classification, bbox regression

### Object Detection의 난제:

* Classification + Regression을 동시에
	- 이미지에서 여러 개의 물체를 classficiation함과 동시에 위치를 찾아야 함
- 다양한 크기와 유형의 오브젝트가 섞여 있음
	- 크기가 서로 다르고, 생김새가 다양한 오브젝트가 섞여 있는 	이미지에서 이들을 Detect함
	- 중요한 Detect 시간
	- Detect 시간이 중요한 실시간 영상 기반에서 Detect해야 하는 요구사항 증대
- 명확하지 않은 이미지
	- 오브젝트 이미지가 명확하지 않은 경우가 많음. 또한 전체 이미지에서 Detect할 오브젝트가 차지하는 비중이 높지 않음(배경이 대부분을 차지하는 경우가 많음)
- 데이터 세트의 부족
	- 훈련 가능한 데이터 세트가 부족(Ms Coco dataset 80개,Google - Open Image 500개) 하며 annotation을 만들어야 하므로 훈련 뎅터 세트를 생성하기가 상대적으로 어려움

## Object Localization 개요
	Object Localization: 하나의 이미지에 하나의 객체
	
![Object Localization](/public/img/Pasted Graphic.png)