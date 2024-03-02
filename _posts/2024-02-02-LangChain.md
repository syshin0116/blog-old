---
layout: post
title: LangChain
date: 2024-02-02 16:20 +0900
categories:
  - ETC
  - Tech
tags: 
math: true
---

## Intro: 

랭체인 공부하고자 랭체인 docs를 보다가 생각보다 양이 많아서, 처음부터 뛰어들기 보다 일단 따라해볼 유튜브나 블로그를 경험해본 후에 official documentation을 정독해 보려 한다. 입문용으로 괜찮아 보이는 유툽을 찾아 따라해보려 한다. 

유붑 link: ![https://www.youtube.com/watch?v=aWKrL4z5H6w](https://www.youtube.com/watch?v=aWKrL4z5H6w)



tags: Streamlit, OpenAI, Lamma2, Gemini Pro


Agenda: Practical Oriented
1. Environment Set up Open AI API Key
2. Building simpoe application with
	- LLM's -- LLM's Amd Chatmodels
	- PRomt Templates
	- Output Parser(PromptTemplate + LLM + OutputParser)


requirements.txt에 ipykernel을 추가하지 않는 이유:
	개발 단계에서만 필요하지 deploy시엔 필요하지 않음


### PDF Query with Langchain and Cassandra DB
### Apache Cassandra(Astra DB)
- open source No-SQL database 
- scalability and high availability

#### DATAX
- tool used to create Cassandra DB


#### Vector Search
- enhances machine learning models by allowing similarity comparisons of embeddings
- a capability of Astra DB



## Agenda(Generative AI)

1. About LLama 2
2. Research Paper of LLama 2
3. Apply and download the llama2 model
4. Huggingface
5. End to End Project(Blog Generation LLM App)


### LLama2


![](https://i.imgur.com/S4Ysuim.png)


#### research paper:

https://arxiv.org/pdf/2307.09288.pdf

- Training Details
	- Adopted most pretraining settings and model architecture from Lamma 1
	- Standard transformer architecture
	- pre-normalization using RMSNorm
	- SwiGLU activation function
	- Hyperparameters
		- AdamW optimizer
		- cosine learning rate schedule, warmup 2000 steps
		- decay final learning rate down to 10% of peark learning rate
		- weight decay of 0.1
		- gradient clipping of 1.0

- Comparison to Lamma1: 
	- increased context length
	- GQA: grouped-query attention

![](https://i.imgur.com/WmosUsb.png)


- Training Hardware & Carbon Footprint
	- Meta's Research Super Cluster & internal production clusters
		- **NVIDIA A100**s for both clusters

![](https://i.imgur.com/wquoJ3D.png)


- Fine-tuning
	- instruction tuning & RLHF(Reinforced Learning and Human Feedback)
	- Supervised Fine-Tuning(SFT)

![](https://i.imgur.com/uFChR4F.png)


- Reward Modeling



### Blog Generation


- langchain.llms.CTransformers doc
	- https://python.langchain.com/docs/integrations/providers/ctransformers

![](https://i.imgur.com/yIlHym2.png)

![](https://i.imgur.com/ogrxVs9.png)


```python

import streamlit as st

from langchain.prompts import PromptTemplate

from langchain_community.llms import CTransformers

  

## Function to get response from Llama 2 model

  

### Llama2

llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',

model_type='llama',

config={'max_new_tokens':256,

'temperature':0.01})

  

print("llm called")

print(llm.invoke("what is the capital of USA?"))

def getLlama2Response(llm, input_text, no_words, blog_style):

## Prompt Template

print(f'getLlama2Response called: {llm}, {input_text}, {no_words}, {blog_style}')

template="""

Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.

"""

  

prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],

template=template)

## Generate the response from LLama 2 model

response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))

print(response)

return response

  

st.set_page_config(

page_title="Generate Blogs",

page_icon='🤖',

layout='centered',

initial_sidebar_state='collapsed'

)

  

st.header("Generate Blogs")

  

input_text= st.text_input("Enter the Blog Topic")

  

## create two columns for additional fields

  
  

col1, col2 = st.columns([5, 5])

  

with col1:

no_words = st.text_input('No. of words')

  

with col2:

blog_style = st.selectbox('Writing the blog for',

('Researchers', 'Data Scientist', 'Common People'), index=0)

  

submit = st.button("Generate")

  

## Final response

if submit:

st.write(getLlama2Response(llm, input_text, no_words, blog_style))
```



### LLM APPS

1. Load pdf
2. Convert to text chunks
3. Use OpenAI Embeddings to convert to vectors
4. Store vectors to search DB(Pincecone)
5. When User Queries inputs, apply similiary search to get result


![](https://i.imgur.com/V0cMx9u.png)


![](https://i.imgur.com/pSEh6nC.png)
#### Pinecone이란?

- **관리형 벡터 검색 서비스**: 머신러닝 모델이 만들어낸 고차원 벡터를 저장, 벡터 간의 유사성을 기반으로 검색할 수 있음
- **고성능 & 유사성 검색 지원**: 수백만 벡터를 몇 밀리초 안에 검색. 유클리드, 코사인 유사도 등 다양한 측정 기준 제공
- **확장성**: 클라우드 기반으로 사용량에 따라 자동 스케일링
- **보안 강화**: 데이터 보호 및 프라이버시에 초점
- **간편한 API**: 쉽게 벡터 검색 기능을 앱에 통합할 수 있는 사용자 친화적 API

#### 사용 사례

- **자연어 처리**: 문서, 질문-답변, 기사 등의 유사성 검색에 활용
- **이미지 인식 및 검색**: 이미지를 벡터로 변환해 유사 이미지 검색 가능
- **추천 시스템**: 사용자 선호도나 행동을 벡터로 표현해 개인화된 추천 생성


## LangChain for LLM Application Development

https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/

### Components

Models
- LLMs: 20+ integrations
- Chat Models
- Text Embedding Models: 10+ integrations

Prompts
- Prompt Templates
- Output Parsers: 5+ implementations
- Retry/fixing logic
- Example Selectors: 5+ implementations

Indexes
- Document Loaders: 50+ implementations
- Text Splitters: 10+ implementations
- Vector stores: 10+ integrations
- Retrievers: 5+ integrations/implementations


