---
title: "[ORACLE-WDP]4일차-DML과 트랜잭션, 테이블 생성관리, 고급쿼리"
date: 2023-05-14 20:00:00 +0900
categories: [Database,ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---


<!--#### 공유url: http://naver.me/xoKMlnp5
#### -->


# Oracle Database 19C

## 8. DML과 트랜잭션

### 8.1 목표
- DML(Data Manipulation Language) 구문
- INSERT
- UPDATE
- DELETE
- TRANSACTION
- COMMIT & ROLLBACK

#### A DML statement is executed when you:
- 테이블에 **새 행 추가**
- 테이블의 **기존 행 수정**
- 테이블에서 **기존 행 삭제**
#### 데이터베이스의 상태 변환을 위한 일련의 논리적 작업 단위 하나의 작업을 수행하기 위해 필요한 DML의 집합
**(단, DDL, DCL은 자동 커밋이 동반되는 명령어)**
- RDBMS의 특징 ACID
- **A**tomicity (원자성)
- **C**onsistency (일관성)
- **I**solation (고립성, 격리성)
- **D**urability (지속성)

#### ACID 의미
- **원자성 (Atomicity)**
**1) All or Noting**
2) 작업단위를 일부분만 실행하지 않는다.
3) 자금 이체 시 양쪽 계좌에 모두 반영 혹은 미 반영
- 일관성 (Consistency)
1) 트랜잭션이 성공적으로 완료되면 **일관된 DB상태를 유지**
예) 자금 이체 할 경우 두 계좌 잔고의 합은 이체 전후가 같아야 함
2) 트랜잭션 이전 이후 DB는 **일관적으로 제약조건을 만족**
3) 기본 키, 외래 키 제약과 같은 명시적인 무결성 제약 조건들 유지
- 고립성 (Isolation)
1) **모든 트랜잭션은 다른 트랜잭션으로부터 독립**되어야 한다는 뜻
2) 동시에 다수 트랜잭션 수행 시, 각 트랜잭션은 고립되어 있어 연속으로 실행된 것과 동일한 결과를 가짐
- 지속성 (Durability)
1) 성공적으로 수행된 트랜잭션은 영원히 반영되어야 함
2) 커밋 이후 시스템 오류가 발생하더라도, **커밋된 데이터는 보장**
3) 이러한 기능 제공은 리두로그를 통해 보장함

### 8.2 DML (Transaction) 처리 – insert
![](https://velog.velcdn.com/images/syshin0116/post/75a4abea-984a-43d5-b74e-f374fce8c064/image.png)

### INSERT 구문
#### 단일행 입력(Single Row Insert) 기본 형식
```sql
  INSERT INTO 		table [(column [, column...])]
  VALUES 			(value [, value...]);
```
#### 단일행 입력 예제
```sql
  INSERT INTO 		departments(department_id,
  					department_name, manager_id, location_id)
  VALUES (70, 'Public Relations', 100, 1700);
 ```
 
 [] 각괄호로 되어 있는 부분은 생략 가능하다는 의미
1.테이블 옆에 컬럼을 안 쓰면 모든 컬럼이 입력 값을 받는다.
2.일부 혹은 모든 컬럼을 명시적으로 표시하면 표시한 컬럼만 입력 값을 받는다.
3.테이블 옆에 컬럼을 일부만 쓰면 나머지 컬럼은 자동으로 NULL이 입력됨

### 8.3 Null 값이 포함된 행 입력
#### 묵시적으로 방법 : 컬럼을 생략하면 NULL로 입력됨
```sql
INSERT INTO 		departments (department_id,
					department_name)
VALUES 				(30, 'Purchasing');
```
#### 명시적 방법: VALUES 절에서 NULL 키워드를 지정
> Column 값을 안쓰면 VALUES에 모든 값을 줘야 한다

```sql
INSERT INTO 	departments
VALUES 			(100, 'Finance', NULL, NULL);
```

### 8.4 다른 테이블의 행 복사
#### INSERT 문을 subquery로 작성:
```sql
INSERT INTO sales_reps(id, name, salary, commission_pct)
SELECT employee_id, last_name, salary, commission_pct
FROM employees
WHERE job_id LIKE '%REP%';
```
- VALUES 절을 사용 하지 않음
- INSERT 절의 열 개수를 subquery의 열 개수와 일치
- subquery에서 반환되는 모든 행을 sales_reps 테이블에 삽입

### 8.5 데이터 입력 할 경우 고려사항
#### ▪ 제약조건
	- NOT NULL
	- UNIQUE
	- PRIMARY KEY
	- FOREIGN KEY
	- CHECK

▪ 데이터 타입
▪ 데이터 사이즈
▪ 컬럼 지정할 경우 컬럼 개수와 순서
▪ 디폴트 값

### 8.6 CTAS(Create Table As SELECT)
#### 기존 테이블의 데이터를 복사할 때 사용
#### 기존 테이블을 참조하여 동일한 구조의 테이블 생성할 때 사용
	– 테이블의 컬럼명과 타입만 복사됨, 제약조건은 복사 안됨
```sql
CREATE TABLE <테이블명>
AS
SELECT [(컬럼 [,컬럼…])] FROM <테이블명>
[WHERE 조건];
```
#### 테이블 데이터 복사
```sql
CREATE TABLE EMPLOYEES_COPY
AS
SELECT * FROM EMPLOYEES;
```

#### 테이블 구조만 복사
where 1=0 을 추가하여 False를 만든 뒤 구조만 복사하는 방법
```sql
CREATE TABLE EMPLOYEES_COPY
AS
SELECT * FROM EMPLOYEES
WHERE 1=0;
```

### 8.7 테이블 데이터(행) 변경
![](https://velog.velcdn.com/images/syshin0116/post/ea04f4e7-0a4e-42a1-adfe-3306aa263ef4/image.png)

### 8.8 UPDATE 구문
#### UPDATE 문을 사용하여 테이블의 기존 값을 수정:
```sql
UPDATE 		table
SET 		column = value [, column = value, ...]
[WHERE 		condition];
```
- 필요한 경우 한 번에 두 개 이상의 행을 갱신.
- **WHERE절을 쓰지 않으면 테이블의 모든 행이 변경되니 주의 필요**

### 8.9 테이블 데이터 Update
- WHERE 절을 지정하면 특정 행에서 값이 수정:
```sql
UPDATE 	employees
SET 	department_id = 50
WHERE 	employee_id = 113;
```
- WHERE 절을 생략하면 테이블의 모든 행에서 값이 수정:
```sql
UPDATE 	copy_emp
SET 	department_id = 110;
```
- 열값을 NULL로 갱신하려면 SET column_name **= NULL**을 지정.

### 8.10 Subquery를 이용한 여러 열 변경
#### 사원 113의 직무와 급여를 사원 205와 일치하도록 갱신
![](https://velog.velcdn.com/images/syshin0116/post/5270ef58-6f63-4230-92e8-8e54b3b6ad77/image.png)

### 8.11 테이블 데이터 삭제
#### Departments
![](https://velog.velcdn.com/images/syshin0116/post/218d2079-0415-435a-a0c7-83c0b6cafe68/image.png)

#### Delete a row from the DEPARTMENTS table:
![](https://velog.velcdn.com/images/syshin0116/post/479d9dbc-1309-4e1d-8e26-2e25475f0e9f/image.png)

### 8.12 DELETE 구문
#### DELETE 문을 사용하여 테이블에서 기존 행을 제거할 수 있다.
```sql
DELETE 	[FROM] 	table
[WHERE 			condition];
```

```sql
DELETE 	FROM 	departments
WHERE 	department_name = 'Finance';
```

```sql
DELETE FROM hr.copy_employees;
```
### 8.13 다른 테이블 기반의 데이터 삭제
- DELETE 문에서 subquery를 사용하여 다른 테이블의 값을 기반으로 테이블에서 행을 제거

```sql
DELETE FROM 	employees
WHERE 			department_id =
						(SELECT 	department_id
						FROM 		departments
						WHERE 		department_name
						LIKE '		%Public%');
```

### 8.14 데이터베이스 트랜잭션의 시작과 종료
#### 데이터베이스 트랜잭션은 다음 중 하나로 구성:
- 데이터를 일관되게 변경하는 여러 DML 문
- 하나의 DDL 문 (데이터 정의 언어 : 테이블 생성/변경/제거)
- 하나의 DCL 문 (데이터 제어 언어 : 권한 부여/회수)
#### **첫 번째 DML SQL 문이 실행될 때 시작**
#### 다음 상황 중 하나가 발생하면 종료:
- COMMIT 또는 ROLLBACK 실행
- **DDL 또는 DCL 문 실행(자동 커밋이 동반되는 명령어)**
- **SQL*Plus(클라이언트 프로그램) 종료**
	**정상종료 : 자동 커밋 / 비정상종료: 자동 롤백**
- 시스템 failure(자동 롤백)

### 8.15 세션, 트랜잭션, DML, 언두의 관계
- 오라클에 사용자가 접속을 하면 하나의 세션이 생성됨
- 세션이 유지되는 동안 여러 개의 트랜잭션 발생 가능
- 트랜잭션은 여러 개의 DML 과 DDL, DCL문으로 구성됨
- 하나의 트랜잭션은 하나의 언두 세그먼트를 할당 받음
- 하나의 세션은 한번에 하나의 트랜잭션만 수행 가능
- **사용자는 세션이 유지되는 동안 다수의 DML로 이루어진 트랜잭션을 일으켜서 업무를 수행**
  - **단, DDL, DCL은 자동 커밋이 동반되는 명령어**
  - **DML문장 사이에 DDL, DCL이 수행되면 자동 커밋 됨**
  
### 8.16 COMMIT과 ROLLBACK 구문
#### COMMIT and ROLLBACK 구문의 특징:
- 논리적으로 관련된 작업 그룹화
- 데이터 일관성 보장
- **변경사항을 영구 적용하기 전에 데이터를 검토 할 수 있는 기회 제공**
실무적으로 
### 8.17 명시적 트랜잭션 제어  (SQLD 단골문제)
![](https://velog.velcdn.com/images/syshin0116/post/9e19792e-2b28-4733-a0bf-90ddd1798584/image.png)

### 8.18 Savepoint를 이용한 rollback (SQLD 단골문제)
- SAVEPOINT 문을 사용하여 현재 트랜잭션에 마커 생성
- ROLLBACK TO SAVEPOINT 문을 사용하여 해당 마커로 롤백 수행

```sql
UPDATE...
SAVEPOINT update_done;
INSERT...
ROLLBACK TO update_done;
```

### 8.19 자동 커밋과 자동 롤백
#### 자동 커밋은 다음 상황에서 발생:
- DDL 구문 사용 시
- DCL 구문 사용 시
- Exit 명령 사용 시 자동 커밋
#### SQL Developer 또는 SQL*Plus가 비정상적으로 종료되거나 시스템 failure가 발생된 경우 자동 롤백 발생.

> * DML : INSERT, UPDATE, **DELETE**
* DDL : CREATE, ALTER, DROP, RENAME, **TRUNCATE**
* DCL : GRANT, REVOKE

#### Delete와 Truncate의 차이점
>### TRUNCATE:
TRUNCATE TABLE 명령어는 개별적으로 행을 삭제할 수 없으며, 테이블 내부의 모든 행을 삭제
#### TRUNCATE 특장:
- TRUNCATE는 DDL(데이터 정의 언어) 명령입니다.
- TRUNCATE는 테이블 잠금을 사용하여 실행되지만, 각 행은 잠기지 않습니다.
- TRUNCATE와 WHERE 절을 함께 사용할 수 없습니다.(개별적으로 행 삭제 불가능)
- TRUNCATE는 테이블에서 모든 행을 제거합니다.
- 트랜잭션 로그에 한 번만 기록되므로 DELETE보다 성능 면에서 더 빠릅니다.
- 인덱싱 된 VIEW(뷰)와 함께 사용할 수 없습니다.
- 테이블에서 TRUNCATE TABLE 명령어를 사용하려면 테이블에 대한 ALTER 권한이 필요합니다.
- ROLLBACK(실행 취소) 불가능합니다.
- 테이블의 용량이 초기화됩니다.
※ 잠금(Lock) : 삽입, 삭제, 갱신 등의 트랜잭션이 수행되는 동안 특정 테이블 또는 행에 대해 CRUD 작업을 할 수 없음을 의미합니다. 즉, TRUNCATE 명령어가 수행되는 동안 해당 테이블에 다른 트랜잭션 작업을 할 수 없습니다.

>### DELETE:
DELETE 명령어는 테이블의 내부의 행을 모두 삭제하며, WHERE 절을 사용하여 개별적으로 행을 삭제할 수 있습니다.
#### DELETE 특징:
- DELETE는 DML(데이터 조작 언어) 명령입니다.
- DELETE는 행 잠금을 사용하여 실행됩니다.
- DELETE는 WHERE 절과 함께 사용하여 특정 행을 삭제할 수 있습니다.
- DELETE는 삭제된 각 행에 대해 트랜잭션 로그를 기록합니다. 따라서 TRUNCATE보다 느립니다.
- DELETE 명령어를 사용하려면 테이블에 대한 DELETE 권한이 필요합니다.
- 인덱싱 된 VIEW(뷰)와 함께 사용할 수 있습니다.
- TRUNCATE보다 더 많은 트랜잭션 공간을 사용합니다.
- ROLLBACK(실행 취소)을 할 수 있습니다.
- 테이블의 용량은 감소하지 않습니다.

>### DROP
DROP TABLE 명령어는 데이터베이스에서 테이블 정의 및 해당 테이블에 대한 모든 데이터, 인덱스, 트리거, 제약 조건 및 권한을 제거합니다.
#### DROP 특징:
- DROP은 DDL(데이터 정의 언어) 명령입니다.
- DROP 명령은 데이터베이스에서 테이블을 제거합니다.
- 테이블의 행, 인덱스 및 권한도 제거됩니다.
- 테이블의 행이 제거될때, DML(데이터 조작 명령어) 트리거가 실행되지 않습니다.
- ROLLBACK(실행 취소) 불가능합니다.

### 8.20 COMMIT or ROLLBACK 전 데이터 상태
- 언두 데이터를 통해 이전의 데이터 상태를 복구할 수 있다.**(원자성)**
- 현재 유저는 SELECT 문을 사용하여 DML 작업의 결과를 확인할 수 있다.
- **다른 유저는 현재 유저가 실행한 DML 문의 결과를 볼 수 없다.(일관성)**
- 영향을 받는 행이 잠기므로 **다른 유저가 영향을 받는 행의 데이터를 변경
할 수 없다.(LOCK, 고립성)**

### 8.21 COMMIT 후 데이터 상태
- 데이터 변경 사항이 데이터베이스에 저장**(지속성)**
- 모든 유저가 변경 완료된 데이터를 조회할 수 있다
- Lock 걸린 행이 해제되어 해제된 행을 다른 유저가 조작가능
- 트랜잭션 내의 모든 SAVEPOINT는 삭제됨

### 8.22 데이터 커밋
```sql
DELETE 	FROM 	employees
WHERE 	employee_id = 99999;
INSERT 	INTO departments
VALUES 	(290, 'Corporate Tax', NULL, 1700);

COMMIT;
```

### 8.23 ROLLBACK 후 데이터 상태
#### ROLLBACK 문을 사용하여 보류 중인 모든 변경 사항을 폐기:
- 데이터 변경 완료
- 이전 데이터 상태로 되돌림
- 보유한 Lock 및 자원은 해제됨

```sql
DELETE FROM copy_emp;
ROLLBACK ;
```
## 8장 DML과 트랜잭션 실습
[08_01_INSERT 및 제약조건 확인.pdf](https://github.com/syshin0116/Study/files/11470892/08_01_INSERT.pdf)

## 8.1 INSERT 및 제약조건 확인
실습 : 다양한 INSERT 구문 실행 및 제약조건 확인
### 1. SCOTT 계정) 실습에 사용할 테이블을 생성 및 테이블 구조 확인
```sql
drop table tbl_insert_test;

CREATE TABLE tbl_insert_test (
 NUM NUMBER(3) NOT NULL,
 VAR VARCHAR2(10),
 DT DATE default sysdate,
 CONSTRAINT pk_tbl_insert_test PRIMARY KEY(NUM),
 CONSTRAINT ck_tbl_insert_test_var CHECK (VAR IN ('ORACLE','oracle','OCP', 'ocp'))
);

drop tbl_insert_test_02;
CREATE TABLE tbl_insert_test_02 (
 NUM NUMBER(3) NOT NULL,
 VAR VARCHAR2(10),
 DT DATE default sysdate,
 CONSTRAINT pk_tbl_insert_test_02 PRIMARY KEY(NUM),
 CONSTRAINT ck_tbl_insert_test_02_var CHECK (VAR IN ('ORACLE','oracle','OCP', 'ocp'))
);
DESC tbl_insert_test;
DESC tbl_insert_test_02;
);
```
### 2. 데이터 입력할 때 고려사항
1. 제약조건
2. 데이터 타입
3. 데이터 사이즈
4. 컬럼 지정할 경우 컬럼 개수와 순서
5. 디폴트 값

### 3. 날짜 형식 지정

```sql
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';
SELECT * FROM NLS_SESSION_PARAMETERS
WHERE PARAMETER = 'NLS_DATE_FORMAT'
```

### 4. 단일행 입력(Single Row Insert)
#### 4.1 컬럼명을 생략하고 테이블에 기술된 컬럼의 순서로 값을 기술
```
INSERT INTO tbl_insert_test VALUES (1, 'ORACLE', SYSDATE);

```
#### 4.2. 컬럼명을 모두 표기하고 값을 기술
```sql
INSERT INTO tbl_insert_test (NUM, var, dt) VALUES (2, 'OCP', SYSDATE);
```
#### 4.3. 테이블 구조와 다르게 컬럼명 순서를 바꿔서 표기하고 값을 기술
```sql
INSERT INTO tbl_insert_test (var, NUM, dt) VALUES ('ORACLE', 3, SYSDATE);
```
#### 4.4. var 컬럼에 묵시적으로 NULL을 입력하도록 함
```sql
INSERT INTO tbl_insert_test (NUM, dt) VALUES (4, SYSDATE);
```
#### 4.5. var 컬럼에 명시적 NULL을 입력하도록 함
```sql
INSERT INTO tbl_insert_test (NUM, var, dt) VALUES (5, NULL, SYSDATE);
```
#### 4.6. commit 하여 영구적으로 반영
```sql
commit;
select * from tbl_insert_test;
```
### 5. 복수행 입력(Multi Row Insert)
#### 5.1 서브쿼리를 이용한 INSERT
```sql
insert into tbl_insert_test_02
select * from tbl_insert_test;
```
#### 5.2 commit 하여 영구적으로 반영
```sql
commit;
select * from tbl_insert_test_02;
```
### 6. CTAS (CREATE TABLE AS SELECT)를 이용한 테이블 생성 및 입력
```sql
CREATE TABLE tbl_insert_test_03
AS
SELECT * from tbl_insert_test;
```
#### 6.1 CTAS로 만들어진 테이블은 구조만 만들어지고 제약조건은 생략된다. (PK 없음)
```sql
insert into tbl_insert_test_03
select * from tbl_insert_test;
commit;
insert into tbl_insert_test_03
select * from tbl_insert_test_02;
```
#### 6.2 commit 하여 영구적으로 반영
```sql
commit;
select * from tbl_insert_test_03;
```
### 7. 제약조건, Data Type, Size등을 고려하여 데이터 입력

#### 7.1 PK 중복으로 인한 입력 오류
```sql
INSERT INTO tbl_insert_test VALUES (1, 'ORACLE', SYSDATE);
```
오류 보고 -
ORA-00001: 무결성 제약 조건(SCOTT.PK_TBL_INSERT_TEST)에 위배됩니다
참고 : 오류번호가 낮을수록 전통적으로 오래된 오류이다.
#### 7.2 PK는 NULL 입력 불가로 오류
```sql
INSERT INTO tbl_insert_test VALUES (NULL, 'ORACLE', SYSDATE);
```
오류 보고 -
ORA-00001: 무결성 제약 조건(SCOTT.PK_TBL_INSERT_TEST)에 위배됩니다
#### 7.3 데이터 타입이 불일치하여 오류(VAR VARCHAR2(10 BYTE)에 숫자형 입력하여 오류 발생)
```sql
INSERT INTO tbl_insert_test VALUES (100, 123, SYSDATE);
```
오류 보고 -
ORA-02290: 체크 제약조건(SCOTT.CK_TBL_INSERT_TEST_VAR)이 위배되었습니다
#### 7.4 데이터 타입이 불일치하여 오류(DT DATE에 날짜가 아닌 문자열 입력하여 오류 발생)
```sql
INSERT INTO tbl_insert_test VALUES (100, 'ORACLE', 'STRING');
```
오류 보고 -
ORA-01841: 년은 영이 아닌 -4713 과 +4713 사이의 값으로 지정해야 합니다.

#### 7.5 num NUMBER(3) 보다 큰 사이즈의 숫자를 입력하여 오류
```sql
INSERT INTO tbl_insert_test VALUES (12345, 'ORACLE', SYSDATE);
```
오류 보고 -
ORA-01438: 이 열에 대해 지정된 전체 자릿수보다 큰 값이 허용됩니다.
#### 7.6 var VARCHAR2(10) 보다 큰 사이즈의 문자열을 입력하여 오류 (실무때 많이 보는 오류 중 하나)
```sql
INSERT INTO tbl_insert_test VALUES (100, 'ORACLE_SIZE_14', SYSDATE);
```
오류 보고 -
ORA-12899: "SCOTT"."TBL_INSERT_TEST"."VAR" 열에 대한 값이 너무 큼(실제: 14, 최대값: 10)
#### 7.7 체크제약 조건 위반으로 인한 오류('ORACLE', 'oracle', 'OCP', 'ocp' 값들만 유효하다)
```sql
INSERT INTO tbl_insert_test VALUES (100, 'AAA', SYSDATE);
```
오류 보고 -
ORA-02290: 체크 제약조건(SCOTT.CK_TBL_INSERT_TEST_VAR)이 위배되었습니다
#### 7.8 표기한 컬럼은 4개 값은 3개로 오류
```sql
INSERT INTO tbl_insert_test (NUM, VAR, DT, 'AAA') VALUES (100, 'OCP', SYSDATE);
```
SQL 오류: ORA-01747: 열명을 올바르게 지정해 주십시오

01747. 00000 - "invalid user.table.column, table.column, or column specification"
#### 7.9 컬럼은 2개 값은 3개로 오류(실무때 많이 보는 오류 중 하나)
```sql
INSERT INTO tbl_insert_test (NUM, VAR) VALUES (100, 'OCP', SYSDATE);
```
SQL 오류: ORA-00913: 값의 수가 너무 많습니다
00913. 00000 - "too many values"
#### 7.10 데이터 입력할 경우 값을 지정하지 않으면 저장되는 디폴트 값을 언제나 확인한다.
```sql
DT DATE default sysdate
INSERT INTO tbl_insert_test (NUM, VAR) VALUES (100, 'OCP');
SELECT * FROM tbl_insert_test WHERE num = 100;
```
## 8.2 세션, 트랜잭션, 언두 세그먼트 모니터링
[08_02_세션, 트랜잭션, 언두 세그먼트 모니터링.pdf](https://github.com/syshin0116/Study/files/11470989/08_02_.pdf)

### 0. 준비사항
SYS (관리자) 세션1
HR 세션2
HR 세션3

### 1. 사용하는 동적성능 뷰 SQL
```sql
-- 현재 접속되어 있는 세션 정보를 확인
SELECT username, sid, serial#, program
FROM v$session
WHERE type = 'USER';
-- 현재 진행중인 트랜잭션 확인
SELECT * FROM v$transaction;
-- 언두 세그먼트 상태를 확인
-- 기본적으로 10개의 언두 세그먼트가 준비 되어있다.
-- 하나의 트랜잭션에 랜덤하게 1개의 세그먼트가 부여된다.
SELECT * FROM v$rollstat
WHERE xacts <> 0;
-- lock의 종류(TM:테이블레벨, TX:로우레벨)
SELECT * FROM v$lock
WHERE type in ('TM', 'TX');
```
### 2. HR 세션2
HR 계정에 실습에 사용할 테이블을 생성 및 입력, 테이블 구조 확인
```sql
DROP TABLE HR.EMP_COPY;
CREATE TABLE HR.EMP_COPY
AS
SELECT EMPLOYEE_ID, LAST_NAME, SALARY FROM HR.EMPLOYEES
WHERE EMPLOYEE_ID IN (100, 200, 202);
DESC HR.EMP_COPY;
```
### 3. SYS (관리자) 세션1
#### 3.1 현재 오라클에 접속되어 있는 세션을 볼 수 있습니다.
```sql
select username, sid, serial# from v$session
where type = 'USER';
```
#### 3.2 현재 오라클에서 진행중인 트랜잭션을 보여줍니다.
조회되는것이 없으면 현재 진행중인 트랜잭션이 없는것입니다.
```sql
select * from v$transaction;
```
### 4. HR 세션2
100번 사원의 성을 변경한다.
```sql
SELECT last_name
FROM emp_copy
WHERE employee_id = '100';
UPDATE emp_copy SET last_name = 'UpdateTest'
WHERE employee_id = 100;
-- last_name이 변경된것을 확인 할 수 있다.
SELECT last_name FROM emp_copy
WHERE employee_id = '100';
```
### 5. SYS (관리자) 세션1
#### 5.1 HR 세션2가 update를 실행해서 트랜잭션이 시작된 것을 확인
```sql
select * from v$transaction;
```
#### 5.2 update를 하면 롤백시 복구를 위해 언두 데이터를 생성함
미리 준비된 언두 세그먼트 10개중 랜덤으로 하나를 할당 받아 변경전의 전값을 저장하고 있다.
```sql
select * from v$rollstat;
```
#### 5.3 해당 세션이 테이블에 TM/TX 락이 설정되는 것을 확인
-- lock의 종류(TM:테이블레벨, TX:로우레벨)
```sql
select * from v$lock
where type in ('TM', 'TX')
```
### 6. HR 세션3
아직 커밋되지 않은 데이터이기 때문에 HR 세션2가 변경한 값이 아닌 본래 값을 보여준다.

오라클이 지원하는 읽기 일관성(Consistency), 언두 데이터를 통해서 데이터를 보여주기 때문에 가능
```sql
select last_name
from emp_copy
where employee_id = '100';
```
### 7. HR 세션2
#### 7.1 업데이트한 내용을 롤백한다.
```sql
rollback;
```
#### 7.2 언두 데이터를 통해 이전값으로 되돌아가서 이전값으로 조회된다.
트랜잭션은 종료된다.
```sql
select last_name
from emp_copy
where employee_id = '100';
```
### 8. 관리자 세션1
#### 8.1 롤백을 하면 트랜잭션이 종료되어 해당 트랜잭션 정보가 조회되지 않는다.
```sql
select * from v$transaction;
```
#### 8.2 트랜잭션이 종료면 트랜잭션에서 사용하는 모든 자원은 해제된다.
```sql
select * from v$rollstat;
select * from v$lock
where type in ('TM', 'TX');
```
### 9. HR 세션2
해당 세션을 종료한다.
sqlplus로 접속했으면 exit로 종료를 하고 SQL Developer로 접속했으면 접속해제를 해주어야한다.
### 10. SYS (관리자) 세션1
HR 세션2는 종료되어 조회 되지 않는다.
```sql
select username, sid, serial#, program
from v$session
where type = 'USER';
```

## 8.3 ROLLBACK 및 SAVEPOINT
[08_03_ROLLBACK 및 SAVEPOINT.pdf](https://github.com/syshin0116/Study/files/11470986/08_03_ROLLBACK.SAVEPOINT.pdf)
### 명령어
- DML을 적용하기 전의 값으로 되돌린다.
```ROLLBACK;```
- 세이브포인트 지정
```SAVEPOINT <세이브포인트명>;```
- 세이브포인트로 롤백
```ROLLBACK TO <세이브포인트명>;```

### 1. HR 계정에서 실습에 사용할 테이블을 생성 및 입력, 테이블 구조 확인
```sql
DROP TABLE HR.EMP_COPY;
CREATE TABLE HR.EMP_COPY
AS
SELECT EMPLOYEE_ID, LAST_NAME, SALARY FROM EMPLOYEES
WHERE EMPLOYEE_ID IN (100, 200, 202);
DESC EMP_COPY;
```

### 2. 세이브포인트
#### 2.1 현재 데이터 확인
```sql
SELECT employee_id, last_name, salary
FROM emp_copy;
```
#### 2.2. 100번 사원 삭제 및 A 세이브 포인트 지정
```sql
DELETE FROM emp_copy
WHERE employee_id = 100;

SAVEPOINT A;

SELECT employee_id, last_name, salary
FROM emp_copy;
```

#### 2.3. 200번 사원 삭제 및 B 세이브 포인트 지정
```sql
DELETE FROM emp_copy
WHERE employee_id = 200;
SAVEPOINT B;
SELECT employee_id, last_name, salary
FROM emp_copy;
```
#### 2.4 202번 사원 삭제
```sql
DELETE FROM emp_copy
WHERE employee_id = 202;

SELECT employee_id, last_name, salary
FROM emp_copy;
```
#### 2.5. B 세이브포인트로 롤백
```sql
-- 세이브포인트 B 이후의 문장은 모두 ROLLBACK 된다.
ROLLBACK TO SAVEPOINT B;

SELECT * FROM emp_copy;
```
#### 2.6. A 세이브포인트로 롤백
```sql
-- 세이브포인트 A 이후의 문장은 모두 ROLLBACK 된다.
ROLLBACK TO SAVEPOINT A;

SELECT * FROM emp_copy;
```
#### 2.7 전체 롤백 및 데이터 확인
```sql
ROLLBACK;

SELECT * FROM emp_copy;
```

## 8.4 자동커밋, 자동롤백
[08_04_자동커밋, 자동롤백.pdf](https://github.com/syshin0116/Study/files/11470984/08_04_.pdf)

### 실습 목록
1. DDL 수행으로 인한 자동커밋
2. DCL 수행으로 인한 자동커밋
3. sqlplus 정상종료로 인한 자동커밋
4. sqlplus 비정상종료로 인한 자동롤백
5. 오라클 비정상 종료로 인한 자동롤백

### 준비사항
- SYS 세션1 (Oracle SQL Developer)
- HR 세션2 (Oracle SQL Developer)
- HR 세션3 (SQLPLUS)
- SYS 세션4 (SQLPLUS)

### 명시적이지 않은 트랜잭션 종료
- 자동커밋이 동반되는 명령어
- DDL : CREATE, ALTER, DROP, RENAME, TRUNCATE
- DCL : GRANT, REVOKE

자동커밋
sqlplus 정상종료(exit, quit)

자동롤백
sqlplus 비정상 종료, 오라클 비정상 종료

* 클라이언트 프로그램중에는 명시적으로 트랜잭션을 종료하지 않은 경우
자동커밋, 자동롤백을 선택 혹은 설정 할 수도 있다. ex) Oracle SQL Developer

### 0. HR 계정에서 실습에 사용할 테이블을 생성 및 입력, 테이블 구조 확인
```sql
DROP TABLE HR.EMP_COPY;
CREATE TABLE HR.EMP_COPY
AS 
SELECT EMPLOYEE_ID, LAST_NAME, SALARY FROM HR.EMPLOYEES
WHERE EMPLOYEE_ID IN (100, 200, 202);
DESC HR.EMP_COPY;
```

### 1. DDL 수행으로 인한 자동커밋
#### 1.1 SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
select * from v$transaction;
```

#### 1.2. HR 세션2 (Oracle SQL Developer)
100번 사원의 성을 조회하고 업데이트 한다.
```sql
SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
UPDATE emp_copy SET last_name = 'AutoCommitDDL'
WHERE employee_id = 100;
```

#### 1.3. SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
SELECT * FROM v$transaction;
```

#### 1.4. HR 세션2 (Oracle SQL Developer)
DDL 을 실행하여 자동커밋 한다.
```sql
CREATE TABLE tbl_auto_commit (id NUMBER);
```

#### 1.5. SYS 세션1 (Oracle SQL Developer)
HR 세션2의 트랜잭션이 자동커밋되어서 종료 되었는지 확인한다.
```sql
SELECT * FROM v$transaction;
```
#### 1.6. HR 세션2 (Oracle SQL Developer)
DDL 수행으로 자동커밋 되었는지 롤백후 조회한다.
```sql
ROLLBACK;
SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
```


### 2. DCL 수행으로 인한 자동커밋
#### 2.1 SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
SELECT * FROM v$transaction;
```

#### 2.2. HR 세션2 (Oracle SQL Developer)
100번 사원의 성을 조회하고 업데이트 한다.
```sql
SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
UPDATE emp_copy SET last_name = 'AutoCommitDCL'
WHERE employee_id = 100;
```
#### 2.3. SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
SELECT * FROM v$transaction;
```
#### 2.4. HR 세션2 (Oracle SQL Developer)
DCL 을 실행하여 자동커밋 한다.
```sql
GRANT SELECT ON emp_copy TO scott;
```
#### 2.5. SYS 세션1 (Oracle SQL Developer)
HR 세션2의 트랜잭션이 자동커밋되어서 종료 되었는지 확인한다.
```sql
SELECT * FROM v$transaction;
```
#### 2.6. HR 세션2 (Oracle SQL Developer)
DCL 수행으로 자동커밋 되었는지 롤백후 조회한다.
```sql
ROLLBACK;
SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
```

### 3. sqlplus 정상종료로 인한 자동커밋
#### 3.1 SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
SELECT * FROM v$transaction;
```
#### 3.2. HR 세션3 (SQLPLUS)
리눅스에서 sqlplus 로 hr 계정에 접속한다.
100번 사원의 성을 조회하고 업데이트 한다.
```sh
[/home/oracle]$ sqlplus hr/hr

SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
SQL> UPDATE emp_copy SET last_name = 'AutoCommitSqlplus'
WHERE employee_id = 100;
```
#### 3.3. SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
select * from v$transaction;
```
#### 3.4. HR 세션3 (SQLPLUS)
exit 명령어로 정상종료 한다.
```sql
SQL> exit;
```
#### 3.5. SYS 세션1 (Oracle SQL Developer)
HR 세션3의 트랜잭션이 자동커밋되어서 종료 되었는지 확인한다.
```sql
SELECT * FROM v$transaction;
```
#### 3.6. HR 세션3 (SQLPLUS)
리눅스에서 sqlplus 로 hr 계정으로
다시 로그인하여 sqlplus 정상종료로 자동커밋 되었는지 조회한다.
```shell
[/home/oracle]$ sqlplus hr/hr
```
```sql
SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
```
### 4. sqlplus 비정상종료로 인한 자동롤백
#### 4.1. SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
```sql
SELECT * FROM v$transaction;
```
#### 4.2. HR 세션3 (SQLPLUS)
100번 사원의 성을 조회 하고 업데이트한다.
```sql
SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';

SQL> UPDATE emp_copy SET last_name = 'AutoRollbackSqlplus'
WHERE employee_id = 100;
```
#### 4.3. SYS 세션1 (Oracle SQL Developer)
현재 진행되고 있는 트랜잭션을 확인한다.
SELECT * FROM v$transaction;
#### 4.4. HR 세션3 (SQLPLUS)
exit 명령어로 윈도우창의 우측 닫기 버튼을 클릭해 비정상종료 한다.
#### 4.5. SYS 세션1 (Oracle SQL Developer)
HR 세션3의 트랜잭션이 자동커밋되어서 종료 되었는지 확인한다.
```sql
select * from v$transaction;
```
#### 4.6. HR 세션3 (SQLPLUS)
다시 접속하여 **sqlplus 비정상종료로 자동롤백** 되었는지 조회한다.
```sh
[/home/oracle]$ sqlplus hr/hr
```
```sql
SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
```

### 5. 오라클 비정상 종료로인한 자동롤백
#### 5.1. HR 세션3 (SQLPLUS)
sqplus로 hr 계정에 접속후 100번 사원의 성을 조회 하고 업데이트한다.
```sql
SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';

SQL> UPDATE emp_copy SET last_name = 'OracleFailure'
WHERE employee_id = 100;

-- 업데이트가 반영되었는지 확인한다.
SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
```
#### 5.2. SYS 세션4 (SQLPLUS) (putty에서 새로운 창으로 접속)
리눅스에서 sqlplus sys/oracle as sysdba 로 접속한다.

오라클을 비정상 종료 및 재시작한다.

*** shutdown abort; 는 전원을 꺼서 비정상 종료하는것과 같다.**
```shell
[/home/oracle]$ sqlplus sys/oracle as sysdba
```
```sql
SQL> shutdown abort;
ORACLE instance shut down.
SQL> startup
ORACLE instance started.
```
#### 5.3. HR 세션3 (SQLPLUS)
오라클이 비정상 종료 되었기 때문에 기존 세션은 종료되었다.

**sqlplus hr/hr 로 다시 접속후** 오라클 비정상종료로 인해 자동롤백 된 것을 확인한다.
```shell
[/home/oracle]$ sqlplus hr/hr
```
```sql
SQL> SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = '100';
```

## 8.5 트랜잭션 ACID
[08_05_트랜잭션 ACID 실습.pdf](https://github.com/syshin0116/Study/files/11471007/08_05_.ACID.pdf)

### 준비사항
- SYS 세션1
- HR 세션2
- HR 세션3
- * SQL Developer 인경우 2개의 프로그램을 실행해서 각각 HR 세션1, HR 세션2를 구성 할 수 있다.

### 실습에서 사용하는 동적성능 뷰
```sql
-- 현재 접속되어 있는 세션 정보를 확인
SELECT username, sid, serial#, program
FROM v$session
WHERE type = 'USER';

-- 현재 진행중인 트랜잭션 확인
SELECT * FROM v$transaction;

-- 언두 세그먼트 상태를 확인
-- 기본적으로 10개의 언두 세그먼트가 준비 되어있다.
-- 하나의 트랜잭션에 랜덤하게 1개의 세그먼트가 부여된다.
SELECT * FROM v$rollstat
WHERE xacts <> 0;

-- lock의 종류(TM:테이블레벨, TX:로우레벨)
SELECT * FROM v$lock
WHERE type in ('TM', 'TX');
```
### 1. HR 계정에 실습에 사용할 테이블을 생성 및 입력, 테이블 구조 확인
```sql
DROP TABLE HR.EMP_COPY;

CREATE TABLE HR.EMP_COPY
AS 
SELECT EMPLOYEE_ID, LAST_NAME, SALARY FROM HR.EMPLOYEES
WHERE EMPLOYEE_ID IN (100, 200, 202);

DESC EMP_COPY
```
### 2. SYS 세션1
세션, 트랜잭션, 언두 세그먼트, 락 상태 확인하기
```sql
-- 현재 접속되어 있는 세션 정보를 확인
SELECT username, sid, serial#, program
FROM v$session
WHERE type = 'USER';

-- 현재 진행중인 트랜잭션 확인
SELECT * FROM v$transaction;

-- 언두 세그먼트 상태를 확인
SELECT * FROM v$rollstat
WHERE xacts <> 0;

-- lock의 종류(TM:테이블레벨, TX:로우레벨)
SELECT * FROM v$lock
WHERE type in ('TM', 'TX');
```
### 3. HR 세션2
100번 사원의 급여를 업데이트함,

HR 세션2 내에서는 업데이트 한 값이 조회됨

HR 세션2 이외에서는 업데이트 이전의 본래값이 조회됨

```sql
SELECT 	employee_id, last_name, salary 
FROM 	emp_copy
WHERE 	employee_id = 100;

UPDATE 	emp_copy
SET 	salary = 50000
WHERE 	employee_id = 100;

SELECT 	employee_id, last_name, salary 
FROM 	emp_copy
WHERE 	employee_id = 100
```

### 4. SYS 세션1
#### 4.1 트랜잭션 생성된 것 확인
```sql
SELECT * FROM v$transaction;
```
#### 4.2 HR세션2에서 생성한 트랜잭션에 언두 세그먼트를 할당 받은 것 확인
```sql
SELECT * FROM v$rollstat
WHERE xacts <> 0;
```
HR 세션2가 LOCK으로 테이블과 테이블의 행을 선점
HR 새션2 이외에는 데이터를 변경하지 못하도록 LOCK을 설정함
```sql
SELECT s.username, l.* 
FROM v$lock l
JOIN v$session s
ON l.sid = s.sid
WHERE l.type in ('TM', 'TX');
```
### 5. HR 세션3
HR 세션2에서 급여를 변경했지만 HR 세션3에서는 본래 급여가 조회되는 것 확인
**오라클이 지원하는 읽기 일관성(Consistency)**, 언두 데이터를 통해서 이전의값을 보여준다.
```sql
SELECT employee_id, last_name, salary 
FROM emp_copy
WHERE employee_id = 100;
```
#### 5.1 HR 세션2에서 테이블과 행에 TM/TX 락을 건 테이블의 행에 업데이트 시도
**업데이트가 완료 되지않고 행이 걸린다.**

HR 세션2에서 TM,TX 락으로 자원을 선점 했기 때문에 HR 세션2가 COMMIT 혹은 ROLLBACK 하여 LOCK을 해제 할때까지 대기한다.


HR 세션2의 트랜잭션은 다른 트랜잭션의 간섭을 받지 않고 독립적으로 수행중이다.
LOCK 매커니즘을 통해서 지원된다.
트랜잭션의 고립성, 격리성(Isolation)을 보여준다.
```sql
UPDATE emp_copy
SET salary = 70000
WHERE employee_id = 100
```
### 6. SYS 세션1
#### 6.1 HR 세션3의 트랙잭션은 아직 시작되지도 않은 것을 확인
```sql
select * from v$transaction;
```
### 7. HR 세션2
```sql
rollback;
```
### 8. SYS 세션1
1. HR 세션2 트랜잭션은 종료 되었고 HR 세션3의 트랜잭션은 진행중인 것을 확인
2. HR 세션3도 DML이 시직되어서 언두 세그먼트를 할당 받은 것 확인
3. HR 세션2에서 rollback을 해서 TM/TX 락을 해제하면 곧 바로 HR 세션3이 LOCK을 설정한다.
```sql
-- 현재 진행중인 트랜잭션 확인
SELECT * FROM v$transaction;

-- 언두 세그먼트 상태를 확인
-- 기본적으로 10개의 언두 세그먼트가 준비 되어있다.
-- 하나의 트랜잭션에 랜덤하게 1개의 세그먼트가 부여된다.
SELECT * FROM v$rollstat
WHERE xacts <> 0;

-- lock의 종류(TM:테이블레벨, TX:로우레벨)
SELECT * FROM v$lock
WHERE type in ('TM', 'TX');
```
### 9. HR 세션3
1. 100번 사원의 성을 업데이트하고 COMMIT한다.
2. 100번 사원의 레코드를 조회하면 급여와 성이 모두 반영 되었다.
3. 모두 반영되거나 모두 반영되지 않아야 원자성을 유지 하는것이다.
4. **트랜잭션의 원자성(Atomicity)을 보여준다.**


1. COMMIT하면 오라클은 COMMIT된 데이터를 보장한다.
2. COMMIT한 바로 직후 업데이트한 정보를 데이터 파일에 쓰지 못한 상태에서 비정상 종료되더라도 재구동하면 COMMIT한 데이터가 보장되어 조회된다.
3. 이것은 오라클의 리두로그 파일을 통해서 지원된다.
4. **트랜잭션의 지속성(Durability)보여준다.**

```sql
update emp_copy
set last_name = 'KingKing'
where employee_id = 100;
commit;
select employee_id, last_name, salary 
from emp_copy
where employee_id = 100
```











## 9. 테이블 생성 관리
### 9.1 목표
- DATABASE OBJECT
- TABLE 생성
- DATA TYPE 활용
- TABLE 변경과 삭제
- 제약조건

### 9.2 데이터베이스 오브젝트
![](https://velog.velcdn.com/images/syshin0116/post/2ff65058-cdf7-4719-a79f-5eb2a9326a7b/image.png)

### 9.3 객체 및 열 이름 규칙

#### 테이블 및 열은 다음의 규칙을 준수해야 한다.
- 문자로 시작해야 한다.
- 길이는 1–30자 사이여야 한다.
- A–Z, a–z, 0–9, _, $, #만 포함할 수 있다.
- 동일한 유저가 소유한 다른 객체의 이름과 중복되지 않아야 한다.
- Oracle 서버 예약어는 사용할 수 없다.

### 9.4 CREATE TABLE 구문
#### 사용자는 다음 권한이 필요:
– CREATE TABLE 권한
– 저장소 사용 권한
```sql
CREATE 	TABLE [schema.]table
			(column datatype [DEFAULT expr][, ...]);
```

#### 구문 필수 요소:
- 테이블 명
- 컬럼 명
- 컬럼 데이터 타입
- 컬럼 크기

### 9.5 다른 사용자의 테이블 참조 방법
- 다른 유저가 소유한 테이블은 유저의 스키마에 없다.
- 이러한 테이블에는 소유자의 이름을 접두어로 사용해야 한다

![](https://velog.velcdn.com/images/syshin0116/post/3f1ac65c-9e3f-41b5-83e6-2e499e49b8e1/image.png)

### 9.6 DEFAULT 옵션
- 삽입 시 열의 기본값을 지정
```sql
...hire_date DATE DEFAULT SYSDATE, ...
```
- 리터럴 값, 표현식 또는 SQL 함수 등을 사용할 수 있다.
- 다른 열의 이름이나 의사 열은 사용 불가
- 기본 데이터 유형은 열 데이터 유형과 일치해야 한다.
```sql
CREATE TABLE hire_dates
				(id NUMBER(8),
				hire_date DATE DEFAULT SYSDATE);
```

### 9.7 Creating Tables
#### 테이블 생성:
```sql
CREATE TABLE dept
			(deptno		NUMBER(2),
            dname		VARCHAR2(14),
            loc			VARCHAR2(13),
            create_date DATE DEFAULT SYSDATE);
```
#### 테이블 생성 확인:
```sql
DESCRIBE dept
```
![](https://velog.velcdn.com/images/syshin0116/post/22312c4d-8398-462b-8247-7248cf9439e0/image.png)

### 9.8 데이터 타입
![](https://velog.velcdn.com/images/syshin0116/post/424a861a-675e-4a0b-93c3-028ac0c18eed/image.png)
NUMBER(정수길이, 소수길이)
ROWID: 

### 9.9 Subquery를 이용한 테이블 생성
- CREATE TABLE 문과 AS subquery 옵션을 결합하여 테이블을 생성하고 행을 삽입합니다.
```sql
CREATE TABLE table
				[(column, column...)]
AS subquery;
```
- 지정된 열 개수와 subquery열 개수를 일치시킵니다.
- 열 이름과 기본값을 가진 열을 정의합니다.

```sql
CREATE TABLE dept80
	AS
    	SELECT 	employee_id, last_name,
        		salary*12 ANNSAL,
                hire_date
        FROM	employees
        WHERE 	department id = 80;
 ```
 => CREATE TABLE succeeded.
 
 ```sql
 DESCRIBE dept80
 ```
 ![](https://velog.velcdn.com/images/syshin0116/post/1dc2fdee-d024-4e13-8b84-0ddd4ec1b0c9/image.png)
### 9.10 ALTER TABLE 구문
#### ALTER TABLE 구문을 사용한 커럼 추가, 변경, 삭제:
```sql
ALTER TABLE table
ADD 		(column datatype [DEFAULT expr]
			[, column datatype]...);
```

```sql            
ALTER TABLE table
MODIFY 		(column datatype [DEFAULT expr]
			[, column datatype]...);
```
```sql
ALTER TABLE table
DROP (column [, column] …);
```

### 9.11 컬럼 추가
- ADD절을 사용하여 열을 추가:
```sql
ALTER TABLE dept80
ADD (job_id VARCHAR2(9));
```
=> ALTER TABLE dept80 succeeded.

- 새 열은 마지막 열로 지정: 
![](https://velog.velcdn.com/images/syshin0116/post/938732bd-063a-448e-9f0c-76883b6209db/image.png)

### 컬럼 수정
- 열의 데이터 타입, 크기 및 기본값을 변경할 수 있다.
```sql
ALTER TABLE dept80
MODIFY		(last_name	VARCHAR2(3));
```
- 기본값 변경은 이후에 테이블에 삽입하는 항목에만 적용된다.

### 컬럼 삭제
- DROP COLUMN 절을 사용하여 테이블에서 더 이상 필요 없는
열을 삭제할 수 있다.

```sql
ALTER TABLE dept80
DROP COLUMN job_id;
```
=> ALTER TABLE dept80 succeeded.

![](https://velog.velcdn.com/images/syshin0116/post/6b4d6242-a914-4e26-98c6-684beda5361f/image.png)

### 9.12 SET UNUSED 옵션
- SET UNUSED 옵션을 사용하여 하나 이상의 열을 unused로 표시
- DROP UNUSED COLUMNS 옵션을 사용하여 unused로 표시된 열을 제거할 수 있다

```sql

ALTER TABLE <table_name>
SET UNUSED(<column_name> [ , <column_name>]);

OR

ALTER TABLE <table_name>
SET UNUSED COLUMN <column_name> [ , <column_name>];
```

```sql
ALTER TABLE <table_name>
DROP UNUSED COLUMNS;
```

### 9.13 테이블 삭제
- 테이블을 Recycle bin으로 이동
- PURGE 절이 지정되면 테이블 및 해당 데이터를 완전히 제거
- 종속 객체 무효화 및 테이블의 객체 권한 제거
```sql
DROP TABLE dept80;
```
=> DROP TABLE dept80 succeeded.

> DROP 실행하면 user_recyclebin 테이블로 이동되고, flashbacl table [table명] to before DROP을 사용해 복구시킬 수 있다.
PURGE 사용법: ```DROP TABLE [table명] purge```

### 9.14 제약조건 (Constraints)
#### 제약 조건의 목적
- 데이터의 특성에 맞는 데이터를 저장하기 위함(데이터 무결성)
- 예) 주민등록번호의 자릿수는 13자리
- 예) 성별은 남,여 만 가능
- 예) 주문수량은 반드시 1 이상의 값
- 입력,변경,삭제 시 데이터 무결성을 위해 제약조건을 검토
#### 제약 조건은 테이블 레벨에서 규칙을 강제 적용
#### 제약조건은 테이블에 종속 관계가 있는 경우 삭제를 방지

### 9.15 제약조건의 종류 (Constraints)
#### NOT NULL
– NULL 입력 불가
#### UNIQUE
– 유일한 값
– NULL 중복은 허용
#### PRIMARY KEY
– 테이블당 오직 1개만 설정 가능하고 데이터의 유일한 값
– **NOT NULL + UNIQUE의 의미**
#### FOREIGN KEY
– 부모 테이블에 존재하는 데이터로만 자식 테이블의 데이터 유지
– NULL 혹은 참조할 수 있는 값이어야 함
– 다**른 제약 조건과는 다르게 부모 테이블의 컬럼을 참조해서 무결성 검사함**
#### CHECK
– 설정한 조건을 만족하는 데이터만 입력,변경 가능

### 9.15 제약조건과 무결성 (integrity)
#### NOT NULL(널 무결성)
- NULL 불허
#### PRIMARY KEY< UNIQUE(고유 무결성)
- 서로 다른 유일한 값
#### FOREIGN KEY(참조 무결성)
- NULL 혹은 참조할 수 있는 외래 키 값만 가능
#### CHECK, DEFAULT, NOT NULL(도메인 무결성)
- 정의한 조건 혹은 범위를 만족하는 값

### 9.16 무결성(integrity)과 정합성(Consistency)
#### 데이터 무결성(Data Integrity)
- 데이터 **값이 정확한 상태**를 의미, **제약조건을 만족하는 값**
#### 데이터 정합성(Data Consistency)
- 어떤 데이터들의 값이 **서로 일치**하는 상태를 의미
#### 예) 정합성은 지켜지지만 무결성이 지켜지지 않는 경우
- 고객정보 테이블에 -100의 값을 갖는 고객 존재
- 주문정보 테이블에 고객번호 -100의 값 존재
- 데이터 무결성 훼손: 고객번호는 마이너스 값이 올 수 없음
- 데이터 정합성 이상 없음 : 고객정보, 주문정보의 고객번호 일치

### 9.17 제약조건 가이드
#### 유저가 제약 조건의 이름을 지정하거나 Oracle 서버가 **SYS_Cn** 형식을 사용하여 이름을 생성할 수 있다.
#### 다음 시점 중 하나에서 제약 조건을 생성:
- At the same time as the creation of the table
- After the creation of the table
#### 열 또는 테이블 레벨에서 제약 조건을 정의
#### **데이터 딕셔너리에서 제약 조건을 확인**

### 9.18 제약조건 정의
- 문법:
```sql
CREATE 	TABLE [schema.]table
		(column datatype [DEFAULT expr]
		[column_constraint],
		...
		[table_constraint][,...]);
```
- 컬럼 레벨 제약조건:
```sql
column [CONSTRAINT constraint_name] constraint_type,
```
- 테이블 레벨 제약조건:
```sql
column,...
		[CONSTRAINT constraint_name] constraint_type
		(column, ...),
```

### 9.19 Defining Constraints

- 컬럼 레벨 제약조건 예: 
```sql
CREATE TABLE employees(
	employee_id NUMBER(6)
		CONSTRAINT emp_emp_id_pk PRIMARY KEY,
    first_name VARCHAR2(20),
    ...);
```
- 테이블 레벨 제약조건 예:
```sql
CREATE TABLE employees(
	employee_id 	NUMBER(6),
	first_name 		VARCHAR2(20),
	...
	job_id 			VARCHAR2(10) NOT NULL,
	CONSTRAINT emp_emp_id_pk
		PRIMARY KEY (EMPLOYEE_ID));
```

### 9.20 NOT NULL 제약조건
- 열에 null값이 허용되지 않도록 보장

![](https://velog.velcdn.com/images/syshin0116/post/10a26b6e-3b21-4f8c-af3e-7bc258c85b6b/image.png)

### 9.21 UNIQUE 제약조건

![](https://velog.velcdn.com/images/syshin0116/post/0f424d9e-b828-41bd-8c24-7c7720e616aa/image.png)

### 9.22 UNIQUE 제약조건
- 테이블 레벨 또는 열 레벨에서 정의
```sql
CREATE TABLE employees(
	employee_id 	NUMBER(6),
	last_name 		VARCHAR2(25) NOT NULL,
	email 			VARCHAR2(25),
	salary 			NUMBER(8,2),
	commission_pct 	NUMBER(2,2),
	hire_date DATE 	NOT NULL,
...
	CONSTRAINT emp_email_uk UNIQUE(email));
```
### 9.23 PRIMARY KEY 제약조건
![](https://velog.velcdn.com/images/syshin0116/post/1ad7dcf7-59f3-4e44-8ef1-89373649b28c/image.png)

### 9.24 FOREIGN KEY 제약조건
![](https://velog.velcdn.com/images/syshin0116/post/a501a5b1-8d59-4602-935c-eb48052989f3/image.png)

- 테이블 레벨 또는 열 레벨에서 정의

```sql
CREATE TABLE employees(
	employee_id 	NUMBER(6),
	last_name V		ARCHAR2(25) NOT NULL,
	email 			VARCHAR2(25),
	salary 			NUMBER(8,2),
	commission_pct 	NUMBER(2,2),
	hire_date DATE 	NOT NULL,
...
	department_id 	NUMBER(4),
	CONSTRAINT emp_dept_fk FOREIGN KEY (department_id)
		REFERENCES departments(department_id),
	CONSTRAINT emp_email_uk UNIQUE(email));
```

### 9.25 FOREIGN KEY 제약조건: 추가 기능
#### FOREIGN KEY
- 테이블 제약 조건 레벨에서 하위 테이블의 열을 정의
#### REFERENCES
- 테이블 및 상위 테이블의 열을 식별
#### ON DELETE CASCADE
- 상위 테이블의 행이 삭제될 때 하위 테이블의 종속 행을 삭제
#### ON DELETE SET NULL
- 종속 Foreign key 값을 null로 변환

### 9.26 CHECK 제약조건
- 각 행이 충족해야 하는 조건을 정의
- 다음 표현식은 허용되지 않는다.:
	- CURRVAL, NEXTVAL, LEVEL, ROWNUM 의사 열에 대한 참조
	- SYSDATE, UID, USER, USERENV 함수에 대한 호출
	- 다른 행의 다른 값을 참조하는 query
    
```sql
..., salary NUMBER(2)
CONSTRAINT emp_salary_min
CHECK (salary > 0),...
```

### 9.27 제약조건 위반 사례

```sql
UPDATE 	employees
SET 	department_id = 55
WHERE 	department_id = 110;
```
![](https://velog.velcdn.com/images/syshin0116/post/9a19f161-abcd-41a1-bb76-9efbba0dd587/image.png)

```sql
DELETE FROM departments
WHERE department_id = 60;
```
![](https://velog.velcdn.com/images/syshin0116/post/6603fae7-e3df-4a05-b47d-faedcccd9a67/image.png)

### 9.28 제약조건 추가
#### ALTER TABLE 구문을 통해 추가 가능
- 제약 조건 추가 뜨는 삭제. 제약 조건의 구조는 수정하지 않음.
- 제약 조건 활성화 또는 비활성화
- MODIFY절을 사용하여 NOT NULL 제약 조건 추가

```sql
ALTER TABLE <table_name>
ADD [CONSTRAINT <contraint_name>]
type (<column_name>);
```

- EMP2 테이블에 FOREIGN KEY 제약 조건을 추가하면 관리자가 이미 EMP2 테이블에 유효한 사원으로 존재해야 함을 나타낸다.
```sql
ALTER TABLE emp2
MODIFY employee_id PRIMARY KEY;
```
=> ALTER TABLE emp2 succeeded
```sql
ALTER TABLE emp2
ADD CONSTRIANT emp_gmr_fk
	FOREIGN KEY(manager_id)
    REFERENCES emp2(employee_id);
```
=> ALTER TABLE succeeded


### 9.29 ON DELETE 절
- 상위 키가 삭제될 때 하위 행을 삭제하려면 ON DELETE CASCADE 절을 사용:
```sql
ALTER TABLE emp2 ADD CONSTRAINT emp_dt_fk
FOREIGN KEY (Department_id)
REFERENCES departments(department_id) ON DELETE CASCADE;
```
=> ALTER TABLE Emp2 succeeded

- 상위 키가 삭제될 때 하위 행을 널로 설정하려면 ON DELETE SET NULL절을 사용:
```sql
ALTER TABLE emp2 ADD CONSTRAINT emp_dt_fk
FOREIGN KEY (Department_id)
REFERENCES departments(department_id) ON DELETE SET NULL;
```

### 9.30 제약조건 삭제
- EMP2 테이블에서 관리자 제약 조건을 제거
```sql
ALTER TABLE emp2
DROP CONSTRIANT emp_gmr_fk;
```
=> ALTER TABLE Emp2 succeeded

- DEPT@ 테이블에서 PRIMARY KEY 제약 조건을 제거하고 EMP@.DEPARTMENT_ID 열에서 연관된 FOREIGN KEY 제약 조건을 삭제:
```sql
ALTER TABLE dept2
DROP PRIMARY KEY CASCADE;
```
=> ALTER TABLE dept2 secceeded

### 9.31 제약조건 비활성화
- ALTER TABLE 문의 DISABLE 절을 실행하여 무결성 제약 조건을 비활성화
- CASCADE 옵션을 적용하여 종속 무결성 제약 조건을 비활 성화할 수 있다.
```sql
ALTER TABLE emp2
DISABLE CONSTRAINT emp_dt_fk;
```
=> ALTER TABLE Emp2 succeeded

### 9.32 제약조건 활성화
- ENABLE 절을 사용하여 테이블 정의에서 현재 비활성화된 무결성 제약 조건을 활성화할 수 있다
```sql
ALTER TABLE 	emp2
ENABLE 			CONSTRAINT emp_dt_fk;
```
=> ALTER TABLE Emp2 succeeded

- UNIQUE KEY 또는 PRIMARY KEY 제약 조건을 활성화하면 UNIQUE 인덱스가 자동으로 생성

### 9.33 Read-Only 테이블
#### ALTER TABLE 명령을 통해:
- 테이블을 읽기 전용 모드로 설정하여 테이블을 유지 관리하는 동안 DDL(TRUNCATE)문 또는 DML 문에 의한 변경을 방지
- 테이블을 다시 읽기/쓰기 모드로 설정
```sql
ALTER TABLE employees READ ONLY;

-- perform table maintenance and then
-- return table back to read/write mode

ALTER TABLE employees READ WRITE;
```

# 9장 실습
## 9.1 테이블 생성 및 제약조건
[09_01.테이블 생성 및 제약조건.pdf](https://github.com/syshin0116/Study/files/11471216/09_01.pdf)

실습 : SUBQUERY를 이용한 테이블 생성 및 입력 / 컬럼 디폴트 값 설정
제약조건 추가, 삭제, 활성화, 비활성화 / 제약조건을 위배하는 케이스 / 제약 조건 확인
딕셔너리 뷰에서 제약 조건 확인 방법
```sql
-- CONSTRAINT_TYPE
-- P : PRIMARY KEY 제약조건
-- R : FOREIGN KEY 제약조건
-- C : CHECK 제약조건
-- U : UNIQUE 제약조건

-- 제약조건 정보를 확인
SELECT OWNER
 	, TABLE_NAME
 	, CONSTRAINT_NAME
 	, CONSTRAINT_TYPE
 	, SEARCH_CONDITION
 	, STATUS
FROM USER_CONSTRAINTS
WHERE TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY TABLE_NAME, CONSTRAINT_TYPE;

-- 제약 조건을 사용한 컬럼
SELECT * FROM USER_CONS_COLUMNS
WHERE TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY TABLE_NAME;

-- 조인하여 컬럼을 포함한 제약조건 정보 확인
SELECT A.OWNER
 	, A.TABLE_NAME
 	, B.COLUMN_NAME
 	, A.CONSTRAINT_NAME
 	, A.CONSTRAINT_TYPE
 	, A.SEARCH_CONDITION
 	, A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
\* 원활한 실습진행을 위해 날짜 형식을 아래와 같이 설정한다.

```sql
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';
SELECT * FROM NLS_SESSION_PARAMETERS
WHERE PARAMETER = 'NLS_DATE_FORMAT';
```

**\* 모든 실습은 SCOTT 계정에서 실행한다**

### 1. 부서 테이블 생성
#### 1.1 SUBQUERY를 이용한 테이블 생성(CTAS) 및 테이블 구조 확인/조회
SUBQUERY를 이용하여 기존의 데이터를 입력하면서 생성한다.
테이블의 제약조건은 제외되고 데이터만 입력된다.

```sql
DROP TABLE MY_DEPT;
CREATE TABLE MY_DEPT

AS

SELECT * FROM DEPT;
DESCRIBE MY_DEPT;
SELECT * FROM MY_DEPT;
```
#### 1.2. 제약조건 추가, PK 설정
```sql
ALTER TABLE MY_DEPT
ADD
(
 	CONSTRAINT PK_MY_DEPT PRIMARY KEY (DEPTNO)
);
```
#### 1.3. 추가한 PK 제약 조건을 확인한다.
```sql
SELECT A.OWNER
 , A.TABLE_NAME
 , B.COLUMN_NAME
 , A.CONSTRAINT_NAME
 , A.CONSTRAINT_TYPE
 , A.SEARCH_CONDITION
 , A.STATUS
 FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
### 2. 사원 테이블을 생성한다.
#### 2.1. PK, FK, CREATE_DATE 컬럼에 디폴트 값을 설정하여 테이블을 생성하고 구조를 확인한다.
```sql
CREATE TABLE MY_EMP
(
	EMPNO NUMBER(4) CONSTRAINT PK_MY_EMP PRIMARY KEY,
	ENAME VARCHAR2(10),
	JOB VARCHAR2(9) NOT NULL,
	MGR NUMBER(4),
	HIREDATE DATE,
	SAL NUMBER(7,2),
	COMM NUMBER(7,2),
	DEPTNO NUMBER(2) CONSTRAINT FK_MY_DEPTNO REFERENCES MY_DEPT,
	 -- 디폴트 값 SYSDATE 설정
	CREATE_DATE DATE DEFAULT SYSDATE
);

DESCRIBE MY_EMP;
```
#### 2.2 SUBQUERY를 이용한 데이터 입력
사원 테이블에 기존 사원 테이블을 SUBQUERY로 조회하여 입력한다.
```sql
INSERT INTO MY_EMP
( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO)
SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO
FROM EMP;

COMMIT;

-- CREATE_DATE 컬럼에 디폴트 값으로 SYSDATE가 들어간 것을 확인한다.
SELECT * FROM MY_EMP;
```

#### 2.3 사원 테이블의 제약 조건을 확인한다.
```sql
-- 컬럼 포함한 제약조건 정보 확인
SELECT A.OWNER
 , A.TABLE_NAME
 , B.COLUMN_NAME
 , A.CONSTRAINT_NAME
 , A.CONSTRAINT_TYPE
 , A.SEARCH_CONDITION
 , A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
### 3. 테이블에 컬럼 추가/삭제 및 제약조건 추가/삭제
#### 3.1 사원 테이블에 컬럼 추가 및 구조 확인
```sql
ALTER TABLE MY_EMP
ADD (
 	EMAIL VARCHAR2(20)
);

DESC MY_EMP;
```
3.2 사원 테이블에 UNIQUE, CHECK 제약조건 추가
```sql
ALTER TABLE MY_EMP
ADD (
 	CONSTRAINT UK_EMAIL UNIQUE (EMAIL)
);
ALTER TABLE MY_EMP
ADD (
 	CONSTRAINT EMP_SALARY_MIN CHECK (SAL > 0)
);
```

#### 3.3 추가한 UNIQUE, CHECK 제약조건 확인
```sql
SELECT A.OWNER
 	, A.TABLE_NAME
 	, B.COLUMN_NAME
 	, A.CONSTRAINT_NAME
 	, A.CONSTRAINT_TYPE
 	, A.SEARCH_CONDITION
 	, A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
#### 3.4 제약 조건 비활성화 및 DISABLE 된 제약조건 확인
```sql
ALTER TABLE MY_EMP
DISABLE CONSTRAINT UK_EMAIL;
SELECT A.OWNER
 , A.TABLE_NAME
 , B.COLUMN_NAME
 , A.CONSTRAINT_NAME
 , A.CONSTRAINT_TYPE
 , A.SEARCH_CONDITION
 , A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
#### 3.5 제약 조건 활성화 및 제약조건 확인
```sql
ALTER TABLE MY_EMP
ENABLE CONSTRAINT UK_EMAIL;
SELECT A.OWNER
 	, A.TABLE_NAME
 	, B.COLUMN_NAME
	, A.CONSTRAINT_NAME
 	, A.CONSTRAINT_TYPE
 	, A.SEARCH_CONDITION
 	, A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
```sql
ALTER TABLE MY_EMP
DROP CONSTRAINT UK_EMAIL;
SELECT A.OWNER
 	, A.TABLE_NAME
 	, B.COLUMN_NAME
 	, A.CONSTRAINT_NAME
 	, A.CONSTRAINT_TYPE
 	, A.SEARCH_CONDITION
 	, A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
```
#### 3.6. 컬럼 속성 변경(MODIFY) 및 구조 확인 (사이즈를 10에서 50으로 변경)
MODIFY 를 이용하여 컬럼의 데이터 타입, 크기, 기본값을 변경 가능하다.
```sql
ALTER TABLE MY_EMP
MODIFY (EMAIL VARCHAR2(50));

DESC MY_EMP;
```

#### 3.7. 컬럼 삭제 (DROP)
두가지 스타일로 모두 가능한다.
```sql
ALTER TABLE MY_EMP
DROP (EMAIL);

ALTER TABLE MY_EMP
DROP COLUMN EMAIL;

DESC MY_EMP;
```
### 4. 제약조건을 위배하는 케이스
#### 4.1 PK 제약 조건 위배
PK를 기존에 있는 **7839** 입력
```sql
SELECT * FROM MY_EMP
WHERE EMPNO = 7839;

INSERT INTO my_emp VALUES(7839, 'KING', 'PRESIDENT', NULL, TO_DATE('1981-11-17', 'YYYY-MM-DD'),
5000, NULL, 10, SYSDATE);
```
ORA-00001: 무결성 제약 조건(SCOTT.PK_EMP)에 위배됩니다
#### 4.2 FK 참조 무결성 제약조건 위배
deptno 를 부모에는 없는 88을 입력
```sql
-- 부모 테이블에 부서번호 88이 없음을 확인한다.
SELECT * FROM MY_DEPT
WHERE DEPTNO = 88;
INSERT INTO my_emp VALUES(8888, 'KING', 'PRESIDENT', NULL, TO_DATE('1981-11-17', 'YYYY-MM-DD'),
7000, NULL, 88, SYSDATE);
```
ORA-02291: 무결성 제약조건(SCOTT.FK_MY_DEPTNO)이 위배되었습니다- 부모 키가 없습니다
#### 4.3 FK 참조 무결성 제약조건 위배
자식이 참조하고 있는 deptno의 10번 부서를 삭제 시도
```sql
-- 자식 테이블에서 부서번호 10번을 사용하고 있음을 확인한다.
SELECT * FROM MY_EMP
WHERE deptno = 10;
```
```sql
DELETE FROM MY_DEPT
WHERE deptno = 10;
```
ORA-02292: 무결성 제약조건(SCOTT.FK_MY_DEPTNO)이 위배되었습니다- 자식 레코드가 발견되었습니다

#### 4.4 NOT NULL 제약 조건 위해
Job 을 NULL 로 입력
```sql
-- JOB 컬럼이 NOT NULL 임을 확인한다.
DESC MY_EMP;
INSERT INTO my_emp VALUES(8888, 'KING', NULL, NULL, TO_DATE('1981-11-17', ' YYYY-MM-DD'), 7000,
NULL, 10, SYSDATE);
```
ORA-01400: NULL을 ("SCOTT"."MY_EMP"."JOB") 안에 삽입할 수 없습니다

#### 4.5 CHECK 제약조건 위배
SAL 0으로 입력
```sql
-- EMP_SALARY_MIN 제약조건을 확인한다.
SELECT A.OWNER
 	, A.TABLE_NAME
 	, B.COLUMN_NAME
 	, A.CONSTRAINT_NAME
 	, A.CONSTRAINT_TYPE
 	, A.SEARCH_CONDITION
	 , A.STATUS
FROM USER_CONSTRAINTS A
JOIN USER_CONS_COLUMNS B
ON A.CONSTRAINT_NAME = B.CONSTRAINT_NAME
WHERE A.TABLE_NAME IN ('MY_EMP', 'MY_DEPT')
ORDER BY A.TABLE_NAME, B.COLUMN_NAME;
INSERT INTO my_emp VALUES(8888, 'KING', 'PRESIDENT', NULL, TO_DATE('1981-11-17', ' YYYY-MM-DD'),
0, NULL, 10, SYSDATE);
```
ORA-02290: 체크 제약조건(SCOTT.EMP_SALARY_MIN)이 위배되었습니다

#### 4.6. 삭제하려고 하는 테이블에 외래키에 의해 참조되는 고유/기본키가 있을 경우 생기는 오류

```sql
DROP TABLE MY_DEPT;
```
ORA-02449: 외래 키에 의해 참조되는 고유/기본 키가 테이블에 있습니다
- 해결방안:
	1. 테이블을 삭제하기 전 제약조건을 먼저 삭제하고 삭제하면 된다.
	2. CASCADE CONSTRAINTS 키워드를 이용하여 제약조건을 함께 삭제

#### 4.7 제약조건을 삭제하고 테이블까지 삭제한다.
DROP TABLE MY_DEPT CASCADE CONSTRAINTS;
### 5. MY_EMP 테이블 읽기 전용 모드로 전환하고 DML, DDL을 적용해본다.
DML은 적용 안되지만 DDL은 TRUNCATE는 적용 안되고 그 외에는 적용이 된다.
#### 5.1 읽기 전용 모드 테이블에 UPDATE 수행

```sql
ALTER TABLE MY_EMP READ ONLY;

UPDATE MY_EMP
SET SAL = 10000
WHERE EMPNO = 7369;
```
SQL 오류: ORA-12081: "SCOTT"."MY_EMP" 테이블에 작업을 업데이트하는 것이 허용되지 않습니다

#### 5.2 읽기 전용 모드 테이블에 TRUNCATE 수행
```sql
TRUNCATE TABLE MY_EMP;
```
ORA-12081: "SCOTT"."MY_EMP" 테이블에 작업을 업데이트하는 것이 허용되지 않습니다

#### 5.3 읽기 전용 모드 테이블에 ALTER 수행
```sql
ALTER TABLE MY_EMP
ADD (
EMAIL VARCHAR2(20)
);
DESC MY_EMP;
Table MY_EMP이(가) 변경되었습니다.
```
#### 5.4 읽기 전용 모드 테이블에 DROP 수행
```sql
DROP TABLE MY_EMP;
```
Table MY_EMP이(가) 삭제되었습니다.
#### 5.5 읽기/쓰기 모드로 전환하는 명령어
```sql
CREATE TABLE MY_EMP
AS
SELECT * FROM DEPT;

ALTER TABLE MY_EMP READ ONLY;
-- READ_ONLY의 값이 YES인 것을 확인한다.

SELECT TABLE_NAME, READ_ONLY
FROM USER_TABLES
WHERE TABLE_NAME = 'MY_EMP';

ALTER TABLE MY_EMP READ WRITE;

-- READ_ONLY의 값이 NO인 것을 확인한다.
SELECT TABLE_NAME, READ_ONLY
FROM USER_TABLES
WHERE TABLE_NAME = 'MY_EMP';
```
# ORACLE 19C
## 10장. 고급 쿼리 기능

### 10.1 목표
- 계층화 쿼리 이해
- 정규표현식 활용
- [연습 문제]

### 10.2 계층화 쿼리(Hierarchical query)
#### 계층화 쿼리?
- 테이블의 **행과 행 사이에 부모 자식 관계**가 있으면 Hierarchical Query가 가능하다.
- **수직적 관계**를 맺고 있는 행들의 계층형 정보를 조회할 수 있다.
- Hierarchical Query를 사용하면 테이블에 있는 행 간의 자연적 계층 관계
에 준하여 데이터를 검색할 수 있다.
- **관계형 데이터베이스는 레코드를 계층 방식으로 저장하지 않는다.** 그
러나 한 테이블의 행 사이에 계층 관계가 존재하면 트리 탐색이라는 프
로세스를 사용하여 계층을 구성할 수 있다.
- 계층화된 트리는 **가계도, 기업 조직도, 종의 진화도, 선후행 배치흐름도**
등에 계층적인 그림으로 표현 할 때 많이 사용된다.
- 계층화 쿼리는 **재귀 쿼리 , 트리구조 쿼리**라고도 한다.

### 10.3 계층화 쿼리(Hierarchical query
#### 선후행 배치 흐름도
#### 배치 작업 간의 의존성을 고려해서 선행과 후행의 관계를 설정
![](https://velog.velcdn.com/images/syshin0116/post/55d6a0d3-f7b9-4511-bfb8-74be237ac7b0/image.png)
#### 사원 테이블의 계층 구조

![](https://velog.velcdn.com/images/syshin0116/post/0050403d-6127-4040-ae26-b510fe062c97/image.png)

#### 계층화 쿼리 Syntax
```sql
SELECT [LEVEL], column, expr...
FROM table
[WHERE condition(s)]
[START WITH condition(s)]
[CONNECT BY PRIOR condition(s)] ;
```
#### Starting point : 충족해야 하는 조건을 지정.
```sql
...START WITH last_name = 'Kochhar'
```
#### 예
```sql
... START WITH manager_id IS NULL
... START WITH employee_id = (SELECT employee_id
							FROM employees
							WHERE last_name = 'Kochhar')
```
#### 계층화 쿼리 : 트리 탐색
```sql
CONNECT BY PRIOR column1 = column2
```
```sql
... CONNECT BY PRIOR employee_id = manager_id
... CONNECT BY PRIOR manager_id = employee_id
... CONNECT BY employee_id = PRIOR manager_id
```
![](https://velog.velcdn.com/images/syshin0116/post/d86e94cc-1613-477a-a83e-c0f887c3c5dc/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/68c72e85-030f-499d-8fe2-e26fef46e4de/image.png)

#### PRIOR 루트로 사용할 컬럼 = 부모ID값을 저장하는 컬럼
#### PRIOR (레벨N의)employee_id = (레벨N+1의)manager_id
#### Ex 하향식) CONNECT BY PRIOR employee_id = manager_id
![](https://velog.velcdn.com/images/syshin0116/post/c7e67985-2cab-4989-87d3-3c3169f7a97b/image.png)

#### PRIOR 루트로 사용할 컬럼 = 부모ID값을 저장하는 컬럼
#### PRIOR (레벨N의)manager_id = (레벨N+1의)employee_id
#### Ex 상향식) CONNECT BY PRIOR manager_id = employee_id
![](https://velog.velcdn.com/images/syshin0116/post/3b394e36-f35f-42cf-9ea0-fd7e16b60be1/image.png)

#### 계층화 쿼리
```sql
SELECT last_name||' reports to '||
PRIOR last_name "Walk Top Down"
FROM employees
START WITH last_name = 'King'
CONNECT BY PRIOR employee_id = manager_id ;
```
![](https://velog.velcdn.com/images/syshin0116/post/4fcd9107-fc8d-4f27-9c2e-a3dcb037dd05/image.png)
#### 계층화 쿼리
- 최상위 레벨에서 시작하여 다음 레벨을 각각 들여 쓴 형태의 회사 관리 레벨이
표시된 보고서를 생성하시오.
```sql
SELECT LPAD(last_name, LENGTH(last_name)+(LEVEL*2)-2,'_')
		AS org_chart
FROM employees
START WITH first_name='Steven' AND last_name='King'
CONNECT BY PRIOR employee_id=manager_id ;
```
- LPAD(char1,n [,char2])는길이 n의왼쪽을 char2의 문자 시퀀스로 채운 char1을 반
환. 인수 n은 터미널 화면에 표시되는 반환 값의 총 길이.
- LPAD(last_name, LENGTH(last_name)+(LEVEL*2)-2,'_')는 표시 형식을 정의
- char1은 LAST_NAME이고, n은 반환 값의 총 길이로 LAST_NAME +(LEVEL*2)-2이
고, char2는 '_' 이다.

![](https://velog.velcdn.com/images/syshin0116/post/e421e2cb-70a0-4deb-8a44-9796692f92ec/image.png)

#### 계층화 쿼리: 분기 제거
- 루트에서 시작하여 하향식으로 탐색하고 결과에서 Higgins 사원은 제거하고 하위 행은 처리
```sql
SELECT 	department_id, employee_id,last_name, job_id, salary
FROM 	employees
WHERE 	last_name != 'Higgins'
START 	WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
```
#### 루트에서 시작하여 하향식으로 탐색하고 Higgins 사원과 하위 행을 모두 제거
```sql
SELECT 		department_id, employee_id,last_name, job_id, salary
FROM 		employees
START 		WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id
AND 		last_name != 'Higgins';
```

#### 계층화 쿼리: 계층구조 전개를 부하직원은 사원번호 순으로 정렬하고자 한다.
```sql
SELECT empno
		, LEVEL lv
		, RPAD(' ', LEVEL*3-2) || ename ename
		, SUBSTR(SYS_CONNECT_BY_PATH(ename, '-'), 2) enames
	FROM emp
START WITH mgr IS NULL
CONNECT BY PRIOR empno = mgr
ORDER BY empno ;
```
![](https://velog.velcdn.com/images/syshin0116/post/7db21f45-05d2-4255-94fc-fe3dddfae869/image.png)

### 10.4 정규 표현식

#### 정규표현식(Regular expression)
- 문자열을 다룰 때, **문자열의 특정한 패턴을 표현하는 일종의 형식 언어**
- 정규 표현식은 문자열에서 **특정 문자 조합을 찾기 위한 패턴**
- 주어진 문장 패턴과 매치 시킬 수 있는 어떤 표현을 기술할 수 있는 기호와 원소들의 집합으로 매우
강력하고 실용적인 패턴 매치기법이다.
- **POSIX 표준 문법**을 따른다.
- 다양한 매치와 검색을 정의하는 **메타 캐릭터**들의 조합으로 이루어진다.
- 대소문자를 구분한다.

#### When?
- ETL (Extract, Transform, Load)
- Data Mining(누적된 정보를 통한 인과관계/통계 분석)
- Data Cleansing(정제)
- Data Validation(검증)
- 제약조건을 이용한 테이블 Data 유효성 검증
####  What?
- Text에서 전화번호, 우편번호, 이메일 주소, 주민등록번호, IP주소 등을 검증 및 추출
- HTML 태그, 숫자, 날짜, 기타 특정 텍스트 데이터와 일치하는 패턴을 확인하고 다른 패턴
으로 대체하는 것이 가능
- 중복 단어의 확인
- 특별한 상태에서 공백의 제거
- 문자의 파싱

#### 정규표현식(Regular expression) 함수
![](https://velog.velcdn.com/images/syshin0116/post/cd3676de-52c3-4db0-be7f-2d58389fd820/image.png)

#### 정규표현식(Regular expression) Meta character
![](https://velog.velcdn.com/images/syshin0116/post/bb433ff0-d100-4cf2-b62b-861e9683ce27/image.png)

#### 정규표현식(Regular expression) 함수 (HR schema) - REGEXP_LIKE
```sql
SELECT first_name, last_name
FROM employees
WHERE REGEXP_LIKE (first_name, '^Ste(v|ph)en$');
```
![](https://velog.velcdn.com/images/syshin0116/post/70871613-d109-4dae-b83f-821c001ab95b/image.png)

>MPLOYEES 에 대한 이 query에서는 first name에 Steven 또는
Stephen이 포함된 모든 사원 정보 표시.
- **는 표현식의 시작**
- **는 표현식의 끝**
- **는둘중 하나(또는)**

#### 정규표현식(Regular expression) 함수 (HR schema) - REGEXP_INSTR

```sql
SELECT street_address,
		REGEXP_INSTR(street_address,'[^[:alpha:]]')
FROM 	locations
WHERE 	REGEXP_INSTR(street_address,'[^[:alpha:]]')> 1;
```
![](https://velog.velcdn.com/images/syshin0116/post/c6725a0f-38b8-492a-b3de-c1d414b205ae/image.png)
  
#### 정규표현식(Regular expression) 함수 (HR schema) - REGEXP_SUBSTR
```sql
SELECT 	REGEXP_SUBSTR(street_address , ' [^ ]+ ’)
AS 		"Road"
FROM 	locations;
```
![](https://velog.velcdn.com/images/syshin0116/post/4e78e268-fed9-47b5-a0e4-7a20d1462679/image.png)

#### 정규표현식(Regular expression) 함수 (HR schema) - REGEXP_REPLACE
```sql
SELECT last_name,
REGEXP_REPLACE(phone_number, '\.','-')
AS phone
FROM employees; 
```
![](https://velog.velcdn.com/images/syshin0116/post/d927230f-d8d6-444d-bb51-fea3abffaafe/image.png)

#### 정규표현식(Regular expression) 함수 (HR schema) - REGEXP_COUNT
![](https://velog.velcdn.com/images/syshin0116/post/913c29c8-f049-4174-9b03-e49eca537b24/image.png)
#### 정규표현식(Regular expression)을 활용한 Data cleansing Exam 2


#### 정규표현식(Regular expression)을 활용한 Data cleansing Exam 1
- Email 주소 분리 = ID | Domain
- REGEXP_SUBSTR(소스 문자열, Pattern \[, 위치 \[, 발생 횟수 \[, Match를 시도할 때의 옵션\]\]\])
- **@가 포함되지 않은 첫번째 문자열, @가 포함되지 않은 두번째 문자열을 반환**
```sql
SELECT 		REGEXP_SUBSTR(email, '[^@]+', 1, 1) AS "ID",
			REGEXP_SUBSTR(email, '[^@]+', 1, 2) AS "MailAddr"
FROM 		(SELECT ‘&input_email' email FROM dual);
```
![](https://velog.velcdn.com/images/syshin0116/post/fe1ef68f-b1c6-491f-8592-09b44a6fd6e1/image.png)

#### 정규표현식(Regular expression)을 활용한 Data cleansing Exam 2
- 주민번호 Masking
- REGEXP_REPLACE(소스 문자열, Pattern \[, 바꿀 문자열 \[, 위치 \[, 발생횟수 \[Match 파라미터]]]])
- **7번째 문자부터 숫자는 '*' 로 변환**
```sql
SELECT REGEXP_REPLACE(SSN, '[0-9]', '*' , 7) REG_REP
FROM ( SELECT '&jumin' as SSN FROM dual );
```
![](https://velog.velcdn.com/images/syshin0116/post/f1527848-9ea2-47c4-8908-2cff9c3b7478/image.png)

#### 정규표현식(Regular expression)을 활용한 Data cleansing Exam 3
- 전화번호 패턴 만들어 저장하기
```sql
SELECT
REGEXP_REPLACE('010.3664.1340','([[:digit:]]{3})\.([[:digit:
]]{4})\.([[:digit:]]{4})','(\1) \2 - \3') AS "Result1"
FROM dual;
```
![](https://velog.velcdn.com/images/syshin0116/post/4368e5b1-2272-4ec9-848b-b1fd1481095d/image.png)

- 생년월일 패턴 만들어 저장하기
```sql
SELECT REGEXP_REPLACE('&생년월일_YYYYMMDD',
'([[:digit:]]{4})([[:digit:]]{2})([[:digit:]]{2})', '\1 년
\2 월 \3 일' )
FROM dual;
```
![](https://velog.velcdn.com/images/syshin0116/post/cdec06ff-af61-466a-b943-6ed3089a299b/image.png)

## 11. 분석 함수
### 11.1 목표
#### 분석 함수란
#### 다양한 분석 함수 사용해 보기
### 11.2 분석 함수 (Analytic Function)

#### 분석 함수는 Aggregate Function 의 계산을 지정하는 행 그룹을 기반으로 계산하여 각 그룹에 대해 여러 행을 반환 할 수 있는 Function 을 말한다.
#### 일반적으로 누적 계산, 집계 및 보고용 결과를 질의 할 때 유용하게 사용 할 수 있으며 복잡한 질의를 보다 간편하고 빠르게 실행 할 수 있게 해준다.
> 윈도우함수(args) OVER (\[ PARTITON BY column]
						\[ ORDER BY column \[ASC | DESC]);
\[\[ROWS|RANGE] BETWEEN UNBOUNDED PRECEDING|CURRENTROW]


```sql
SELECT empno, ename, sal, deptno, sum(sal) dept_tot
FROM scott.emp ;

ERROR at line 1:
ORA-00937: not a single-group group function
```
#### 위의 문장은 SUM 이라는 집계함수(Group Function)를 GROUP BY 절 없이 일
반 컬럼들과 함께 사용하였기 때문에 발생한 에러다.


#### 오류를 분석 함수로 해결해 본다.
- 샘플 스키마 중 scott 사용자를 사용한다
```sql
SELECT empno, ename, sal, deptno,
		sum(sal) over(partition by deptno) as dept_tot
FROM scott.emp ;
```
![](https://velog.velcdn.com/images/syshin0116/post/2674606e-7c6b-4b70-b826-4aeeae7ebf44/image.png)

> partition by : group by와 비슷하지만 over()함수 안에서 쓰임

- 각 그룹당 동일한 Function 의 결과를 반복 출력하며 에러 없이 실행 가능
- 만약 위와 같은 결과를 확인하고자 했을 때 분석함수를 사용하지 않는다면 어떤 문장을 사용해야 할까요?
```sql
SELECT a.empno, a.ename, a.sal, a.deptno, b.dept_tot
FROM emp a, ( SELECT deptno, sum(sal) dept_tot
FROM emp
GROUP BY deptno ) b
WHERE a.deptno = b.deptno ;
```
- **불필요한 Sub-Query**를 이용해야 하며 원본 집합인 EMP 테이블을 반복적으로 Access 하는 등 비효율적인 문장이 된다.
- 분석함수는 원하는 결과를 가져다 주는 **SQL 을 보다 쉽게 만들 수 있도록
도와주며 성능 역시 향상** 시켜준다.

- 분석 함수는 집계 함수 뒤에 Analytic Clause (OVER 절)을 통해 행 그룹의정의를 지정하고 각 그룹당 결과 값을 반복하여 출력 한다.
- 여기서 행 그룹의 범위를 WINDOW 라 부른다.
- 하나의 WINDOW 가 계산을 수행하는데 사용되는 행들의 집합을 결정하게 되며 PARTITION BY, ORDER BY, WINDOWING 을 통하여 조절하게 된다.
- 또한 분석 함수는 Join 문장, WHERE, GROUP BY, HAVING 등과 함께 쓰일 때 가장 마지막에 연산(집계)을 진행하며 SELECT 절과 ORDER BY 절에서만 사용이 가능하다.
- SQL Language Reference 19c 매뉴얼 참고
	- [https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/AnalyticFunctions.html#GUID-527832F7-63C0-4445-8C16-307FA5084056](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/AnalyticFunctions.html#GUID-527832F7-63C0-4445-8C16-307FA5084056)

### 11.3 OVER 절
- PARTITION BY 절은 GROUP BY 절과 동일한 역할을 수행 한다.
- 단, GROUP BY 절을 사용하지 않고 필요한 집합으로 (WINDOW) 행들을 그룹화 시킴.
- 다음은 사원 테이블(emp) 전체의 평균 급여를 구한 것이다.
```sql
SELECT empno, ename, sal, avg(sal) over( ) as avg_sal
FROM emp;
```
![](https://velog.velcdn.com/images/syshin0116/post/627f0e02-80a2-4af2-a6f3-775cb3867346/image.png)
- PARTITION BY 절은 GROUP BY 절과 동일한 역할을 수행 한다.
- 단, GROUP BY 절을 사용하지 않고 필요한 집합으로 (WINDOW) 행들을 그룹화 시킴.
- 다음은 사원 테이블의 **부서 및 업무 별** 평균 급여를 구한 것이다
```sql
SELECT 	empno, ename, sal, deptno, job,
		avg(sal) over(PARTITION BY deptno, job) as avg_sal
FROM 	emp;
```
![](https://velog.velcdn.com/images/syshin0116/post/cdd58ff6-7fe5-4578-aff3-e39420fd3599/image.png)

- PARTITION BY 절은 GROUP BY 절과 동일한 역할을 수행 한다.
- **분석 함수는 Join 문장, WHERE, GROUP BY, HAVING 등과 함께 쓰일 때가장 마지막에 연산(집계)을 진행**한다.
- 다음은 사원, 부서 테이블을 조인한 뒤 부서별 평균 급여를 구한 것이다

```sql
SELECT 	d.deptno, d.dname, e.ename, e.sal,
		trunc(avg(e.sal) over(PARTITION BY d.deptno)) as avg_sal
FROM 	emp e, dept d
WHERE 	d.deptno = e.deptno;
```
![](https://velog.velcdn.com/images/syshin0116/post/af9754b0-20a6-431a-90a8-9238dbfa369c/image.png)

- ORDER BY 절은 Partition by 로 정의된 WINDOW 내에서의 행들의 정렬 순
서를 정의 한다.
- 전체 사원을 대상으로 급여를 오름차순 정렬 한 뒤 행 순서 번호를 출력한다.
```sql
SELECT 	empno, ename, sal, deptno,
		row_number( ) over ( ORDER BY sal ASC ) as rnum
FROM 	emp ;
```
![](https://velog.velcdn.com/images/syshin0116/post/9df8eede-fd69-49fe-afcb-097d98e28907/image.png)

- ORDER BY 절은 Partition by 로 정의된 WINDOW 내에서의 행들의 정렬 순서를 정의 한다.
- 다음은 부서별 급여를 내림차순 정렬 한 뒤 부서 별 급여 랭킹을 출력한다.

```sql
SELECT 	empno, ename, sal, deptno,
		row_number( ) over
		( PARTITION BY deptno ORDER BY sal DESC ) as rnum
FROM emp;
```
![](https://velog.velcdn.com/images/syshin0116/post/6f5b107c-aedd-427d-babe-2edd5245f374/image.png)

- ORDER BY 절은 Partition by 로 정의된 WINDOW 내에서의 행들의 정렬순서를 정의 한다.
- 다음은 NULL 값 기준 정렬 시 기본적으로 가장 큰 값으로 인식한다

```sql
SELECT 	empno, ename, sal, comm,
		DENSE_RANK( ) over ( ORDER BY comm ASC ) as rnum
FROM 	emp
WHERE 	deptno = 30 ;
```

### 11.4 순위 관련 함수: RANK(), DENSE_RANK(), ROW_NUMBER()


>SQLD 
UNBOUNDED PRECENDING : 첫번쨰 행
UNBOUNDED FOLLOWING: 마지막 행
select SEMPNO, ENAME, SAL, 
	SUM(SAL OVER (order by EMPNO ASC) AS SUM_SAL
FROM EMP WHERE DEPTNO IN (10,20);


## 12. 외부 데이터 활용과 분석
[Uploading 한국장학재단_대학별 평균등록금_20220430.csv…]()

### 12.1 목표
- 외부 데이터 활용
- 공공 데이터를 테이블로 로드
- 간단한 분석 작업

### 12.2 외부 데이터 활용과 분석
#### Exam1) 전국대학별등록금통계현황
- 해당 자료를 통해 업무적으로 조회 가능한 질문을 생각해 본다.
	- 사립,공립,국립들의 각각의 대학등록금 평균값과 대학등록금 중 최고등록과 최저등록의 비교
- 공공 데이터 추출
	- 전국_대학별등록금통계_현황.csv
- 자료를 통해 Data Structure (Table) 생성 후 Data Load
```sql
create table univ_tution
(
division varchar2(20), 				-- 학제별
type varchar2(20), 					-- 설립별
university varchar2(60), 			-- 대학명
area varchar2(40), 					-- 지역별
admission_capacity number(10), 		-- 입학정원합(명)
avg_admission_fee number(10), 		-- 평균입학금(원)
tution number(10) -- 평균등록금(원)
);
```
![](https://velog.velcdn.com/images/syshin0116/post/dce83349-646d-4c77-aba2-6188463020bc/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/046e439e-f154-43b5-8a94-f7e5751c5b79/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/ed44323a-2d32-467f-b39c-cfe2cfc28b1f/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/1088d8b3-8873-4280-a6ff-ebe51594737a/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/6a02a5d1-ce9b-485b-9cb5-b925e6849519/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/207fb93f-e70f-4d79-8c39-3717e22d4bd6/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/7a90d112-1aa9-432c-bb6a-ba80f17b57d3/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/52685dfd-e55e-4506-9681-f82f62e7fee7/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/10b4a687-d3aa-4a1a-a0a5-858b332cfa83/image.png)

### 12. 연습문제
#### Exam1) 전국대학별등록금통계현황
▪ 해당 자료를 통해 의미 있는 질문(SQL Query)을 작성
1) 사립,공립,국립의 평균등록금

#### Exam2-1) 전국대학별등록금통계현황
▪ 해당 자료를 통해 의미 있는 질문(SQL Query)을 작성-분석함수를 사용하는 방법1
2) 대학등록금 중 최고등록금과 최저등록금의 비교

#### Exam2-2) 전국대학별등록금통계현황
▪ 해당 자료를 통해 의미 있는 질문(SQL Query)을 작성-분석함수를 사용하는 방법2
2) 대학등록금 중 최고등록금과 최저등록금의 비교

#### Exam2-3) 전국대학별등록금통계현황
▪ 해당 자료를 통해 의미 있는 질문(SQL Query)을 작성-분석함수를 사용하지 않는 방법1
2) 대학등록금 중 최고등록금과 최저등록금의 비교

#### Exam2-4) 전국대학별등록금통계현황
▪ 해당 자료를 통해 의미 있는 질문(SQL Query)을 작성-분석함수를 사용하지 않는 방법2
2) 대학등록금 중 최고등록금과 최저등록금의 비교

#### Exam1) 전국대학별등록금통계현황
▪ 분석 결과
1) 분석결과는 평균적으로 사립이 국립에 비해 220만원정도 높았고
2) 최고의 등록금과 최저등록금 거의 대략 8백만원 이상 차이를 보였다.
3) 결론은 정부에서 실행하고 있는 반값등록금이 잘 이행되는지 의문이고
4) 학자금 대출이 그만큼 많아질 거로 보인다