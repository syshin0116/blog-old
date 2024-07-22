## AIOPs를 위한 데이터 통합 플랫폼 도입기

- 발표자: 수빈님


### PoscoEnC 데이터가 왜 불편했는가

- 도메인 specific
- 데이터 특성:
	- 명료하게 정리되지 않은 시스템, 불규칙성
	- 원천 데이터와도 다른 실데이터로 발생하는 추가 공수

### Data Catalog
- 데이터 수집 → 메타 데이터 생성 → 메타 데이터 추가/보완 → 메타 데이터 수정, 사용자 리뷰/평가

### Data Lineage
- 데이터가 사용되는 흐름을 시각화 → 이해하기 편함

> explainable 데이터도 되지 않을까


> Huggingface 데모에서 Docker → AimStack, Shiny
Docker 선택 시:
>- Docker in Docker 형태로 가동


### DataHub vs Shiny

- Python vs YAML: YAML이 더 많은 기능 지원

#### DataHUB



## RAG 기법 이해와 최적의 플로우 도출
- 발표자: 명찬님

### Advanced RAG
우리에게 맞는 최적의 방법론이 무엇인가?
- Pre-Retrieval: 쿼리가 검색되기 이전의 작업들
- Retrieval: 검색 작업
- Post-Retrieval: 검색 이후, 검색된 결과를 가지고 LLM 생성 이전에 진행되는 작업
- Generation: 생성 작업

### QA 생성

- 162개 생성 →  127개 선정(Human in the loop)


### 설정

- Pass: 아무 작업을 하지 않고 넘어가게 할 수 있음

### 높은 성능을 가진 성능
#### Pre-retrieval: 
- Hyde
- Multi-query
- Pass(O)

#### Retrieval: 
- BM25(O)
- vectordb(bge_m3)
- vectordb(openai)
- vectordb(intfloat_inst)
#### Post-Retrieval

#### Compressor
- Tree-summarizer:
- Pass(O)

#### Long context Reorder
- 사용(O)
- 미사용

## PEFT의 이해와 활용

### LLM 모델
#### LLaMA
- 파라메터가 너무 퍼지는것을 방지하기 위해 Normalization을 진행하는데, 조금 더 앞단계에서 했더니 성능 향상이 있었다
- Transformer에서 절대적인 위치를 표현하는 Embedding(Positive Embedding)과 Relative Embedding 방식을 합침
- Group Query Attention: Llamma 버전 업그레이드에 따라 이것만 바뀜

#### Mistral
- Group Query Attention: Llama2와 같은 방식
- Sliding Window Attention 방식 채택
- Rolling Bufer Cache: 최대 Cache 사이즈를 정해서 Cache Memory 사용량 줄이는 방법
- Pre-fill and Chunking: 초기 입력으로 들어오는 Pompt값을 알고 있음 → 미리 KV 값을 채울 수 있음
- MOE 방식: 전문가를 선택하여 학습&추론 과정 진행. 깊이보다 넓이를 선택

#### Solar
- DUS: Mistral과는 반대로 넓이 보다 깊이 선택
- Mistral의 초기 가중치를 가지고 학습 진행
- Layer 구조는 Llama2구조를 기본 모델로 선택

#### EEVE
- Base Model로 Upstage의 Solar방식
- 학습 방법: Parameter Freeze를 이용한 7단계 학습 방법
- 입력 토큰과 출력 토큰 크기가 같아야 함



### PEFT란?
파라미터를 효과적으로 Fine-Tuning하는 방법

- Optimization of Resources
- Mastery over Catastrophic Forgetting
- Superiority in Data-Sparse Environments
- Easy Portability and Deployment: Stable Diffusion
- Matching Performance with Economized Tuning


### PEFT의 종류
- Additive Fine Tuning
- Unified Fine Tuning
- Reparameterized Fune Tuning
- Hybrid Fine Tuning
- Partial Fine Tuning

## vLLM
- 발표자: 안실장님