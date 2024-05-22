---
layout: post
title: RAG용 PDF Loader 비교
date: 2024-05-22 22:07 +0900
categories:
  - Deep-Learning
  - LangChain
tags: 
math: true
---

## Intro: 

RAG 성능 향상 방법엔 여러가지 기법이 있지만, 기본적으로 자료에서 Document를 얼마나 잘 가져오느냐가 중요할것이라 판단된다. 특히, Hallucination 확인, 자세한 출처 표기, 그리고 알맞은 image extraction을 위해, 성능이 좋은 PDF Loader은 필수적이다. 따라서, LangChain 라이브러리에 포함된 pdf loader들을 비교해보고자 한다.

## PDF Loader 목록
- PyDFium2Loader



## PyMuPDF
[테디노트 PyMuPDF 개발자 라이브 미팅 유투브](https://www.youtube.com/watch?v=VemLpb1UXRs&t=18s)
- 고객사: OpenAI, Notion, Anthropic
### PyMuPDF4LLM
- PDF to Markdown converter
- 기본적으로 모든 페이지 파싱하지만, subset