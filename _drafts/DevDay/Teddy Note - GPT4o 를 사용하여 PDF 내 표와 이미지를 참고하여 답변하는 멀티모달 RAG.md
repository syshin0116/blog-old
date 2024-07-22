
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


![](https://i.imgur.com/rqUfDaj.png)

## 핵심 코드

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

```python
def create_multi_vector_retriever(
    vectorstore, text_summaries, texts, table_summaries, tables, image_summaries, images
):
    """
    요약을 색인화하지만 원본 이미지나 텍스트를 반환하는 검색기를 생성합니다.
    """

    # 저장 계층 초기화
    store = InMemoryStore()
    id_key = "doc_id"

    # 멀티 벡터 검색기 생성
    retriever = MultiVectorRetriever(
        vectorstore=vectorstore,
        docstore=store,
        id_key=id_key,
    )

    # 문서를 벡터 저장소와 문서 저장소에 추가하는 헬퍼 함수
    def add_documents(retriever, doc_summaries, doc_contents):
        doc_ids = [
            str(uuid.uuid4()) for _ in doc_contents
        ]  # 문서 내용마다 고유 ID 생성
        summary_docs = [
            Document(page_content=s, metadata={id_key: doc_ids[i]})
            for i, s in enumerate(doc_summaries)
        ]
        retriever.vectorstore.add_documents(
            summary_docs
        )  # 요약 문서를 벡터 저장소에 추가
        retriever.docstore.mset(
            list(zip(doc_ids, doc_contents))
        )  # 문서 내용을 문서 저장소에 추가

    # 텍스트, 테이블, 이미지 추가
    if text_summaries:
        add_documents(retriever, text_summaries, texts)

    if table_summaries:
        add_documents(retriever, table_summaries, tables)

    if image_summaries:
        add_documents(retriever, image_summaries, images)

    return retriever
```


### 4. Retrieval Chain

```python

def split_image_text_types(docs):
    """
    base64로 인코딩된 이미지와 텍스트 분리
    """
    b64_images = []
    texts = []
    for doc in docs:
        # 문서가 Document 타입인 경우 page_content 추출
        if isinstance(doc, Document):
            doc = doc.page_content
        if looks_like_base64(doc) and is_image_data(doc):
            doc = resize_base64_image(doc, size=(1300, 600))
            b64_images.append(doc)
        else:
            texts.append(doc)
    return {"images": b64_images, "texts": texts}


def img_prompt_func(data_dict):
    """
    컨텍스트를 단일 문자열로 결합
    """
    formatted_texts = "\n".join(data_dict["context"]["texts"])
    messages = []

    # 이미지가 있으면 메시지에 추가
    if data_dict["context"]["images"]:
        for image in data_dict["context"]["images"]:
            image_message = {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image}"},
            }
            messages.append(image_message)

    # 분석을 위한 텍스트 추가
    text_message = {
        "type": "text",
        "text": (
            "You are financial analyst tasking with providing investment advice.\n"
            "You will be given a mixed of text, tables, and image(s) usually of charts or graphs.\n"
            "Use this information to provide investment advice related to the user question. Answer in Korean. Do NOT translate company names.\n"
            f"User-provided question: {data_dict['question']}\n\n"
            "Text and / or tables:\n"
            f"{formatted_texts}"
        ),
    }
    messages.append(text_message)
    return [HumanMessage(content=messages)]


def multi_modal_rag_chain(retriever):
    """
    멀티모달 RAG 체인
    """

    # 멀티모달 LLM
    model = ChatOpenAI(temperature=0, model="gpt-4o", max_tokens=2048)

    # RAG 파이프라인
    chain = (
        {
            "context": retriever | RunnableLambda(split_image_text_types),
            "question": RunnablePassthrough(),
        }
        | RunnableLambda(img_prompt_func)
        | model
        | StrOutputParser()
    )

    return chain
```
##  테스트

#### 테이블 기반 테스트


```python
# 검색 결과 확인
query = "국가별 및 완성차 그룹별 전기차(BEV) 판매량에서 중국이 2020년 판매량이 몇대야?"
docs = retriever_multi_vector_img.invoke(query, limit=6)

print(table_summaries[3])
print(docs[0])
```

	2020-2022년 전기차 판매량 및 시장 점유율 데이터. 중국, 유럽, 미국, 한국, 캐나다, 일본, 인도, 기타 국가별 판매량과 성장률. 주요 브랜드 및 그룹별 판매량과 성장률. 테슬라, BYD, 상해기차, VW, Geely, 르노닛산, 현대차그룹 등 포함. 전기차 전체 판매량과 완성차 전체 판매량 비교. 

	브랜드 구분 2020 판매량(대) M/S(%) 2021 판매량(대) M/S(%) 2022 판매량(대) M/S(%) 성장률 (2020-2021) 성장률 (2021-2022) 중국 1,054,123 47.5 2,727,313 57.1 5,075,286 63.3 158.7% 86.1% 유럽* 782,561 35.2 1,292,751 35.2 1,622,895 20.2 65.2% 25.5% 미국 260,055 11.7 505,267 11.7 802,653 10.0 94.3% 58.9% 국 가 한국 46,909 2.1 101,112 2.1 162,987 2.0 115.5% 61.2% 별 캐나다 30,928 1.4 50,033 1.0 92,871 1.2 61.8% 85.6% 일본 16,028 0.7 23,291 0.5 61,251 0.8 45.3% 163.0% 인도 4,386 0.2 10,043 0.2 47,563 0.6 129.0% 373.6% 기타 25,366 1.1 68,507 1.4 155,049 1.9 170.1% 126.3% 테슬라 494,244 22.3 938,435 19.6 1,313,887 16.4 89.9% 40.0% BYD 123,627 5.6 335,582 7.0 925,782 11.5 171.4% 175.9% 상해기차 235,425 10.6 612,867 12.8 900,418 11.2 160.3% 46.9% 그 룹 별 VW Geely 220,818 43,581 9.9 2.0 442,960 120,637 9.3 2.5 574,708 422,903 7.2 5.3 100.6% 176.8% 29.7% 250.6% 르노닛산 196,471 8.8 261,736 5.5 392,244 4.9 33.2% 49.9% 현대차그룹 145,609 6.6 245,174 5.1 374,963 4.7 68.4% 52.9% 기타 760,581 34.3 1,820,926 38.1 3,115,650 38.8 139.4% 71.1% 전기차 합계 (비중*) 2,220,356 (2.9%) 100 4,778,317 (5.9%) 100 8,020,555 (9.9%) 100 115.2% 67.9% 완성차 전체 77,766,294 - 81,439,571 - 80,631,101 - 4.7% △1.0%

![](https://i.imgur.com/jQDpf2h.png)


```python
print(
    chain_multimodal_rag.invoke(
        "국가별 및 완성차 그룹별 전기차(BEV) 판매량에서 중국이 2020년 판매량이 몇대야?"
    )
)
```

	2020년 중국의 전기차(BEV) 판매량은 1,054,123대입니다.

![](https://i.imgur.com/PRoUfO5.png)




#### 이미지 기반 테스트

```python
# 검색 질의 실행
query = "테슬라 사이버트럭 내부 사진"

# 질의에 대한 문서 6개를 검색합니다.
docs = retriever_multi_vector_img.invoke(query, limit=6)

# 문서의 확인
docs[0]
```


![](https://i.imgur.com/qGTn7k6.png)


```python
image_summaries[94]
```
	'테슬라 사이버트럭 내부'
```python
# RAG 체인 실행
print(chain_multimodal_rag.invoke("테슬라 사이버트럭 내부 사진"))
```

테슬라 사이버트럭의 내부 사진을 보면, 이 차량이 매우 미래지향적이고 혁신적인 디자인을 가지고 있음을 알 수 있습니다. 이는 테슬라가 전기차 시장에서의 리더십을 유지하고자 하는 강한 의지를 반영합니다. 테슬라는 전기차 시장에서의 선도적인 위치를 차지하고 있으며, 사이버트럭은 그들의 제품 라인업을 더욱 다양화하고 강화하는 중요한 모델입니다. 사이버트럭의 독특한 디자인과 기능은 많은 소비자들의 관심을 끌고 있으며, 이는 테슬라의 매출 증가와 주가 상승에 긍정적인 영향을 미칠 수 있습니다. 투자 관점에서 볼 때, 테슬라의 사이버트럭은 다음과 같은 이유로 긍정적인 신호로 해석될 수 있습니다: 
1. **혁신적인 디자인과 기술**: 사이버트럭의 독특한 디자인과 첨단 기술은 시장에서의 경쟁력을 높여줄 것입니다. 
2. **강력한 브랜드 인지도**: 테슬라는 이미 전 세계적으로 강력한 브랜드 인지도를 가지고 있으며, 사이버트럭은 이를 더욱 강화할 것입니다. 
3. **전기차 시장의 성장**: 전기차 시장은 지속적으로 성장하고 있으며, 테슬라는 이 시장에서의 리더로서 큰 혜택을 볼 것입니다. 
4. **다양화된 제품 라인업**: 사이버트럭은 테슬라의 제품 라인업을 다양화하여 더 많은 소비자층을 타겟으로 할 수 있게 합니다. 따라서, 테슬라의 주식은 장기적인 투자 관점에서 긍정적인 선택이 될 수 있습니다. 다만, 전기차 시장의 경쟁이 치열해지고 있는 만큼, 투자 시에는 시장 동향과 테슬라의 재무 상태를 지속적으로 모니터링하는 것이 중요합니다.
### 코드
[Multi modal RAG GPT 4o.ipynb](hook://file/iTvJQhutn?p=U3R1ZHkvRGV2RGF5&n=Multi%20modal%20RAG%20GPT%204o%2Eipynb)

## 참조

- [\[유튜브 테디노트\] GPT4o를 사용하여 PDF 내 표와 이미지를 참고하여 답변하는멀티모달 RAG](https://youtu.be/U_f4-Br3_Y0?si=Q-cRhXih576BoDcg)
- https://blog.langchain.dev/semi-structured-multi-modal-rag/
