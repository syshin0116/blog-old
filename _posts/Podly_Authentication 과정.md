---
layout: post
title: Podly_Authentication 과정
date: 2024-08-31 19:44 +0900
categories:
  - Project
  - Podly
tags: 
math: true
---

# Podly 인증 프로세스 요약

## 1. 소셜 로그인 (초기 인증)

- **프로세스**: 소셜 로그인 버튼 클릭 → 소셜 제공자 인증 → 백엔드로 인증 코드 전송
- **응답**: 
  ```json
  {
    "access_token": "...",
    "refresh_token": "...",
    "token_type": "bearer"
  }
  ```

## 2. 사용자 정보 조회

- **엔드포인트**: `GET /api/users/me`
- **헤더**: `Authorization: Bearer {access_token}`
- **응답**: 사용자 기본 정보 (ID, 이메일, 이름 등)

## 3. 인증된 요청

- 모든 인증 필요 요청에 access token 포함
- **헤더**: `Authorization: Bearer {access_token}`

## 4. token 갱신

- **엔드포인트**: `POST /api/auth/refresh`
- **헤더**: `Authorization: Bearer {refresh_token}`
- **응답**: 새로운 access token과 refresh token

## 5. 로그아웃

- **엔드포인트**: `POST /api/auth/logout`
- **헤더**: `Authorization: Bearer {access_token}`
- **프로세스**: 백엔드 token 무효화 → 프론트엔드 token 삭제

## 주요 보안 사항

- HTTPS 사용 필수
- 클라이언트: token 안전 저장 (HttpOnly 쿠키 권장)
- 서버: 모든 요청 시 token 검증

## token 수명

- access token: config에서 설정(60분)
- refresh token: config에서 설정(30일)
- access token이 5분 남았을때 refresh token을 사용하여 access token 재생성

