---
layout: post
title: LLM Chain Chatbot + RAG
date: 2024-04-11 23:34 +0900
categories:
  - Deep-Learning
  - NLP
tags: 
math: true
---

https://api.python.langchain.com/en/latest/chains/langchain.chains.conversational_retrieval.base.ConversationalRetrievalChain.html

## ConversationalRetrievalChain

Chain for having a conversation based on retrieved documents.

args:
- chat history(list of messages)
- new question

returns:
- answer to question


  
## ConversationalRetrievalChain의 중요성

대화형 시스템에서 사용자 질문에 대한 정확하고 신속한 응답은 필수적이다. `ConversationalRetrievalChain`은 이러한 요구를 충족시키기 위해 개발된 핵심 컴포넌트로, 복잡한 자연어 처리 알고리즘과 데이터 검색 기술을 통합하여 사용자 질문에 가장 관련성 높은 정보를 제공한다. 이 체인은 다양한 소스에서 데이터를 동적으로 추출하고 분석하여, 빠르고 정확한 대답을 가능하게 한다

### 기능 및 구조

`ConversationalRetrievalChain`은 다음과 같은 여러 구성 요소로 이루어져 있습니다:

1. **질문 이해**: 사용자의 질문을 분석하고 이해하는 첫 단계로, NLP 기술을 활용하여 질문의 핵심 키워드와 의도를 파악
2. **정보 검색**: 분석된 키워드와 의도를 바탕으로 데이터베이스나 인터넷과 같은 다양한 정보 소스에서 관련 정보를 검색
3. **정보 가공 및 최적화**: 검색된 정보를 사용자가 이해하기 쉬운 형태로 가공하며, 불필요한 정보를 제거하고 중요한 정보를 강조
4. **응답 생성**: 최종적으로 가공된 정보를 바탕으로 사용자에게 응답을 제공합니다. 이 과정에서도 자연어 생성 기술을 활용하여 자연스러운 대화형 응답을 만들어낸다.

### 설정 및 사용 방법

1. **환경 설정**: 필요한 라이브러리와 API 키를 설치 및 설정
2. **데이터 소스 연결**: 정보 검색을 위한 데이터 소스와의 연결을 구성한다. 이는 데이터베이스 연결 문자열이나 API 엔드포인트를 포함할 수 있다.
3. **파라미터 설정**: 검색 정확도, 응답 속도, 로깅 레벨 등 다양한 파라미터를 사용자의 요구에 맞게 설정한다.

### 사용 예시

```python
from langchain.chains import (
    StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
)
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI

combine_docs_chain = StuffDocumentsChain(...)
vectorstore = ...
retriever = vectorstore.as_retriever()

# This controls how the standalone question is generated.
# Should take `chat_history` and `question` as input variables.
template = (
    "Combine the chat history and follow up question into "
    "a standalone question. Chat History: {chat_history}"
    "Follow up question: {question}"
)
prompt = PromptTemplate.from_template(template)
llm = OpenAI()
question_generator_chain = LLMChain(llm=llm, prompt=prompt)
chain = ConversationalRetrievalChain(
    combine_docs_chain=combine_docs_chain,
    retriever=retriever,
    question_generator=question_generator_chain,
)
```