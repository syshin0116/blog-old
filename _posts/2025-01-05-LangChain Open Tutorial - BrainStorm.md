---
layout: post
title: "[LangChain Open Tutorial]Week2-BrainStorm"
date: 2025-01-05 16:11 +0900
categories:
  - Project
  - LangChain Open Tutorial
tags: 
math: true
---

## 신규 튜토리얼 개발자 1팀

### 제출 항목:

- 기능명: 기능의 제목 또는 이름 
- 기능 설명: 목적과 핵심 내용 2~3줄 요약 
- 필요 데이터: 기능 구현에 필요한 데이터 형식이나 예시. (모든 활용 데이터는 영어로 작성되어야 합니다.)




## BrainStorm

### GraphRAG
- Neo4j 활용 그래프 레그

#### Datasets
- Harry Potter 
- Movies
- 맛집


- [LangChain: Neo4j](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)
- [Neo4j: Turn a Harry Potter Book into a Knowledge Graph](https://neo4j.com/developer-blog/turn-a-harry-potter-book-into-a-knowledge-graph/)
- [Neo4j: Example Datasets](https://neo4j.com/docs/getting-started/appendix/example-data/)


제가 알기로 LangGraph 챕터가 이미 있어서, 새로 제안하는 아이디어가 어디에 들어가야 할지 애매한 부분이 있다고 생각합니다.

제가 생각하는 아이디어는 short-term과 long-term 메모리 기능인데, 이 기능을 LangGraph로 구현하다 보니 자연스럽게 LangGraph 챕터 아래로 포함시키는 게 맞는지 고민됩니다.

이런 주제여도 괜찮은지, 아니면 따로 새로운 섹션으로 구성하는 것이 더 적절할지 검토 부탁드립니다.

---
기능명: Short-term, Long-term Memory
기능 설명:
- Short-term Memory와 Long-term Memory로 메모리를 나눠서 관리하는 기능

필요 데이터:
	•	대화 이력
	•	사용자/세션 메타데이터

---

감사합니다!




기능 세부 사항:
	1.	Short-term Memory
	•	대화 이력을 관리하기 위해 메시지 리스트를 LangGraph 상태로 저장
	•	불필요한 오래된 메시지를 제거하거나 대화 요약 생성 가능
	2.	Long-term Memory
	•	장기적으로 저장할 사실, 경험, 프로파일 데이터를 커스텀 네임스페이스에 저장
	•	LangGraph Store를 통해 메모리 검색 및 유사도 기반 조회


기능명: Short-term, Long-term Memory 기능 설명:

- Short-term Memory와 Long-term Memory로 메모리를 나눠서 관리하는 기능

필요 데이터: • 대화 이력 (메시지 리스트) • 사용자/세션 메타데이터(사용자 ID, 스레드 ID, 네임스페이스 등)



### Table of Contents
```

- [Overview](#overview)
    - [What is Memory?](#what-is-memory)
    - [Short-term vs Long-term Memory](#short-term-vs-long-term-memory)
- [Environment Setup](#environment-setup)
    - [Installing Dependencies](#installing-dependencies)
    - [Database Configuration](#database-configuration)
- [Short-term Memory](#short-term-memory)
    - [Using LangGraph](#using-langgraph)
        - [ConversationBufferMemory](#conversationbuffermemory)
        - [Checkpointer](#checkpointer)
    - [Without LangGraph](#without-langgraph)
        - [Manual Buffer Management](#manual-buffer-management)
- [Long-term Memory](#long-term-memory)
    - [Using LangGraph](#using-langgraph-long-term-memory)
        - [Summarizing Conversations](#summarizing-conversations)
        - [Storing Key Information](#storing-key-information)
    - [Without LangGraph](#without-langgraph-long-term-memory)
        - [Custom Summarization Logic](#custom-summarization-logic)
        - [Manual Key-Value Storage](#manual-key-value-storage)
- [Combining Short-term and Long-term Memory](#combining-short-term-and-long-term-memory)
    - [Using LangGraph](#combining-memory-with-langgraph)
    - [Without LangGraph](#combining-memory-without-langgraph)
- [Personalization Examples](#personalization-examples)
    - [Adapting to User Preferences](#adapting-to-user-preferences)
    - [Automating Repetitive Queries](#automating-repetitive-queries)
- [Tips and Best Practices](#tips-and-best-practices)
- [Complete Code Examples](#complete-code-examples)

```

### Overview

In modern AI systems, **memory management** plays a critical role in creating personalized and efficient user experiences. Imagine interacting with an AI that remembers nothing about your previous conversations—it would be frustrating to repeat the same information every time! To address this, memory management systems are designed to handle and organize information effectively.

This guide focuses on managing **Short-term** and **Long-term Memory** for conversational AI, specifically for building personalized chatbots. We will explore two implementation paths:

1. **Using LangGraph**: A structured and feature-rich framework for managing AI memory.
2. **Without LangGraph**: A more manual, flexible approach for situations where LangGraph is unavailable.

---

#### What is Memory?

Memory in AI refers to the ability to **store, retrieve, and use information** during interactions. In conversational systems, memory can enhance user experience by:

- **Adapting to user preferences**
- **Handling repetitive queries automatically**
- **Providing continuity across sessions**

---

#### Short-term vs Long-term Memory

|**Type**|**Scope**|**Purpose**|**Example**|
|---|---|---|---|
|**Short-term Memory**|Single conversational thread|Keeps track of recent interactions to provide immediate context|Remembering the last few messages in a chat|
|**Long-term Memory**|Shared across multiple threads and sessions|Stores critical or summarized information to maintain continuity across conversations|Storing user preferences, important facts, or conversation summaries|

- **Short-term Memory**: Ideal for maintaining the flow within a single conversation, like tracking the most recent messages.
- **Long-term Memory**: Useful for creating personalized experiences by recalling past interactions, preferences, or key facts over time.
