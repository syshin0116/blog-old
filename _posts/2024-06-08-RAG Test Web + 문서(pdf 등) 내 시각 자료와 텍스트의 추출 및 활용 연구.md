---
layout: post
title: RAG Test Web + 문서(pdf 등) 내 시각 자료와 텍스트의 추출 및 활용 연구
date: 2024-06-08 22:43 +0900
categories:
  - 연구
  - DevDay
tags: 
math: true
---



# 연구
## 문서(pdf 등) 내 시각 자료와 텍스트의 추출 및 활용


  

# Multi-Modal RAG

  

### 배경:

- GPT-4V, GPT-4o와 같은 다중 모달 LLM 등장

- RAG에서 text뿐만 아니라 image도 함께 활용하는 방안

  

### Why Text Extraction is hard

  

Extracting text from a PDF can be pretty tricky. In several cases there is no clear answer what the expected result should look like:

  

1. **Paragraphs**: Should the text of a paragraph have line breaks at the same places where the original PDF had them or should it rather be one block of text?

2. **Page numbers**: Should they be included in the extract?

3. **Headers and Footers**: Similar to page numbers - should they be extracted?

4. **Outlines**: Should outlines be extracted at all?

5. **Formatting**: If text is **bold** or _italic_, should it be included in the output?

6. **Tables**: Should the text extraction skip tables? Should it extract just the text? Should the borders be shown in some Markdown-like way or should the structure be present e.g. as an HTML table? How would you deal with merged cells?

7. **Captions**: Should image and table captions be included?

8. **Ligatures**: The Unicode symbol [U+FB00](https://www.compart.com/de/unicode/U+FB00) is a single symbol ﬀ for two lowercase letters ‘f’. Should that be parsed as the Unicode symbol ‘ﬀ’ or as two ASCII symbols ‘ff’?

9. **SVG images**: Should the text parts be extracted?

10. **Mathematical Formulas**: Should they be extracted? Formulas have indices, and nested fractions.

11. **Whitespace characters**: How many new lines should be extracted for 3cm of vertical whitespace? How many spaces should be extracted if there is 3cm of horizontal whitespace? When would you extract tabs and when spaces?

12. **Footnotes**: When the text of multiple pages is extracted, where should footnotes be shown?

13. **Hyperlinks and Metadata**: Should it be extracted at all? Where should it be placed in which format?

14. **Linearization**: Assume you have a floating figure in between a paragraph. Do you first finish the paragraph or do you put the figure text in between?

  

Then there are issues where most people would agree on the correct output, but the way PDF stores information just makes it hard to achieve that:

  

1. **Tables**: Typically, tables are just absolutely positioned text. In the worst case, ever single letter could be absolutely positioned. That makes it hard to tell where columns / rows are.

2. **Images**: Sometimes PDFs do not contain the text as it’s displayed, but instead an image. You notice that when you cannot copy the text. Then there are PDF files that contain an image and a text layer in the background. That typically happens when a document was scanned. Although the scanning software (OCR) is pretty good today, it still fails once in a while. PyPDF2 is no OCR software; it will not be able to detect those failures. PyPDF2 will also never be able to extract text from images.

  

### 목표:

1. 문서 내의 시각 데이터 추출, 답변 생성시 관련있는 시각 데이터 답변에 포함

2. 문서 내의 시각 데이터에 담긴 정보 이해

### 주요 방법:

  

#### 1. Retrieve Raw Image

- 다중 모달 임베딩(ex: CLIP)을 사용하여 이미지와 텍스트를 임베딩

- 유사성 검색을 사용하여 둘 다 검색

- 다중 모달 LLM에 원본 이미지와 텍스트 조각을 전달하여 답변 합성

  

#### 2. Retrieve Image Summary

- 다중 모달 LLM(ex: GPT-4V, GPT-4o, LLaVA, FUYU)를 사용하여 이미지에서 텍스트 요약 생성

- 텍스트 임베딩, 검색

- LLM에 텍스트 조각을 전달하여 답변을 합성

#### 3. Retrieve Raw Image + Image Summary

- 다중 모달 LM(ex: GPT-4V, GPT-4o, LLaVA, FUYU)을 사용하여 이미지에서 텍스트 요약 생성

- 원본 이미지에 대한 참조와 함께 이미지 요약을 임베딩하고 검색

- 다중 모달 LLM에 원본 이미지와 텍스트 조각을 전달하여 답변을 합성

  

> Demo에선 UnStructured PDF Loader 사용

> - 이유: partition_pdf(이미지 추출 기능) 제공

  

![](https://i.imgur.com/rqUfDaj.png)

  

## 절차

  

### 1. 데이터 로드

  

#### 1-1. PDF에서 요소(image, text) 추출

```python

def extract_pdf_elements(path, fname):

"""

PDF 파일에서 이미지, 테이블, 그리고 텍스트 조각을 추출합니다.

path: 이미지(.jpg)를 저장할 파일 경로

fname: 파일 이름

"""

return partition_pdf(

filename=os.path.join(path, fname),

extract_images_in_pdf=True, # PDF 내 이미지 추출 활성화

infer_table_structure=True, # 테이블 구조 추론 활성화

chunking_strategy="by_title", # 제목별로 텍스트 조각화

max_characters=4000, # 최대 문자 수

new_after_n_chars=3800, # 이 문자 수 이후에 새로운 조각 생성

combine_text_under_n_chars=2000, # 이 문자 수 이하의 텍스트는 결합

image_output_dir_path=path, # 이미지 출력 디렉토리 경로

)

```

  

#### 1-2. 요소 유형별(테이블, 텍스트)로 분류

  

```python

def categorize_elements(raw_pdf_elements):

"""

PDF에서 추출된 요소를 테이블과 텍스트로 분류합니다.

raw_pdf_elements: unstructured.documents.elements의 리스트

"""

tables = [] # 테이블 저장 리스트

texts = [] # 텍스트 저장 리스트

for element in raw_pdf_elements:

if "unstructured.documents.elements.Table" in str(type(element)):

tables.append(str(element)) # 테이블 요소 추가

elif "unstructured.documents.elements.CompositeElement" in str(type(element)):

texts.append(str(element)) # 텍스트 요소 추가

return texts, tables

```

  
  

### 2. 데이터 요약

  

#### 2-1. 텍스트 및 테이블 요약

```python

def generate_text_summaries(texts, tables, summarize_texts=False):

"""

텍스트 요소 요약

texts: 문자열 리스트

tables: 문자열 리스트

summarize_texts: 텍스트 요약 여부를 결정. True/False

"""

  

# 프롬프트 설정

prompt_text = """You are an assistant tasked with summarizing tables and text for retrieval. \

These summaries will be embedded and used to retrieve the raw text or table elements. \

Give a concise summary of the table or text that is well optimized for retrieval. Table or text: {element} """

prompt = ChatPromptTemplate.from_template(prompt_text)

  

# 텍스트 요약 체인

model = ChatOpenAI(temperature=0, model="gpt-4")

summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()

  

# 요약을 위한 빈 리스트 초기화

text_summaries = []

table_summaries = []

  

# 제공된 텍스트에 대해 요약이 요청되었을 경우 적용

if texts and summarize_texts:

text_summaries = summarize_chain.batch(texts, {"max_concurrency": 5})

elif texts:

text_summaries = texts

  

# 제공된 테이블에 적용

if tables:

table_summaries = summarize_chain.batch(tables, {"max_concurrency": 5})

  

return text_summaries, table_summaries

```

  
  

#### 2-2. 이미지 요약

  

```python

def generate_img_summaries(path):

"""

이미지에 대한 요약과 base64 인코딩된 문자열을 생성합니다.

path: Unstructured에 의해 추출된 .jpg 파일 목록의 경로

"""

  

# base64로 인코딩된 이미지를 저장할 리스트

img_base64_list = []

  

# 이미지 요약을 저장할 리스트

image_summaries = []

  

# 요약을 위한 프롬프트

prompt = """You are an assistant tasked with summarizing images for retrieval. \

These summaries will be embedded and used to retrieve the raw image. \

Give a concise summary of the image that is well optimized for retrieval."""

  

# 이미지에 적용

for img_file in sorted(os.listdir(path)):

if img_file.endswith(".jpg"):

img_path = os.path.join(path, img_file)

base64_image = encode_image(img_path)

img_base64_list.append(base64_image)

image_summaries.append(image_summarize(base64_image, prompt))

  

return img_base64_list, image_summaries

```

  
  

### 3. Vectorstore에 저장

  

- Docstore: 원본 텍스트, 테이블, 이미지

- Vectorstore: 벡터

  
  
  

## 참조

  

- [\[유튜브 테디노트\] GPT4o를 사용하여 PDF 내 표와 이미지를 참고하여 답변하는멀티모달 RAG](https://youtu.be/U_f4-Br3_Y0?si=Q-cRhXih576BoDcg)

- [\[DeepLearning.AI\]building-multimodal-search-and-rag](https://learn.deeplearning.ai/courses/building-multimodal-search-and-rag)

- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)



- https://www.youtube.com/watch?v=U_f4-Br3_Y0

- [Medium]Multimodal RAG using Langchain Expression Language And GPT4-Vision]([https://medium.aiplanet.com/multimodal-rag-using-langchain-expression-language-and-gpt4-vision-8a94c8b02d21](https://medium.aiplanet.com/multimodal-rag-using-langchain-expression-language-and-gpt4-vision-8a94c8b02d21))
- [[Langchain]How to pass multimodal data directly to models](https://python.langchain.com/v0.2/docs/how_to/multimodal_inputs/)
- [https://paperswithcode.com/paper/llava-uhd-an-lmm-perceiving-any-aspect-ratio](https://paperswithcode.com/paper/llava-uhd-an-lmm-perceiving-any-aspect-ratio)
- [https://huggingface.co/docs/transformers/en/model_doc/llava](https://huggingface.co/docs/transformers/en/model_doc/llava)
- [https://github.com/langchain-ai/langchain/blob/master/cookbook/multi_modal_output_agent.ipynb](https://github.com/langchain-ai/langchain/blob/master/cookbook/multi_modal_output_agent.ipynb)