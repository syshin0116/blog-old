---
layout: post
title: Transformers
date: 2023-11-30 16:08 +0900
categories:
  - SeSAC
  - NLP
tags: 
math: true
---

## Intro: 
### Attention Function

- Q = Query: t 시점의 디코더 셀에서의 은닉 상태
	- 현재 처리하고 있는 단어나 문장 부분
- K = Key: 모든 시점의 인코더 셀의 은닉 상태들
	- 비교 대상이 되는 데이터 세트에서의 요소들
- V = Values : 모든 시점의 인코더 셀의 은닉 상태들
	- 각 Key에 연관된 출력값


![](https://i.imgur.com/GFzEHdt.png)

#### 예시

'나는 학교에 간다'를 영어로 번역한다면

- Key : 번역 모델이 학습한 데이터에서 '나는 학교에 간다'와 유사한 구조나 의미를 가진 요소들
- Query: '나는 학교에 간다'라는 문장의 각 단어
- Value: '나는 학교에 간다'에 해당하는 영어 문장 구조의 요소들이 Value

- Attention Function은 이 세 요소를 사용하여 입력된 Query와 가장 관련이 높은 정보를 Key-Value 쌍에서 찾아냄. 
- 이 과정을 통해, 모델은 '나는 학교에 간다'라는 문장의 각 단어나 구문이 영어로 어떻게 번역되어야 할지를 학습한 데이터를 기반으로 결정

예를 들어, '나는'이라는 단어(Query)에 대해, 모델은 학습 데이터에서 이와 관련된 Key-Value 쌍을 찾아 'I'(Value)로 번역한다. 이러한 과정이 전체 문장에 걸쳐 이루어지며, 최종적으로 '나는 학교에 간다'는 'I go to school'로 변환된다.

이 과정에서 중요한 것은 모델이 각 단어의 맥락을 이해하고, 문장 전체의 의미를 유지하면서 적절한 번역을 찾아내는 것이다.


### Seq to Seq 의 문제점

- RNN을 사용했기 때문에 문장이 길어질수록 **기울기 소실 문제**가 발생. 이를 LSTM으로 보정하지만 완벽히 방지할 수 있는 것은 아님
- **인코더 부분에서 입력 시퀀스를 고정된 크기의 vector로 만들기 때문에 정보를 압축하는 과정에서 손실**이 발생. 
- 이러한 문제는 입력 시퀀스가 클수록 성능을 많이 저하시킴

Seq to Seq 논문: [https://proceedings.neurips.cc/paper_files/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf](https://proceedings.neurips.cc/paper_files/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf)


### Transformers

![](https://i.imgur.com/L7sDZke.png)


- Encoder의 입력: 문장 전체(논문에서 512 element, input length: 512)
- Decoder로 전달시: 단어 하나씩



![](https://i.imgur.com/iObb6zu.png)


#### Teacher Forcing in Transformers

- **정의**: 학습 중 모델 예측 대신 실제 정답 토큰 사용. 이전 정답 토큰을 다음 입력으로 제공.
- **목적**: 모델이 정확한 시퀀스 빠르게 학습하도록 도움. 오류 누적 방지.
- **Transformers에서의 역할**: 디코더 학습 중 중요. 정답 단어를 입력으로 사용해 다음 단어 예측 향상.
- **장단점**: 
    - 장점: 학습 속도와 효율성 향상.
    - 단점: 과도한 의존 시 실제 운영 환경에서 자체 예측 능력 부족 가능성.


### Attention


![](https://i.imgur.com/pZQCxHn.png)


#### Encoder Self-Attention
- 

![](https://i.imgur.com/61Oa9Rh.png)


