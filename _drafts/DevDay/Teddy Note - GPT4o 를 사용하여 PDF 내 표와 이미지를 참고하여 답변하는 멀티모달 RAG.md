
# Multi-Modal RAG

### 배경:
- GPT-4V, GPT-4o와 같은 다중 모달 LLM 등장
- RAG에서 text뿐만 아니라 image도 함께 활용하는 방안 

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
        extract_images_in_pdf=True,  # PDF 내 이미지 추출 활성화
        infer_table_structure=True,  # 테이블 구조 추론 활성화
        chunking_strategy="by_title",  # 제목별로 텍스트 조각화
        max_characters=4000,  # 최대 문자 수
        new_after_n_chars=3800,  # 이 문자 수 이후에 새로운 조각 생성
        combine_text_under_n_chars=2000,  # 이 문자 수 이하의 텍스트는 결합
        image_output_dir_path=path,  # 이미지 출력 디렉토리 경로
    )
```

#### 1-2. 요소 유형별(테이블, 텍스트)로 분류

```python
def categorize_elements(raw_pdf_elements):
    """
    PDF에서 추출된 요소를 테이블과 텍스트로 분류합니다.
    raw_pdf_elements: unstructured.documents.elements의 리스트
    """
    tables = []  # 테이블 저장 리스트
    texts = []  # 텍스트 저장 리스트
    for element in raw_pdf_elements:
        if "unstructured.documents.elements.Table" in str(type(element)):
            tables.append(str(element))  # 테이블 요소 추가
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            texts.append(str(element))  # 텍스트 요소 추가
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
    Give a concise summary of the table or text that is well optimized for retrieval. Use Korean. \
    Table or text: {element} """
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





![](https://i.imgur.com/eSO9CoH.png)

![](https://i.imgur.com/IGfnuxc.png)


![](https://i.imgur.com/ZMTUlU3.png)


![]()

[https://oaidalleapiprodscus.blob.core.windows.net/private/org-DgSLdlUMXlL7qrgA1oHMiKjw/user-E2OP0NHHbvQkEsXieWtCrg78/img-Ld1avlnHfQv4mGbjBcz8lqak.png?st=2024-06-24T23%3A54%3A53Z&se=2024-06-25T01%3A54%3A53Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-24T16%3A53%3A57Z&ske=2024-06-25T16%3A53%3A57Z&sks=b&skv=2023-11-03&sig=iaMxyC%2BnH86SuwxLyTxCEOQ9EoKPlaTNr2C7kRD5QUU%3D](https://oaidalleapiprodscus.blob.core.windows.net/private/org-DgSLdlUMXlL7qrgA1oHMiKjw/user-E2OP0NHHbvQkEsXieWtCrg78/img-Ld1avlnHfQv4mGbjBcz8lqak.png?st=2024-06-24T23%3A54%3A53Z&se=2024-06-25T01%3A54%3A53Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-24T16%3A53%3A57Z&ske=2024-06-25T16%3A53%3A57Z&sks=b&skv=2023-11-03&sig=iaMxyC%2BnH86SuwxLyTxCEOQ9EoKPlaTNr2C7kRD5QUU%3D)



