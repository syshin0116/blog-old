---
layout: post
title: LangGraph
date: 2024-03-06 21:06 +0900
categories:
  - Deep-Learning
  - LangChain
tags: 
math: true
---

## 정보

- Docs: [https://python.langchain.com/docs/langgraph](https://python.langchain.com/docs/langgraph)
- Github: [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- TeddyNote Youtube: [https://www.youtube.com/watch?v=1scMJH93v0M](https://www.youtube.com/watch?v=1scMJH93v0M)


#### LangChain 공식 홈페이지 LangGraph 정의

[LangGraph](https://github.com/langchain-ai/langgraph) is a library for building stateful, multi-actor applications with LLMs, built on top of (and intended to be used with) [LangChain](https://github.com/langchain-ai/langchain). It extends the [LangChain Expression Language](https://python.langchain.com/docs/expression_language/) with the ability to coordinate multiple chains (or actors) across multiple steps of computation in a cyclic manner. It is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The current interface exposed is one inspired by [NetworkX](https://networkx.org/documentation/latest/).

The main use is for adding **cycles** to your LLM application. Crucially, this is NOT a **DAG** framework. If you want to build a DAG, you should just use [LangChain Expression Language](https://python.langchain.com/docs/expression_language/).

Cycles are important for agent-like behaviors, where you call an LLM in a loop, asking it what action to take next.


## 정리

- TeddyNote 유튜브: [LangChain](https://www.youtube.com/hashtag/langchain) 이 만든 [#LangGraph](https://www.youtube.com/hashtag/langgraph) 출시! LangGraph 의 멀티 에이전트 콜라보레이션 찍먹하기
- [샘플 노트북](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/multi-agent-collaboration.ipynb)
### 다중 에이전트 협업(Multi-Agent Collaboration)

- divide-and-conquer 접근법
	- 각 작업이나 도메인에 대해 전문화된 에이전트를 만들고 작업을 올바른 '전문가'에게 라우팅
	- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) 방식에 LangGraph 활용
	- 각 Agent마다 담당하는 분야를 할당(ex. 검색용 Agent, 차트 생성용 Agent, 코드 작성 Agent)

![](https://i.imgur.com/CUNZuok.png)

> 엄연한 로직, flow가 존재함


