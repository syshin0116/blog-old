---
title: "[ORACLE-WDP]2일차- SELECT, WHERE, ORDERBY절"
date: 2023-05-07 10:00:00 +0900
categories: [Database,ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---


## 윈도우용 64bit 인스턴트 클라이언트 설치 및 sqlplus 접속 테스트

1. oracle client download 19c로 검색하여 다운로드 사이트 클릭
설치파일 : WINDOWS.X64_193000_client.zip
2. WINDOWS.X64_193000_client.zip을 클릭하여 다운로드
3. WINDOWS.X64_193000_client.zip 파일 압축을 푼다
4. WINDOWS.X64_193000_client\client\setup.exe 을 실행한다.
5. 인스턴트 클라이언트를 선택하고 다음을 누른다.

![image](https://user-images.githubusercontent.com/99532836/236651852-235633f3-be84-4a05-9704-7b276e24eb2b.png)
6. 소프트웨어 위치를 아래와 같이 입력하고 다음을 누른다
```
C:\app\user\product\19.0.0\client_1
```

![image](https://user-images.githubusercontent.com/99532836/236651868-ee26a785-a9de-44f0-a117-0a98cba8286f.png)
7. 설치를 누른다.
8~9. 다음, 닫기
10. 아래경로와 같게 …\network\admin 폴더를 만든다.
```
C:\app\user\product\19.0.0\client_1\network\admin
```
12. 자신의 리눅스 환경에 맞게 IP, PORT, SERVICE_NAME을 편집한다.
* 주의사항 tnsnames.ora 작성시 들여쓰기를 반드시 해야 한다.
들여쓰기를 안 하면 에러가 발생하여 접속이 안될 수 있다.

![image](https://user-images.githubusercontent.com/99532836/236651919-2489412b-63a0-4f2e-9e8f-b0eea1ad7d15.png)
13. TNS_ADMIN 환경변수 설정
13.1 시스템 속성창의 고급 탭 열기
```
C:\>sysdm.cpl,3
```
13.2 환경변수 클릭
13.3 시스템 변수(S)의 편집 클릭
13.4 변수이름(N), 변수 값(V) 설정
```
TNS_ADMIN
C:\app\user\product\19.0.0\client_1\network\admin
```
![image](https://user-images.githubusercontent.com/99532836/236651965-e37f35f7-90ae-483a-8dbd-1c9fbc6c213d.png)
14. path 환경변수에 sqlplus 경로 등록 여부 확인 및 설정
```
C:\> path
PATH=C:\app\user\product\19.0.0\client_1
C:\> where sqlplus
C:\app\user\product\19.0.0\client_1\sqlplus.exe
```
15. path가 설정 되어있지 않다면 시스템 환경변수의 path에
C:\app\user\product\19.0.0\client_1 추가한다.
C:\app\user\product\19.0.0\client_1 에는 sqlplus.exe 실행파일이 존재하는 곳이다

15.1 시스템 변수(S)의 Path를 선택하고 편집(I) 버튼 클릭
15.2 환경 변수 편집 화면에서 새로 만들기(N) 버튼 클릭
C:\app\user\product\19.0.0\client_1 를 추가

![image](https://user-images.githubusercontent.com/99532836/236651995-013b1a50-4680-431e-a1bf-d89499da7636.png)
![image](https://user-images.githubusercontent.com/99532836/236652001-9ba95821-f557-4b8f-bce3-3185bca07329.png)
16. 윈도우의 cmd 창에서 sqlplus 실행해서 오라클에 접속한다.
```
C:\> sqlplus sys/oracle@10.0.2.2:1521/ORA19C as sysdba
* ORA19C 는 tnsnames.ora에서 SERVICE_NAME이 아닌 호스명인 ORA19C 이다
```
18. oracle 계정으로 접속 후 리스너 구동 및 오라클 startup (리눅스 서버쪽)
```
$ lsnrctl status
$ lsnrctl start
$ sqlplus sys/oracle as sysdba
SQL> startup
ORACLE instance started.
Total System Global Area 1610609200 bytes
Fixed Size 8897072 bytes
Variable Size 335544320 bytes
Database Buffers 1258291200 bytes
Redo Buffers 7876608 bytes
Database mounted.
Database opened.
```

## rlwrap 설치 매뉴얼

### rlwarp이란?
- rlwrap은 sqlplus에서 up, down 방향키로 과거 입력 명령어를 찾을 수 있게 해준다.

- 사용법: sqlplus를 실행 시 rlwrap 실행
-  자동 실행 설정 방법: alias 를 정의
	ex) sqlplus / as sysdba -> rlwrap sqlplus / as sysdba 로 변환

### 1. root 계정으로 접속
1.1 yum ```-y install epel-release```

1.2. ```yum -y install rlwrap```

### 2. oracle 계정으로 로그인
2.1. ```vi ~/.bash_profile``` 실행하여 아래 내용을 추가
```alias sqlplus="rlwrap sqlplus"```

![image](https://user-images.githubusercontent.com/99532836/236652080-16dd303d-2b14-4ebb-85b1-aa40f84c239c.png)
2.2. bash_profile을 적용한다. (혹은 다시 로그인한다.)
```source ~/.bash_profile```

2.3. alisa 명령어로 설정된 alias 리스트를 확인한다

![image](https://user-images.githubusercontent.com/99532836/236652130-077fea5f-81df-4c85-8150-4907f6e8388d.png)

## Oracle Database 19c SQL.pdf



## 1. RDBMS 이해
#### 데이터베이스란?
- 데이터의 모음
- 데이터베이스는 여러 사람이 공유하여 사용할 목적으로 체계화하여 관리하는 데이터의 집합을 의미
- 일반적으로 데이터베이스는 DBMS에 의해 제어
#### 데이터베이스의 유형
#### 관계형 데이터베이스
- 데이터는 각 엔터티에 대한 정보를 저장
- **행과 열을 통해 미리 정의된 범주를 나타내는 테이블로 구성**
- 이 정형 데이터는 효율적이고 유연하게 액세스 가능
#### 비관계형 데이터베이스
- 비정형 또는 반정형 데이터를 저장
- **행과 열이 있는 테이블을 사용하지 않음**
- 저장되는 데이터 형식의 특정 요구사항에 맞게 최적화된 스토리지
모델을 사용
- 큰 분산 데이터 세트를 빠르게 액세스, 업데이트, 분석 가능

#### DBMS(DataBase Management System)
#### 데이터베이스를 운영하고 관리하는 소프트웨어
- DBA / DB 사용자 / 응용프로그램과 Database 사이의 **중재자**
- Database에 대한 **모든 접근을 처리**하는 소프트웨어적 시스템
- SQL은 RDBMS에서 데이터의 검색과 관리, 스키마 생성과 수정,
객체 접근 관리 등을 위해 설계된 특수 목적 프로그래밍 언어

![image](https://user-images.githubusercontent.com/99532836/236652251-8230cb79-71a6-453c-997c-c2ce6ce26e8d.png)

#### **통합**된 데이터(integrated data)
- 산재되어 있지 않고 한곳에 있어야 함
- 모든 데이터가 **중복을 최소화**하면서 통합 > data integrity
#### **저장** 데이터 (stored data)
- 컴퓨터에서 처리가 가능하도록 전자적 형태로 저장
- 디스크, 테이프 등 컴퓨터가 접근 가능한 저장 매체에 저장된 데이터
#### **공유** 데이터(shared data)
- 한 조직의 여러 응용 시스템들이 **공동**으로 소유, 유지, 이용하는 데이터

### RDBMS 설계
#### 데이터베이스 설계 순서
#### 요구사항 수집 및 분석
#### 개념적 설계
- 주제영역 정의
- 핵심 엔티티 도출
- 엔티티간 관계 정의
#### 논리적 설계
**- 도출된 엔티티를 상세화**
- 정규화 과정 거쳐 엔티티를 분할하고 데이터 중복을 최소화
- 속성정의, 식별자 확정, M:N 관계해소, 참조 무결성 정의**
    
#### 물리적 설계
- 필요시 역정규화 수행
- 논리적 설계를 특정 RDBMS의 명령어를 이용하여 변환
    
### DMBS 유형
#### 계층적 데이터 모델 (Hierarchical Data Model)
- 데이터를 저장하는 단위(Entity)의 구조가 상하 종속적인 관계로 구성
- 개체를 노드로 표현하고 개체 집합들 사이의 관계를 링크로 연결한
트리(Tree)형태의 자료구조 (예: 탐색기)
- 마지막 정보의 변경 시 종속관계의 모든 정보를 수정해야 하는 종속
성 문제점으로 데이터 활용의 비효율성을 가짐.

![image](https://user-images.githubusercontent.com/99532836/236652357-df37a7d5-529a-4db9-9bac-c4945fe6ff74.png)

#### 망 데이터 모델(Network Data Model)
- CODASYL이 제안(CODASYL DBTG 모델이라고도 함)
- 그래프를 이용해서 데이터 논리구조를 표현한 데이터 모델
- 상위와 하위 레코드 사이에서 **다대다(N:M)** 대응 관계를 만족
하는 구조
- 비종속적 표현이 가능하지만, 복잡하여 조그만 문제에 대해
서의 처리가 어려울 수도 있음.

![image](https://user-images.githubusercontent.com/99532836/236652425-a82c3cc3-b29c-490b-b58a-27c53d6ae0cc.png)
#### 관계 데이터 모델 (Relational Data Model)
- 1970년 IBM의 연구원으로 있던 E.F.Codd가 **수학적 기초**에
근거를 두고 고안한 것이 관계형 데이터베이스(Relational
Database)
- 기본 개념: 데이터베이스는 **최소한의 의미를 가지는 테이블**
들로 구성되며 그 테이블들에 있는 **필드들로 연결한 것**이다.
필드 또한 가장 작은 논리적인 단위로 구분하는 것이 좋다.
- 장 점 : **업무 변화에 대한 적응능력, 유지 보수 편리성, 높은
생산성, 응용 프로그램의 개발 용이**
- 단 점 : 시스템의 부하가 상대적으로 높다. 
- 개체 집합에 대한 속성 관계를 표현하기 위하여 개체를
**테이블(table)**로 사용하고 **개체 집합들 사이의 관계는
공통 속성으로 연결**하는 독립된 형태의 데이터 모델


![image](https://user-images.githubusercontent.com/99532836/236652471-69ed8f08-10f8-44a5-8cba-ea4f5b14615e.png)

#### 관계 데이터 모델 (Relational Data Model)
- **실체(Entity)와 관계(Relation)를 중심**으로 기업의 정보 구조와 업무
프로세서를 정의 한다.
![image](https://user-images.githubusercontent.com/99532836/236652482-3b4bb07a-7585-423b-a882-b58844c9d724.png)

### 관계 형 모델의 구성요소
#### 관계 형 데이터 모델 용어
![image](https://user-images.githubusercontent.com/99532836/236652514-76554b66-5ed5-4b4a-8cce-845e9b7e4b72.png)
#### 관계 형 데이터 모델 용어: Table, Column, Row
- 관계 데이터베이스에 데**이터를 저장할 수 있는 형식 테이블**
(**Table=Relation**) : SQL에서 릴레이션보다는 테이블이란 용어를 사용
- 행과 열의 교차점은 원자 값(atomic value)이라는 오직 하나의 값으로
구성
- 테이블에서 행은 순서가 정해져 있지 않다.
- 테이블의 내용은 실제적인 **행의 집합**으로 간주된다

![image](https://user-images.githubusercontent.com/99532836/236652538-e24e54d9-de0c-4c29-a898-6b42b59f074f.png)
1. Row 
2. Index(?)
3. Column
4. Foreign Key
5. Value
6. Null

### 관계 형 모델의 구성요소 (HR Data Set)
![image](https://user-images.githubusercontent.com/99532836/236652539-df32e280-afa9-4c42-b181-1d3aa1c79000.png)

### DBMS Transaction
#### Transaction 이란?
- Transaction 은 하나의 논리적 작업 단위를 구성하는 연산들의 집합
	- the unit of work
	- the unit of recovery
	- the unit of concurrency
    
- 성 → **ACID**
- 예
	- ATM 기기
	- 은행 거래
	- 주식 거래
	- 마일리지 적립 작업
#### ACID 의미
- 원자성 (Atomicity)
	1) 트랜잭션과 관련된 작업들이 모두 수행되었는지 아니면 모두 실행이 안되었는지를 보장
	2) 자금이체의 양쪽 계좌에 대한 이체는 수행되거나 전혀 수행되지 않음을 보장
	3) COMMIT, ROLLBACK
    
- 일관성 (Consistency)
	1) 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지
	2) 트랜잭션 수행이 보존해야 할 일관성은 기본 키, 외래 키 제약과 같은 명시적인 무결성 제약조건들뿐만 아니라
	3) 자금 이체에서 두 계좌 잔고의 합은 이체 전후가 같아야 한다
- 고립성 (Isolation)
	1) 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장
	2) 여러 트랜잭션이 동시에 수행되더라도 각각의 트랜잭션은 다른 트랜잭션의 수행에 영향을 받지 않고 독립적으로 수행되어야 한다
- 지속성 (Durability)
	1) 성공적으로 수행된 트랜잭션은 영원히 반영되어야 함
	2) 지속성 저장 장치 에 로그로 기록 시스템에 이상이 발생하면 로그를 사용하여 이상 발생 이전 상태로 복구하는 것으로 지속성을 실현
    
## 2. SELECT 절
### 목표
- ERD 보는 법
- SQL 구문
- SELECT 절 이해
- 연산자 활용
- NULL 값 이해
- 연습문제

### SQL History
- 1973년 SQUARE(structured queries as relational expressions) 
- 1974년 SEQUEL(structured English as query language) 

SQL: Structured Query Language

### Human Resources (HR) Data Set
![](https://velog.velcdn.com/images/syshin0116/post/191f20cc-41c9-414a-a100-561fa2c7a490/image.png)

### HR.EMPLOYEES 테이블의 계층 구조
![](https://velog.velcdn.com/images/syshin0116/post/0e542ff1-b6e1-4055-94c5-f6368ee6f02d/image.png)
### SQL 구문
![](https://velog.velcdn.com/images/syshin0116/post/1077992a-d878-4aea-a047-747c437aaee9/image.png)

### 기본 SQL 이해 – SELECT절 이해
![](https://velog.velcdn.com/images/syshin0116/post/08fbf632-6831-4723-98e2-9cf7f1aae42e/image.png)

- 산술 연산자를 사용하여 숫자 및 날짜 데이터로 표현식 작성 가능

![](https://velog.velcdn.com/images/syshin0116/post/0671f709-c311-4602-aef1-3ac6f2db1e26/image.png)


- Null은 사용할 수 없거나, 할당되지 않았거나, 알 수 없거나, 적용할 수 없는 값
- Null은 0 이나 공백과 다름
```sql
SELECT last_name, job_id, salary, commission_pct
FROM employees;
```
- Null 값을 포함하는 산술식은 Null로 계산됨
```sql
SELECT last_name, 12*salary*commission_pct
FROM employees;
```
#### Column alias 사용

![](https://velog.velcdn.com/images/syshin0116/post/47200c43-be26-4e85-ab51-0a2c713f4727/image.png)
#### 연결 연산자

![](https://velog.velcdn.com/images/syshin0116/post/5257ae6a-e0db-4e27-9172-57f35f100f8d/image.png)

#### 대체 인용(**q**) 연산자
- 따옴표 구분자 지정
- 구분자를 임의로 선택
- 가독성 및 사용성 증가

![](https://velog.velcdn.com/images/syshin0116/post/029b1616-e81f-48c5-853a-7a5438bf2801/image.png)
    
#### 중복 행 제거
![](https://velog.velcdn.com/images/syshin0116/post/2b5dbda7-d2d5-4b5e-83e9-6be2f19091db/image.png)

### 연습문제
##### Exam0) Oracle SQL Developer에서 HR, SCOTT ERD를 추출 하고 테이블이 어떤 컬럼들로 이루어져 있고 테이블 간의 관계는 어떻게 설정되어 있는지 파악 하십시오.
![](https://velog.velcdn.com/images/syshin0116/post/e614e81d-85dd-43d0-ae4c-dd03fda01ac5/image.png)
##### Exam1) HR ERD를 참고하여 HR의 모든 테이블에 대해서 아래와 같은 SQL을 작성하고 데이터를 확인하십시오.

1. DESC를 이용하여 테이블 구조 파악
2. 모든 컬럼을 조회하는 SQL 작성 및 결과 확인
3. PK, FK 컬럼을 조회하는 SQL

##### Exam2) HR.employees table의 구조를 확인하고
사원ID, 사원의성, 직무ID, 채용 날짜를 출력하십시오.
HIRE_DATE 컬럼은 alias로 STARTDATE를 입력하십시오.
```sql
DESCRIBE employees
SELECT employee_id, last_name, job_id, hire_date as STARTDATE
FROM employees;
```
![](https://velog.velcdn.com/images/syshin0116/post/d81912f2-218e-4c9f-806d-4530fde6859d/image.png)

##### Exam3) EMPLOYEES 테이블에서 중복을 제거하고 직무ID를 출력하십시오. 
```sql
SELECT DISTINCT job_id
FROM employees
```

![](https://velog.velcdn.com/images/syshin0116/post/8210d4de-3017-4814-8b03-5a16951d758c/image.png)

##### Exam4) HR 부서에서 보고에 적합하도록 열 머리글의 사원 정보를 쉽게 표시해 달라고 합니다.
열 머리글의 이름을 각각 Emp #, Employee, Job, Hire Date로 지정합니다
```sql
SELECT employee_id "Emp #"
, last_name Employee
, job_id Job
, hire_date "Hire Date"
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/48a84358-13ee-4e0e-b38e-628772accfb0/image.png)

##### Exam5) HR 부서에서 모든 사원과 그들의 직무 ID에 대한 보고서를 요청했습니다. 성과 직무ID를 출력하고(쉼표와 공백으로 구분) 열 이름을 Employee and Title로 지정합니다.
```sql
SELECT last_name||', '||job_id "Employee and Title"
FROM employees; 
```

![](https://velog.velcdn.com/images/syshin0116/post/6c02bb50-1e10-4160-beb5-a42caaffa96b/image.png)

## 3. WHERE 절과 ORDER BY

### 목표
- WHERE 절 이해
- 다양한 조건 처리 방법
- 치환변수
- ORDER BY를 통해 행 정렬
- [연습문제]

### WHERE절을 이용한 행 선택

#### 선택되는 행 제한
```sql
SELECT employee_id, last_name, job_id, department_id
FROM employees
WHERE department_id = 90 ;

SELECT last_name, job_id, department_id
FROM employees
WHERE last_name = 'Whalen' ;

SELECT last_name
FROM employees
WHERE hire_date = '17-FEB-96' ;
```
- 문자열 및 날짜 값은 작은따옴표로 묶는다.
- 문자 값은 대소문자를 구분하고 날짜 값은 형식을 구분
- 기본 날짜 표시 형식은 YY/MM/DD
- 참고 : alter session set nls_date_format = 'YY/MM/DD';

#### 비교 연산자
![](https://velog.velcdn.com/images/syshin0116/post/1ee93653-f1da-48c4-9ab8-63c7b3d2ba3b/image.png)
```sql
SELECT last_name, salary
FROM employees
WHERE salary <= 2200 ;

SELECT last_name, salary
FROM employees
WHERE salary BETWEEN 2200 AND 2400 ;

SELECT employee_id, last_name, salary, manager_id
FROM employees
WHERE manager_id IN (100, 101, 201);
```

#### 비교 연산자(like)
Q) 성에 "a"와 "e"가 모두 포함된 모든 사원의 성을 출력?
- LIKE 연산자는 문자열의 일부가 포함된 데이터를 조회
- LIKE 연산자와 함께 사용할 수 있는 와일드카드
	- % 는 0개 이상의 모든 문자를 의미
	- _ 은 한 개의 문자 를 의미
    
```sql
SELECT first_name
FROM employees
WHERE first_name LIKE 'S%' ;
SELECT last_name
FROM employees
WHERE last_name LIKE '_o%' ;
```
- **ESCAPE** 식별자를 사용하여 **실제 % 및 _ 기호를 검색**할 수 있다
![](https://velog.velcdn.com/images/syshin0116/post/dd7db10f-066d-40c4-b736-9d8fd22fef03/image.png)

#### Null 연산자
담당 관리자가 없는 모든 사원의 이름(last_name)을 출력하시오
- Null값은 알 수 없는 값이므로 어떤 값 과도 같거나 같을 수 없다.
- 알 수 없는 값인 NULL은 비교 불가, 연산 불가!
```sql
SELECT last_name, manager_id
FROM employees
WHERE manager_id IS NULL ;
```
#### 논리 연산자
![](https://velog.velcdn.com/images/syshin0116/post/8b370fb9-0fdb-46de-9d80-4b7bf89cdadc/image.png)

#### 논리 연산자 (AND, OR)
```sql
SELECT employee_id, last_name || ' ' ||
first_name, job_id, salary
FROM employees
WHERE salary >= 10000
AND job_id LIKE '%MAN%' ;

SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary >= 10000
OR job_id LIKE '%MAN%' ;
```
####  논리 연산자 (NOT)

```sql
SELECT last_name, job_id
FROM employees
WHERE job_id
NOT IN ('IT_PROG', 'ST_CLERK', 'SA_REP') ;
```
![](https://velog.velcdn.com/images/syshin0116/post/0559ad32-0861-445e-9b0a-1b162d81619e/image.png)

#### 연산 우선 순위
- AND > OR 이지만, 가독성을 위해서 괄호사용을 권장
```sql
SELECT last_name, job_id, salary
FROM employees
WHERE job_id = 'SA_REP'
OR job_id = 'AD_PRES'
AND salary > 15000;
```
```sql
SELECT last_name, job_id, salary
FROM employees
WHERE (job_id = 'SA_REP'
OR job_id = 'AD_PRES')
AND salary > 15000;
```

## 4. 함수(Function) 활용

### 목표
- 함수(FUNCTION) 이해
- 문자 처리 함수
- 숫자 처리 함수
- 날짜 처리 함수
- [연습문제]

### 기본 SQL 이해 – 기본 함수 사용
![](https://velog.velcdn.com/images/syshin0116/post/49fc53d7-7fa7-4c27-86b4-94f8f66e7899/image.png)

#### 대소문자 변환 함수

![](https://velog.velcdn.com/images/syshin0116/post/270cc5f5-df93-4115-adda-29ff0cf8da08/image.png)

#### 특징(Highlight) 설정 기능
```sql
SELECT 'The job id for '||UPPER(last_name)||' is '
		||LOWER(job_id) AS "EMPLOYEE DETAILS"
FROM employees;
```

#### 대소문자 변환 함수
```sql
SELECT employee_id, last_name, department_id
FROM employees
WHERE last_name = 'higgins';
```
```sql
SELECT employee_id, last_name, department_id
FROM employees
WHERE LOWER(last_name) = 'higgins';
```

#### 문자조작함수
![](https://velog.velcdn.com/images/syshin0116/post/e34d5ca5-f278-4387-b651-50018eafbe3c/image.png)

```sql
SELECT employee_id, CONCAT(first_name, last_name) NAME,
		job_id, LENGTH (last_name),
		INSTR(last_name, 'a') "Contains 'a'?"
FROM employees
WHERE SUBSTR(job_id, 4) = 'REP';
```
![](https://velog.velcdn.com/images/syshin0116/post/bc8868b9-e9e4-44bd-9322-f9e5d7499c89/image.png)

#### Translate()
- 단순 문자열 치환 : TRANSLATE('대상문자열', '비교문자', '바꿀문자')
```sql
SELECT translate('12345', '1', 'x') FROM dual;
```
- 숫자 제거 : TRANSLATE('대상문자열', ' +.0123456789', ' ')
```sql
SELECT trim(translate(‘abc1def2’, ‘+.0123456789’, ‘ '))
FROM dual;
```
- Exam) 사원의 성(last_name)은 소문자로, 급여(salary)는 한글로 변환하시오.
![](https://velog.velcdn.com/images/syshin0116/post/2f671567-ec3b-4b70-887e-39516beda3f0/image.png)

#### 숫자 함수
- ROUND: (숫자, 소수점 자리수)
	- 2: 소수점 두자리
    - -1: 10의자리
```sql
SELECT ROUND(45.923,2), ROUND(45.923,0),
		ROUND(45.923,-1)
FROM DUAL;
```
- TRUNC: 자르기(숫자, 소수점 자리수)
```sql
SELECT TRUNC(45.923,2), TRUNC(45.923),
		TRUNC(45.923,-1)
FROM DUAL;
```
- MOD: 나머지(숫자, 나눌 수)
	- python의 % 와 비슷
```sql
SELECT last_name, salary, MOD(salary, 5000)
FROM employees
WHERE job_id = 'SA_REP';
```
#### 날짜 함수
- 내부 숫자 형식(년, 월, 일, 시, 분, 초)으로 날짜를 저장
- 기본 날짜 표시 형식은 YYYY-MM-DD로 가정
```sql
SELECT last_name, hire_date
FROM employees
WHERE hire_date < '2003-06-17';
```
- 날짜에 숫자를 더하거나 빼서 결과 날짜 값을 구할 수 있다.
- 시간 수를 24로 나눠 날짜에 시간을 더 할 수 있다.

![](https://velog.velcdn.com/images/syshin0116/post/c208adf9-a9f8-4169-aae0-360756a28eb2/image.png)

```sql
SELECT last_name, (SYSDATE-hire_date)/7 AS WEEKS
FROM employees
WHERE department_id = 90;
```

![](https://velog.velcdn.com/images/syshin0116/post/caad45a9-cc90-43ee-9fc1-4281590f3c0f/image.png)
Exam) 근속 기간이 250개월 미만인 모든 사원에 대해 사원 번호, 채용 날짜, 근속 월수, 6개월 평가 날짜,
채용 날짜 이후의 첫 번째 금요일, 채용된 월의 말일을 표시.
#### 날짜 함수 : SYSDATE
![](https://velog.velcdn.com/images/syshin0116/post/de055b23-dc2b-4d19-85b9-bc5b5e6e9624/image.png)
Exam) 2005년에 입사한 모든 사원에 대해 채용 날짜를 비교하고, 사원 번호를 표시하고 ROUND
및 TRUNC 함수를 사용하여 사원번호, 채용 날짜 및 시작 월을 출력하시오.
```sql
SELECT employee_id, hire_date, ROUND(hire_date, 'MONTH'), TRUNC(hire_date, 'MONTH')
FROM employees
WHERE hire_date LIKE '%97';
```

Exam) 각 사원들이 입사 이후 현재까지의 일수,주수,월수,년수 및 아래와 같이 xx년 xx개월 되었는지(근속년월수)를 출력하시오

![](https://velog.velcdn.com/images/syshin0116/post/1ca0824f-fe35-49a8-b884-b94b5fc3b21e/image.png)
```sql
select last_name,
	round(sysdate-hire_date) as days,
	round((sysdate-hire_date)/7) as weeks,
	round((sysdate-hire_date)/(365/12)) as months,
	round((sysdate-hire_date)/365) as years,
	trunc(months_between(sysdate, hire_date) / 12) || '년, ' ||
	trunc(mod(months_between(sysdate, hire_date), 12)) || '개월' as "근속년월수"
from employees;
```

### 주의사항
- 월 단위 이상을 계한 할 떄는 add_months 함수를 이용한다.
- 월별로 일 수가 일정하지 않고(ex. 28일, 30일, 31일), 윤년, 평년도 있어서 계산하기 어렵다.

```sql
SELECT
	add_months(to_Date('20230227', 'YYYYMMDD'), 1), -- 1
    add_months(to_Date('
    
FROM dual;
```

- TRUNC는 특정 데이터의 뒤쪽 데이터를 잘라버리는 함수이다.

```sql
SELECT
	to_char(sysdate, 'YYYY-MM-DD HH24
```
- 날짜/시간 변경 예제
- 일단위 이하를 계산할때는 산술연산자를 이용한다.
```sql
SELECT to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS') 현재시간
, to_char(sysdate + 1, 'YYYY-MM-DD HH24:MI:SS') "현재시간+1일"
, to_char(sysdate + (1/24), 'YYYY-MM-DD HH24:MI:SS') "현재시간+1시간"
, to_char(sysdate + 1/24/60, 'YYYY-MM-DD HH24:MI:SS') "현재시간+1분"
, to_char(sysdate + 1/24/60/60, 'YYYY-MM-DD HH24:MI:SS') "현재시간+1초"
, 1/24 "1시간"
FROM dual;
```
### 목표
- 변환 함수
- NULL 처리 함수
- 조건부 함수
- 피벗 함수
- [연습문제]

### 기본 SQL 이해 – 기본 함수 사용

#### 변환 함수 : 날짜에 TO_CHAR 함수 사용
![](https://velog.velcdn.com/images/syshin0116/post/322c89cc-71d9-4306-b164-6a7731288bd7/image.png)

```sql
SELECT employee_id, TO_CHAR(hire_date, 'MM/YY') Month_Hired
FROM employees
WHERE last_name = 'Higgins';
```

#### 변환 함수 : 날짜에 TO_CHAR 함수 사용
- 시간 요소는 날짜에서 시간부분의 형식 지정 가능
	HH24:MI:SS AM -> 15:45:32 PM
- 문자열은 큰 따옴표로 묶어서 추가 가능
	DD "of" MONTH -> 12 of OCTOBER
- 숫자 접미어는 숫자를 영어 철자로 표기
	ddspth -> fourteenth
    
#### 변환 함수 : 숫자에 TO_CHAR 함수 사용
![](https://velog.velcdn.com/images/syshin0116/post/bfc0ae1e-4d4b-4930-8de1-428f5184ec2c/image.png)
```SQL
SELECT TO_CHAR(salary, '$99,999.00') SALARY
FROM employees
WHERE last_name = 'Ernst';
```
- 정수의 자릿수가 지정된 범위를 초과하는 경우 숫자 대신 (#) 표시

#### 함수 중첩
![](https://velog.velcdn.com/images/syshin0116/post/6bfbb71e-dffd-4811-8b4e-177246ddc379/image.png)

#### Null 관련 함수
![](https://velog.velcdn.com/images/syshin0116/post/d31c6f2d-6317-4879-b5f6-bc105d9e3b14/image.png)

#### Null 관련 함수 : NVL 함수 (Null 값을 실제 값으로 변환)
- Data Type이 반드시 일치해야 함
	– NVL(commission_pct,0)
	– NVL(hire_date,'01-JAN-97')
	– NVL(job_id,'No Job Yet')
```sql
SELECT last_name, salary, NVL(commission_pct, 0),
	(salary*12) + (salary*12*NVL(commission_pct, 0)) AN_SAL
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/2370f8e6-7727-455d-9938-bc57ce8d5899/image.png)

#### Null 관련 함수 : NVL2 함수
- 첫번째 표현식이 null이면 세번째 표현식 반환.
	첫번째 표현식이 null이 아니면 두번째 표현식을 반환

```sql
SELECT last_name, salary, commission_pct,
	NVL2(commission_pct,
		'SAL+COMM', 'SAL') income
FROM employees WHERE department_id IN (50, 80);
```

![](https://velog.velcdn.com/images/syshin0116/post/7564f899-4036-4619-8add-15033e7a7a72/image.png)

#### Null 관련 함수: NULLIF 함수
- NULLIF는 expr1과 expr2를 비교. 두 표현식이 같으면 null을 반환. 두 표현식이 다르면 expr1을 반환.
```sql
SELECT first_name, LENGTH(first_name) "expr1",
		last_name, LENGTH(last_name) "expr2",
		NULLIF(LENGTH(first_name), LENGTH(last_name)) result
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/ce76d056-ee29-4791-8833-a9f9e516a670/image.png)

#### Null 관련 함수 : COALESCE 함수
- COALESCE 함수의 인수의 개수는 동적으로 입력 가능
- NULL이 아닌 첫번째 인수의 값을 반환
- 모든 인수가 NULL 이면 NULL 을 반환
```sql
SELECT last_name, employee_id,
	COALESCE(TO_CHAR(commission_pct),TO_CHAR(manager_id),
		'No commission and no manager')
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/446b99ca-dd6c-4133-b2a4-d0466011f6a0/image.png)

#### 조건부 표현식 관련 함수(DECODE): SQL 문에서 IF-THEN-ELSE 논리를 사용
```sql
SELECT last_name, job_id, salary,
	DECODE(job_id, 'IT_PROG', 1.10*salary,
			'ST_CLERK', 1.15*salary,
			'SA_REP', 1.20*salary,
			salary)
	REVISED_SALARY
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/9ce17fb9-8737-46d4-9d67-cb8c7aca0fad/image.png)

#### 조건부 표현식 관련 함수(CASE): SQL 문에서 IF-THEN-ELSE 논리를 사용
```sql
SELECT last_name, job_id, salary,
	CASE job_id WHEN 'IT_PROG' THEN 1.10*salary
		WHEN 'ST_CLERK' THEN 1.15*salary
		WHEN 'SA_REP' THEN 1.20*salary
	ELSE salary END "REVISED_SALARY"
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/7a39fc12-7dd7-4a94-bebd-622b754e1192/image.png)

#### CASE와 DECODE와 다른 점은 조건비교에 있어서 크다(>), 작다(<),
같다(=) 로직이 가능
```sql
SELECT last_name,salary,
      (CASE WHEN salary < 5000 THEN 'Low'
          WHEN salary < 10000 THEN 'Medium'
          WHEN salary < 20000 THEN 'Good'
          ELSE 'Excellent'
      END) as qualified_salary
FROM employees;
```
```sql
--급여별로 인상율을 다르게 계산 (scott)
SELECT ename ,
		CASE
			WHEN sal < 1000 THEN sal+(sal*0.8)
			WHEN sal BETWEEN 1000 AND 2000 THEN sal+(sal*0.5)
			WHEN sal BETWEEN 2001 AND 3000 THEN sal+(sal*0.3)
			ELSE sal+(sal*0.1)
		END sal
FROM scott.emp; 
```
### CASE 함수 응용 – Virtual Column
#### **가상 컬럼** 이란? 테이블에 포함되는 일반적인 컬럼은 해당 데이터
타입에 맞는 데이터만 갖지만, 가상 컬럼은 여러 개의 데이터를 연
산한 결과값을 저장하는 컬럼 (11g NF)
```shell
orcl@SCOTT> create table copy_emp as select * from emp;
orcl@SCOTT> alter table copy_emp
2 		add (sal_grade varchar2(6)
3 		as (CASE
4 				WHEN sal between 1 and 1000 THEN 'LOW'
5 				WHEN sal between 1001 and 2000 THEN 'MEDIUM'
6 				WHEN sal between 2001 and 3000 THEN 'HIGH'
7 				ELSE 'ULTRA'
8 			END) virtual );
orcl@SCOTT> select ename, sal, sal_grade from copy_emp;
orcl@SCOTT> insert into copy_emp (empno, ename, sal) values (9999,'LEE',4000);
orcl@SCOTT> select table_name, column_name, data_type, data_default
2 from user_tab_columns
3 where table_name='COPY_EMP';
```
### pivot / unpivot 함수
#### pivot( )
- row 형태의 데이터를 column 형태로 보여주는 쿼리를 row-to-column
#### unpivot( ) 
- column 형태를 row 형태로 보여주는 쿼리를 column-to-row
#### Syntax
```sql
SELECT * FROM
(
	SELECT column1, column2
	FROM tables
	WHERE conditions
)
PIVOT
(
	aggregate_function(column2)
	FOR column2
	IN ( expr1, expr2, ... expr_n) | subquery
)
ORDER BY expression [ ASC | DESC ];
```

#### DECODE를 이용하여 복잡한 조건식 평가나 여러 컬럼을 이용한 조건식을 평가해야 하는 경우, 문장의 복잡성과 성능에 문제점을 가질 수 있다
```sql
SELECT department_id,
  SUM(DECODE(job_id, 'IT_PROG', salary)) "IT MAN" ,
  SUM(DECODE(job_id, 'SA_REP', salary)) "SALES MAN" ,
  SUM(DECODE(job_id, 'ST_CLERK', salary)) "STOCK MAN"
FROM employees
GROUP BY department_id ;
```
#### 11g 부터는 PIVOT 와 UNPIVOT 절을 통해서 보다 쉽게 구현 가능
```sql
SELECT *
FROM ( SELECT department_id, job_id, salary
FROM employees )
PIVOT ( SUM(salary) FOR job_id IN ( 'IT_PROG' AS "IT MAN"
                                    ,'SA_REP' AS "SALES MAN"
                                    ,'ST_CLERK' AS "STOCK MAN")) ;
```
#### Example 1: 부서 별 사원수 집계 현황?
```sql
SELECT department_id
, COUNT(*)
FROM employees
GROUP BY department_id;
```
![](https://velog.velcdn.com/images/syshin0116/post/25acc728-6f8d-4c4e-b28c-4dddfd3e744e/image.png)

```sql
SELECT *
FROM (SELECT department_id
FROM employees)
PIVOT(COUNT(*)
FOR (department_id)
IN (10,20,50,60
,80,90,110,190));
```

![](https://velog.velcdn.com/images/syshin0116/post/c16efbc9-cd2c-4d65-b92a-59ec9dd82773/image.png)

#### Example 2: 사원의 월 별 급여 집계?
```sql
SELECT * FROM
	(SELECT '1월' 월, '이태정' 성명, 110 급여 FROM DUAL UNION ALL
	SELECT '1월' 월, '이태정' 성명, 305 급여 FROM DUAL UNION ALL
	SELECT '1월' 월, '이태서' 성명, 210 급여 FROM DUAL UNION ALL
	SELECT '2월' 월, '이태정' 성명, 120 급여 FROM DUAL UNION ALL
	SELECT '2월' 월, '이태서' 성명, 220 급여 FROM DUAL)
	PIVOT ( SUM(급여) FOR 월 IN ('1월', '2월') );
	SELECT * FROM
(
	SELECT '이태정' 성명, 140 일월, 120 이월 FROM DUAL UNION ALL
	SELECT '이태서' 성명, 210 일월, 220 이월 FROM DUAL
)
UNPIVOT ( 급여 FOR 월 IN (일월, 이월) );
```
#### Exam3) 사원의 성과 커미션 금액을 출력. 사원이 커미션을 받지 않으면 "No Commission"을 표시.커미션의 포맷은 ‘90.99’ Alias를 COMM으로 지정
```sql
SELECT last_name,
		NVL(TO_CHAR(commission_pct, 90.99), 'No Commission') COMM
FROM employees; 
```
#### Exam4) 성, 급여, 커미션, 새 급여를 출력 하십시오.커미션을 받지 않는 사원에게는 $2,000의 급여 인상을 하고 커미션을 받는 사원의 경우에는 기존 급여에 커미션 금액을 추가한 새 급여를 출력 하십시오
```sql
SELECT last_name
	, salary
	, commission_pct
	, COALESCE((salary+(commission_pct*salary)), salary+2000, salary) as "New
Salary"
FROM employees;
```
#### Exam5) 다음 데이터를 사용하여 DECODE/CASE 함수를 통해 JOB_ID 열의 값을 기반으로 모든 사원의 등급을 출력하시오.
```sql
SELECT job_id, decode (job_id,
	'ST_CLERK', 'E',
	'SA_REP', 'D',
	'IT_PROG', 'C',
	'ST_MAN', 'B',
	'AD_PRES', 'A',
	'0')GRADE
FROM employees;
```
```sql
SELECT job_id
	, CASE job_id WHEN 'ST_CLERK' THEN 'E'
		WHEN 'SA_REP' THEN 'D'
		WHEN 'IT_PROG' THEN 'C'
		WHEN 'ST_MAN' THEN 'B'
		WHEN 'AD_PRES' THEN 'A'
		ELSE '0'
	END AS GRADE
FROM employees
order by job_id, GRADE;
```
![](https://velog.velcdn.com/images/syshin0116/post/9b78d6fb-c2d8-43f0-9967-1fdecf02958a/image.png)
#### 실무 Tip) 은행에서 입금되는 숫자 금액을 한글로 변환하여 입력하는 SQL을 작성하시오.
```sql
    SELECT salary
    , TRANSLATE
    ( SUBSTR(money, 1,1)||DECODE(SUBSTR(money, 1,1),0,'','천')
    || SUBSTR(money, 2,1)||DECODE(SUBSTR(money, 2,1),0,'','백')
    || SUBSTR(money, 3,1)||DECODE(SUBSTR(money, 3,1),0,'','십')
    || SUBSTR(money, 4,1)||DECODE(SUBSTR(money, 1,4),0,'','조')
    || SUBSTR(money, 5,1)||DECODE(SUBSTR(money, 5,1),0,'','천')
    || SUBSTR(money, 6,1)||DECODE(SUBSTR(money, 6,1),0,'','백')
    || SUBSTR(money, 7,1)||DECODE(SUBSTR(money, 7,1),0,'','십')
    || SUBSTR(money, 8,1)||DECODE(SUBSTR(money, 5,4),0,'','억')
    || SUBSTR(money, 9,1)||DECODE(SUBSTR(money, 9,1),0,'','천')
    || SUBSTR(money,10,1)||DECODE(SUBSTR(money,10,1),0,'','백')
    || SUBSTR(money,11,1)||DECODE(SUBSTR(money,11,1),0,'','십')
    || SUBSTR(money,12,1)||DECODE(SUBSTR(money, 9,4),0,'','만')
    || SUBSTR(money,13,1)||DECODE(SUBSTR(money,13,1),0,'','천')
    || SUBSTR(money,14,1)||DECODE(SUBSTR(money,14,1),0,'','백')
    || SUBSTR(money,15,1)||DECODE(SUBSTR(money,15,1),0,'','십')
    || SUBSTR(money,16,1)
    , '1234567890', '일이삼사오육칠팔구') money
FROM (SELECT salary, LPAD(salary,16,'0') money FROM employees);
```

![](https://velog.velcdn.com/images/syshin0116/post/f1d148e9-4faa-4a26-83e6-f3f08324b290/image.png)

## 5. 그룹 데이터 처리
### 목표
- GROUP BY 절 이해
- 그룹 데이터 조건 처리를 위한 HAVING 절
- 상위 집계처리를 위한 ROLLUP과 CUBE
- [연습문제]

### Group data 처리 – 집계처리
#### Group Function
- AVG
- COUNT
- MAX
- MIN
- STDDEV
- SUM
- VARIANCE
#### Group Function : 숫자처리 함수 AVG(), SUM()
```sql
SELECT AVG(salary), MAX(salary),
MIN(salary), SUM(salary)
FROM employees
WHERE job_id LIKE '%REP%';
```
![](https://velog.velcdn.com/images/syshin0116/post/f7afb56b-a5ca-47cc-8cec-e0a459e38de2/image.png)

#### Group Function : 숫자, 문자, 날짜처리 함수 MAX(), MIN()
```sql
SELECT MIN(hire_date), MAX(hire_date)
FROM employees;
```
![](https://velog.velcdn.com/images/syshin0116/post/acb644ed-9beb-450d-91b4-6cf1ed0410b0/image.png)

#### Group Function : 테이블의 모든 행 수 COUNT(*)
```sql
SELECT COUNT(*)
FROM employees
WHERE department_id = 50;
```

#### Group Function : null이 아닌 값을 가진 행 수 COUNT(expr)
```sql
SELECT COUNT(commission_pct)
FROM employees
WHERE department_id = 80;
```
#### Group Function : expr의 null과 중복 값이 아닌 행 수 COUNT(DISTINCT expr)
```sql
SELECT COUNT(DISTINCT department_id)
FROM employees;
```
#### Group Function는 컬럼에 있는 null 값 무시
```sql
SELECT AVG(commission_pct)
FROM employees;

```
#### NVL을 이용하여 강제로 그룹 함수에 null 을 사용가능 값으로
```sql
SELECT AVG(NVL(commission_pct, 0))
FROM employees;
```
#### Quiz1> 전체 사원수와 2008년에 입사한 사원수를 출력하시오.
```sql
SELECT '총 사원수 = ' || COUNT(*) total,
‘2008년 입사한 사원수 = ' ||
_________________________________________________
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/119cf73f-c999-496f-b446-1d28f090857a/image.png)

#### Quiz1> 전체 사원수와 2008년에 입사한 사원수를 출력하시오.
```sql
SELECT '총 사원수 = ' || COUNT(*) total,
'2008년 입사한 사원수 = ' ||
SUM(DECODE(TO_CHAR(hire_date,'YYYY'),2008,1,0)) "2008"
FROM employees;
```
```sql
SELECT '총 사원수 = ' || COUNT(*) total
, '2008년 입사한 사원수 = '
|| COUNT(CASE WHEN to_char(hire_date,'YYYY’) LIKE '2008%’
THEN 1 END) "2008"
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/de97b71d-4ba0-4cfc-a12c-1c3b1d913209/image.png)

### Group data 처리 – 집계처리(pivot() : 11gNF)
#### Quiz2> 2002, 2004, 2008년도에 입사한 사원들의 급여 합계를 구하시오.
```sql
SELECT
	SUM(DECODE(to_char(hire_date,'YYYY'), '2002', salary, 0)) "2002",
	SUM(DECODE(to_char(hire_date,'YYYY'), '2004', salary, 0)) "2004",
	SUM(DECODE(to_char(hire_date,'YYYY'), '2008', salary, 0)) "2008"
FROM employees;
```
```sql
SELECT *
FROM (SELECT to_char(hire_date, 'YYYY') as HDATE, salary
		FROM employees)
PIVOT (
		sum(salary) for HDATE in ('2002', '2004', '2008')
);
```
#### Group data 처리

![](https://velog.velcdn.com/images/syshin0116/post/2ec3dc49-f327-44d7-aa24-529985b626e0/image.png)
#### Group data 처리 : group by 절을 이용하여 행을 더 작은 그룹으로…
- 그룹 함수에 속하지 않는 SELECT 리스트의 모든 열은 GROUP BY 절에 있어야 한다
```sql
SELECT AVG(salary)
FROM employees
GROUP BY department_id ;
```

![](https://velog.velcdn.com/images/syshin0116/post/cb857cf2-f9c4-4e74-9ef4-405701d80cb5/image.png)

- 다중 컬럼 group by
```sql
SELECT department_id, job_id, SUM(salary)
FROM employees
WHERE department_id > 40
GROUP BY department_id, job_id
ORDER BY department_id;
```
![](https://velog.velcdn.com/images/syshin0116/post/28ad4299-b557-437b-a253-86b9cb0542cd/image.png)
#### 잘못된 예
![](https://velog.velcdn.com/images/syshin0116/post/fac5a85a-4915-4f04-84d6-76b8262908c5/image.png)

#### Group data 결과 제한(Having)
![](https://velog.velcdn.com/images/syshin0116/post/aec1ae02-b05e-4e22-8ca3-0a3dd2c77695/image.png)

#### Group data 결과 제한 : Having

#### Quiz) 사원 테이블에서 업무에 REP가 포함된 것은 제외하고 업무별 전체 급여 합계를 구하고 업무별 전체 급여 합계 중 \$13000 보다 큰 것만 조건으로 전체 급여 합계로 오름차순 정렬해서 출력 하시오.

```sql
SELECT job_id, SUM(salary) PAYROLL
FROM employees
WHERE job_id NOT LIKE '%REP%'
GROUP BY job_id
HAVING SUM(salary) > 13000
ORDER BY SUM(salary) ASC;
```

#### Group 함수를 중첩하는 경우 반드시 Group by 절을 사용해야 한다
```sql
SELECT MAX(AVG(salary))
FROM employees
GROUP BY department_id;
```
### 생각해봅시다(1)
![](https://velog.velcdn.com/images/syshin0116/post/4912f6ec-63e4-4310-aaef-d30de77c0ff7/image.png)

### 생각해봅시다(2)
![](https://velog.velcdn.com/images/syshin0116/post/5f852fc5-1d55-4ddd-aae6-1f2d98865209/image.png)

### Group data 처리 – 집계처리(연습문제)
#### Exam1) 각 직무 유형에 대해 최소, 최대, 합계 및 평균 급여를 표시하고, Maximum, Minimum, Sum, Average로 지정하시오.

```sql
SELECT job_id,
MAX(salary) "Maximum",
MIN(salary) "Minimum",
SUM(salary) "Sum",
ROUND(AVG(salary),0) "Average"
FROM employees
GROUP BY job_id; 
```
![](https://velog.velcdn.com/images/syshin0116/post/52982ee4-ca6b-4868-ba5a-65d2c1442936/image.png)

#### Exam2) 동일한 직무를 수행하는 사람 수를 출력하시오.
```sql
SELECT job_id, COUNT(*)
FROM employees
GROUP BY job_id; 
```
![](https://velog.velcdn.com/images/syshin0116/post/8a52c5a3-6475-483b-b5ee-396619da347b/image.png)

#### Exam3) 관리자를 나열하지 않는 채로 관리자 수를 출력하고, alias는 Number of Managers로 지정. 

```sql
SELECT COUNT(DISTINCT manager_id) "Number of Managers"
FROM employees;
```
#### Exam4) 관리자 번호 및 해당 관리자에 속한 사원의 최저 급여를 출력. 관리자를 알 수 없는 사원 및 최저 급여가 \$6,000 미만인 그룹은 제외시키고, 최저급여에 대한 내림차순 정렬 하시오.
```sql
SELECT manager_id, MIN(salary)
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING MIN(salary) >= 6000
ORDER BY MIN(salary) DESC;
```

#### Exam5) 부서별 사원수를 구하고, 전체 사원수가 3이하인 부서정보만 출력하시오. 단, 사원 중 부서에 소속되어 있지 않은 사원은 제외하고, 부서별로 오름차순 정렬하시오
```sql
SELECT department_id, COUNT(*)
FROM EMPLOYEES
WHERE department_id IS NOT NULL
GROUP BY department_id
HAVING COUNT(*) <= 3
ORDER BY department_id ;
```
![](https://velog.velcdn.com/images/syshin0116/post/f1408b4e-0c6b-41e7-ba46-21a277fb14bb/image.png)

#### Exam6) 업무별 급여 합계 및 평균급여를 \$표시와 함께 출력하시오. 단, 80번 부서에 대한 정보만 출력하고, 업무별로 오름차순 정렬하시오.
```sql
SELECT job_id,
TO_CHAR(SUM(salary), '$999,999.00') tot_sal,
TO_CHAR(AVG(salary), '$999,999.00') avg_sal
FROM employees
WHERE department_id = 80
GROUP BY job_id
ORDER BY job_id ;
```
![](https://velog.velcdn.com/images/syshin0116/post/73aeec22-e8df-4c2b-93d9-945d0856b4eb/image.png)

#### Exam7) 사원의 총 수와 2005년, 2006년, 2007년 및 2008년에 채용된 사원 수를 출력.(alias - TOTAL, 2005, 2006, 2007, 2008 로 표시)
```sql
SELECT COUNT(*) total,
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2005,1,0)) "2005",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2006,1,0)) "2006",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2007,1,0)) "2007",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'),2008,1,0)) "2008"
FROM employees;
```
#### Exam8) 업무를 표시하고 해당 업무에 대해 부서별 급여 및 부서 20, 50, 80 및 90의 급여 총액을 출력.(alias - JOB, Dept20, Dept50, Dept80, Dept90, Total 로 표시)

```sql
SELECT job_id "Job",
SUM(DECODE(department_id , 20, salary)) "Dept 20",
SUM(DECODE(department_id , 50, salary)) "Dept 50",
SUM(DECODE(department_id , 80, salary)) "Dept 80",
SUM(DECODE(department_id , 90, salary)) "Dept 90",
SUM(salary) "Total"
FROM employees
GROUP BY job_id;
```
![](https://velog.velcdn.com/images/syshin0116/post/163d2f4a-7209-48f7-95b6-c5c2991d3771/image.png)
#### Exam9) 한 줄로 월별 입사한 사원수의 총합을 구하고 부서별, 월별 입사한 사원수를 구하시오
```sql
SELECT
SUM(DECODE(TO_CHAR(hire_date,'MM'), '01', 1, 0)) "1월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '02', 1, 0)) "2월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '03', 1, 0)) "3월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '04', 1, 0)) "4월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '05', 1, 0)) "5월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '06', 1, 0)) "6월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '07', 1, 0)) "7월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '08', 1, 0)) "8월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '09', 1, 0)) "9월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '10', 1, 0)) "10월"
, SUM(DECODE(TO_CHAR(hire_date,'MM'), '11', 1, 0)) "11월"
, SUM(DECODE(TO_CHAR(hire_date,'mm'), '12', 1, 0)) "12월"
FROM employees;
```
```sql
SELECT
department_id,
SUM(DECODE(TO_CHAR(hire_date,'MM'), '01', 1, 0)) "1월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '02', 1, 0)) "2월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '03', 1, 0)) "3월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '04', 1, 0)) "4월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '05', 1, 0)) "5월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '06', 1, 0)) "6월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '07', 1, 0)) "7월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '08', 1, 0)) "8월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '09', 1, 0)) "9월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '10', 1, 0)) "10월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '11', 1, 0)) "11월",
SUM(DECODE(TO_CHAR(hire_date,'MM'), '12', 1, 0)) "12월"
FROM employees
GROUP BY department_id
ORDER BY department_id;
```

### Group data 처리 – 고급(상위)집계처리
#### GROUP BY에 ROLLUP 및 CUBE 연산자 사용
- GROUP BY에 ROLLUP 또는 CUBE를 사용하여 상호 참조 열별로 대 집계 행을 생성.
- ROLLUP 그룹화는 일반 그룹화 행과 소계, 총계 값을 포함한 결과 집합을 생성.
- CUBE 그룹화는 ROLLUP에 따른 행과 교차 분석 행이 포함된 결과 집합을 생성.

#### GROUP BY에 ROLLUP 사용
- ROLLUP 연산자 없이 n차원(즉, GROUP BY 절에 있는 n개의 열)에서 소
계를 생성하려면 n+1개의 SELECT 문을 UNION ALL과 연결해야 한다.
- 이렇게 하면 SELECT 문마다 테이블에 액세스하게 되므로 쿼리가
비효율적으로 실행되므로
- ROLLUP 연산자는 테이블에 한 번만 액세스하여 해당 결과를 수집한다.
- 소계 생성에 관련된 열이 많을 경우에는 ROLLUP 연산자가 유용
#### ROLLUP(col1[col2,...coln])

#### GROUP BY에 ROLLUP 사용: 각 부서의 급여 합계 계산
```sql
SELECT department_id, job_id, SUM(salary)
FROM employees
WHERE department_id < 60
GROUP BY ROLLUP(department_id, job_id);
```
![](https://velog.velcdn.com/images/syshin0116/post/b0449c62-d721-46f4-ab65-d7bde12354a0/image.png)
#### GROUP BY에 CUBE 사용
- CUBE 연산자를 사용하여 단일 SELECT문으로 교차 분석 값 생성
- ROLLUP은 가능한 소계 조합의 일부만 생성하지만, CUBE는 GROUP BY
절에 지정된 가능한 모든 그룹화 조합의 소계와 총계를 생성
- GROUP BY절에 N 열이나 표현식이 있을 경우 개의 가능한 대 집계
조합을 생성
- 응용 프로그램이나 프로그래밍 도구를 사용하여 이러한 대집계 값을
차트와 그래프에 제공하여 결과와 관계를 시각적이고 효율적으로 전
달할 수 있다.
#### CUBE(col1[col2,...coln])
#### GROUP BY에 CUBE사용
```sql
SELECT department_id, job_id, SUM(salary)
FROM employees
WHERE department_id < 50
GROUP BY CUBE(department_id, job_id)
ORDER BY department_id nulls last, job_id nulls last;
```
![](https://velog.velcdn.com/images/syshin0116/post/625675bc-ce01-4832-bcc7-4ca0e0eaa954/image.png)
#### GROUPING 함수
- CUBE 또는 ROLLUP 연산자와 함께 사용
- 행에서 소계를 형성하는 그룹을 찾는데 사용
- ROLLUP 또는 CUBE로 생성된 NULL 값과 저장된 NULL 값을 구분하는
데 사용
- **0** (해당 열을 이용한 group data 고려) 또는 1(고려 안 함)을 반환
#### GROUPING_ID(col1[col2,...coln])
#### GROUPING(col1)
#### GROUPING 함수
```sql
SELECT department_id, job_id
, GROUPING_ID(department_id, job_id)GRP_D_J_ID
, GROUPING(department_id) GRP_DEPT
, GROUPING(job_id) GRP_JOB
, SUM(salary)
FROM employees
WHERE department_id < 50
GROUP BY CUBE(department_id, job_id)
ORDER BY GROUPING_ID(department_id, job_id),
department_id, job_id;
```

![](https://velog.velcdn.com/images/syshin0116/post/7b9e9cdf-10d5-4f69-8f87-ffcaf9716563/image.png)





## HR,SCOTT 스키마 실습환경 설정하기

### 명령어
#### 유저생성
```sql
CREATE USER <유저명> IDENTIFIED BY 패스워드;
```
#### 유저변경
```sql
ALTER USER <유저명> IDENTIFIED BY 패스워드;
ALTER USER <유저명> ACCOUNT UNLOCK;
ALTER USER <유저명> IDENTIFIED BY 패스워드 ACCOUNT UNLOCK;
ALTER USER <유저명> QUOTA 사이즈 ON USERS;
```
#### 권한부여
```sql
GRANT <권한> TO <유저명>;
```
### 1. SCOTT 스키마 생성 스크립트 확인 및 생성
@는 해당 경로의 sql 파일을 실행한다
```shell
vi $ORACLE_HOME/rdbms/admin/utlsampl.sql
sqlplus sys/oracle as sysdba
SQL> @$ORACLE_HOME/rdbms/admin/utlsampl.sql
SQL> select username, account_status
from dba_users
where username in ('HR', 'SCOTT');
```

### 2. SCOTT 계정 접속
```shell
sqlplus scott/tiger
SQL> desc emp;
```

### 3. HR 계정 접속
```shell
sqlplus hr/hr
ERROR:
ORA-28000: The account is locked.
```
### 4. 관리자 계정 접속
#### 4.1 SCOTT, HR 상태 및 테이블스페이스 쿼터 정보 확인
```sql
select username, account_status
from dba_users
where username in ('HR', 'SCOTT');
select * from dba_ts_quotas
where username in ('HR', 'SCOTT');
```


#### 4.2 HR 계정 락 해제
    
```sql
ALTER USER HR ACCOUNT UNLOCK;
```
#### 4.3 HR 계정 비밀번호 변경
```sql
ALTER USER HR IDENTIFIED by hr;
```
### 5. HR 계정 접속
```
sqlplus hr/hr
desc employees;
```

#### 5.1. HR 계정에서 job_grades 테이블 생성
```sql
DROP TABLE job_grades;
CREATE TABLE job_grades (
grade_level CHAR(1),
lowest_sal NUMBER(8,2) NOT NULL,
highest_sal NUMBER(8,2) NOT NULL
);
ALTER TABLE job_grades
ADD CONSTRAINT job_grades_grade_level_pk PRIMARY KEY (grade_level);

INSERT INTO job_grades VALUES ('A', 1000, 2999);
INSERT INTO job_grades VALUES ('B', 3000, 5999);
INSERT INTO job_grades VALUES ('C', 6000, 9999);
INSERT INTO job_grades VALUES ('D', 10000, 14999);
INSERT INTO job_grades VALUES ('E', 15000, 24999);
INSERT INTO job_grades VALUES ('F', 25000, 40000);
COMMIT;
```
### 6. SCOTT, HR, USER01의 권한, 롤, 쿼터 확인
```sql
-- SCOTT, HR, USER01에게 부여된 시스템 권한
select grantee, privilege
from dba_sys_privs
where grantee IN ('SCOTT', 'HR', 'USER01')
order by grantee;
-- SCOTT, HR, USER01에게 부여된 롤
select *
from dba_role_privs
where grantee IN ('SCOTT', 'HR', 'USER01')
order by grantee, granted_role;
-- 롤에 부여된 시스템 권한 조회
select role, privilege
from role_sys_privs
where role in ('RESOURCE', 'CONNECT')
order by role;
-- 계정에 부여된 테이블스페이스 쿼터 조회
select * from dba_ts_quotas
where username in ('HR', 'SCOTT', 'USER01');
```

### 7. HR ERD 확인
![](https://velog.velcdn.com/images/syshin0116/post/55cbcafc-ac11-4568-8ef5-38cc4c9cb19c/image.png)

### 8. SCOTT ERD 확인
![](https://velog.velcdn.com/images/syshin0116/post/07e80754-6a71-4fba-b40a-cc0331b4a0c9/image.png)

## 유저생성 및 권한부여
![](https://velog.velcdn.com/images/syshin0116/post/96c9cc07-c66a-46a9-9a77-aa282f36030c/image.png)

#### 유저생성
```sql
CREATE USER <유저명> IDENTIFIED BY 패스워드;
```
#### 유저변경
```sql
ALTER USER <유저명> IDENTIFIED BY 패스워드;
ALTER USER <유저명> ACCOUNT UNLOCK;
ALTER USER <유저명> IDENTIFIED BY 패스워드 ACCOUNT UNLOCK;
ALTER USER <유저명> QUOTA 사이즈 ON USERS;
```
#### 권한부여
```sql
GRANT <권한> TO <유저명>;
유저생성, 권한부여 한번에 하는 예제
GRANT CREATE SESSION, CREATE TABLE, UNLIMITED TABLESPACE TO USER01 IDENTIFIED BY oracle;
```
#### 1. 유저 만들기
```
# sqlplus sys/oracle as sysdba
SQL > create user user01 identified by oracle;
```
#### 2. 생성한 user01 계정으로 접속 시도
```
$> sqlplus user01/oracle
ERROR
ORA-01045: user USER01 lacks CREATE SESSION privilege; logon denied
```
세션 생성 권한이 없어서 발생

#### 3. user01 계정에 세션생성 권한 부여

* 관리자 계정(sys)
```
SQL > grant create session to user01;
```
사용자에게 세션 생성 권한을 부여해야지 오라클 서버에 접속하여 사용할 수 있음


#### 4. user01 계정 접속 재시도
```
$> sqlplus user01/oracle
```

#### 5. user01 계정으로 테이블 생성
```
SQL > create table tbl_test
(
 id varchar2(10)
);
ERROR
ORA-01031: insufficient privileges
테이블 생성 권한이 없어서 에러 발생
```
#### 6. user01에게 테이블 생성 권한 부여
```
* 관리자 계정(sys)
SQL > grant create table to user01;
```
#### 7. user01 계정으로 테이블 생성
```
SQL > create table tbl_test (
 id varchar2(10)
);
```
#### 8. user01.tbl_test에 데이터 입력 및 테이블스페이스 쿼터(할당) 용량 조회
```
insert into tbl_test (id) values('01');
ERROR
ORA-01950: no privileges on tablespace 'USERS'
테이블스페이스에 얼마만큼의 영역을 할당할 것인지 정해지지 않아서 생기는 오류
select * from user_ts_quotas;
-- 테이블스페이스에 할당된 용량이 없는 경우 아무것도 조회되지 않는다
```
#### 9. user01에게 테이블스페이스 쿼터(할당) 용량 설정
```
* 관리자 계정(sys)
ALTER USER user01 QUOTA 10M ON USERS;
ALTER USER user01 QUOTA UNLIMITED ON USERS;
select * from dba_ts_quotas
where username in ('USER01');
```
#### 10. user01.tbl_test에 데이터 입력 및 확인
```
* user01 계정
insert into tbl_test (id) values('01');
insert into tbl_test (id) values('02');
select * from tbl_test;
commit;
select * from user_ts_quotas;
```
#### 11. user01에게 롤 부여
```
* 관리자 계정(sys)
grant connect, resource to user01;
```
#### 12. user01의 시스템 권한, 롤, 쿼터 확인
```
-- 관리자 계정(sys)
-- user01에게 부여된 시스템 권한
select grantee, privilege
from dba_sys_privs
where grantee IN ('USER01')
order by grantee;
-- user01에게 부여된 롤
select *
from dba_role_privs
where grantee IN ('USER01')
order by grantee, granted_role;
-- 롤에 부여된 시스템 권한 조회
select role, privilege
from role_sys_privs
where role in ('RESOURCE', 'CONNECT')
order by role;
-- 계정에 부여된 테이블스페이스 쿼터 조회
select * from dba_ts_quotas
where username in ('USER01');
```
#### 13. SCOTT, HR, USER01의 시스템 권한, 롤, 쿼터 조회 및 비교
```
-- SCOTT, HR, USER01에게 부여된 시스템 권한
select grantee, privilege
from dba_sys_privs
where grantee IN ('SCOTT', 'HR', 'USER01')
order by grantee;
-- SCOTT, HR, USER01에게 부여된 롤
select *
from dba_role_privs
where grantee IN ('SCOTT', 'HR', 'USER01')
order by grantee, granted_role;
-- 롤에 부여된 시스템 권한 조회
select role, privilege
from role_sys_privs
where role in ('RESOURCE', 'CONNECT')
order by role;
-- 계정에 부여된 테이블스페이스 쿼터 조회
select * from dba_ts_quotas
where username in ('HR', 'SCOTT', 'USER01');
```

## Oracle SQL Developer에서 HR ERD 추출 방법
#### 1. 파일 > Data Modeler > 임포트 > 데이터 딕셔너리 선택
![](https://velog.velcdn.com/images/syshin0116/post/7734bee9-bf57-4622-9f29-95f24238424f/image.png)
#### 2. HR 선택후 다음 버튼 클릭
![](https://velog.velcdn.com/images/syshin0116/post/14f7b713-523a-45d9-9aec-90860a8bda10/image.png)
#### 3. HR 선택후 다음 버튼 클릭
![](https://velog.velcdn.com/images/syshin0116/post/ef44574e-feb2-4141-a312-7d587cfaaf1b/image.png)

#### 3. 모두 선택하고 다음 버튼 클릭
![](https://velog.velcdn.com/images/syshin0116/post/d17ff16f-1f1a-4d62-98bc-2c35111e11d3/image.png)
#### 4. 완료 버튼 클릭

#### 5. HR 테이블 다이어그램 확인
#### 6. 다이어그램에서 컬럼(열)만 보여주기 설정
우측 마우스 클릭 > 세부정보 보기 > 열 클릭
![](https://velog.velcdn.com/images/syshin0116/post/b2f40d00-67d5-4b7b-8022-e0e4cd6056b3/image.png)

## SQL 수행되는 순서
5. SELECT
1. FROM
2. WHERE
3. GROUP BY
4. HAVING
6. ORDER BY
