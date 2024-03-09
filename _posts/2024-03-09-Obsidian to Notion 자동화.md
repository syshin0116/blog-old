---
layout: post
title: Obsidian to Notion 자동화
date: 2024-03-09 13:37 +0900
categories:
  - ETC
  - etc
tags: 
math: true
---

## Intro: 

개인적으로 Obsidian은 개인적 사용에 있어 매우 강력한 도구로, 반면 Notion은 협업 목적에 더 적합하다고 생각한다. 두 도구는 모두 Markdown 형식을 기반으로 하기 때문에, Obsidian에서 작성한 개인적인 문서를 Notion의 협업 페이지로 쉽게 복사하여 붙여넣을 수 있어, 두 도구를 유연하게 함께 사용할 수 있는 장점이 있다. 이러한 반복 작업을 자동화할 수 있는 방법이 있을지 궁금하여 탐색해보았다.

Obsidian을 개인 Github-Git Action과 연동하여 사용하고 있었고, 이번엔 협업용 Notion과 연동을 할 생각이다.

## 탐색
검색해보니 공감가는 글이 많이 보였다. 대체로 Notion은 협업이나 미디어 임베딩시 유용했고, Obsidian은 그 외 작업에 유용했다는 의견이 많았다. 그리고 extention이 많은 VSCode까지도 같이 사용하는 사람도 가끔 보였다.

- [3 Proven Ways to Use Notion with Obsidian](https://bloggingx.com/use-notion-with-obsidian/) 


## 설치 방법

### 1. Share to Notion 플러그인 설치

Obsidian Community Market에서 [Share to Notion](obsidian://show-plugin?id=obsidian-to-notion) 플러그인 설치

![](https://i.imgur.com/23at9Dw.png)

Community Plugin에서 활성화 시켜주는걸 잊지 말자

![](https://i.imgur.com/l3gusTE.png)


### 2. Notion-API 적용

참고 자료: https://developers.notion.com/docs/create-a-notion-integration

#### 2-1 Integration 생성

https://www.notion.so/my-integrations 에서 새로운 API 통합 생성


![](https://files.readme.io/90c7d2e-integration.gif)

#### 2-2 Secret Key 복사

![](https://i.imgur.com/HXqGQFj.png)

#### 2-3 Integration에 Page 권한 주기

![](https://files.readme.io/fefc809-permissions.gif)

> 안보일시 Notion 재접속

secret_DFdMaXbPq0xPb9d3KlJ0224NByxu5RqPryAw8S6M36a

