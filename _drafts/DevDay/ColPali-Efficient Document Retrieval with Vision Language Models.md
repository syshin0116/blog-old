Paper: https://arxiv.org/pdf/2407.01449v2
HuggingFace Model: https://huggingface.co/vidore
Github: https://github.com/illuin-tech/colpali



![](https://cdn-uploads.huggingface.co/production/uploads/60f2e021adf471cbdf8bb660/T3z7_Biq3oW6b8I9ZwpIa.png)

### Models
- SigLIP: 바닐라 모델
	- vision-language bi-encoder model
	- image-text 쌍으로 사전학습
- BiSigLIP: +파인튜닝
	- figure retrival + table retrieval
	- 복잡한 형식 이해 능력 향상
- BiPali: +LLM
	- LLM 모델: PaliGemma https://arxiv.org/pdf/2407.07726
- ColPali: +Late Interaction

### ColBert: Late Interaction for efficient and effective passage search


![](https://i.imgur.com/IxwVgOJ.jpeg)


장점: 
- 후기 상호작용은 쿼리와 문서 간에 보다 세분화된 매칭 프로세스를 가능하게 합니다. 쿼리의 각 구성 요소를 문서의 각 구성 요소와 비교함으로써 시스템은 보다 전체적인 접근 방식으로는 놓칠 수 있는 관련성의 뉘앙스를 포착할 수 있습니다.
- **인코딩과 상호작용 단계를 분리함으로써 후기 상호작용 모델은 쿼리와 독립적으로 커멘트 임베딩을 미리 계산하고 색인을 생성할 수 있습니다. 따라서 임베딩 생성의 계산 집약적인 부분이 이미 완료되었으므로 쿼리 단계에서 모델의 효율성이 매우 높아집니다.**
- 쿼리가 실제로 수행될 때까지 비교 과정이 연기되기 때문에, 후기 연동 모델은 전체 문서 코퍼스를 재처리할 필요 없이 동적 및 임시 쿼리를 쉽게 처리할 수 있습니다.
### 참고 자료:
- https://www.youtube.com/watch?v=0C0FL0iFd1E
- 
