---
layout: post
title: "[Modular RAG] Short Term, Long Term Memory"
date: 2024-12-22 16:52 +0900
categories:
  - Project
  - Modular RAG
tags: 
math: true
---

## Intro
Memory 기능을 구현하는데 어떻게 하면 챗봇이 사람처럼 기억을 할 수 있을까, 어떻게 구현하면 가장 도움이 될까 고민했다. 고민 결과, 각 채팅방에 중요 정보는 Long Term memory로, 최신 정보는 Shot Term memory로 구현하고자 한다.

## 정보
### 기본 Memory의 유형

#### 단기 기억 (Short-term memory)

- 하나의 대화 스레드 내에서 기억을 유지
- 대화 이력을 기반으로 에이전트의 상태를 관리
- 대화가 길어지면 메모리의 효율성을 유지하기 위해 메시지 리스트를 관리하거나 요약

#### 장기 기억 (Long-term memory)

- 여러 대화 스레드에서 정보를 공유하며, 스레드 간 경계를 넘어 기억할 수 있다
- 사용자, 조직, 또는 특정 문맥(namespace)을 기반으로 기억을 저장하며, JSON 문서 형태로 관리

### 심리학적 Memory 유형
#### Semantic Memory

- Vectorstore에서 주로 사용하는 Semantic search와 헷갈려 하기 쉽지만 엄연히 다른 용어다.
- Semactic Memory는 심리학에서 기반한 기억 저장 방법으로 사용자에 대한 사실 및 지식을 저장한다

![](https://i.imgur.com/56d6RXa.png)



## 구현 방법

우선, 공부를 하면서 구현을 해야하는 상황이기 때문에, Short Term Memory를 Redis로 먼저 구현하고, 공부하면서 차차 발전해나갈 생각이다.




## 출처
- [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)
- [https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put)
- [https://langchain-ai.github.io/langgraph/concepts/persistence/#basic-usage](https://langchain-ai.github.io/langgraph/concepts/persistence/#basic-usage)
- [How to add summary of the conversation history](https://langchain-ai.github.io/langgraph/how-tos/memory/add-summary-conversation-history/)


- [How to create a custom checkpointer using Redis](https://langchain-ai.github.io/langgraph/how-tos/persistence_redis/#how-to-create-a-custom-checkpointer-using-redis "Permanent link")
- 