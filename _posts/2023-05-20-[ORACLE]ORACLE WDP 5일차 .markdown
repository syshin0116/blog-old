---
title: "[ORACLE-WDP]5일차-Oracle Architecture, 1. 소개, 2. 구조탐색"
date: 2023-05-20 20:00:00 +0900
categories: [Database,ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---


<!--#### 공유url: http://naver.me/xoKMlnp5
#### -->


# Exploring the Oracle Database Architecture
# 1. 소개
[01_오라클 과정 소개.pdf](https://github.com/syshin0116/Study/files/11521160/01_.pdf)

• 과정 목표 설명
• 과정 일정 설명
• HR 스키마 설명

## 1.1 과정 목표
• 오라클 아키텍처 설명
• 응용 프로그램 지원을 위한 데이터베이스 구성
• 데이터베이스 보안 관리 및 감사(audit) 구현
• 기본 백업 및 Recovery 절차 구현
• 데이터베이스 및 파일 간 데이터 이동
• 기본 모니터링 절차 적용 및 성능 관리
• 리소스 관리 및 작업 자동화
• Oracle Support 활용

## 1.2 과정 예제: HR 예제 스키마

![](https://velog.velcdn.com/images/syshin0116/post/ec2d91e1-3563-4884-acc4-ce8b798940f4/image.png)

# 2. 오라클 데이터베이스 구조 탐색
## 2.1 목표
• 오라클 기본 배경지식 설명
• 오라클 데이터베이스를 구성하는 주요 요소 설명
• 메모리 구조 설명
• 백그라운드 프로세스 설명
• 논리적/물리적 저장 영역 구조 상호 연관
• 플러그 가능한 데이터베이스 설명(멀티테넌트 아키텍처)
• ASM 저장 영역 구성 요소 설명

## 2.2 오라클 기본 배경지식
- 운영체제(OS)
- 프로그램
- 프로세스
- 메모리
	- 캐시기능
	- 버퍼기능
- 인스턴스
- 데이터베이스
- 오라클 서버
- SID(System Identifier)
- Service Name(데이터베이스명)
- 오라클이 지향하는 점

> ## 용어 정리:
#### 운영체제(OS):
오라클 입장에서의 운영체제의 역할
	- 자원 배분 역할
#### 프로그램:
디스크에 저장되어 있는 실행할 수 있는 바이너리 파일
#### 프로세스:
실행중인 프로그램
방식:
OS에게 프로그램 실행 요청
프로그램
	- 프로세스(1개 이상)
    - 메모리
    	1. 프로세스만 전용으로 사용하는 메모리 공간(PGA)
        2. 오라클과 같이 복잡도가 높은 프로그램인 경우
        	- 프로세스가 여러개 생성
            - 프로세스들 간에 공유할 수 있는 메모리 공간(SGA)
#### 메모리:
1. 캐시: 
	- 디스크에서 필요 자료를 메모리에 로딩/캐시/저장/기록
    - 두번째 필요시에는 디스크에 접근하지 않고 메모리에서 해당 데이터를 재사용
2. 버퍼:
	- 데이터를 한꺼번에 모았다가 디스크에 기록

#### 인스턴스:
프로세스 + 메모리를 통칭하는 용어
#### 데이터베이스:
물리적 파일(데이터 파일, 리두로그 파일, 컨트롤 파일)
#### 오라클 서버:
인스턴스(메모리 + 프로세스) + 데이터베이스(3개 파일)

## 2.3 메모리의 캐시 기능
- 메모리보다 매우 느린 Disk I/O
- 메모리는 나노 세컨드 속도
- 디스크는 밀리 세컨드 속도
	- 같은 데이터를 자주 사용할 경우 **데이터를 메모리에 저장(로딩, 적재, 캐시)** 해서 **빠르게 재사용**
- 디스크로부터 데이터를 **읽는 횟수를 줄여서** 성능 개선
- 캐시로 사용하는 메모리 영역
	- Shared Pool(라이브러리 캐시)
	- Shared Pool(데이터 딕셔너리 캐시)
	- Shared Pool(리절트 **캐시**)
	- 데이터베이스 버퍼 **캐시**
    
## 2.4 메모리의 버퍼 기능
- 메모리보다 매우 느린 Disk I/O
	- 메모리는 나노 세컨드 속도
	- 디스크는 밀리 세컨드 속도
- 디스크에 기록할 데이터들을 **모아서 한꺼번에 처리**
- 데이터를 디스크에 **기록하는 횟수를 줄여서** 성능 개선
- 버퍼로 사용하는 메모리 영역
	- 데이터베이스 버퍼 캐시
	- 리두 로그 버퍼
- 예) 동영상 재생 할 때(네트워크를 통해 동영상 자료를 미리 다운로드함)

## 2.5 Service Name와 SID의 관계
- Service Name : SID = 1 : N
- SID (System Identifier)
	**- 인스턴스의 식별자**
	- SID는 오라클 DB에서 유니크한 이름
	- 한 서버에 여러 개의 인스턴스를 사용하고자 하는 경우 **인스턴스마다 다른 SID 지정**
- Service Name(데이터베이스명)
	- 네트워크 내에서 데이터베이스를 특정하기 위한 명칭
	- RAC (Real Application Clusters) 같이 **여러 인스턴스를 하나의 DB로 서비스하는 경우 SID는 다르지만 모두 같은 Service Name을 사용**
- Service Name은 데이터베이스 명이라고도 함

## 2.6 Service Name과 SID를 확인 하는 법

#### 1. 오라클 인스턴스의 SID 확인하는 방법

```sql
select instance_name from v$instance;
select instance from v$thread;
```
리눅스 oracle 계정 :``` echo $ORACLE_SID```

#### 2. 오라클 Service Name, 데이터베이스명 확인하는 방법
```sql
select name, db_unique_name from v$database;

show parameter service_names;
```

#### 3. 오라클 버전 확인하는 방법
```sql
selct * from v&version;
```

## 2.7 오라클이 지향하는 점
- 다중 사용자 환경에서 높은 처리량 지향
- 사용자의 요구사항에 대한 빠른 응답속도
- commit한 데이터 보장
	- commit 직후 오라클에 장애 발생 하여도 보장
    - 리두 로그 파일을 통해 보장
> 리두 로그 파일이 있기 때문에 commit한 내용 보장도 되고, rollback도 가능하다
## 2.8 데이터베이스 Instance에 연결
- 연결: User Process와 Instance 간의 통신
- 세션: 오라클 DB에서 데이터 베이스 접속을 시작으로 **여러 작업**을 수행한 뒤 접속을 종료하기까지의 **전체기간**
	- 세션 > 트랜잭션 > DML
	- 동일한 유저일지라도 접속 할 때마다 세션이 생성됨

![](https://velog.velcdn.com/images/syshin0116/post/136acab1-baa5-491d-8255-58d7b1ee7be6/image.png)


> session 확인
```sql
select sid, serial#, username
from v$session
where username is not null
order by username;
```
![](https://velog.velcdn.com/images/syshin0116/post/63f483fb-ed6e-4114-bcea-7a96c697ff0d/image.png)


## 2.9 오라클 데이터베이스 Instance 구성
- **클러스터**란 두개 이상의 독립된 서버들과 **디스크를 하나로 연결하는 기법**
- 여러 개의 서버상에 기동 된 인스턴스를 하나의 데이터베이스처럼 사용가능
- 데이터의 일관성을 유지 하기위해 **스토리지는 공유함**
- RAC의 목적 : 데이터베이스의 **확장성, 가용성**을 높이기 위함

![](https://velog.velcdn.com/images/syshin0116/post/5acb66c8-0986-41aa-bbe8-83c35dc2ec6e/image.png)

## 2.10 오라클 서버의 구조: 개요
![](https://velog.velcdn.com/images/syshin0116/post/05d94ab7-ae90-4617-8da3-94ff5bfc3b17/image.png)

## 2.11 오라클 서버의 3대 요소 (메모리, 프로세스, 데이터베이스)

![](https://velog.velcdn.com/images/syshin0116/post/039df959-4479-4615-a400-352ea4712bb5/image.png)

> 동작 방식:
1. 리스너 시작
리스터: user process와 서버 프로세스를 연결하는 역할
2. 클라이언트에서 sql문을 날리면 서버 프로세스 동작
PGA: 서버 프로세스가 사용하는 메모리 공간
SGA: 공용으로 사용되는 메모리 공간



## 2.12 오라클 서버 / 인스턴스 / 데이터베이스
1. 오라클 서버
	- **오라클 인스턴스와 오라클 데이터베이스로 구성**
2. 오라클 인스턴스
	- **메모리 구조와 백그라운드 프로세스**로 구성
	- 오라클 데이터베이스를 액세스하는 수단
3. 오라클 데이터베이스
	- **데이터 파일**은 사용자의 실제 데이터와 시스템 데이터가 포함되어 있는 파일
		- Ex) HR, SCOTT 사용자의 테이블들이 물리적으로 저장
	- **리두 로그 파일**은 데이터베이스의 변경 이력을 기록
		- 장애가 발생했을 때 데이터를 복구하는데 사용
	- **컨트롤 파일**은 물리적인 데이터베이스 구조 정보와 오라클 서버의 일관성에 대한 정보를 관리

> 컨트롤 파일: 
사이즈는 작지만 중요한 정보들을 담고있음, 오라클이 버전업이 될 수록 많은 정보를 담을 것

## 2.13 유저 프로세스와 서버 프로세스
#### 1. 유저 프로세스
- 오라클 서버에 접속하는 클라이언트 프로그램을 실행하면 사용자의 컴퓨터에 생성되는 프로세스
- ex) sqlplus, SQL Developer
- 사용자의 SQL을 전달하고 실행결과를 받는 역할

#### 2. **서버 프로세스**
- 사용자가 요청한 SQL을 전달받아 처리하고 실행된
결과를 유저 프로세스에게 전달하는 역할
- SQL 파싱 및 실행계획 저장
- SQL의 결과 생성에 필요한 데이터를 데이터 파일로부터 데이터 버퍼 캐시로 블록 단위로 로딩
- 변경이력을 Redo Log Buffer 에 기록
- SQL의 결과를 전달하기 전에 정렬처리

## 2.14 백그라운드 프로세스
- 유저 프로세스의 요구에 따른 직접적인 처리를 하지않고 **각자 담당하고 있는 고유역할 수행**
- **필수** 백그라운드 프로세스
	- 데이터베이스 구동을 위해 반드시 필요한 프로세스
	- 한 개라도 문제 발생시 데이터베이스는 Shutdown 됨
	- DBWR, LGWR, CKPT, PMON, SMON등
- **선택** 백그라운드 프로세스
	- 특정 기능 사용을 위한 선택 가능한 프로세스
	- ARCn(Archiver), Snnn(Shared Server) 등

> 전통적인 프로세스: DBWR, LGWR, CKPT, PMON, SMON
## 2.15 리스너 프로세스
1. 리스너는 클라이언트 프로그램에서 네트워크를 통해 송신된 인스턴스로의 접속을 수신하는 프로세스
2. 접속 요청을 수신한 리스너는 유저 프로세스와 서버 프로세스를 연결 시켜 줌
3. 원격접속
- 리스너를 통해 접속하는 형태
- ex) ```sqlplus hr/hr@orcl```
4. 로컬접속
- 같은 서버 안에서 리스너를 통하지 않고 접속
- ex) ```sqlplus hr/hr```

## 2.16 오라클 데이터베이스 메모리 구조:개요
![](https://velog.velcdn.com/images/syshin0116/post/1318cf40-e1f0-4a0c-a16b-84eef7d48fd6/image.png)
> SGA는 System Global Area이지만 Shared Global Area라고도 부른다
중요도:
1. Shared Poo
2. 데이터베이스 버퍼 캐쉬
3. 리두 로그

## 2.17 SGA(System Global Area)

1. **백그라운드 / 서버 프로세스가 작업하는 공유 메모리 영역**
2. Shared Global Area 라고도 함
3. SGA는 여러 메모리 구조로 구성
 	- Shared Pool
	- Data Buffer Cache
    - Redo Log Buffer
	- Large Pool, Java Pool, Stream Pool
4. **SGA 할당량 조회**
	- SQL> SHOW SGA
    ![](https://velog.velcdn.com/images/syshin0116/post/3fc54416-4182-4fe0-8d6f-aff98c5922bf/image.png)

5. **SGA의 상세 정보**
	- SQL > SELECT * FROM V$SGASTAT;
    ![](https://velog.velcdn.com/images/syshin0116/post/5debe0ac-dd0b-44aa-8e0e-fb70d6a8e65d/image.png)

    
## 2.18 Shared Pool
1. 데이터 블록 이외의 공유 가능한 데이터를 임시로 보관하기 위한 메모리 영역
2. 라이브러리 캐시
	- **SQL 실행계획 저장 및 공유**
3. 데이터 딕셔너리 캐시
	- 딕셔너리 정보 저장 및 공유
4. 리절트 캐시
	- SQL 쿼리 결과값 저장
![](https://velog.velcdn.com/images/syshin0116/post/b1abefc2-de1a-4c88-aa23-2abb3d166323/image.png)
> Shared Pool에서 가장 중요한 부분: 라이브러리 캐시
라이브러리 캐시, 데이터 딕셔너리 캐시: 그 어떤 유저가 접속해도 실행된다

## 2.19 Shared Pool 관련 프로세스
- 서버 프로세스
	- SQL 파싱 및 실행계획 저장
![](https://velog.velcdn.com/images/syshin0116/post/1b4d1135-7b9b-4b88-a750-4ab39cac495f/image.png)

## 2.20 SQL 파싱 과정
#### 사용자가 SQL 문장을 실행

1. 문장 확인(Syntax)
	- SP2-0734 에러 
    ```ex) sel empno frm emp;```
2. Semantic 확인
	- SQL에 사용된 테이블명, 컬럼명이 맞는지 권한이 있는지 이터 딕셔너리를 참조하여 확인
	- ORA-00942 에러 
    ex) ```select empno from empX;```
3. 기존에 동일한 SQL이 수행된 적이 있는지 확인
	- 소프트 파싱 : SQL의 실행계획이 있으면 재사용
	- 하드파싱 : SQL 수행이력이 없거나 LRU 의해 버려진 경우
4. 실행계획 생성(Optimization)
	- SQL을 어떤 방식으로 실행할 것인지 최단경로 선택

**실행계획을 생성할 때 많은 CPU 자원을 사용**
-> 가능하면 재사용하는것(소프트 파싱)이 효율적

> 소프트파싱 하드파싱차이: 캐쉬가 있으면 재사용하여 소프트 파싱, 없으면 하드 파싱으로 진행 

## 2.21 SQL 파싱 완료 후

- 파싱된 SQL 문장과 실행계획이 라이브러리 캐시에 저장
	- 공유 SQL 영역(Shared SQL Area)
	- 공유 Pl/SQL 영역(Shared PL/SQL Area)
- 동일한 SQL을 사용하는 사용자들에게 **실행계획을 공유 및 재사용**

** \* Shared Pool의 가장 중요한 역할 \* **
- **실행계획 공유 및 재사용**
- CPU 자원의 절약 효과
	- 실행계획을 생성하려면 많은 CPU 자원을 사용
    
## 2.22 LRU(Least Recently Used) 알고리즘
- 사용자가 실행한 모든 SQL를 저장할 수 없음
- 메모리의 공간은 유한하기 때문
	- 메모리는 상대적으로 비싼 자원
- 오라클은 LRU 알고리즘을 이용하여 SQL을 보관
	- SQL 문장들 가운데 가장 최근까지 자주 사용된 SQL 문장들만 보관
	- 마지막에 사용하고 가장 오랫동안 사용이 안된 SQL을 메모리에서 삭제하여 저장 공간 확보
	- 최근에 가장 적게 사용한 것을 스케줄링
>오라클의 메모리 저장, 캐싱 알고리즘!!
## 2.23 Shared Pool(Library Cache)
1. 파싱한 SQL 정보(실행계획)와 컴파일된 PL/SQL 코드 저장
2. 저장된 실행계획은 다른 사용자와 **공유 및 재사용**됨
	- SQL 처리 속도 향상
	- 요청한 SQL에 대한 빠른 응답
3. 관련 초기화 파라미터
	- shared_pool_size
4. 관련 뷰
	- v$sql, v$sqlarea

## 2.24 Shared Pool(Dictionary Cache)
1. SQL 파싱 과정의 semantic 검사단계에서 서버 프로세스는 데이터 딕셔너리에서 객체 명, 접근권한 등을 참조
2. SQL 파싱 과정에서 참조된 데이터 딕셔너리 오브젝트 정보를
저장하는 공간
3. 딕셔너리 캐시에 저장되는 정보
	- 모든 테이블과 뷰의 이름
	- 테이블의 컬럼명과 데이터 타입
	- 모든 사용자의 권한 등 객체에 대한 정보
	- 오라클 내부의 구성정보
4. 데이터 딕셔너리 정보를 메모리에 캐시 하면 SQL과 DML에 대한 응답 시간을 줄이는 효과 발생

5. 데이터 딕셔너리 캐시 공간 확인
```sql
select 	pool, name, bytes/1024/1024 MB
from 	v$sgastat
where 	name = 'row cache';
```
6. 데이터 딕셔너리 히트 율
```sql
select 	( 1-(sum(getmisses)/sum(gets))) * 100 "ratio"
from 	v$rowcache;
```
	- 파싱 작업에서 Data Dictionary에 대한 데이터를 요구 했을 때
Cache에서 읽은 횟수(GETS)와 Cache에 없어서 디스크 I/O를
진행했을 때(GETMISSES)의 비율

## 2.25 데이터 딕셔너리가 저장된 곳
1. SYS가 소유자
2. SYSTEM 테이블 스페이스에 저장 되어있음
  ```sql
  select 		t.ts#, t.name tablespace_name, d.name file_name
  from 		v$tablespace t
  join 		v$datafile d
  on 			t.ts# = d.ts#
  order by 	t.ts#;
  ```
![](https://velog.velcdn.com/images/syshin0116/post/4f829331-bc01-42ab-b6e9-77ff840e5514/image.png)

3. SYSTEM 테이블 스페이스를 구성하는 테이블 조회
  ```sql
  select 	owner, tablespace_name, table_name
  from 	dba_tables
  where 	owner = 'SYS'
          and 	tablespace_name = 'SYSTEM';
  ```
![](https://velog.velcdn.com/images/syshin0116/post/74c2b889-3ae4-496a-8bfb-1a616c78b1a0/image.png)


## 2.26 SQL문과 프로그래밍언어의 차이
1. 프로그래밍 언어는 **프로그래머가 처리 방법을 기술**
2. SQL문은 **처리 방법을 기술하지 않음**
3. **옵티마이저**가 가장 효율적인 방법으로 SQL을 수행할 최적의 처리 경로를 생성
	- 비용기반 알고리즘을 사용
	- 처리 시간, I/O 횟수가 가장 작다고 예측되는 방법 선택
	- 비용이란 처리에 필요한 시간 또는 자원 사용량
	- 시간을 예측하기 위해 통계정보를 활용
		- 테이블내 로우 건수, 데이터 량, 컬럼의 최소/최대 값 등
4. 실행계획에는 인덱스 사용여부,
테이블의 검색순서, 조인 방법이 포함
> 옵티마이저의 역할: 
여러 방법들을 실행해 보고 가장 효율적인 방법으로 결정, 실행


## 2.27 데이터베이스 버퍼 캐시
1. SGA의 일부
2. 데이터 파일에서 읽은 데이터 블록 복사본을 보관함
3. 모든 유저가 동시에 공유함

![](https://velog.velcdn.com/images/syshin0116/post/7d077b3b-827b-4c3e-9ae0-677cb410bd4f/image.png)

4. 사용자가 SQL를 실행하면 쿼리 결과 값을 가지는 데이터
파일에서 읽은 데이터 블록 복사본을 저장함
5. 이후 같은 데이터 블록을 요구하는 SQL은 데이터베이스 버퍼
캐시에 있는 해당 블록을 읽어서 처리
6. 디스크 I/O 없이 메모리에서 블록 읽기는 성능 향상 효과
	- **SGA 영역 중에서 데이터 버퍼 캐시가 가장 큰 크기의 공간을 할당 하는 이유**
    
![](https://velog.velcdn.com/images/syshin0116/post/65b51e29-0646-4dc5-b5c4-d0e629bd16b3/image.png)

## 2.28 데이터베이스 버퍼 캐시 관련 프로세스
1. 서버 프로세스
	- 디스크로부터 데이터 블록을 읽어서 데이터 버퍼 캐시에 저장
2. DBWR 백그라운드 프로세스
	- 데이터 버퍼 캐시에 있는 변경 완료된 블록을 디스크로 기록
![](https://velog.velcdn.com/images/syshin0116/post/fb7f1eb3-29fc-4df1-9f24-2d6e50abd304/image.png)

> DBWR: DB Writer

## 2.29 다양한 블록 크기 설정
- 기본적인 데이터 블록의 크기 확인 방법(EX. 8KB)
  ```sql
   show parameter DB_BLOCK_SIZE;
  ```
  
- 다양한 크기의 데이터 블록을 설정하여 사용가능
  ```sql
  show parameter K_CACHE_SIZE
  ```
  - 2K, 4K, 8K, 16K, 32K 데이터 블록 크기
  - 테이블스페이스 생성 시 데이터 블록 크기 설정 가능
  - 블록 크기에 맞는 db_nk_cache_size 설정이 우선되어야 테이블 스페이스를 생성 가능

## 2.30 데이터베이스 버퍼 캐시 구성
1. Default 버퍼 풀
	- 기본 데이터베이스 버퍼 캐시
	- 기본적으로 생성됨
2. Keep 버퍼 풀
	- 자주 사용하는 테이블/인덱스를 저장
	- Default 버퍼 풀에 있는 경우는 LRU 알고리즘에 의해 나가야 하는 상황 발생을 방지 하기 위함
    ```sql
    alter table scott.emp storage(buffer_pool keep);
    ```
3. Recycle 버퍼 풀
	- 자주 사용되지 않는 테이블을 저장
    ```sql
    alter table scott.emp storage(buffer_pool recycle);
    ```
> Default 버퍼 풀 중심으로 공부

## 2.31 리두 로그 버퍼
1. 사용자가 DML, DDL 문을 실행하여 DB에 저장된 값 혹은 DB의 구조 변경이 생기는 경우 모든 변경 이력을 리두로그 버퍼에 저장
2. commit 되는 순간 즉시 LGWR에 의해 리두 로그 파일로 기록
3. 리두 로그 파일의 목적
	**- 데이터베이스 장애 발생 시 복구를 위함**
4. 순환 버퍼: 순차적으로 기록하고 마지막 항목이 다 채워지면 처음으로 돌아가서 덮어쓴다.
![](https://velog.velcdn.com/images/syshin0116/post/c5187f3f-522e-46b4-ac56-615cdf036bda/image.png)
5. Write-Ahead (선 로그 기법)
	- DML (update, delete, insert)이 수행되면 데이터 버퍼 캐시보다** 먼저 Redo Log Buffer에 저장**
	- DBWR가 더티 버퍼를 디스크에 기록하기 전에 LGWR이 **먼저** 호출되어 리두 로그 버퍼의 정보를 **리두 로그 파일에 기록**
6. Log force at commit
	- commit 후 **즉시** 리두로그 버퍼 정보를 **리두 로그 파**일에 기록
    

## 2.32 리두 로그 버퍼 관련 프로세스
1. 서버 프로세스
	- 사용자의 DML, DDL 변경이력을 리두 로그 버퍼에 저장
2. LGWR 백그라운드 프로세스
	- 특정 조건을 만족 할 때 리두 로그 파일에 기록
	- 대표적으로 사용자가 commit 할 때
![](https://velog.velcdn.com/images/syshin0116/post/be231c9d-ceaf-4c04-9ce0-9257f2be16ba/image.png)

## 2.33 Large Pool
다음을 위한 대규모 메모리 할당을 제공합니다.
- **프로세스간 크기가 큰 데이터를 주고받을 때 이용**
- Shared Server 접속 시 서버 프로세스간 통신
- 대용량 테이블을 조회 시 사용하는 병렬 쿼리에서 사용
- 오라클 데이터베이스 백업 및 복원 작업
- **공유 풀과는 달리 재사용 되지 않으므로 LRU 적용 안함**
![](https://velog.velcdn.com/images/syshin0116/post/ed83bdd0-a6cd-4d36-b81a-ea281facd552/image.png)

## 2.34 Java Pool

- 오라클 JVM을 실행할 때 사용하는 메모리 영역
- Java Pool 메모리는 JVM의 모든 세션 별 Java 코드 및 데이터를 저장하는 데 사용
![](https://velog.velcdn.com/images/syshin0116/post/2c803c75-b2cd-42d3-99a5-4bc28c1e8cfc/image.png)

## 2.35 Streams Pool
Streams Pool 메모리는 Oracle Streams에서 다음 작업 전용으로 사용된다
1. 버퍼링된 큐 메시지 저장
2. Oracle Streams 프로세스용 메모리 제공
![](https://velog.velcdn.com/images/syshin0116/post/fcc4c708-9e45-4505-b404-c4c0710f9b1b/image.png)

## 2.36 PGA(Program Global Area)
![](https://velog.velcdn.com/images/syshin0116/post/8b6cc36a-f409-45a5-b379-b28297f33b0e/image.png)

1. 세션을 생성한 사용자 프로세스의 요구를 처리하기 위한 서버 프로세스가 사용하는 메모리 공간
2. SQL 작업공간(Work Area)
	- 정렬 작업을 수행하기 위해 사용되는 공간
	- 정렬 작업 공간이 부족하게 되면 임시 테이블스페이스의 임시 세그먼트를 사용하여 정렬을 진행(디스크 정렬)
	- **메모리 정렬이 디스크 정렬보다 성능상 유리**
3. 세션정보 : 사용자 세션 정보 저장
4. 커서 정보 : SQL의 파싱 정보를 저장하는 커서의 주소 저장
5. 변수 저장 공간 : SQL에서 바인드 변수의 값을 저장
6. PGA = UGA + 변수 저장 공간
> PGA and UGA
What is PGA and UGA in Oracle?
pga and uga is always a server side concept. they are oracle memory regions. pga is PROCESS global area, it is in dedicated and shared servers (never in the SGA) the uga is USER global area, it is session memory and it is in the PGA when using dedicated server, in the SGA when using shared server.

## 2.37 In-Memory 열 저장소: 소개
1. 메모리에 테이블 또는 파티션을 **통째로 In-Memory 열 저장소 올려서 Disk I/O 시간을 제거**하여 성능을 크게 개선
2. Row Format 이 아닌 **Column Format 으로 압축해서 로딩**
	- 컬럼 기준으로 반복되는 데이터를 압축 저장 시 매우
효율적인 구조
	- 압축률이 높아지면, 한정된 자원인 메모리에 더 많은 테이블을 로딩이 가능하고 메모리에서 데이터를 읽어올 때도 읽는 양을 줄여서 DISK I/O 감소로 속도 향상
3. Instant query 응답:
	- 열에서 **매우 큰 테이블**에 대한 Query 속도 증가(100x)
	- 스캔, 조인 및 집계 사용
	- 인덱스 없음
	- Analytics에 최적: 적은 수의 열, 많은 수의 행


## 2.38 In-Memory 열 저장소: 개요
- In-Memory 열 저장소
	- IM 열 저장소를 채우는 세그먼트는 열 형식으로 변환됩니다.
	- In-Memory 세그먼트는 버퍼 캐시와 트랜잭션별로 일관됩니다.
- 디스크에서는 행 형식으로 된 단 하나의 세그먼트
![](https://velog.velcdn.com/images/syshin0116/post/0c5c3c4b-2508-4ab3-a32c-2f267b8ebf8c/image.png)

## 2.39 In-Memory 열 저장소: 소개
#### Oracle 19c에서는 Oracle Database In-Memory에 대해 Oracle Database Resource Manager가 자동으로 활성화 됨
- INMEMORY_SIZE 초기화 매개 변수를 0보다 큰 값으로 설정
- 메모리 내 동적 스캔을 활용하려면 Resource Manager가 필요
- CPU 리소스 할당에 대한 향상된 성능 및 **자동 관리의 이점을 얻을 수 있음**
#### DBRM(Database Resource Manager Process)
- 리소스 계획을 설정하고 데이터베이스 리소스 매니저와 관련된 기타 작업들을 수행

## 2.40 전체 데이터베이스 In-Memory 캐시 저장
![](https://velog.velcdn.com/images/syshin0116/post/82398532-cc61-45ef-adcd-918f266115b3/image.png)

## 2.41 Memoptimize pool : 소개
1. Memoptimize pool은 선택적 구성 요소
2. MEMOPTIMIZE FOR READ로 지정된 힙 구성 테이블에 대한 버퍼 및 관련 구조를 저장함
3. 이 구조는 SELECT * FROM emp WHERE empno = 10과 같은 key 기반 쿼리에 대해 높은 성능과 확장성을 제공함
4. 엔드 투 엔드 응답 시간을 줄이기 위해 클라이언트는 요청된 버퍼를 네트워크를 통해 SGA에서 직접 끌어와 CPU 및 OS의 오버헤드를 방지함
5. 애플리케이션은 코드를 변경할 필요 없이 memoptimize pool의 이점을 누릴 수 있음
6. Memoptimize buffer area
	- 디스크 I/O를 방지하기 위해 memoptimize pool에 존재하는 MEMOPTIMIZE FOR READ 테이블에 대한 버퍼를 영구적으로 잠금
	- memoptimize 버퍼는 db buffer cache의 버퍼와 동일한 구조를 사용함
	- memoptimize pool의 버퍼는 db buffer cache와 완전히 분리되어 db buffer cache 크기에 반영되지 않음
	- memoptimize buffer area는 memoptimize pool의 75%를 차지함
7. Hash index
	- Hash index는 비 지속적인(non-persistent) 세그먼트 구조
	- Hash index를 여러 비 연속 메모리 단위로 할당함
	- 각 단위에는 여러 개의 해시 버킷이 포함되어 있음
	- 별도의 맵 구조는 메모리 단위를 기본 키와 연관시킴
	- 해시 인덱스는 memoptimize pool의 25%를 차지함    
  
## 2.42 ASMM (Automatic Shared Memory Management)
1. SGA에서 Redo Log Buffer를 제외한 데이터베이스 버퍼 캐시, 공유 풀, 라지 풀 등의 크기를 자동으로 조절하는 기능
2. MMAN는 현재 SGA의 Workload를 보고 메모리가 충분한곳, 부족한곳을 판단하여 적절하게 재배치 함
3. SGA_TARGET를 0보다 큰 값으로 설정할 때 작동
4. 자동 튜닝 되는 영역
	- DB_CACHE_SIZE
	- SHARED_POOL_SIZE
	- LARGE_POOL_SIZE
	- JAVA_POOL_SIZE
	- STREAMS_POOL_SIZE
5. SGA와 PGA를 자동으로 조절하는 기능
6. AMM 기능을 활성화하면 오라클은 SGA와 PGA의 합계 크기가 SGA_MEMORY_TARGET에 설정한 값 안에서 상황에 따라 적절하게 자동으로 사이즈 조절
7. SGA_MEMORY_TARGET, MEMORY_MAX_TAGER 이 0보다 큰 값으로 설정할 때 작동

## 2.43 프로세스 아키텍처
#### User process
	- 오라클 데이터베이스에 연결하는 응용 프로그램 또는 도구
#### 서버 프로세스: Oracle Instance에 연결되며
	- 유저가 세션을 설정하면 시작됩니다.
#### 백그라운드 프로세스
	- Oracle Instance가 시작될 때 시작됩니다.
#### Daemon/응용 프로그램 프로세스
	- 네트워킹 리스너
	- Grid Infrastructure Daemon
    
## 2.44 프로세스 구조
![](https://velog.velcdn.com/images/syshin0116/post/29a7244a-810f-4eda-a5cf-04e3cd26a73a/image.png)

## 2.45 DBWn(데이터베이스 기록자 프로세스)
1. 데이터베이스 버퍼 캐시의 수정된(더티) 버퍼를 다음과 같이 디스크에 기록한다.
	- 다른 처리를 수행하는 동안 비동기적으로 기록
	- 체크포인트 이벤트 발생시
![](https://velog.velcdn.com/images/syshin0116/post/a9577414-1ee3-41b0-b6e1-a613aed5ed0f/image.png)
2. DBWR 의 특징
	- Deferred Write(지연쓰기)
		- Dirty 버퍼 발생 즉시 디스크에 기록하지 않고 여러 개의 변경된 Dirty 버퍼를 모아서 한번에 디스크로 저장, **I/O 감소**
	- Faster Commit(빠른 커밋)
		- **commit 시 로그 정보는 즉시 디스크에 기록 하고 Dirty 버퍼는 지연 쓰기 함**
3. 디스크에 기록 하는 대표적인 경우
	- 체크포인트 이벤트 발생
	- 더티 버퍼가 임계 값에 도달
	- 사용 가능한 버퍼가 없는 경우
    
> 지연쓰기: 로그 정보를 기록한 뒤에 버퍼 작업이 진행됨

## 2.46 데이터베이스 버퍼 캐시의 상태
1. Dirty : 변경 완료되어서 디스크로 기록하기를 대기하는 상태
2. Pinned : 현재 작업중인 버퍼
3. Free/Unused : 사용 안하고 있는 버퍼, 언제든 사용 가능
4. Clean : 변경이 완료된 후 디스크에 기록된 버퍼로 다시 기록될 수 있는 상태의 버퍼
![](https://velog.velcdn.com/images/syshin0116/post/2a954ac3-11f1-45fe-b834-7ece9d3e058a/image.png)

## 2.47 LGWR(로그 기록자 프로세스)
1. 리두 로그 버퍼를 디스크의 리두 로그 파일에 기록합니다.
	- User Process가 트랜잭션을 커밋할 때
	- 온라인 리두 로그 스위치가 발생할 때
	- 리두 로그 버퍼가 1/3 찼거나 1MB의 버퍼된 데이터를 포함할 때
	- DBWn 프로세스가 디스크에 수정된 버퍼를 쓰기 전에
	- 마지막 쓰기 작업 후 3초가 지났을 때
2. 여러 개의 LGWn을 이용하여 병렬로 빠르게 로그를 기록
![](https://velog.velcdn.com/images/syshin0116/post/68e5ecf7-0ec4-4104-b8ff-2de93033a5d3/image.png)
3. 왜 변경된 데이터에 대한 REDO 로그를 먼저 디스크에 기록 하고 실제 변경된 데이터의 기록은 나중에 하는가?
4. 장애 발생시 데이터베이스 복구를 위해
	- **“오라클은 commit 된 데이터를 보장한다.”**
5. 리두 로그를 디스크에 저장하는게 더 빠르기 때문
	- 리두 로그는 블록에 순차적으로 변경이력을 기록
	- 데이터 버퍼 캐시의 블록은 불필요한 데이터도 포함
		- ex) select empno from scott.emp where empno = 7369;
		- 하나의 empno 를 조회하기 위해서는 8K 블록이 사용됨
	- 상대적으로 디스크 I/O가 적게 발생함
	- commit 에 대한 완료 메시지를 빠르게 응답 할 수 있음
		- **“오라클은 빠른 응답 속도를 지향”**

## 2.48 REDO 로그 파일의 순환 기록
![](https://velog.velcdn.com/images/syshin0116/post/2ce4852e-4212-4f41-981a-cd8ae29b4310/image.png)

- 리두 로그 멤버 : 리두 로그 버퍼의 내용을 기록하는 파일
	리두 로그 멤버는 하나의 리두 로그 파일
- 리두 로그 그룹 : 동일한 로그 기록을 저장, 리두 로그 멤버들의 집합을 의미
- 로그 스위치 : REDO 로그 파일을 순환하는 처리
- **로그 스위치시 데이터는 덮어쓰게 된다.**

## 2.49 CKPT(체크포인트 프로세스)
1. DBWn에게 더티 버퍼를 디스크에 기록하라고 요청
2. 체크포인트 정보
	- 어디까지 commit 된 더티 버퍼를
3. 디스크에 기록 하였는 지의 정보
4. 체크포인트 정보를 기록하는 위치:
	- Control File
	- 각 데이터 파일 헤더
5. 체크포인트가 발생하는 경우
	- 로그 스위치
	- 3초마다
	- 사용자 명령 등
6. 체크포인트 정보
	- 어**디까지 트랜잭션의 commit 된 데이터**를 디스크에 기록하였는 지의 정보
	- 오라클은 데이터베이스를 복구할 때 컨트롤 파일의 체크
	포인트 정보를 이용해 **복구의 시작 위치**를 알 수 있음
	- 데이터베이스의 일관성을 유지하기 위한 메커니즘

## 2.50 commit 한 데이터는 보장한다!
-  만약 체크 포인트를 수행하기 전에, 즉 commit 된 트랜잭션의 더티 블록이 디스크에 기록 되기전에 오라클 서버에 장애가 발생하면 commit 된 데이터는 손실이 있을까?
	- Redo 로그 파일이 손실되는 장애 경우 빼고는 손실 불가능
- 가능한 이유
	1. commit 한 데이터의 변경이력은 리두로그 파일에 기록되어 있음
	2. 어디까지 commit 된 데이터가 디스크에 기록 되었는지 컨트롤 파일의 체크포인트 정보로 알 수 있음
	3. 마지막으로 디스크에 기록된 commit 이후부터 리두로그 파일을
적용하여 복구 가능

## 2.51 SMON(시스템 모니터 프로세스)
- 정기적으로 인스턴스의 상태를 감시
- 인스턴트 시작 시 Recovery가 필요할 경우 Recovery 수행
- 사용하지 않는 임시 테이블 스페이스나, 세그먼트 정리 작업
![](https://velog.velcdn.com/images/syshin0116/post/22b83176-d59e-4f68-b2bb-71ff53f621c5/image.png)

## 2.52 PMON(프로세스 모니터 프로세스)
1. 유저 프로세스가 비정상적으로 종료되거나 실패했을 때 Recovery를 수행
2. 데이터베이스 버퍼 캐시 정리
	- User Process에서 사용하는 리소스 해제
3. 고아 프로세스나 좀비 프로세스를 정리하고 Idle 세션을 관리
![](https://velog.velcdn.com/images/syshin0116/post/f1918930-10a4-4fb3-839d-5703942c6ab3/image.png)

## 2.53 RECO(복구자 프로세스)
- 분산 데이터베이스 환경에서 사용
- 분산 데이터베이스에서 시스템 장애나 네트워크 문제로 인해 트랜잭션을 실패했을 때 자동으로 해결
- 문제가 발생한 트랜잭션이 사용하던 테이블, 행의 락 해제
- In-Doubt(불확실한) 분산 트랜잭션과 관련된 다른 데이터베이스에 자동으로 연결
![](https://velog.velcdn.com/images/syshin0116/post/88dfafa6-f2a5-4a24-a09c-272c39852113/image.png)

## 2.54 LREG(리스너 등록 프로세스)
- 인스턴스가 시작되었을 때 리스너에게 DB에 대한 정보를 등록시켜주는 역할
- 리스너가 시작한 후 LREG는 최대 60초 안에 자동으로 리스너에게 DB 정보를 등록(1분주기로 등록 시도)
- alter system register 명령으로 수동으로 등록 가능
![](https://velog.velcdn.com/images/syshin0116/post/de212bcc-722e-4fb8-8734-31f2f1c2db86/image.png)

## 2.55 ARCn(아카이버 프로세스)
- 리두 로그 파일의 내용이 가득 차서 로그 스위치 될 때 리두로그 파일을 아카이브 저장소로 복사
- 아카이브 모드일 때만 사용 가능
- 아카이브란 장기적인 저장을 목적으로 유지하는 파일

![](https://velog.velcdn.com/images/syshin0116/post/8774452b-1128-49b0-a1e2-6ea42fbbab48/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/9139b184-ae25-438d-bb0d-3f58b44f9198/image.png)

- 아카이브 로그 모드: 데이터베이스가 REDO 데이터를 덮어쓰기 전에 REDO 데이터를 아카이브 REDO 로그 파일로 복사하는 작동방식
- 아카이브 로그 모드로 운영하면 로그 스위치시 REDO 파일을 복사함
- 에러가 발생해서 복구해야 할 경우 아카이브 REDO 로그 파일을 적용하는 것으로 장애 발생 시점까지 복구 가능

## 2.56 데이터베이스 저장 영역 구조
![](https://velog.velcdn.com/images/syshin0116/post/db7b7bd8-a39c-4abe-9621-0650863989c1/image.png)

## 2.57 데이터베이스
1. 데이터베이스의 구성
	- 데이터 파일
	테이블, 인덱스, UNDO 데이터, 임시 데이터 저장
	- REDO 로그 파일(두 개 이상)
	변경이력 저장
	- 컨트롤 파일
		제어정보, 물리적 파일들에 대한 위치 정보 저장
2. 데이터베이스를 구성하는 파일은 OS의 파일시스템에 존재
3. 데이터베이스 파일위치(기본설정인 경우)
	- < $ORACLE_BASE>/oradata/<\SID>
	Ex) ls $ORACLE_BASE/oradata/ORA19C/

## 2.58 논리적 및 물리적 데이터베이스 구조  
![](https://velog.velcdn.com/images/syshin0116/post/c6ba8b37-e525-4847-a6ae-cfb57466f421/image.png)

## 2.59 세그먼트, Extent, 블록
- 세그먼트는 테이블스페이스 내에 존재합니다.
- 세그먼트는 Extent 모음입니다.
- Extent는 데이터 블록 모음입니다.
- 데이터 블록은 디스크 블록에 매핑됩니다.
![](https://velog.velcdn.com/images/syshin0116/post/d74850bf-31d5-44dc-8558-e0c6e6781166/image.png)

## 2.60 데이터 블록
1. **데이터를 읽고 쓰는 작업을 데이터 블록 단위로 수행**
2. 테이블, 인덱스 등의 오브젝트는 블록 단위로 데이터 파일에 보관
3. 버퍼 캐시도 블록 단위로 관리
	- 블록 크기는 2KB, 4KB, 8KB, 16KB, 32KB 중 하나를 지정
4. 데이터베이스 블록의 기본 크기는 DB 생성시 지정
	- 기본 블록 사이즈(standard block size)
	- 비표준 블록 사이즈(non standard block size)
	- 테이블스페이스에서 비표준 블록 크기로 저장 가능
	- DB_nK_CACHE_SIZE 를 지정해 데이터 버퍼 캐시 구성 필요
5. 데이터 블록 크기는 불필요한 I/O를 피하기 위해 운영 체제 블록 크기의 배수
6. **기본크기 블록 사이즈 확인 방법**
	- show parameter BLOCK_SIZE;
    
## 2.61 데이터 파일과 테이블 스페이스의 관계
![](https://velog.velcdn.com/images/syshin0116/post/ba6d1aca-68b7-45b7-bfdb-61575c564483/image.png)

1. 데이터 파일
	- 테이블이나 인덱스, 그 밖의 오브젝트가 데이터 파일에 보관
	- OS의 파일 시스템상에 존재하는 **물리적인 파일, 실제로 확인 가능**
2. 테이블 스페이스
	- **한 개 이상의 데이터 파일**을 그룹화 해서 이름 붙인 **논리적인 저장공간**
	- 오라클이 정의한 논리적 저장 공간이므로 **실제로 존재 하지 않음**
	- **테이블이나 인덱스 등의 오브젝트를 생성해 저장할 곳으로 데이터 파일을 지정하지 않고 테이블 스페이스를 지정**
- 테이블 스페이스가 어떤 데이터 파일로 구성 되어 있는지 몰라도 됨
- 오브젝트를 생성할 해당 테이블 스페이스명만 주의하면 됨
3. 딕셔너리 뷰로 확인
```sql
select * from dba_data_files;
select tablespace_name, contents from dba_tablespaces;
```

## 2.62 테이블 스페이스의 종류
1. 영구 테이블 스페이스
	- 테이블이나 인덱스 등을 저장하기 위한 **데이터 보존용**
	- ex) USERS, SYSTEM, SYSAUX
2. 임시 테이블 스페이스
	- 임시 세그먼트라 불리는 작업용 디스크 영역을 보관
	- **정렬 처리** 진행 시 데이터양이 적은 경우는 PGA의 SQL Work Area에서 처리
	- SQL Work Area 가 부족하면 임시 세그먼트를 할당하여 처리
	- 테이블이나 인덱스 등의 오브젝트를 저장하는 것은 불가능
3. UNDO 테이블 스페이스
	- UNDO 세그먼트를 저장하기 위한 전용 테이블 스페이스
	- UNDO 세그먼트는 **변경 전의 데이터를 보관**
	- 트랜잭션이 시작되면 트랜잭션에 자동으로 UNDO 세그먼트 할당
	- UNDO 데이터는 **트랜잭션의 롤백이나 읽기 일관성을 위해 존재**
	- 테이블이나 인덱스 등의 오브젝트를 저장하는 것은 불가능
    
## 2.63 SYSTEM 및 SYSAUX 테이블스페이스
1. SYSTEM, SYSAUX는 **오라클 동작 필수, 온라인 필수 **영구 테이블 스페이스
2. SYSTEM 테이블스페이스
	- 오라클이 동작하는 데 필요한 오브젝트 및 관리 정보 등이 저장 (ex. 데이터 딕셔너리)
3. SYSAUX 테이블스페이스
	- 주로 오라클 서버의 **성능 튜닝**을 위한 데이터들이 저장
	- **AWR(Auto Workload Repository)** 데이터들이 저장
4. SYSTEM 및 SYSAUX 테이블스페이스는 사용자 데이터가 저장되면 관리의 어려움이 생기므로 **따로 저장**

## 2.64 멀티테넌트(Multitenant) 아키텍처 소개
1. 클라우드 아키텍처 개념을 접목
2. 전통적인 서버 아키텍처의 문제점인 자원의 비효율적 사용, 자원의 낭비를 해결하기 위해 탄생
3. 여러 개의 DB를 관리하면서 **프로세스나 메모리 등의 자원은 공유하지만 각 시스템(PDB)의 데이터는 개별로 저장**
	- **OS 자원을 낭비 없이 효율적으로 사용**
	- 각각의 시스템의(PDB) 데이터 독립성 보장
	- DBA가 각 DB별로 관리하는 부담 감소, 운영비용 감소 4. CDB라 불리는 통합용 데이터베이스에
여러 대의 데이터 베이스(PDB)를 통합시키는 방식
5. CDB에 통합된 여러 대의 PDB는 **CDB 인스턴스 하나로 관리**
	- CDB : Container Database (통합용/관리용 데이터베이스)
	- PDB : Pluggable Database (업무용 데이터베이스)
6. CDB : Container Database (통합용/관리용 데이터베이스)
  - CDB 내부에는 총 252개의 PDB 관리 가능
  - Physical Level에 데이터베이스 Instance와 데이터베이스 파일존재
7. PDB : Pluggable Database (업무용 데이터베이스)
  - 플러그/언 플러그 가능 데이터베이스, **유연성 제공**
  - 데이터베이스 스키마의 집합이며, 유저와 응용 프로그램에는 논리적으로
별도의 데이터베이스로 인식됨, **독립성 보장**
8. 컨테이너 타입
  - Root 컨테이너, CDB$ROOT
  - Seed 컨테이너, PDB$SEED
  - 내부적으로 생성해 놓은 기본 데이터베이스 이미지(템플릿), PDB 생성시 사용
  - PDB 컨테이너
9. PDB 생성방법
  - 기존 DB(Non-CDB)를 CDB에 통합할 때는 PDB 형태로 변환
  - PDB$SEED로 부터 생성
  - 기존 PDB를 복제해서 다른 PDB를 생성
  - 임의의 CDB에서 PDB를 언플러그 해서 다른 CDB에 플러그 가능    
![](https://velog.velcdn.com/images/syshin0116/post/af930e6c-c946-461d-8562-f15f6166dce4/image.png)

## 2.65 오라클 데이터베이스 Instance 구성
1. **클러스터**란 두개 이상의 독립된 서버들과 디스크를 하나로 연결하는 기법
2. 여러 개의 서버상에 기동 된 인스턴스를 하나의 데이터베이스처럼 사용가능
3. 데이터의 일관성을 유지 하기위해 **스토리지는 공유함**
4. RAC의 목적 : 데이터베이스의 **확장성, 가용성**을 높이기 위함
![](https://velog.velcdn.com/images/syshin0116/post/89ccf011-8afe-4911-ae0f-9160a4bc2037/image.png)

## 2.66 멀티테넌트(Multitenant) 아키텍처 소개
1. 오라클에서는 기존에 사용해 오던 데이터베이스 아키텍처에서
	멀티테넌트 아키텍처로 일원화할 것이라고 발표
2. 멀티테넌트 아키텍처가 확산 중이고 더욱 확산될 예정
3. Multitenant Administrators Guide 19c
4. multitenant-administrators-guide-19c.pdf 참고
5. https://docs.oracle.com/en/database/oracle/oracledatabase/19/multi/index.html

## 2.67 Automatic Storage Management(자동저장영역관리)
- Oracle Database File을 위해 특별히 구현된 Disk 관리 시스템으로 **Disk Load Balancing 유지 되도록 분산 저장 및 Mirroring 지원> 성능향상**
- 새로운 Disk를 추가/삭제할 경우 **재구성 작업이 자동으로 발생하여 Disk Load Balancing 유지 > 관리편리**
- 이식 가능한 고성능 클러스터 파일 시스템
- ACFS(ASM 클러스터 파일 시스템)으로 응용 프로그램 파일을 관리합니다.

![](https://velog.velcdn.com/images/syshin0116/post/b638706d-9bd6-49d0-957d-db09c0d1d2b6/image.png)

## 2.68 ASM 저장 영역 구성 요소
![](https://velog.velcdn.com/images/syshin0116/post/f73ffb87-e7e8-4aef-9938-f8161ade0aa1/image.png)

## 요약
#### 이 단원에서는 다음 내용을 설명했습니다.
1. 오라클 기본 배경지식 설명
2. 오라클 데이터베이스를 구성하는 주요 요소 설명
3. 메모리 구조 설명
4. 백그라운드 프로세스 설명
5. 논리적/물리적 저장 영역 구조 상호 연관
6. 플러그 가능한 데이터베이스 설명(멀티테넌트 아키텍처)
7. ASM 저장 영역 구성 요소 설명

## 연습(중요)
#### 다음 단어들의 각 의미를 이해한 만큼 정의해 보세요.
1. 오라클 서버를 구성하는 3대 요소는?
2. 프로세스
3. 메모리
4. 캐시
5. 버퍼
6. 인스턴스
7. 데이터베이스
8. 서버 프로세스
9. 유저 프로세스
10. 리스너 프로세스

# 실습
## 2.1 라이브러리 캐시에 저장된 SQL의 소프트 파싱, 하드 파싱 확인
1. SYS 계정(sysdba 권한)에서 SHARED POOL 영역을 초기화한다.
SHARED POOL 초기화한후에도 내부적으로 SQL이 실행되기 때문에 SYS 소유의 SQL이 보여진다.
```sql
ALTER SYSTEM FLUSH SHARED_POOL;
```
2. HR 계정에서 SQL 문장을 실행한다.
```sql
SELECT EMPLOYEE_ID EMPID, LAST_NAME
FROM HR.EMPLOYEES;
```
3. SYS 계정에서 V$SQL 뷰를 통해서 SQL 문장을 확인
```sql
SELECT PARSING_SCHEMA_NAME, SQL_ID, SQL_TEXT FROM V$SQL
WHERE (SQL_TEXT LIKE '%EMPID%' or SQL_TEXT LIKE '%empid%')
AND PARSING_SCHEMA_NAME IN ('HR');
```
![](https://velog.velcdn.com/images/syshin0116/post/b3786f22-884f-4878-be81-e79711b66240/image.png)
>SQL_ID: sql에 id가 부여되어 캐시에 저장된다 -> 이후 소프트 파싱시 사용된다
주의) 한 글자만 틀려도(띄어쓰기 포함) 다른 문장으로 이해하여 하드파싱으로 진행된다

4. HR 계정에서 같은 SQL 문장을 재실행한다.
```sql
SELECT EMPLOYEE_ID EMPID, LAST_NAME
FROM HR.EMPLOYEES;
```
5. SYS 계정에서 V$SQL 뷰를 통해서 SQL 문장을 확인
동일한 SQL_ID 가 조회된다. 동일한 SQL은 재사용 되고 있다는 의미(소프트 파싱)
```sql
SELECT PARSING_SCHEMA_NAME, SQL_ID, SQL_TEXT FROM V$SQL
WHERE (SQL_TEXT LIKE '%EMPID%' or SQL_TEXT LIKE '%empid%')
AND PARSING_SCHEMA_NAME IN ('HR');
```
6. HR 계정에서 새로운 SQL 문장을 실행한다.
```sql
SELECT EMPLOYEE_ID EMPID, FIRST_NAME
FROM HR.EMPLOYEES;
라이브러리 캐시에 저장된 SQL의 소프트 파싱, 하드 파싱 
```
7. SYS 계정에서 V$SQL 뷰를 통해서 SQL 문장을 확인
새로운 SQL_ID가 조회된다. 새로운 SQL은 새로운 SQL_ID가 부여된다.(하드파싱)
```sql
SELECT PARSING_SCHEMA_NAME, SQL_ID, SQL_TEXT FROM V$SQL
WHERE (SQL_TEXT LIKE '%EMPID%' or SQL_TEXT LIKE '%empid%')
AND PARSING_SCHEMA_NAME IN ('HR');
```

## 2.2 데이터베이스 버퍼 캐시 기능 확인

AUTOTRACE의 통계 출력값
db block gets 변경을 위한 블록 요청 횟수
consistent gets 조회를 위한 블록 요청 횟수
**physical reads 디스크에서 읽어 온 블록의 합계**
redo size 생성된 REDO의 합계(바이트 단위)
sorts(memory) 디스크를 사용하지 않고 메모리에서만 수행한 정렬 작업 수
sorts(disk) 한 번 이상 디스크를 사용한 정렬 작업 수
rows processed 작업 중에 처리된 로우의 수
### 1. HR 계정에서 임시 테이블 생성과 데이터를 입력후 건수를 확인한다. SQL Develpoer 에서 실행
```sql
DROP TABLE EMP_COPY;
CREATE TABLE EMP_COPY
AS SELECT * FROM EMPLOYEES;
BEGIN
 FOR I IN 1..1000
 LOOP
 INSERT INTO EMP_COPY
 SELECT * FROM EMPLOYEES;
 END LOOP;
 COMMIT;
END;
/
-- 107107 건이 조회됨
SELECT COUNT(*) FROM EMP_COPY;
```
### 2. sqlplus sys/oracle as sysdba 로 접속하여 실행계획과 실행 통계만 표시하도록 설정하고 처리 시간을 표시하도록 설정한다.

```alter system flush buffer_cache;``` 은 데이터베이스 버퍼 캐시에 보관된 블록을 제거한다.
```sql
set autotrace traceonly;
set timing on;
SQL> ALTER SYSTEM FLUSH BUFFER_CACHE;
System altered.
```
#### 2.1 HR.EMP_COPY을 조회하여 실행 통계를 확인한다.
physical reads는 디스크에서 읽어온 블록의 합계이다.
1127 physical reads
```sql
SQL> SELECT * FROM HR.EMP_COPY;
```
```sql
107107 rows selected.
Elapsed: 00:00:00.56
Execution Plan
----------------------------------------------------------
Plan hash value: 281390045
------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
------------------------------------------------------------------------------
| 0 | SELECT STATEMENT | | 107 | 7383 | 3 (0)| 00:00:01 |
| 1 | TABLE ACCESS FULL| EMP_COPY | 107 | 7383 | 3 (0)| 00:00:01 |
------------------------------------------------------------------------------
Statistics
----------------------------------------------------------
 0 recursive calls
 0 db block gets
 8195 consistent gets
 1127 physical reads
 0 redo size
 9230389 bytes sent via SQL*Net to client
 78927 bytes received via SQL*Net from client
 7142 SQL*Net roundtrips to/from client
 0 sorts (memory)
 0 sorts (disk)
 107107 rows processed
```

#### 2.2 HR.EMP_COPY을 두번째 조회하여 실행 통계를 확인한다.
physical reads 는 디스크에서 읽어온 블록의 합계이다.
두번째 결과
0 physical reads
```sql
SQL> SELECT * FROM HR.EMP_COPY;
```
```
107107 rows selected.
Elapsed: 00:00:00.88
Execution Plan
----------------------------------------------------------
Plan hash value: 281390045
------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
------------------------------------------------------------------------------
| 0 | SELECT STATEMENT | | 107 | 7383 | 3 (0)| 00:00:01 |
| 1 | TABLE ACCESS FULL| EMP_COPY | 107 | 7383 | 3 (0)| 00:00:01 |
------------------------------------------------------------------------------
Statistics
----------------------------------------------------------
 0 recursive calls
 0 db block gets
 8195 consistent gets
 0 physical reads
 0 redo size
 9230389 bytes sent via SQL*Net to client
 78927 bytes received via SQL*Net from client
 7142 SQL*Net roundtrips to/from client
 0 sorts (memory)
 0 sorts (disk)
 107107 rows processed
```
#### 2.3 physical reads 통계 값을 비교하여 결과를 확인하다.
1. physical reads는 디스크에서 읽어온 블록의 합계이다.
2. ```ALTER SYSTEM FLUSH BUFFER_CACHE;``` 를 이용하여 데이터베이스 버퍼 캐시에 보관된 블록을 제거한후
3. 첫번째 조회 결과는 디스크에서 읽어와서 조회했고
4. 두번째 조회 결과는 데이터베이스 버퍼 캐시에서 읽어와서 조회했다.
5. 두번째부터는 디스크에서 읽어온 블록의 합계가 0이다.
6. 즉 모든 블락을 캐시에서 읽어왔고 디스크 읽기 작업은 하지 않았다.

##### 첫번째 결과:
1127 physical reads
##### 두번째 결과:
0 physical reads

## 2.3 UPDATE문을 통한 리두로그, 언두 세그먼트 생성 확인

AUTOTRACE의 통계 출력값
db block gets 변경을 위한 블록 요청 횟수
consistent gets 조회를 위한 블록 요청 횟수
physical reads 디스크에서 읽어 온 블록의 합계
redo size 생성된 REDO의 합계(바이트 단위)
sorts(memory) 디스크를 사용하지 않고 메모리에서만 수행한 정렬 작업 수
sorts(disk) 한 번 이상 디스크를 사용한 정렬 작업 수
rows processed 작업 중에 처리된 로우의 수

V$TRANSACTION
xid 트랜잭션 ID
xidusn 트랜잭션에 할당된 UNDO 세그먼트 번호
status 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
start_time 트랜잭션이 시작된 시간

V$ROLLSTAT
usn UNDO 세그먼트 번호
rssize UNDO 세그먼트 크기(Byte)
extents UNDO 세그먼트에서 할당된 익스텐트 개수
xacts UNDO 세그먼트를 사용중인 트랜잭션 개수
status UNDO 세그먼트의 상태

### 1. sqlplus sys/oracle as sysdba 로 접속하여 아래와 같이 실행
SYSDBA 권한을 가진 SYS 계정으로 plustrce.sql를 실행해 PLUSTRCE 롤을 생성
PLUSTRCE 과 DBA 롤을 HR 사용자에게 권한을 부여
@는 리눅스의 경로의 plustrce.sql 파일을 실행시켜주기 위함이다.
SQL> @$ORACLE_HOME/sqlplus/admin/plustrce.sql
SQL> grant plustrace to hr;
SQL> grant dba to hr;
### 2. HR 계정으로 SQL Developer 로 접속하여 실행한다.
임시 테이블 생성과 데이터를 입력후 건수를 확인한다.
```sql
DROP TABLE EMP_COPY PURGE;

CREATE TABLE EMP_COPY
AS SELECT * FROM EMPLOYEES;

BEGIN
 FOR I IN 1..100
 LOOP
 INSERT INTO EMP_COPY
 SELECT * FROM EMPLOYEES;
 END LOOP;
COMMIT;
END;
/

-- 10807 건이 조회됨
SELECT COUNT(*) FROM EMP_COPY;
```

### 3. sqlplus hr/hr 로 접속하여 아래 명령어를 실행한다.
EMP_COPY에 1건의 UPDATE문을 실행하고 REDO, UNDO 세그먼트 변화를 확인한다.
#### 3.1 1건의 UPDATE로 인해 redo size의 값이 316으로 된 것을 확인할 수 있다.
```sql
SQL> SET AUTOTRACE TRACEONLY;
SQL> UPDATE EMP_COPY SET EMPLOYEE_ID = 1000
WHERE EMPLOYEE_ID = '7369';
```
```
1 row updated.
Execution Plan
----------------------------------------------------------
Plan hash value: 1880658981
-------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
-------------------------------------------------------------------------------
| 0 | UPDATE STATEMENT | | 1 | 4 | 3 (0)| 00:00:01 |
| 1 | UPDATE | EMP_COPY | | | | |
|* 2 | TABLE ACCESS FULL| EMP_COPY | 1 | 4 | 3 (0)| 00:00:01 |
-------------------------------------------------------------------------------
Predicate Information (identified by operation id):
---------------------------------------------------
 2 - filter("EMPLOYEE_ID"=7369)
Statistics
----------------------------------------------------------
 0 recursive calls
 2 db block gets
 121 consistent gets
 0 physical reads
 316 redo size
 410 bytes sent via SQL*Net to client
 416 bytes received via SQL*Net from client
 2 SQL*Net roundtrips to/from client
 0 sorts (memory)
 0 sorts (disk)
 1 rows processed
 ```
 
#### 3.2 SYS 계정으로 SQL Developer 로 접속하여 실행한다.
SYS 계정에서 트랜잭션과 UNDO 세그먼트의 크기 등을 확인한다.
UPDATE 문이 실행되면 자동적으로 트랜잭션이 시작되고 하나의 트랜잭션에는 하나의 UNDO 세그먼트
가 할당된다. 언두 세그먼트 크기가 2168KB인 것을 확인하자

```sql
-- 트랜잭션 확인
SELECT XID 			-- 트랜잭션 ID
 , XIDUSN 			-- 트랜잭션에 할당된 UNDO 세그먼트 번호
 , STATUS 			-- 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
 , START_TIME 		-- 트랜잭션이 시작된 시간
FROM V$TRANSACTION;


-- 언두 세그먼트 확인
SELECT USN 				-- UNDO 세그먼트 번호
 , RSSIZE/1024 KB 		-- UNDO 세그먼트 크기(BYTE)
 , EXTENTS 				-- UNDO 세그먼트에서 할당된 익스텐트 개수
 , XACTS 				-- UNDO 세그먼트를 사용중인 트랜잭션 개수
 , STATUS 				-- UNDO 세그먼트의 상태
FROM V$ROLLSTAT
WHERE XACTS = '1';


-- 트랜잭션과 언두 세그먼트 동적 성능뷰를 조인하여 함께 확인
SELECT TRAN.XID 		-- 트랜잭션 ID
 , TRAN.XIDUSN 			-- 트랜잭션에 할당된 UNDO 세그먼트 번호
 , TRAN.STATUS 			-- 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
 , TRAN.START_TIME 		-- 트랜잭션이 시작된 시간
 , NAME.NAME 			-- 언두 세그먼트 이름
 , UNDO.USN 			-- 언두세그먼트 번호
 , UNDO.RSSIZE/1024 KB 	-- 언두 세그먼트 크기
 , UNDO.EXTENTS 		-- 해당 언두 세그먼트에서 할당된 익스텐트 개수
 , UNDO.XACTS 			-- 해당 언두 세그먼트를 사용중인 트랜잭션 개수
 , UNDO.STATUS
FROM V$ROLLSTAT UNDO
JOIN V$ROLLNAME NAME
ON UNDO.USN = NAME.USN
JOIN V$TRANSACTION TRAN
ON TRAN.XIDUSN = UNDO.USN
AND UNDO.XACTS <> 0;
```

### 4. sqlplus 를 이용한 HR 계정에서 테이블 전체에 업데이트 하여 리두로그를 대량 발생 시킨다.
redo size가 316에서 5344592으로 변경된 것을 확인할 수 있다.
UPDATE를 1건 했을 때는 redo size 가 316 UPDATE를 전체에 적용했을 때는 5344592로 늘어났다는 것
은 많은 UPDATE로 인해 redo size가 커진 것을 확인할 수 있다.
```sql
SQL> UPDATE EMP_COPY SET EMPLOYEE_ID = ROWNUM;
```
```
21507 rows updated.
Execution Plan
----------------------------------------------------------
Plan hash value: 3160081842
--------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
--------------------------------------------------------------------------------
| 0 | UPDATE STATEMENT | | 107 | 428 | 3 (0)| 00:00:01 |
| 1 | UPDATE | EMP_COPY | | | | |
| 2 | COUNT | | | | | |
| 3 | TABLE ACCESS FULL| EMP_COPY | 107 | 428 | 3 (0)| 00:00:01 |
--------------------------------------------------------------------------------
Statistics
----------------------------------------------------------
 0 recursive calls
 21904 db block gets
 247 consistent gets
 0 physical reads
 5344592 redo size
 195 bytes sent via SQL*Net to client
 391 bytes received via SQL*Net from client
 1 SQL*Net roundtrips to/from client
 0 sorts (memory)
 0 sorts (disk)
 21507 rows processed
 ```
 
### 5. SYS계정에서 트랜잭션과 UNDO 세그먼트 크기 등의 정보를 확인한다.
언두 세그먼트 크기가 2168KB에서 5240KB로 늘어난 것을 확인할 수 있다.
UPDATE를 전체로 적용해서 UNDO 데이터 량이 늘어난 것을 확인할 수 있다.
```sql
-- 트랜잭션 확인
SELECT XID 			-- 트랜잭션 ID
 , XIDUSN 			-- 트랜잭션에 할당된 UNDO 세그먼트 번호
 , STATUS 			-- 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
 , START_TIME 		-- 트랜잭션이 시작된 시간
FROM V$TRANSACTION;


-- 언두 세그먼트 확인
SELECT USN 			-- UNDO 세그먼트 번호
 , RSSIZE/1024 KB 	-- UNDO 세그먼트 크기(BYTE)
 , EXTENTS 			-- UNDO 세그먼트에서 할당된 익스텐트 개수
 , XACTS 			-- UNDO 세그먼트를 사용중인 트랜잭션 개수
 , STATUS 			-- UNDO 세그먼트의 상태
FROM V$ROLLSTAT
WHERE XACTS = '1';


-- 트랜잭션과 언두 세그먼트 동적 성능뷰를 조인하여 함께 확인
SELECT TRAN.XID 		-- 트랜잭션 ID
 , TRAN.XIDUSN 			-- 트랜잭션에 할당된 UNDO 세그먼트 번호
 , TRAN.STATUS 			-- 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
 , TRAN.START_TIME 		-- 트랜잭션이 시작된 시간
 , NAME.NAME 			-- 언두 세그먼트 이름
 , UNDO.USN 			-- 언두세그먼트 번호
 , UNDO.RSSIZE/1024 KB 	-- 언두 세그먼트 크기
 , UNDO.EXTENTS 		-- 해당 언두 세그먼트에서 할당된 익스텐트 개수
 , UNDO.XACTS 			-- 해당 언두 세그먼트를 사용중인 트랜잭션 개수
 , UNDO.STATUS
FROM V$ROLLSTAT UNDO
JOIN V$ROLLNAME NAME
ON UNDO.USN = NAME.USN
JOIN V$TRANSACTION TRAN
ON TRAN.XIDUSN = UNDO.USN
AND UNDO.XACTS <> 0;
UPDATE문을 통한 리두로그, 언두 세그먼트 생성 확인
```
### 6. sqlplus 를 이용한 HR 계정에서 롤백을 한다.
```sql
ROLLBACK;
```

### 7. SYS계정에서 트랜잭션과 UNDO 세그먼트 크기 등의 정보를 확인한다.
rollback으로 인하여 트랜잭션이 종료되고 트랜잭션에 할당되었던 UNDO 세그먼트도 해제되었다.
```sql
-- 트랜잭션 확인
SELECT XID -- 트랜잭션 ID
 , XIDUSN -- 트랜잭션에 할당된 UNDO 세그먼트 번호
 , STATUS -- 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
 , START_TIME -- 트랜잭션이 시작된 시간
FROM V$TRANSACTION;


-- 언두 세그먼트 확인
SELECT USN 			-- UNDO 세그먼트 번호
 , RSSIZE/1024 KB 	-- UNDO 세그먼트 크기(BYTE)
 , EXTENTS 			-- UNDO 세그먼트에서 할당된 익스텐트 개수
 , XACTS 			-- UNDO 세그먼트를 사용중인 트랜잭션 개수
 , STATUS 			-- UNDO 세그먼트의 상태
FROM V$ROLLSTAT WHERE XACTS = '1';


-- 트랜잭션과 언두 세그먼트 동적 성능뷰를 조인하여 함께 확인
SELECT TRAN.XID 		-- 트랜잭션 ID
 , TRAN.XIDUSN 			-- 트랜잭션에 할당된 UNDO 세그먼트 번호
 , TRAN.STATUS 			-- 트랜잭션의 상태, 실행 중인 트랜잭션일 때는 ‘ACTIVE’
 , TRAN.START_TIME 		-- 트랜잭션이 시작된 시간
 , NAME.NAME 			-- 언두 세그먼트 이름
 , UNDO.USN 			-- 언두세그먼트 번호
 , UNDO.RSSIZE/1024 KB 	-- 언두 세그먼트 크기
 , UNDO.EXTENTS 		-- 해당 언두 세그먼트에서 할당된 익스텐트 개수
 , UNDO.XACTS 			-- 해당 언두 세그먼트를 사용중인 트랜잭션 개수
 , UNDO.STATUS
FROM V$ROLLSTAT UNDO
JOIN V$ROLLNAME NAME
ON UNDO.USN = NAME.USN
JOIN V$TRANSACTION TRAN
ON TRAN.XIDUSN = UNDO.USN
AND UNDO.XACTS <> 0;
```

## 2.4 PGA의 정렬공간 크기에 따른 메모리/디스크 정렬방식 확인

AUTOTRACE의 통계 출력값
db block gets 변경을 위한 블록 요청 횟수
consistent gets 조회를 위한 블록 요청 횟수
physical reads 디스크에서 읽어 온 블록의 합계
redo size 생성된 REDO의 합계(바이트 단위)
sorts(memory) 디스크를 사용하지 않고 메모리에서만 수행한 정렬 작업 수
sorts(disk) 한 번 이상 디스크를 사용한 정렬 작업 수
rows processed 작업 중에 처리된 로우의 수
### 1. sqlplus sys/oracle as sysdba 로 접속하여 아래와 같이 실행
SYSDBA 권한을 가진 SYS 계정으로 plustrce.sql를 실행해 PLUSTRCE 롤을 생성
PLUSTRCE 과 DBA 롤을 HR 사용자에게 권한을 부여
@는 리눅스의 경로의 plustrce.sql 파일을 실행시켜주기 위함이다.

```sql
@$ORACLE_HOME/sqlplus/admin/plustrce.sql

grant plustrace to hr;
grant dba to hr;
```
### 2. hr 계정에서 임시 테이블 생성과 데이터를 입력후 건수를 확인한다.
sqlplus 에서 실행한다.
```sql
drop table emp_copy purge;


create table emp_copy
as select * from employees;


BEGIN
 FOR I IN 1..100
 LOOP
 insert into emp_copy
 select * from employees;
 END LOOP;
END;
/
commit;


-- 10807 건이 조회됨
select count(*) from emp_copy;
```
### 3. hr 계정으로 오라클에 접속해 옵티마이저 통계를 수집한다.
데이터를 입력한후 통계 수집을 해서 정확한 실행계획이 작성되도록 하기 위함이다.

```sql
EXECUTE DBMS_STATS.GATHER_SCHEMA_STATS('HR');
```
### 4. emp_copy를 정렬조건 없이 조회하여 실행계획과 통계정보를 확인한다.
실행계획과 실행 통계만 표시하도록 설정하고 처리 시간을 표시하도록 설정한다.
Statistics의 sorts (memory), sorts (disk)가 0 이므로 정렬 처리가 발생하지 않았다는 것을 알 수 있다.
```sql
set autotrace traceonly;

set timing on;

SQL> select * from emp_copy;
```
```
10807 rows selected.
Elapsed: 00:00:00.06
Execution Plan
----------------------------------------------------------
Plan hash value: 281390045
------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
------------------------------------------------------------------------------
| 0 | SELECT STATEMENT | | 107 | 7383 | 3 (0)| 00:00:01 |
| 1 | TABLE ACCESS FULL| EMP_COPY | 107 | 7383 | 3 (0)| 00:00:01 |
------------------------------------------------------------------------------
Statistics
----------------------------------------------------------
 0 recursive calls
 0 db block gets
 834 consistent gets
 0 physical reads
 0 redo size
 933311 bytes sent via SQL*Net to client
 8304 bytes received via SQL*Net from client
 722 SQL*Net roundtrips to/from client
 0 sorts (memory)
 0 sorts (disk)
 10807 rows processed
```
### 5. emp_copy를 정렬조건과 함께 조회하여 실행계획과 통계정보를 확인한다.
Execution Plan 에서는 SORT ORDER BY의 실행계획이 수행된 것을 알 수 있다.
Statistics 의 sorts (memory)가 1인것으로 보아 메모리에서 정렬한 것을 알 수 있다.
Elapsed: 00:00:00.06 소요시간도 확인하자.
```sql
SQL> select * from emp_copy order by last_name;
10807 rows selected.
Elapsed: 00:00:00.06
Execution Plan
----------------------------------------------------------
Plan hash value: 428799061
-------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
-------------------------------------------------------------------------------
| 0 | SELECT STATEMENT | | 107 | 7383 | 4 (25)| 00:00:01 |
| 1 | SORT ORDER BY | | 107 | 7383 | 4 (25)| 00:00:01 |
| 2 | TABLE ACCESS FULL| EMP_COPY | 107 | 7383 | 3 (0)| 00:00:01 |
-------------------------------------------------------------------------------
Statistics
----------------------------------------------------------
 0 recursive calls
 0 db block gets
 121 consistent gets
 0 physical reads
 0 redo size
 307573 bytes sent via SQL*Net to client
 8323 bytes received via SQL*Net from client
 722 SQL*Net roundtrips to/from client
 1 sorts (memory)
 0 sorts (disk)
 10807 rows processed
 ```
### 6. emp_copy를 디스크로 정렬할 수 있는 환경을 인위적으로 설정
현재는 PGA 자동관리를 사용하고 있어서 세션 레벨에서 PGA를 수동관리로 전환
#### 6.1 workarea_size_policy를 세션 레벨에서 MANUAL로 설정
#### 6.2 sort_area_size를 세션 레벨에서 30KB(30720 Byte)로 설정
Execution Plan 에서는 SORT ORDER BY의 실행계획이 수행된 것을 알 수 있다.
Statistics 의 sorts (disk) 가 1인것으로 보아 디스크 정렬이 일어난 것을 알 수 있다.
Elapsed: 00:00:00.06 => 00:00:00.91 소요시간도 늘어난 것을 확인할 수 있다.
```
-- PGA 관리방법을 세션 레벨에서 수동으로 설정
alter session set workarea_size_policy = MANUAL;
-- 디스크에서 정렬이 일어나도록 메모리의 정렬공간을 의도적으로 30KB로 작게 설정
alter session set sort_area_size = 30720;
SQL> select * from emp_copy order by last_name;
10807 rows selected.
Elapsed: 00:00:00.91
Execution Plan
----------------------------------------------------------
Plan hash value: 428799061
-------------------------------------------------------------------------------
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |
-------------------------------------------------------------------------------
| 0 | SELECT STATEMENT | | 107 | 7383 | 4 (25)| 00:00:01 |
| 1 | SORT ORDER BY | | 107 | 7383 | 4 (25)| 00:00:01 |
| 2 | TABLE ACCESS FULL| EMP_COPY | 107 | 7383 | 3 (0)| 00:00:01 |
-------------------------------------------------------------------------------
Statistics
----------------------------------------------------------
 2 recursive calls
 56 db block gets
 121 consistent gets
 440 physical reads
 0 redo size
 291013 bytes sent via SQL*Net to client
 8323 bytes received via SQL*Net from client
 722 SQL*Net roundtrips to/from client
 0 sorts (memory)
 1 sorts (disk)
 10807 rows processed
 ```
### 7. 결론
현재 테이블의 데이터 량이 많지 않아 소요시간에는 별 차이는 없지만 대량의 데이터 인경우에는 메모
리 정렬과 디스크 정렬은 소요시간의 차이가 많이 발생할 것이다.

오라클은 서버 프로세스에 할당된 PGA의 정렬공간의 크기를 초과하는 데이터를 정렬할 때 디스크를 사
용한다(TEMP 테이블스페이스의 임시 세그먼트를 사용) 대량의 데이터 정렬을 할 때는 PGA의 정렬공간
을 크게 해 디스크 정렬을 방지하는 것이 성능면에서 유리하다.