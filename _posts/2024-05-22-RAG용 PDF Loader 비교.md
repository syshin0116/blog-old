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

## PDF Loader 비교 목록
- PyMuPDF
- PyPDFium2Loader

## PyMuPDF
[테디노트 PyMuPDF 개발자 라이브 미팅 유투브](https://www.youtube.com/watch?v=VemLpb1UXRs&t=18s)
[PyMuPDF for LLM&RAG](https://pymupdf.readthedocs.io/en/latest/rag.html)
- 고객사: OpenAI, Notion, Anthropic
- License: 상업목적 사용시 license 구매 필요
- 특징: 
   - C 기반의 MuPDF기반 -> 매우 빠름 (Pdfminer.six 대비 6배 빠른 속도)
![](https://i.imgur.com/AkluzNm.png)




참고:
- https://medium.com/social-impact-analytics/comparing-4-methods-for-pdf-text-extraction-in-python-fd34531034f
- https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf/#using-pymupdf
- https://api.python.langchain.com/en/latest/_modules/langchain_community/document_loaders/pdf.html#PyPDFium2Loader
- https://pypdf.readthedocs.io/en/latest/meta/comparisons.html
- https://pymupdf.readthedocs.io/en/latest/about.html#license-and-copyright