---
layout: post
title: An LLM Compiler for Parallel Function Calling
date: 2025-01-26 19:15 +0900
categories:
  - ETC
  - Paper-Summary
tags: 
math: true
---
- paper: [https://arxiv.org/abs/2312.04511](https://arxiv.org/abs/2312.04511)
- github: [https://github.com/SqueezeAILab/LLMCompiler](https://github.com/SqueezeAILab/LLMCompiler)
- youtube: [https://youtu.be/aoLtTIYAafY?si=9d4O99LWEWpX15Oc](https://youtu.be/aoLtTIYAafY?si=9d4O99LWEWpX15Oc)

## Abstract

#### **Problem**: 
current methods for LLM function calling often require sequential reasoning and acting for each function which can result in **high latency, cost, and sometimes inaccurate behavior**

#### Key Question: 
what is the most effective approach to incorporate multiple function calls?


#### LLM Compiler
- executes functions in parallel to efficiently orchestrate multiple function calls
- consists of three components:
  1. Function Calling Planner: formulates execution plans for function calling
  2. Task Fetching Unit: dispatches function calling tasks
  3. Executor: executes these tasks in parallel

Observation compared to **ReAct**:
- consistent latency speedup of up to 3.7×
- cost savings of up to 6.7×
- accuracy improvement of up to ∼9%



## Background information

- Funciton(Tool) Calling: ability of LLMs to invoke provided functions and use the function outputs to help complete their tasks
- ReAct: method in which LLM calls a function, analyzes the outcomes, and then reasons about the next action, which involves a subsequent function call



### ReAct vs LLM Compiler

![](https://i.imgur.com/MXtRn9V.png)


## Evaluation

| **Evaluation Task**             | **Dataset/Benchmark**                          | **Observations**                                                          | **Compared To**  |
| ------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------- | ---------------- |
| **Embarrassingly Parallel**     | HotpotQA (Yang et al., 2018)                   | - 1.80× speedup<br>- 3.37× cost reduction                                 | ReAct            |
|                                 | Movie Recommendation (Srivastava et al., 2022) | - 3.74× speedup<br>- 6.73× cost reduction                                 | ReAct            |
| **Complex Patterns**            | ParallelQA                                     | - Up to 2.27× speedup<br>- 4.65× cost reduction<br>- 9% improved accuracy | ReAct            |
| **Dynamic Replanning**          | Game of 24 (Yao et al., 2023b)                 | - 2× speedup                                                              | Tree-of-Thoughts |
| **Interactive Decision-Making** | WebShop                                        | - Up to 101.7× speedup<br>- 25.7% improved success rate                   | Baselines        |

### Recent Research in Latency Optimization for LLMs and Comparison

**Model and system-level optimization**
  - Studies focus on optimizing model design and system efficiency
  - Limitation: 
	  - Little attention to application-level optimizations
	  - critical for black-box LLMs where model modifications are restricted

**Skeleton-of-Thought (Ning et al., 2023)**
  - Approach: Parallel decoding via skeleton generation and execution
  - Limitation: Assumes tasks are independent, making it unsuitable for complex problems like coding or math

**OpenAI's parallel function calling**
  - Feature: Simultaneous function call generation to reduce latency
  - Limitation: Only available for proprietary OpenAI models

**ReWOO (Xu et al., 2023)**
  - Separates reasoning, execution, and observation phases to reduce token usage and cost compared to ReAct
  - Limitation: Does not support parallel function calling or dynamic replanning

**LLMCompiler's advancements**
  - Allows parallel function calling to reduce latency and cost
  - Supports dynamic replanning for problems with undetermined execution flows
  - Handles interdependent tasks, enabling broader applicability in complex scenarios
  - Achieves better latency and cost efficiency compared to existing approaches



## Methodology

Query: How much does Microsoft’s market cap need to increase to exceed Apple’s market cap?


![](https://i.imgur.com/xOrVoXe.png)


1. `Function Calling Planner` generates a DAG of tasks with their interdependencies
2. Tasks are then dispatched by the Task Fetching Unit to the Executor in parallel based on their dependencies
3. Task 1 and Task 2 are fetched together for parallel execution of two independent search tasks
4. After each task is performed, the results are forwarded back to the `Task Fetching Unit` to unblock the dependent tasks after replacing their placeholder variables (e.g.)


---


## 1. LLMCompiler의 목적

- LLMCompiler는 에이전트를 위한 컴파일러를 만드는 첫 시도로, 다양한 기능 호출을 효율적으로 처리하는 것을 목표로 함 [10]
- 발표자는 Seun, Sohung Moon, Ryan Tabrizy, Nicholas Lee, Michael Mahoney, Ker 등 여러 연구자들과 협력하여 진행 [11]

## 2. LLM의 기능 호출 발전

- LLM의 기능 호출은 최근 1년간 발전했으며, 특히 **컨텍스트 학습**과 같은 새로운 행동이 등장 [19]
- 예를 들어, LLM에 몇 가지 예시를 제공하면 이를 바탕으로 새로운 질문에 답변 가능 [21]
- 그러나 복잡한 수학 문제 해결이나 개인 데이터베이스 접근에는 한계가 있음 [30]

## 3. 도구 사용의 필요성

- LLM이 복잡한 계산을 수행할 때, 계산기 등의 도구를 사용할 수 있도록 하는 방법이 제안됨 [33]
- LLM이 도구가 필요할 경우 특정 토큰을 출력하여 도구를 호출하도록 유도 [40]
- 이러한 접근 방식은 LLM의 성능을 크게 향상시킴 [46]

## 4. React 프레임워크의 한계

- React 프레임워크에서는 LLM이 도구를 호출할 때 무한 루프에 빠지거나 중간 결과를 잊어버리는 등의 문제가 발생할 수 있음 [64]
- 이를 해결하기 위한 다양한 솔루션이 제안되었으나, 여전히 해결해야 할 과제가 많음 [76]

## 5. LLMCompiler의 설계

- LLMCompiler는 **LLM 플래너, 작업 가져오기 유닛, 실행기**의 세 가지 주요 구성 요소로 이루어짐 [129]
- LLM 플래너는 사용자 입력을 이해하고 이를 여러 작업으로 분해하여 실행 가능하도록 함 [131]
- 사용자는 도구 정의와 예시를 제공하여 LLMCompiler를 구성할 수 있음 [150]

## 6. 평가 및 성과

- LLMCompiler는 **HAAQA, BigBench** 등의 벤치마크를 사용하여 평가됨 [159]
- 기존 React 방법보다 **1.8배~3.7배** 빠른 성능을 보임 [179]
- 정확도 또한 개선되었으며, 비용 절감 효과도 있음 [191]

## 7. 재계획 기능

- LLMCompiler는 **재계획 기능**을 통해 실행 중 발생하는 오류를 처리할 수 있음 [197]
- 예를 들어, 웹에서 아이템을 구매할 때 예상치 못한 결과가 발생하면 재계획이 필요함 [201]

## 8. 미래 방향성

- 기존 컴파일러의 **최적화 기법**을 적용하여 다양한 모델을 효율적으로 사용할 수 있도록 발전할 계획 [367]
- 이를 통해 LLM의 자원 사용을 최적화하고, 복잡한 작업 처리에 기여할 것 [372]

## 9. 결론 및 Q&A

- 발표자는 LLMCompiler의 가능성과 향후 연구 방향을 설명하고 청중의 질문에 답변 [375]
- LLMCompiler는 다양한 응용 프로그램에서 유용하게 활용될 가능성이 큼 [338]