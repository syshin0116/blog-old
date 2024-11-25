---
layout: post
title: "[Modular RAG]구조"
date: 2024-10-20 12:38 +0900
categories:
  - Project
  - Modular RAG
tags: 
math: true
---
Naive RAG에 여러 RAG를 하기 위해 Advanced RAG를 충분히 다뤘다고 생각한다. 하지만, 점점 더 복잡한 작업을 최소화하고 효율성을 높이기 위해 Modular RAG 방식을 적용하고자 한다. 마치 LEGO 블록처럼 모듈들을 쌓아가며 나만의 재사용 가능한 RAG 자산을 구축하는 것이 목표다. Modular RAG는 시스템의 유연성과 확장성을 크게 향상시킬 수 있어, 이를 통해 다양한 애플리케이션 요구 사항에 맞게 모듈을 조합하고 최적화하는 방향으로 발전시키고자 한다

Modular RAG 논문: [https://arxiv.org/html/2407.21059v1](https://arxiv.org/html/2407.21059v1)

![](https://i.imgur.com/Vh7vEHw.png)

![](https://i.imgur.com/kqjz87X.png)

![](https://i.imgur.com/HUHBVIJ.png)


### 기술 스택

이 프로젝트에서는 다양한 기술을 활용하여 **모듈화된 RAG 시스템**을 구축함. 주요 기술 스택은 다음과 같음:

- **FastAPI**: API 서버 프레임워크로 사용. 비동기 처리를 지원하며, 고성능 API를 쉽게 구축할 수 있음
- **Docker**: 각 서비스를 독립된 컨테이너로 관리하고, 배포 환경을 쉽게 설정할 수 있도록 사용. 나중에 DB와 Redis 같은 서비스도 Docker Compose를 통해 관리 예정
- **Poetry**: 의존성 관리 및 패키지 관리를 위해 사용. Python 패키지 관리의 안정성과 유연성을 제공
- **LangGraph**: 노드와 엣지를 기반으로 워크플로우를 구성하고, 다양한 모듈을 유연하게 조합하는 데 사용
- **LLM**: GPT, Llama 등 다양한 LLM을 통합하여 여러 상황에 맞는 대화 모델을 제공
- **Chroma, Faiss, Milvus**: 다양한 벡터 스토어로, 검색 성능을 향상시키기 위해 선택적으로 사용

## 구조
```

modular-rag/
│
├── app/                       # FastAPI 애플리케이션 코드
│   ├── main.py                # FastAPI 메인 엔트리 포인트
│   ├── routers/               # API 경로 관리
│   │   └── core.py            # 핵심 API 라우팅
│   ├── services/              # 서비스 모듈
│   │   ├── retrievals/        # retrieval 관련 로직
│   │   │   ├── pre_retrieval.py
│   │   │   ├── retrieval.py
│   │   │   ├── post_retrieval.py
│   │   ├── vectorstores/     # 벡터 스토어 관련
│   │   │   ├── chroma_store.py
│   │   │   ├── faiss_store.py
│   │   │   └── milvus_store.py
│   │   ├── preprocessing/     # 전처리 관련 로직
│   │   ├── web_search.py      # 웹 검색 관련
│   │   ├── llm_handler.py     # 다양한 LLM 관리 (GPT, Llama 등)
│   │   ├── prompt_manager.py  # 프롬프트 관리
│   │   ├── parsers/           # 파일 파서 모듈
│   │   │   ├── llama_parser.py
│   │   │   ├── web_parser.py
│   │   │   └── generic_parser.py
│
├── docker/                    # Docker 설정 파일
│   ├── fastapi/               # FastAPI 관련 Docker 설정
│   │   ├── Dockerfile
│   ├── nginx/                 # Nginx 관련 설정
│   │   ├── Dockerfile
│   │   ├── nginx.conf
│
├── compose.yaml          # Docker Compose 설정 파일 (루트 디렉토리에 위치)
│
├── langgraph/                 # LangGraph 관련 로직 폴더
│   ├── node_definitions.py    # 노드 정의 (LLM, 리트리버, 벡터 스토어 등)
│   ├── langgraph_handler.py   # LangGraph 구성 및 핸들러 (node_definitions 활용)
│
├── config/                    # 설정 파일
│   └── settings.py            # LLM, 리트리버, 파서 등 환경설정
│
├── tests/                     # 테스트 관련 폴더
│   ├── __init__.py            # 테스트 폴더 초기화
│
├── poetry.lock                # Poetry 잠금 파일
├── pyproject.toml             # Poetry 의존성 및 프로젝트 설정 파일
└── README.md                  # 프로젝트 설명
```



### 현재: 
```
15 directories, 15 files
❯ tree -L 5
.
├── README.md
├── compose.yaml
├── docker
│   ├── Dockerfile.fastapi
│   ├── Dockerfile.nginx
│   └── nginx.conf
├── fastapi
│   └── app
│       ├── configs
│       │   ├── mysql.py
│       │   ├── redis.py
│       │   └── settings.py
│       ├── db
│       │   ├── crud
│       │   ├── models
│       │   │   ├── base.py
│       │   │   └── user.py
│       │   ├── schemas
│       │   │   └── user.py
│       │   └── session.py
│       ├── main.py
│       ├── routers
│       │   └── user.py
│       ├── services
│       │   └── langgraph
│       ├── static
│       │   ├── img
│       │   └── sample.css
│       └── templates
│           └── login.html
├── poetry.lock
└── pyproject.toml
```

## 구조 요약

### services/retrievals

검색 관련 로직을 단계별로 나눔. RAG 방법론에 따라 pre_retrieval, retrieval, post_retrieval로 나누어 각 단계를 처리할 예정

- pre_retrieval: 검색 전 전처리 로직
- retrieval: 검색 로직
- post_retrieval: 검색 후 후처리

### services/vectorstores

여러 벡터 스토어(Chroma, Faiss, Milvus 등)를 사용할 수 있도록 구성할 예정

### services/preprocessing

파싱된 데이터를 벡터 스토어에 넣기 전 전처리 과정 담당. 데이터 클리닝과 변환 등 작업 포함

### services/websearch

웹 검색 관련 모듈을 구성. 다양한 웹 검색 소스를 처리할 수 있도록 설계

### services/prompt_manager

프롬프트를 저장하고 관리하는 공간

### services/parsers

Llama parser와 파일 확장자별 파서들을 정의하여 다양한 파일 형식을 처리

### services/llm_handler

공개 및 비공개 LLM 호출 함수들을 정의하고 관리

### langgraph/node_definitions

LLM, 리트리버, 벡터 스토어 등 주요 기능을 각각 노드로 정의. 노드는 독립적으로 동작하며, 다양한 워크플로우에서 유연하게 재사용 가능

### langgraph/langgraph_handler

LangGraph를 관리하고, node_definitions에서 정의된 노드들을 불러와 엣지로 연결해 워크플로우를 구성. 사용자의 요구에 맞춰 동적으로 노드를 선택하거나 연결할 수 있도록 구조화
