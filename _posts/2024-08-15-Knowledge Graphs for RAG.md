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

- Knowledge Graph used: Neo4jGraph


```python
from langchain_community.graphs import Neo4jGraph

kg = Neo4jGraph(
    url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE
)
```


![](https://i.imgur.com/cutLMPA.png)


(Person) - \[ACTED_IN\] → (Movie)


### Node properties

![](https://i.imgur.com/A0EADne.png)


### Edges-Relationships between a Person and a Movie

![](https://i.imgur.com/nqVR5Jg.png)

- enables description of perplex situations when a person acted in AND directed a movie


### Cypher
- Neo4j's query language
- uses pattern matching to find thins inside of the grass

#### Basic
```python
# number of all the nodes
cypher = """
  MATCH (n) 
  RETURN count(n)
  """
```

```python
result = kg.query(cypher)
result
```

	[{'count(n)': 171}]


#### Alias
```python
cypher = """
  MATCH (n) 
  RETURN count(n) AS numberOfNodes
  """
result = kg.query(cypher)
result
```

	[{'numberOfNodes': 171}]

```python
print(f"There are {result[0]['numberOfNodes']} nodes in this graph.")
```

	There are 171 nodes in this graph.


#### Match

```python
cypher = """
  MATCH (n:Movie) 
  RETURN count(n) AS numberOfMovies
  """
kg.query(cypher)
```

	[{'numberOfMovies': 38}]


```python
cypher = """
  MATCH (tom:Person {name:"Tom Hanks"}) 
  RETURN tom
  """
kg.query(cypher)
```
	[{'tom': {'born': 1956, 'name': 'Tom Hanks'}}]
	