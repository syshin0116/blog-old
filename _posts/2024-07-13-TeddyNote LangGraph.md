---
layout: post
title: TeddyNote LangGraph
date: 2024-07-13 16:27 +0900
categories:
  - ETC
  - 세미나
tags: 
math: true
---

## TeddyNote LangGraph 

### LangGraph 개발 단계

1. 문서 검색, 답변 생성
2. 답변을 평가 -> 정보가 부족할 시 웹 검색

![](https://i.imgur.com/yNo87W4.png)


### Conventional RAG의 문제점

- 기본 RAG의 모든 점( chuck size, query, 검색 방법 등등)이 고정되어있다. 유연하지 않다
   - 따라서 모든 단계를 한번에 다 잘해야 함
   - 이전 단계로 되돌아가기 어려움


### LangGraph 제안

![](https://i.imgur.com/ogutiIB.png)

![](https://i.imgur.com/ilY8gVk.png)

![](https://i.imgur.com/0CnfDdc.png)


### LangGraph 
- Node, Edge, State를 통해 LLM을 활용한 워크플로우에 순환(Cycle) 연산 기능을 추가하여 손쉽게 흐름 제어
   - Conditional Edge: 조건부(if문)와 같은 흐름 제어
   - Human in the loop: 필요시 사람이 중간 개입하여 다음 단계를 결정
   - Checkpointer: 과거 실행 과정에 대한 수정 & 리플레이


#### State

![](https://i.imgur.com/pVe0k8T.png)

![](https://i.imgur.com/186KzNJ.png)

- 모든 값을 채울 필요 없음
- 이전 노드에서 가져온 값들을 유지, 필요시 추가 or 덮어쓰기


![](https://i.imgur.com/YaZqBzy.png)

- 평가(4번)에서 BAD가 뜬 경우
   1. 질문 재작성
   2. 문서 재검색(다른 retriever 사용, chuck size 변경, 추가 rag 방법, web 검색 추가 등등)
   3. 답변 재생성(다른 llm사용, temperature값 변경, 프롬프트 조절 등등)

![](https://i.imgur.com/5jd7Uzo.png)

![](https://i.imgur.com/uCufWCk.png)

![](https://i.imgur.com/1Aq9jtG.png)


#### 노드(Node)
> 테디님: 잘 만들어 두면, 프로젝트마다 골라서 뽑아 쓰기 좋을것 같다

![](https://i.imgur.com/Dm4GlEv.png)

#### 엣지(Edge)
- 노드와 노드 연결
- `add_edge("from 노드이름", "to 노드이름")`
![](https://i.imgur.com/5GjhygY.png)


#### 조건부 엣지(Edge)

- `add_contitional_edges("노드이름", 조건부 판단 함수, dict로 다음 단계 결정)`

![](https://i.imgur.com/pf96zBY.png)


#### 시작점 지정(entry point)

![](https://i.imgur.com/wXd2Qq0.png)


#### 체크포인터(memory)

![](https://i.imgur.com/39mFXrP.png)


#### 그래프 시각화

![](https://i.imgur.com/I8ZtjR0.png)


#### 그래프 실행
- Runnable Config에 recursion_limit을 주고 실험하는것을 추천
   - 비용 발생
![](https://i.imgur.com/YzYeFiT.png)



### Self-RAG

- 고정된 RAG 를 사용시 검색에 노이즈 발생, 문서 내 다른 정보 참고 혹은 제대로 된 답변이 나오지 않음
   - 선택적 Retrieval 도입(필요한 만큼만 Retrieve)
   - Retrieval로부터 답변을 도출
   - 도출된 답변과 Retrieval Passage간 관련성 체크

![](https://i.imgur.com/F5xXe0N.png)

![](https://i.imgur.com/4HDcGki.png)


![](https://i.imgur.com/ldabrPK.png)


### Corrective-RAG
- 문제점: RAG의 답변 결과는 검색된 문서의 관련성에 의존적
- 제안: 사용자 입력 쿼리에 대하여 검색된 문서의 품질을 평가


![](https://i.imgur.com/OZo3k1S.png)



