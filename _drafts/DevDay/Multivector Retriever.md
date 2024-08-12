
**MultiVector Retriever**:
- LangChain 라이브러리에서 제공하는 문서 검색 도구로
- 각 문서에 대해 여러 벡터를 저장하여 검색 성능을 향상시키는 방법을 사용

문서 생성 방법:
1. **Smaller Chunks (작은 조각)**: 문서를 작은 조각으로 나누어 각각을 임베딩
2. **Summary (요약)**: 각 문서에 대해 요약을 생성하고, 문서와 함께 또는 대신에 요약을 임베딩
3. **Hypothetical Questions (가설 질문)**: 문서에 적합한 가설 질문을 생성하고, 문서와 함께 또는 대신에 질문을 임베딩합니다.

이러한 방법을 통해 각 문서에 대해 여러 벡터를 생성하고 저장하여 검색의 유연성과 정확성을 높일 수 있습니다.

**사용 예시**:

1. **Smaller Chunks**:
    - 문서를 작은 조각으로 나눈 후, 각 조각을 벡터로 변환하여 저장.
    - 예: `RecursiveCharacterTextSplitter`를 사용하여 문서를 작은 조각으로 나눈 후 `Chroma` 벡터 스토어에 저장.
2. **Summary**:
    - 문서의 요약을 생성하여 벡터로 변환하여 저장.
    - 예: `ChatOpenAI`를 사용하여 요약을 생성하고 이를 벡터로 변환하여 저장.
3. **Hypothetical Questions**:
    - 문서에 대한 가설 질문을 생성하고 이를 벡터로 변환하여 저장.
    - 예: `ChatOpenAI`를 사용하여 가설 질문을 생성하고 이를 벡터로 변환하여 저장.

![](https://i.imgur.com/oagBKKs.png)

