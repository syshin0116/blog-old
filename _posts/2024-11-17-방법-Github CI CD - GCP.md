---
layout: post
title: "[방법]Github CI/CD - GCP"
date: 2024-11-17 16:24 +0900
categories:
  - ETC
  - Github
tags: 
math: true
---

## 사전 준비

1 GCP 계정 및 Compute Engine 인스턴스
2 Docker Hub 계정
3 GitHub 계정 및 Repository


## CI/CD를 위한 큰 순서

### 1. 초기 환경 준비

- 1-1 GCP Compute Engine 인스턴스 생성 및 설정
    - GCP에서 VM 인스턴스를 생성하고 Docker, Docker Compose 설치
    - 필요한 포트(예: 80, 443, 8000, 3306) 열기
    - SSH 키를 설정해 원격 접속 준비
- 1-2 Docker Hub 계정 및 레포지토리 준비
    - Docker 이미지를 저장할 Docker Hub 계정과 Private/Public 레포지토리 생성

### 2. 로컬 환경에서 Docker 이미지 빌드

- 애플리케이션 코드와 Dockerfile을 사용해 로컬에서 Docker 이미지를 빌드
- 로컬에서 이미지가 정상적으로 작동하는지 확인

### 3. GitHub Actions 설정

- GitHub 저장소에 워크플로우 파일 (`github/workflows/deployyml`) 추가
- GitHub Secrets에 Docker Hub와 GCP의 민감 정보 등록

### 4. GitHub Actions 워크플로우 파일 작성

- .github/workflows/deploy.yml 파일을 생성
- Push가 성공적으로 수행되면 GCP에서 사용할 준비가 완료

### 5. 테스트
- GitHub Actions 실행 확인
- Docker Hub에서 푸시된 이미지 확인
- GCP 서버에서 컨테이너 확인


## 1. 초기 환경 준비
### 1-1 GCP Compute Engine 인스턴스 생성 및 설정
- GCP에서 VM 인스턴스를 생성하고 Docker, Docker Compose 설치
- 필요한 포트(예: 80, 443, 8000, 3306) 열기
- SSH 키를 설정해 원격 접속 준비

### 1-2 Docker Hub 계정 및 레포지토리 준비
- Docker 이미지를 저장할 Docker Hub 계정과 Private/Public 레포지토리 생성


#### Docker Hub 레포지토리 생성
1. 로그인 후 **Repositories** 탭을 클릭

![](https://i.imgur.com/yRYqs6j.png)
2. **Create Repository** 클릭, **레포지토리 설정**
	• **Name**: 레포지토리 이름 입력 (예: fastapi-image, nginx-image)
	• **Description (Optional)**: 간단한 설명 추가 (예: “FastAPI Docker Image”)
	• **Visibility**: Public 또는 Private 선택:
		• **Public**: 누구나 이미지를 볼 수 있음
		• **Private**: 권한이 있는 사용자만 접근 가능 (보안을 위해 권장)

![](https://i.imgur.com/0IoEjzc.png)

3. **Create Repository** 버튼 클릭

## **2. 로컬 환경에서 Docker 이미지 빌드**

### 2-1. **Dockerfile 작성**

로컬에서 사용할 Dockerfile을 준비합니다. 여기서는 FastAPI와 Nginx를 예로 들어 설명합니다.

#### Dockerfile 예시 - `docker/Dockerfile.fastapi`
```Dockerfile
# FastAPI Dockerfile
FROM python:3.11-slim

WORKDIR /code

# Poetry 설치
RUN pip install poetry

# pyproject.toml 및 poetry.lock 복사
COPY ./fastapi/pyproject.toml ./fastapi/poetry.lock /code/

# 의존성 설치
RUN poetry install --no-root

# FastAPI 소스 코드 복사
COPY ./fastapi/ /code

# FastAPI 서버 실행
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

#### Dockerfile 예시 - `docker/Dockerfile.nginx`
```Dockerfile
# Nginx 기반 이미지
FROM nginx:alpine

# Nginx 설정 복사
COPY ./docker/nginx.conf /etc/nginx/nginx.conf
```


### 2-2. **Docker Compose 테스트**

로컬에서 여러 컨테이너를 실행하기 위해 `docker-compose.yaml`을 사용합니다.

#### 로컬용 `docker-compose.yaml`

```yaml
version: '3.8'

services:
  fastapi:
    build:
      context: .
      dockerfile: ./docker/Dockerfile.fastapi
    container_name: fastapi
    ports:
      - "8000:8000"
    volumes:
      - ./fastapi:/app

  nginx:
    build:
      context: .
      dockerfile: ./docker/Dockerfile.nginx
    container_name: nginx
    ports:
      - "80:80"
    depends_on:
      - fastapi

```


### 2-3. **로컬에서 빌드 및 테스트**

1. **Docker Compose로 컨테이너 빌드**:
    
    `docker-compose build`
    
2. **컨테이너 실행**:
    
    `docker-compose up`
    
3. **테스트**:
    
    - 브라우저에서 `http://localhost`로 Nginx를 통해 FastAPI가 작동하는지 확인
    - FastAPI는 기본적으로 `http://localhost:8000`에서 작동하며, Nginx가 이를 리버스 프록시로 연결

### 2-4. **Docker Hub에 Push 준비**

1. Docker 이미지 태그 설정:
    
```bash
docker tag <이미지-ID> <dockerhub-username>/<repository-name>:<tag>
```
    
예:
```bash
docker tag modular-rag-fastapi:latest syshin0116/modular-rag:fastapi-latest
docker tag modular-rag-nginx:latest syshin0116/modular-rag:nginx-latest
```

    
2. Docker Hub에 Push 테스트:
    
```bash
docker push mydockerhubuser/fastapi-image:latest 
docker push mydockerhubuser/nginx-image:latest
```

예:
```bash
docker push syshin0116/modular-rag:fastapi-latest
docker push syshin0116/modular-rag:nginx-latest
```

![](https://i.imgur.com/HFlbG0d.png)


3. Push가 성공했는지 Docker Hub에서 확인
    - FastAPI와 Nginx 컨테이너가 정상적으로 실행되고 통신이 되는지 확인
	- Nginx가 FastAPI를 리버스 프록시로 설정했는지 확인
	- Docker 이미지를 Docker Hub에 Push하여 공유 가능한 상태인지 확인

## 3. GitHub Actions 설정

- GitHub 저장소에 워크플로우 파일 (`github/workflows/deployyml`) 추가
- GitHub Secrets에 Docker Hub와 GCP의 민감 정보 등록

#### 3-1. GitHub Secrets 설정

1. **GitHub Secrets에 민감 정보 등록**
    - GitHub 저장소의 **Settings > Secrets and variables > Actions**에서 **New repository secret**을 클릭.
    - 다음 정보를 추가:
        - `DOCKER_USERNAME`: Docker Hub 사용자명
        - `DOCKER_PASSWORD`: Docker Hub 비밀번호
        - `GCP_IP`: GCP Compute Engine 외부 IP 주소
        - `GCP_USERNAME`: GCP VM 인스턴스의 사용자 이름 (`ubuntu` 또는 `gcp-user` 등)
        - `GCP_SSH_KEY`: GCP VM 접속에 사용하는 SSH 프라이빗 키



### `GCP_IP`, `GCP_USERNAME`, `GCP_SSH_KEY` 정보를 얻는 방법

#### **1. `GCP_IP`: GCP Compute Engine 외부 IP 주소**

GCP에서 생성된 Compute Engine 인스턴스의 **외부 IP 주소**를 얻는 방법.

1. **GCP Console 접속**:
    - GCP Console에 로그인
2. **Compute Engine으로 이동**:
    
    - 좌측 메뉴에서 **Compute Engine > VM 인스턴스**를 클릭
3. **외부 IP 주소 확인**:
    
    - 생성된 VM 인스턴스 리스트에서 **외부 IP**(External IP) 열을 확인

---

#### **2. `GCP_USERNAME`: GCP VM 인스턴스의 사용자 이름**

1. **SSH로 직접 접속해서 확인**: SSH를 사용하여 VM에 접속한 뒤, 현재 사용자 이름을 확인:

```bash
whoami
```    
   
- 출력된 값이 `GCP_USERNAME` 이다. 
1. **커스텀 사용자 이름 설정** (선택):
    - SSH 키를 등록하거나 VM을 생성할 때 사용자 이름을 커스텀으로 설정할 수 있다

---

#### **3. `GCP_SSH_KEY`: GCP VM 접속에 사용하는 SSH 프라이빗 키**

`SSH 프라이빗 키`는 **GCP VM에 접속하기 위해 필요한 비밀 키**다

##### **방법 1: 새 SSH 키 생성**
1. **로컬 머신에서 SSH 키 생성**:
    
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- 기본 경로는 `~/.ssh/id_rsa`.
- 생성된 키 쌍:
	- **`~/.ssh/id_rsa`**: 프라이빗 키 (GitHub Secrets에 등록)
	- **`~/.ssh/id_rsa.pub`**: 공개 키 (GCP에 등록)

1. **공개 키를 GCP에 등록**:
    
    - GCP Console에서 **VM 인스턴스 > SSH 키** 섹션으로 이동
    - **Edit** 버튼 클릭 후, 공개 키(`~/.ssh/id_rsa.pub`)의 내용을 붙여넣고 저장

2. **GitHub Secrets에 프라이빗 키 등록**:
    
    - `~/.ssh/id_rsa`의 내용을 복사하여 GitHub Secrets에 **`GCP_SSH_KEY`**로 저장:
        `cat ~/.ssh/id_rsa`
        

##### **방법 2: 기존 SSH 키 확인**

- 이미 SSH 키를 생성한 적이 있다면:
    1. **프라이빗 키 경로 확인**: 기본 경로는 `~/.ssh/id_rsa`
    2. **GCP VM에 등록된 공개 키 확인**: GCP Console에서 **VM 인스턴스 > SSH 키** 섹션을 확인
    3. **GitHub Secrets에 프라이빗 키 등록**:
        `cat ~/.ssh/id_rsa`

![](https://i.imgur.com/UPdNQqy.png)


## 4. GitHub Actions 워크플로우 파일 작성

**GitHub Actions**를 설정하여, **Docker 이미지를 빌드 및 푸시**하고 **GCP 서버에 배포**하는 자동화 파이프라인을 구성

```yaml
name: CI/CD to Docker Hub, GCP Server

on:
  push:
    branches:
      - main  # main 브랜치에 Push 시 실행

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    # 1. 코드 체크아웃
    - name: Checkout code
      uses: actions/checkout@v4

    # 2. Docker Hub 로그인
    - name: Log in to Docker Hub
      run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

    # 3. Docker, Docker Compose 설치
    - name: Install Docker and Docker Compose
      run: |
        # Add Docker's official GPG key:
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc

        # Add the repository to Apt sources:
        echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
          $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
          sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    # 4. Docker Compose로 이미지 빌드
    - name: Build Docker images
      run: |
        docker compose build

    # 5. Docker 이미지 푸시
    - name: Push Docker images to Docker Hub
      run: |
        docker push syshin0116/modular-rag:fastapi-latest
        docker push syshin0116/modular-rag:nginx-latest

    # 6. GCP 서버로 배포
    - name: Deploy to GCP Server
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.GCP_IP }}
        username: ${{ secrets.GCP_USERNAME }}
        key: ${{ secrets.GCP_SSH_KEY }}
        script: |
          cd /home/syshin0116/modular-rag
          docker compose pull
          docker compose up -d --remove-orphans
```

> 버전 문제가 있어서 appleboy/ssh-action@master로 설정해주었다



## 5. .env 와 compose.yaml, nginx.conf 파일 서버에 생성


![](https://i.imgur.com/x2xZVKi.png)

## 6. 테스트

#### Github Push

![](https://i.imgur.com/r8zIJUn.png)
#### Github Actions 확인


![](https://i.imgur.com/hlsPPl5.png)

![](https://i.imgur.com/53YgSIb.png)
