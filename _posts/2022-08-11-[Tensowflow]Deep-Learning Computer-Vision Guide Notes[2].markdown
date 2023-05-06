---
title: Deep-Learning Computer-Vision Guide Notes[2]
date: 2022-08-11 16:50:23 +0900
categories: [Deep-Learning, Computer-Vision]
tags: [ai, deep learning, computer vision] 
---
# Deep-Learning Computer-Vision Guide Notes[2]


## Object Localization과 Detection의 이해

### Object Localization 개요
#### Object Localization: 하나의 이미지에 하나의 객체


FC Layer: Fully Connected Layer

Label 와 유사하게 Annotation파일을 사용

* Bounding Box의 꼭지점 좌표값을 포함하고 있음
* Yolo의 경우 Bounding Box의 중앙점 좌표값 사용

Bounding Box Regression을 함께 진행
Feature Map에서 특정 특성이 나오면 진행할 Regression을 지정

Object Localization - Bounding box 학습

<br>
<p align="center">
<img width="827" alt="Pasted Graphic 2" src="https://user-images.githubusercontent.com/99532836/184108231-3712ea60-416d-4895-bf35-b3de4aca67f9.png" >
</p>
<br>

* Class Confidence Score : ex) 객체가 Car일 확률이 0.9

Object Detection - 두개 이상의 Object를 검출
Bounding Box만 모델에 넣으면 inference 자체가 어려워짐 (예측하는 것이 어려워짐)

* 따라서 Object가 있을만한 위치를 먼저 찾은 후에 해당 영역의 Object를 예측하는 방법 사용
* Region Proposal: 객체가 있을만한 위치

## Region Proposal(영역 추정)의 이해와 슬라이딩 윈도우와의 비교

원본 이미지 -> Feature Extract Layer(추상화된 Feature Layer가 만들어짐)

### Slide in Window 방식

- Slide in Window 방식:
	- 다양한 형태의 윈도우를 한칸씩 움직이면서 윈도우 내에서의 객체를 찾음 -> Bounding Box 예측
	- 왼쪽 상단에서부터 오른쪽 하단까지
	- 단점: 윈도우 사이즈와 객체 사이즈, 형태에 따라 Detect가 어려울 수 있다, 오래걸림
	1. Opt1: 다양한 형태의 Window를 각각 sliding 시키는 방식 (Window를 변형)
	2. Opt2: Window Scale 은 고정하고 scale 을 변경한 여러 이미지를 사용 (이미지를 변형)
	- Opt1, Opt1를 합쳐서도 사용
	- Object Detection의 초기 기법으로 활용
	- 오브젝트 없는 영역도 무조건 슬라이딩 하여야 하며 여러 형태의 Window와 여러 Scale을 가진 이미지를 스캔하면서 검출해야 하므로 수행 시간이 오래 걸리고 검출 성능이 상대적으로 낮음
	- Region Proposal(영역추정) 기법의 등장으로 활용도는 떨어졌지만 Object Detection 발전을 위한 기술적 토대 제공
		- Region Proposal의 Anchor Box에서 유사한 박싱방식이 사용됨
		- SSD -> + FPN

### 이미지 Scale 조정에 따른 여러 크기의 Object Detection
* Window 가 커서 객체가 Window안에 다 들어가지 않을 수 있다 -> 윈도우 사이즈는 그대로 둔 체로 이미지 사이즈를 줄인다
	* Window 안에 여러 객체가 포함되면 기존 이슈가 동일하게 발생할 가능성이 있다

## Region Proposal(영역 추정) - Selective Search 기법

### Region Proposal(영역 추정) 방식:

<br>
<p align="center">
￼<img width="780" alt="Screen Shot 2022-08-11 at 3 47 23 PM" src="https://user-images.githubusercontent.com/99532836/184108264-3628ecc0-5bfc-40ac-aa69-5745a2ca8f96.png">
</p>
<br>

## Selective Search - Region Proposal의 대표 방법

* 빠른 Detection과 높은 Recall 예측 성능을 동시에 만족하는 알고리즘
* 컬러(Color), 무늬(Texture), 크기(Size), 형태(Shape)에 다라 유사한 Region을 계층적 그루핑 방법으로 계산
* Selective Search는 최초에는 Pixel Intensity 기반판 graph-based segment 기법에 따라 Over Segmentation을 수행


- pixel단위로 masking을 하는데, 비슷한 특성을 가진 pixel끼리 masking 
- Over Segmentation을 먼저 한 다음 후보 Segmentation으로 줄여나감

### Selective Search의 수행 프로세스

1. 개별 Segment된 모든 부부늗ㄹ을 Bounding Box로 만들어서 Region Proposal 리스트로 추가
2. 컬러, 무늬, 크기, 형태에 따라 유ㅏ도가 비슷한 Segment들을 그루핑함
3. 다시 1번 Step Region Proposal 리스트 추가, 2번 Step 유사도가 비슷한 Segment를 그루핑을 계속 반복 하면서 Region Proposal 을 수행


<br>
수행 과정:
<p align="center">
<img width="577" alt="image" src="https://user-images.githubusercontent.com/99532836/184112726-d4dbbbd6-a279-437a-a9a3-fb95ee7d2ccb.png">
</p>
Over Segmentation에서 시작하여 중복되거나 유사도가 높은 그룹들이 서로 그룹화 되가는 과정을 확인해 볼 수 있다
<br>

