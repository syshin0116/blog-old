---
layout: post
title: "[LangGraph]Web-Search Research"
date: 2025-01-18 12:57 +0900
categories:
  - Project
  - LangChain Open Tutorial
tags: 
math: true
---


## Research

- [Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models](https://arxiv.org/abs/2310.04406)
- [Building (and Breaking) WebLangChain](https://blog.langchain.dev/weblangchain/)
- [Plan-and-Execute Agents](https://blog.langchain.dev/planning-agents/)


### Notebooks
- [Reasoning without Observation](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rewoo/rewoo.ipynb)
- [LLMCompiler](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/llm-compiler/LLMCompiler.ipynb)
- [Plan-and-Execute](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb)



# Plan-and-Execute Agents

- LLM과 외부 툴(API, DB, 검색엔진 등)을 연결해 문제 해결 또는 작업 수행
- 전형적인 에이전트 흐름
    - 액션 제안: LLM이 사용자에게 직접 답변할지, 도구를 호출할지 결정
    - 액션 실행: 실제 코드로 툴 호출
    - 결과 관찰: 응답을 바탕으로 추가 액션 또는 최종 응답 결정
- ReAct 에이전트
    - 매 단계마다 LLM이 “Thought → Act → Observation”을 반복
    - 단순하지만, 도구 호출 때마다 LLM을 불러야 하므로 비용과 시간 면에서 비효율적

> ReAct는 개념적으로 이해하기 쉽지만, 멀티 스텝 작업에서 비용이 급등할 수 있음  
> 예를 들어 10번의 툴 사용이 필요한 경우, 10번 모두 대형 모델을 호출하게 됨

---

## Plan-And-Execute

![](https://blog.langchain.dev/content/images/2024/02/plan-and-execute.png)

- Wang 등의 Plan-and-Solve Prompting, BabyAGI에서 영감을 받은 구조
- 동작 방식
    - Planner가 전체 작업에 대한 여러 단계를 미리 계획
    - Executor가 각 단계별로 툴을 순차적으로 호출해 실행
    - 필요 시 재계획(Re-planning)을 통해 작업 보강
- 장점
    - Planner(LLM)를 매번 불러올 필요 없이, 한 번 계획 세운 뒤 단계별 툴 사용
    - 작업 단계를 명시적으로 계획하기 때문에 복잡한 문제에도 유리
- 단점
    - 순차 실행으로 인해 각 단계가 독립적 병렬 실행을 하긴 어려움

> 예를 들어 “맛집 리스트를 뽑고, 해당 맛집들의 위치를 지도 API로 조회한 뒤, 가장 가까운 지하철역까지의 거리를 계산” 같은 경우  
> 한 번에 전체 플랜을 짜두면, 반복적으로 대형 모델을 호출할 필요 없이 순차적으로 작업을 처리할 수 있음

---

## ReWOO (Reasoning Without Observations)

![](https://blog.langchain.dev/content/images/2024/02/rewoo.png)

- Xu 등이 제안한 방식으로, 변수를 통한 참조를 지원
- Planner가 작업 계획(Plan)과 실행(E#)을 한 번에 모두 제시
- 예시
    - Plan: #E1 작업에서 얻은 결과를 #E2가 참조하도록 계획
    - E1: “Search(‘현재 슈퍼볼에 출전하는 팀 정보’)”
    - E2: “LLM(‘#E1의 결과 중 첫 번째 팀의 쿼터백은 누구인가?’)”
- 구조
    - Planner: 전체 단계 및 변수(#E1, #E2 등)를 명시
    - Worker: 각 단계 실행 후 결과를 변수에 할당
    - Solver: 최종적으로 모든 결과를 취합해 사용자에게 답변
- 장점
    - 복잡한 의존 관계를 Planner가 명확히 표현 가능
    - 각 실행 스텝은 필요한 정보만 참조
- 단점
    - 순차 실행이므로 작업이 많으면 지연 시간이 길어질 수 있음

> ReWOO는 중간 결과를 변수로 저장해두고, 후속 스텝에서 그대로 활용하기 때문에 로직이 깔끔해짐  
> 마치 프로그래밍에서 함수의 리턴 값을 받아 쓰듯이, 에이전트 내에서 데이터를 자연스럽게 흘려보낼 수 있음

---

## LLMCompiler

![](https://blog.langchain.dev/content/images/2024/02/llm-compiler-1.png)

- Kim 등이 제안한 고속 실행 지향 에이전트 구조
- 구성 요소
    - Planner
        - DAG(Directed Acyclic Graph) 형태의 태스크를 스트리밍으로 생성
    - Task Fetching Unit
        - Planner에서 나오는 작업 목록을 받아, 종속성이 충족되는 즉시 실행
        - 병렬 실행 지원
    - Joiner
        - 전체 작업 결과를 모은 뒤 최종 답변을 생성할지, 아니면 재계획할지 결정
- 특징
    - 작업을 스트리밍 처리해 Planner의 계획이 끝나기 전에 일부 태스크를 실행 가능
    - 종속성이 없는 태스크들은 동시에 실행하여 처리 속도 향상
    - 최종적으로 대형 모델을 적게 호출하면서도 빠른 응답 제공

> DAG 방식으로 병렬 처리를 지원한다는 점은 대규모 데이터 파이프라인 설계와 유사함  
> 예를 들어 서로 의존하지 않는 API 호출들을 한 번에 처리하면, 대기 시간을 크게 줄일 수 있음


### DAG 란?
**DAG (Directed Acyclic Graph)**: 컴퓨터 과학과 데이터 처리에서 자주 사용되는 그래프 구조

#### **DAG의 구성 요소**

- **Directed (유향)**
    
    - 그래프의 모든 간선(edge)은 방향성이 있습니다
    - 예를 들어, A → B는 A에서 B로만 갈 수 있음을 의미합니다
- **Acyclic (비순환)**
    
    - 사이클이 존재하지 않습니다
    - 즉, 그래프 내에서 한 노드에서 시작해 다시 자신으로 돌아오는 경로가 없습니다
- **Graph (그래프)**
    
    - 노드(node)와 간선(edge)로 구성됩니다
    - 노드는 데이터나 작업을 표현하고, 간선은 노드 간의 관계를 나타냅니다

#### **DAG의 활용 사례**

1. **작업 스케줄링**
    
    - 복잡한 작업을 여러 단계로 나눠 실행할 때 사용
    - 예: 빌드 시스템(컴파일러), 워크플로우 자동화 도구 (Apache Airflow, Prefect)
2. **데이터 처리**
    
    - 데이터 흐름을 정의하는 데 사용
    - 예: 데이터 파이프라인 (ETL 작업)
3. **버전 관리**
    
    - Git의 버전 히스토리는 DAG로 표현
    - 브랜치와 병합이 방향성과 비순환성을 갖는 구조를 이룸
4. **의존성 관리**
    
    - 프로젝트의 종속성을 추적하고 처리 순서를 결정
    - 예: Python 패키지 설치 시 종속 관계를 DAG로 표현

---

## 간단 비교 표

|에이전트 구조|실행 방식|병렬 처리|변수 활용|주요 장점|
|---|---|---|---|---|
|Plan-and-Execute|순차적|거의 불가|제한적|단순 구현, 비용 절감|
|ReWOO|순차적|불가|가능|작업 간 의존 관계 명시적 표현|
|LLMCompiler|병렬 가능|가능|가능|빠른 실행, 리소스 효율 극대화|

---

## 결론

- Plan-and-Execute 계열 에이전트는 “계획(Planner)과 실행(Executor)을 분리”해 멀티 스텝 작업을 효율적으로 처리
- 여러 툴 또는 API를 잇달아 호출해야 하는 복잡한 환경에서 시간을 단축하고 비용을 절약할 수 있음
- 작업을 명확히 정의하고 분할하므로 결과 품질도 향상 가능
- 순차 실행 구조(Plan-and-Execute, ReWOO)와 병렬 실행 구조(LLMCompiler)를 요구사항에 맞추어 선택하면 됨

> 만약 서비스에서 동시에 여러 API를 불러야 한다면 LLMCompiler 구조가 가장 유리할 수 있음  
> 하지만 구현 복잡도가 높을 수 있으므로, 초기에는 Plan-and-Execute 스타일로 시작해보는 것도 좋은 접근임