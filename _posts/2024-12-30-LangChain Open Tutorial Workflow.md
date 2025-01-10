---
layout: post
title: "[LangChain Open Tutorial]Commit Flow"
date: 2024-12-30 21:05 +0900
categories:
  - Project
  - LangChain Open Tutorial
tags: 
math: true
---
## 기본 커밋 방식
1. [LangChain-OpenTutorial](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial) fork
2. 

## Environment & Package
- Python 3.11 사용

### Poetry Env 사용

- 기본적인 package는 사전 구성
- 추가 패키지는 프로젝트 진행하면서 추가
- 중앙 관리팀 존재(충돌 방지)
	- Package 추가 희망 시 중앙 팀에게 요청

## Workflow
1. [LangChain-OpenTutorial](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial)Fork
2. 각자 개인 Fork에서 작업
3. Main(original) repository에 PR(pull request)
4. PEER 리뷰(2명)
5. Merge


![](https://i.imgur.com/iBaH2cy.png)


## Commit Message

```markdown
[Team] {소속팀}
[Title] {작업 제목 요약}
[Version] {initial / revision / bugfix / other}
[Language] {KO / ENG}
[Packages] {사용한 주요 패키지 목록}

{상세 설명}
```

- packages(참고용): 정확하게 안적어도 됨. 콤마 구분자로 작성
- 상세 설명: 생략 가능, 간단하게 한줄

## Template

### Title
```markdown
# Title
- Author: [Teddy](https://github.com/teddylee777)
- Design: [Teddy](https://github.com/teddylee777)
- This is a part of [LangChain Open Tutorial](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain-academy/blob/main/module-4/sub-graph.ipynb) [![Open in LangChain Academy](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/66e9eba12c7b7688aa3dbb5e_LCA-badge-green.svg)](https://academy.langchain.com/courses/take/intro-to-langgraph/lessons/58239937-lesson-2-sub-graphs)
```


- Title: 
	- `#`H1 사용
	- 원본 타이틀 고집하지 않아도 됨. 더 적당한 타이틀 환영!
- Author: 가급적이면 본인 깃허브 링크 사용, 
- Designer: 디자이너 협업 시


### Overview
- `##`: H2 사용
- 튜토리얼에 대한 전반적인 내용 작성
- 튜토리얼의 목적/주로 다로는 내용 언급
- 최소 3문장 이상 기입

#### 이미지 작업
- 이미지 도식이 필요한 경우 excalidraw등 툴 사용
- 필요시 디자이너분께 요청
- 디자이너 한분임...웬만하면 혼자 해결하자

### Table of Contents
- `###`: H3 사용
- Anchor 사용(해당 부분으로 링크)
- 이후 내용에서 `##`로 이루어신 내용만 포함

### References
- `###`: H3 사용
- 테디노트 튜토리얼 제외 참조한 외국 사이트, 논문


### 구분선 `----`
- Intro 와 본문 내용 구분을 위한 `----` 


## Environment Setup

`package install` 부분 제외 복붙

#### package
- package 부분 본인 작업 튜토리얼  맞게 수정
- 코랩에서 실행시 필요한 필수 패키지만 기재

#### env variables
- 가급적이면 Langsmith 설정
- `LANGCHAIN_PROJECT`: 튜토리얼 제목과 동일하게


## Markdown 규칙

- `#`: 제목에만 사용
- `##`: 소제목에 사용. 큰 주제별로 나눌때 table of contents 내용
- `###`: 제목의 하위 카테고리에 사용
- `####`: 사용하지 않는다

- `##`, `###`: 자유롭게 사용 가능하나, 컨텐츠 추가 필수

#### 당부사항
- `**`: 강조
	- ex) `다음 단계에서는 **쿼리 라우팅** 과 ** 문서 평가** 를 수행합니다.`
	- `**` 이후에 꼭 공백
- \`: `변수`, `함수`, `모듈명`
	- ex) 다음은 `ChatOpenAI`를 활용하는 예시입니다
- Strict markdown: 개행시 `\n` 두개


## 코드 포맷터
- `VSCode`, `Cursor`: 
	1. Extension에서 `Black Formatter` 설치
	2. `Ctrl` + `Shift` + `P`
	3. `Open User Settings`
	4. https://gist.github.com/teddylee777/e9d9845fabfd3379dfcd7ffbc37d1286 내용 복붙


아래 설정은 필수
```json
// editor 설정
"editor.fontSize": 16,  // 에디터의 기본 글꼴 크기를 16으로 설정합니다.
"editor.fontVariations": false,  // 글꼴 스타일 변형을 사용하지 않습니다.
"editor.defaultFormatter": "ms-python.black-formatter",  // 에디터의 기본 코드 포맷터로 Black을 지정합니다.

// 노트북 설정     
"notebook.output.wordWrap": true,// 노트북 출력에서 자동 줄바꿈을 활성화합니다.  
"notebook.formatOnSave.enabled": true,  // 노트북 저장 시 자동으로 포맷합니다.
"notebook.output.scrolling": true,  // 노트북 출력을 스크롤 가능하게 설정합니다.
"notebook.lineNumbers": "on",  // 노트북에서 줄 번호를 표시합니다.

// 언어별 설정 (Python)
"[python]": {         
	"editor.defaultFormatter": "ms-python.black-formatter",
	"editor.formatOnType": true,
	"editor.formatOnSave": true,
	"editor.parameterHints.enabled": true,
	}
```



---

## Core Contributer

조건:
1. PR 오픈 및 PUSH 매주 수요일 23:59까지
2. 1차 Reviewer: 목요일 23:59까지 PR 리뷰

- 신규 개발팀도 동일



