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