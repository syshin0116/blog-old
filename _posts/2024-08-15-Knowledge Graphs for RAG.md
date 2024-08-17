---
layout: post
title: Knowledge Graphs for RAG
date: 2024-08-15 21:37 +0900
categories:
  - Deep-Learning
  - 기법
tags: 
math: true
---

참고 자료: https://learn.deeplearning.ai/courses/knowledge-graphs-rag/lesson/1/introduction

### What is Knowledge Graph?
A Database that stores information in **nodes** and **relationships**

- provides way to sort and organize data
- emphasizes the relationship between things
- uses graph based structure:
	- nodes: represents entity
	- edges: represents relationship between nodes


![](https://i.imgur.com/v3dXFGn.png)


## Fundamentals

### Nodes and Edges

![](https://i.imgur.com/aqQtqhM.png)

Representation: (Person) - \[Knows] - (Person)

> Nodes are "in" relationship, relation with properties


![](https://i.imgur.com/Kmhm0zd.png)

Representation: (Person) - \[TEACHES] → (Course) ← \[INTRODUCES] - (Person)


![](https://i.imgur.com/bOdx0b4.png)

- Like node, Edges also has key/value structure



**Knowledge Graph Overview:**

- Knowledge Graph: Stores information in nodes and relationships
- Nodes and Relationships: Both can have properties
- Nodes: Can be labeled to group them together
- Relationships: Always have a type and direction


## Querying Knowledge Graphs

