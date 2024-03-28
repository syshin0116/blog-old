---
layout: post
title: Docker Compose에서 Flask와 MySQL 연결 문제
date: 2024-03-27 22:54 +0900
categories:
  - ETC
  - Docker
tags: 
math: true
---
### 문제 상황

- WSL(Windows Subsystem for Linux) 환경에서 Docker Compose를 사용해 Flask(백엔드), MySQL(DB), Nginx(프록시) 컨테이너 설치
- MySQL에 `test@%` 계정을 만들고 proposalDB 권한 부여
- Flask에서 pymysql로 MySQL 접속 시도하지만 실패

### 해결 과정

#### 1. 네트워크 확인

- `docker network ls` 명령으로 생성된 네트워크 확인
- Flask와 MySQL 컨테이너가 동일 네트워크에 연결되어 있는지 확인

#### 2. MySQL 계정 및 권한 확인

- MySQL 컨테이너에 접속: `docker exec -it <mysql_container_name> mysql -u root -p`
- `SELECT User, Host FROM mysql.user;` 로 `kadap@%` 계정 존재 확인
- `SHOW GRANTS FOR 'test'@'%';` 로 proposalDB 권한 확인

#### 3. Flask 코드 확인

- MySQL 연결 정보(호스트, 포트, 사용자, 비밀번호) 올바른지 확인
- 호스트는 MySQL 컨테이너 이름 또는 Docker 내부 IP 사용

#### 4. 방화벽 확인

- WSL 환경에서 방화벽 활성화 시 MySQL 포트(3306) 열려 있는지 확인

#### 5. 로그 확인

- Flask 애플리케이션 및 MySQL 로그 확인하여 추가 정보 얻기

#### 6. MySQL 계정 확인

- `kadap@%` 계정에 proposalDB 전체 권한 부여되어 있음
- 네트워크 연결 문제일 가능성 높음

#### 7. 네트워크 확인 및 코드 수정

- `docker network ls`로 Docker 네트워크 확인
- `docker ps`로 MySQL 컨테이너 이름/IP 확인
- Flask 코드에서 MySQL 연결 부분 수정: `mysql://kadap:비밀번호@<mysql_container_name_or_ip>/proposalDB`

#### 8. 컨테이너 재시작

- Flask 및 MySQL 컨테이너 재시작: `docker restart <flask_container_name> <mysql_container_name>`

#### 9. MySQL 계정 추가 (선택)

- `test@localhost` 계정 추가로 생성하여 보안 강화 가능


