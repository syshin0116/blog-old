---
layout: post
title: "[LangChain Open Tutorial] - Week 2- PeerReview"
date: 2025-01-10 01:48 +0900
categories:
  - Project
  - LangChain Open Tutorial
tags: 
math: true
---


## 04-GraphRAG / 07-AcademicSearchSystem

생각나는대로 냅다 다 적겠습니다ㅎㅎ가벼운 마음으로 고려해주시면 감사하겠습니다!

#### 1. Overview

1. 설명해야할 내용이 너무 많은 주제라 고민이 많으셨을것 같아요. 핵심만 잘 정리중이신 느낌이라 좋지만 `Knowledge Graph`와 같이 중요하지만 한마디로 설명하기엔 너무 복잡한 내용은 잘 설명된 곳으로 링크 보내면 좀 더 친절한 글이 될 것 같습니다
    
2. GraphRAG의 장점을 잘 설명해주셨는데, 구축 난이도와 같은 단점은? 이라는 생각이 일부러 안넣으신건가? 라는 생각과 함께 들었습니다.
    

#### 2. Environment Setup:

사소하지만, `!pip install` 임시방편 부분들 공통부분에 넣으면 되는걸로 알고있습니다ㅎ

```python
# Install required packages
from langchain_opentutorial import package

package.install(
    [
        "langchain-neo4j",
        "pyalex"
    ],
    verbose=False,
    upgrade=False,
)
```

#### 3. 데이터

1. 노드에 대한 설명은 잘 해주셨으나, 엣지는 어떻게 구성되어있는지 한번에 볼 수 있는 그림이 있으면 좋을것 같다는 생각이 들었습니다.
    
2. json 파일 내용도 어떻게 구성되어있는지 살짝 보여주시면 좋을것 같습니다.
    

#### 4. 실행 코드

마지막에서 두번째 셀

```python
chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, verbose=True, qa_prompt=CYPHER_QA_PROMPT, cypher_prompt=CYPHER_GENERATION_PROMPT,
    allow_dangerous_requests = True
)
```

마지막에서 두 번째 셀의 `from_llm` 부분은 현재 방식이 오래된 것 같습니다.

예전(3~4개월 전) 기준으로는 LangChain이 해당 클래스를 업데이트하지 않았던 것으로 기억하는데, 최신 상태에서도 그대로인지 살짝 확인해보시면 좋을 것 같습니다.

---

완전 초안이고, 생각나는 대로 마구잡이로 적어본 내용이라 가볍게 참고만 해주시면 좋겠습니다! 고생하셨습니다!
## 04-GraphRAG / 08-AcademicQASystem

생각나는대로 마구 아이디어 적어보겠습니다. 가볍게 읽어보시고 맘에 드시는점들 반영 고려 해주시면 감사하겠습니다!
### Overview

GraphRAG와 Knowledge graph가 생소할 사람들이 많을것 같은데, flow를 설명해주는 이미지가 있어서 너무 좋은것 같습니다! 논문도 일부러 관련 논문 가져오신것 같네요ㅎㅎ실습하면서 자연스럽게 논문 내용도 엿볼 수 있어서 좋은 아이디어이신것 같아요ㅎㅎ저도 따라해봐야겠어요
### Load arXiv PDFs

pdf 다운로드 링크를 친절히 적어주셨지만, code 형태로 다운로드해서 `./data/` 디렉토리에 넣어주는 칸이 있으면 더 친절한 튜토리얼이 될 것 같습니다!

혹시 도움이 되실까 싶어 제가 1주차때 썼던 다운로드 코드 예시 남깁니다. 

```python
# Download and save sample PDF file to ./data directory
import requests

def download_pdf(url, save_path):
    """
    Downloads a PDF file from the given URL and saves it to the specified path.

    Args:
        url (str): The URL of the PDF file to download.
        save_path (str): The full path (including file name) where the file will be saved.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes

        # Save the file to the specified path
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"PDF downloaded and saved to: {save_path}")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")


# Configuration for the PDF file
pdf_url = "https://arxiv.org/pdf/1706.03762v7"
file_path = "./data/1706.03762v7.pdf"

# Download the PDF
download_pdf(pdf_url, file_path)
```


### Text Chunking and Text Extracting

`TextUnitExtractor`을 사용하셔서 dataframe형태로 document를 청킹하셨는데, 간단하게 사용하기 좋네요ㅎㅎ하나 배워갑니다

### Entity Relationship Extraction

와우..말씀하신것처럼 오래걸리긴 하네요. 괜히 gpt-4o-mini를 쓰신게 아닌것 같아요. 더 짧은 논문으로 시간을 줄여보는것도 고려해보시면 좋을것 같습니다. 

### Graph Generation
`EntityRelationshipDescriptionSummarizer` : 요약을 어떤식으로 했는지, 예시로 한개 print해보면 좋을것 같아요!

---

그래프RAG의 단점인 구축 난이도를 자동화 할 수 있다는 점에서 개인적으로 완성된 튜토리얼이 굉장히 기대됩니다ㅎㅎ

고생하셨습니다!