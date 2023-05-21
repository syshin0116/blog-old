---
title: "[ORACLE-WDP]6일차-3.데이터베이스 관리도구, 4.인스턴스관리, 5.네트워크 환경 구성, 6.유저 보안 관리"
date: 2023-05-21 20:00:00 +0900
categories: [Database,ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---


<!--#### 공유url: http://naver.me/xoKMlnp5
#### -->


# 3. 오라클 데이터베이스 관리 도구

### 3.1 목표
1. SQL*Plus를 사용하여 오라클 데이터베이스에 액세스
2. SQL Developer 를 사용하여 오라클 데이터베이스에 액세스
3. Oracle Enterprise Manager Database Express를 사용하여 관리 작업 수행

### 3.2 오라클 데이터베이스 관리 도구: 소개
1. SQL*Plus는 데이터베이스에 다음을 수행할 수 있는 인터페이스를 제공합니다.
	- 데이터베이스 관리 작업 수행
	- 데이터베이스에서 데이터를 Query, 삽입, 갱신 및 삭제하는 SQL 명령 실행
2. SQL Developer
	- 오라클 데이터베이스 Instance에 액세스하기 위한 Graphical User Interface
	- SQL 및 PL/SQL을 사용한 개발을 모두 지원
	- 기본으로 설치한 오라클 데이터베이스에서 사용 가능
3. Oracle Enterprise Manager Database Express

### 3.3 SQL*Plus 사용
SQL*Plus의 특징
	- 명령행 도구
	- 대화식 또는 일괄 처리 모드에서 사용

### 3.4 셸 스크립트에서 SQL*Plus 호출
![](https://velog.velcdn.com/images/syshin0116/post/187f0fd2-aa40-49c0-b239-17baa648ecc7/image.png)


> ### 배치파일로 실행
```shell
vi batch_sqlplus.sh
```
shell 작성
ex)
```
# update employees set salary = salary*1.10;
# Name of this file: batch_sqlplus.sh
# Count employees and give raise.
sqlplus hr/hr <<EOF
select count(*) from employees;
commit;
quit
EOF
```
실행권한 부여
```chmod 744 ./batch_sqlplus.sh``` 
실행
```./batch_sqlplus.sh```

### sqlplus로 실행
```shell
vi script.sql
```
script.sql에 sql문 작성
ex)
```
select * from departments where location_id = 1400;
quit
```
실행1
```shell
sqlplus hr/hr @script.sql
```
실행2(비번 감추는 방법)
```shell
sqlplus hr @script.sql
```

# 4. 데이터베이스 Instance 관리

### 4.1 목표
1. 오라클 데이터베이스 Instance와 구성 요소 시작 및 정지
2. 데이터베이스 초기화 파라미터 수정
3. 데이터베이스 시작 단계 설명
4. 데이터베이스 종료 옵션 설명
5. Alert Log 보기
6. Dynamic Performance 뷰 액세스

### 4.2 초기화 파라미터 파일
![](https://velog.velcdn.com/images/syshin0116/post/38a25a08-b83b-46b6-9807-449ee4f0a0d0/image.png)

1. **오라클 인스턴스 기동 시 필요한 파라미터 값을 가지고 있음**
2. 파일이 없거나 읽을 수 없는 경우 인스턴스를 시작 못함
3. 각종 **메모리 영역의 크기, 다양한 기능의 ON/OFF, 프로세스 동작 방식** 등을 변경 가능
4. 서버 파라미터 파일(SPFILE)
	- Binary File로 구성, 편집기로 편집이 불가능
	- 인스턴스 종료 및 시작 시에도 지속 유지
	- 기본 파일명 : spfile<\SID>.ora
5. 텍스트 초기화 파라미터 파일(PFILE)
    - 텍스트 기반으로 편집기로 편집이 가능
    - 인스턴스 실행 시에 파라미터가 적용되어, 새로 적용하고자 한다면 인스턴스 다시 시작 필요
    - SPFILE을 찾을 수 없는 경우 인스턴스 시작 시 자동으로 검색
    - 기본 파일명 : init<\SID>.ora
 
기본 설정 확인
```shell
env | grep ORA
```

### 4.3 초기화 파라미터 확인방법

1. SHOW PARAMETERS [검색 문자열]
2. V$PARAMETER
	- 현재 세션에 적용된 초기화 파라미터의 정보 표시
3. V$SYSTEM_PARAMETER
	- 현재 인스턴스에 적용된 초기화 파라미터의 정보 표시
4. V$SPPARAMETER
	- 서버 파라미터 파일 내용에 대한 정보 표시
![](https://velog.velcdn.com/images/syshin0116/post/ab20be65-f83c-44bc-9397-7ad62880a464/image.png)

### 4.4 초기화 파라미터 유형
![](https://velog.velcdn.com/images/syshin0116/post/85c38967-dbd4-40bf-883e-cf3a7e57a557/image.png)
> 기본, 고급 따질것 없이 다 중요한 파일들이다

### 4.5 초기화 파라미터: 예제
![](https://velog.velcdn.com/images/syshin0116/post/c0d79ca3-7191-4f13-86b3-42e4984dd05c/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/728b3b1d-20f9-4775-be03-cf43cccba8ac/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/02be0e21-dd03-4000-8ce2-1f913254fff4/image.png)

### 4.6 SQL*Plus를 사용하여 파라미터 확인

![](https://velog.velcdn.com/images/syshin0116/post/13f6c5d1-bdf8-4e9f-abd1-777b6434c5ba/image.png)
### 4.7 초기화 파라미터 값 변경
1. Static Parameter:
	- 파라미터 파일에만 변경 가능, 즉시 반영 안됨
	- Instance를 재시작해야 적용됨
2. Dynamic Parameter:
	- 데이터베이스가 온라인 상태에서 변경 가능, 즉시 반영 가능
	- 다음 레벨에서 수정 가능
		- 세션 레벨
		- 시스템 레벨
	- 세션 기간 또는 SCOPE 설정에 따른 기간 동안 유효함
	- ALTER SESSION 및 ALTER SYSTEM 명령을 사용하여 변경
    
3. 인스턴스 레벨에서의 변경
	- ALTER SYSTEM SET <파라미터명> = <설정 값>
	SCOPE = { MEMORY | SPFILE | BOTH(기본값) }
4. 세션 레벨에서의 변경
	- ALTER SESSION SET <파라미터명> = <설정 값>
	SCOPE = { MEMORY | SPFILE | BOTH(기본값) }
    
	MEMORY : 변경한 설정이 즉시 반영, 재 기동하면 초기화됨
	SPFILE : 서버 파라미터 파일에만 반영, 재 기동후에 적용됨
	BOTH : 변경 설정이 즉시 반영, 서버 파라미터 파일에도 반영
5. 기동 중일 때 변경할 수 없는 초기화 파라미터도 존재 MEMORY 혹은 BOTH로 설정할 때 유의

### 4.8 파라미터 값 변경: 예제
![](https://velog.velcdn.com/images/syshin0116/post/d63bd27f-b81a-48f8-bf6a-54790afa19dd/image.png)
> SEC_MAX_FAILED_LOGIN_ATTEMPT = 3
보안을 위해 로그인 시도 횟수 설정

### 4.9 오라클 데이터베이스 Instance 시작: NOMOUNT
![](https://velog.velcdn.com/images/syshin0116/post/5df16bf6-26a8-4d07-81ca-92a5f95b580e/image.png)

### 4.10 INSTANCE 시작할 때 SPFILE과 PFILE의 우선순위
1. $ORACLE_HOME/dbs/spfile<\SID>.ora
2. $ORACLE_HOME/dbs/spfile.ora
3. $ORACLE_HOME/dbs/init<\SID>.ora
  
  
- STARTUP에서 PFILE의 경로를 지정 하여 사용가능
	- startup pfile='/app/oracle/product/19.3/db_1/dbs/initORA19C.ora';
- SPFILE 기준으로 PFILE 생성 가능
	- SYSDBA 권한으로 접속
	- SQL> CREATE PFILE FROM SPFILE;

### 4.11 오라클 데이터베이스 Instance 시작:MOUNT
![](https://velog.velcdn.com/images/syshin0116/post/c2d68cb2-a7a9-4ab4-bbb1-7c5f20858238/image.png)

### 4.12 오라클 데이터베이스 Instance 시작: OPEN
![](https://velog.velcdn.com/images/syshin0116/post/8297113f-73b8-45a6-86c0-fa02387ea750/image.png)

### 4.13 각 단계별 장애 추측
1. 시작을 못하면
	- 서버 파라미터 문제
2. NOMOUNT 상태에서 정지
	- 컨트롤 파일 문제
3. MOUNT 상태에서 정지
	- 데이터 파일 혹은 REDO 로그 파일 문제

### 4.14 각 단계에서 가능 작업
1. NOMOUNT
	- 컨트롤 파일 재생성
2. MOUNT
	- 데이터 파일, REDO 로그 파일의 파일명/경로 변경
	- 데이터베이스 복구
	- 아카이브 모드 적용 및 해제
3. OPEN
	- 온라인 데이터 파일 확인
	- 온라인 리두 로그 파일 확인
	- 언두 세그먼트 온라인 상태로 변경
    
### 4.15 인스턴스 시작과 ALERT 로그 출력
1. ALERT 로그 위치
	```
	SELECT NAME, VALUE FROM $DIAG_INFO
	WHERE NAME IN ('Diag Alert', 'Diag Trace’);
	```
2. Alert log 실시간 모니터링
	- tail -f alert_<\SID>.log
	- tail -f alert_ORA19C.log
3. Alert log 파일 관리
	- 운영 중에 Alert log 파일을 삭제해도 무방
	- Alert log 가 입력 될 때 자동으로 파일 생성
4. Alert log 파일 찾기
	- find / -name alert_*.log 2>/dev/null
    
    
### 4.16 시작 옵션: 예제
#### SQL*Plus 유틸리티 사용:
```sql
SQL> startup				--1
SQL> alter database mount;	--2
SQL> alter database open;	--3
SQL> startup nomoun			--4
```
    
### 4.17 종료 모드
![](https://velog.velcdn.com/images/syshin0116/post/63757321-a61f-48cf-95c5-807782dc16c3/image.png)
#### 종료 모드:
- A = ABORT
- I = IMMEDIATE
- T = TRANSACTIONAL
- N = NORMAL
    
### 4.18 SHUTDOWN 명령어 사용
```SHUTDWON [ NORMAL | TRANSACTIONAL | IMMEDIATE | ABORT ]```
• NORMAL : 기본값, 접속 된 세션 종료까지 대기후 인스턴스 종료
• TRANSACTIONAL : 트랜잭션 종료까지 대기후 인스턴스 종료
• IMMEDIATE : 실행중인 트랜잭션이 있다면 **롤백**하고 인스턴스 종료
• ABORT : **전원이 꺼진 것과 같음**, 재 구동할 때 인스턴스 복구 수행
>NORMAL: 모든 접속되어있는 유저가 종료할떄까지 기다려야 한다
따라서 보통의 경우는 ```shutdown immediate;```를 사용한다

commit 되지 않은 트랜잭션은 종료 실행 전에 롤백 되지 않았음
또한 체크포인트로 더티 버퍼를 디스크에 기록하지 않았기 때문에
**내부적으로 일관성이 확보되지 않은 상태** => 인스턴스 크래쉬 발생

#### Transaction Recovery
인스턴스 크래쉬 발생 후에 Redo 파일을 이용해 Roll Forward 완료 후 시스템 장애 시점에 commit 되지 않은 트랜잭션은 모두 롤백 한다.   

>여태 shutdown immediate를 하지 않았는데 잘 작동된 이유:
인스턴스 크래쉬 발생되어도 Transaction Recovery가 실행되어 트랜잭션이 자동 롤백되고 있었다
shutdown immediate 하는 습관을 들이자..

### 4.19 종료 옵션
![](https://velog.velcdn.com/images/syshin0116/post/9d569050-0791-42fb-ad2e-58df105ad18a/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/d98c2cc6-5c16-4443-98af-3acb20b99e8d/image.png)

### 4.20 Trace File 사용
1. 각 서버 프로세스와 백그라운드 프로세스는 연관된 Trace File에 정보를 기록할 수 있습니다.
2. 오류 정보는 해당하는 Trace File에 기록됩니다.
3. ADR(Automatic Diagnostic Repository)
	- 오라클11g부터는 로그파일, 데이터베이스 상태를 확인하고 진단하는데 필요한 데이터를 ADR로 일괄 관리
	- **V$DIAG_INFO** 에서 경로 확인 가능
	- 데이터베이스 진단 데이터
		- Trace
		- Alert log
		- 상태 모니터 보고서

### 4.21 Alert Log 파일
1. 오라클 서버에 에러가 발생하거나 문제가 발생하면 제일 먼저 분석해야 하는 파일
2. 인스턴스의 시작부터 종료까지 발생한 이벤트 정보 포함(운영 정보와 에러 정보)
3. Alert Log 파일의 주요정보
	- 데이터베이스 시작 및 종료 과정 정보
	- 컨트롤 파일 변경 정보
	- 오라클 내부 에러 정보
	- 로그 스위치 정보
	- 체크포인트 정보
	- 파라미터 정보

### 4.22 DDL 로그 파일 관리
1. ENABLE_DDL_LOGGING을 TRUE로 설정하여 특정 DDL 문을 DDL 로그 파일로 캡처할 수 있습니다.
2. DDL 로그에는 각 DDL 문마다 하나씩 로그 레코드가 있습니다.
3. 두 개의 DDL 로그에 동일한 정보가 있습니다.
	- XML DDL 로그: log.xml은
	```$ORACLE_BASE/diag/rdbms/<\dbname>/<\SID>/log/ddl```에 기록됨
	- Text DDL: ddlsid.log는
	```$ORACLE_BASE/diag/rdbms/<\dbname>/<\SID>/log```에 기록됨
4. 예제:
```
$ more ddl_orcl.log
Thu Nov 15 08:35:47 2012
diag_adl:drop user app_user
```

### 4.23 디버그 로그 파일 이해
1. 디버그 로그에는 오라클 데이터베이스 구성 요소의 올바른 작동에 문제가 되지 않는 조건, 상태 또는 이벤트에 대한 경고가 있습니다.
2. 이 로그는 Oracle Support에서 문제를 진단하는 데 사용하기 위한 것입니다.
3. IPS(Incident 패키지 서비스) Incident 패키지에 포함되어 있습니다.
4. 로그는
```$ORACLE_BASE/diag/rdbms/<db_name>/<SID>/debug```에 기록됩니다.

> 오라클사에서만 알 수 있는 형식으로 되있기 때문에 오라클 support을 받을때만 활용한다고 보면 된다

### 4.24 Dynamic Performance 뷰 사용
![](https://velog.velcdn.com/images/syshin0116/post/d671cdd9-f2a1-4433-8991-2c4e7b00c628/image.png)

### 4.25 Dynamic Performance
1. 오라클의 동작 상태에 따라 내용이 **지속적으로 변하는 각종 통계 정보나 동작 상태** 확인 가능
2. 메모리 상태 및 현재 세션에 대한 정보 확인 가능
3. 성능 문제를 트러블 슈팅 하는데 있어 가장 기본적이며 유용한 스냅샷 데이터
4. 동적 성능 뷰의 종류
	- 프로세스, 세션, 메모리 영역의 상태, 대기 이벤트, 기타
5. 세션 관련 동적 성능 뷰
	- ```select * from v$session;```
	- ```select * from v$transaction;```
	- ```select * from v$process;```
	- ```select * from v$sql;```
	- ```select * from v$sql_plan;```

### 4.26 Dynamic Performance 뷰: 사용 예제
```sql
SELECT 	sql_text, executions FROM v$sql
WHERE 	cpu_time > 200000;
```
```sql
SELECT 	* FROM v$session
WHERE 	machine = 'EDXX9P1'
AND 	logon_time > SYSDATE - 1;
```
```sql
SELECT 	sid, ctime FROM v$lock
WHERE 	block > 0;
```

### 4.27 Dynamic Performance 뷰: 고려 사항

1. 이러한 뷰는 SYS 유저가 소유합니다.
2. 데이터베이스 단계에 따라 조회 가능한 뷰가 제한
	- 데이터베이스가 노 마운트 상태
	- 데이터베이스가 마운트 상태
	- 데이터베이스가 열린 경우
3. V$FIXED_TABLE을 Query하면 모든 뷰 이름을 볼 수 있습니다.
4. 이 뷰를 "v-dollar 뷰"라고도 부릅니다.
5. 데이터가 동적이기 때문에 이 뷰에서는 읽기 일관성이보장되지 않습니다.

### 4.28 Oracle 19c에 도입된 새로운 동적 성능 뷰
1. V$AQ_PARTITION_STATS
	- 큐 파티션 캐시 및 큐에서 빼기 로그 파티션 캐시에 대한 사용 통계를 표시합니다.
2. V$ASM_ACFSAUTORESIZE
	- 마운트된 각 Oracle ACFS 파일 시스템에 대한 자동 크기 조정 설정을 표시합니다.
3. V$ASM_DBCLONE_INFO
	- 상위 데이터베이스와 특정 시점 데이터베이스 클론 간의 관계를 보여줍니다.
4. V$MEMOPTIMIZE_WRITE_AREA
	- 큰 풀의 빠른 수집 데이터에 대한 정보를 표시합니다.
5. V$SQL_TESTCASES
	- SQL Test Case Builder에서 내보낸 테스트 케이스에 대한 정보를 표시

### 4.29 데이터 딕셔너리: 개요
![](https://velog.velcdn.com/images/syshin0116/post/5f8fc6b0-7c63-4b74-9f5c-3811ae2a40cc/image.png)


### 4.30 데이터 딕셔너리 뷰
#### 데이터 딕셔너리 뷰
	- **데이터베이스에 존재하는 오브젝트 및 기타 정보 확인 가능**
	- 오라클 데이터베이스 서버가 유저, 객체, 제약 조건 및 저장 영역에 대한 정보를 찾는 데 사용
	- 객체 구조나 정의가 수정될 때 오라클 데이터베이스 서버에 의해 유지 관리
	- **데이터 딕셔너리는 SYS 계정이 소유**
	- **SYSTEM 테이블 스페이스에 저장되어 있어서 데이터베이스 오픈상태에서 조회 가능**
#### 데이터 딕셔너리 뷰의 종류
	- 오브젝트 관련
	- 유저 및 권한 관련
	- 스토리지 관련
	- 기타

![](https://velog.velcdn.com/images/syshin0116/post/f2280b3c-a216-4597-bafe-cb36d89a0f5f/image.png)

1. DBA_
	- 데이터베이스 관리자만 접근 가능한 객체 등의 정보를 조회
	- Ex) ```select owner, table_name from dba_tables;```
2. ALL_
	- 자신의 계정 소유 또는 권한을 부여 받은 객체 등에 관한 정보를 조회
	- Ex) ```select owner, table_name from all_tables;```
3. USER_
    - 자신의 계정이 소유한 객체 등에 관한 정보를 조회
    - Ex) ```select table_name from user_tables;```
    
### 4.31 데이터 딕셔너리: 사용 예제
```sql
--1
SELECT table_name, tablespace_name
FROM user_tables;

--2
SELECT sequence_name, min_value, max_value,
increment_by
FROM all_sequences
WHERE sequence_owner IN ('MDSYS','XDB');

--3
SELECT USERNAME, ACCOUNT_STATUS
FROM dba_users
WHERE ACCOUNT_STATUS = 'OPEN';

--4
DESCRIBE dba_indexes
```

### 4.32 요약
1. 오라클 데이터베이스 Instance와 구성 요소 시작 및 정지
2. 데이터베이스 초기화 파라미터 수정
3. 데이터베이스 시작 단계 설명
4. 데이터베이스 종료 옵션 설명
5. Alert Log 보기
6. Dynamic Performance 뷰 액세스


# 4장 실습:
## 다운로드 파일:
[04.01.파라미터 기본 정보 알아보기.pdf](https://github.com/syshin0116/Study/files/11524002/04.01.pdf)
[04.02.파라미터값 확인 및 변경(SPFILE 환경).pdf](https://github.com/syshin0116/Study/files/11524003/04.02.SPFILE.pdf)
[04.03.파라미터 파일 백업 및 SPFILE, PFILE 생성.pdf](https://github.com/syshin0116/Study/files/11524004/04.03.SPFILE.PFILE.pdf)
[04.04.오라클 시작(startup) 실습.pdf](https://github.com/syshin0116/Study/files/11524005/04.04.startup.pdf)
[04.05.오라클 종료(shutdwon) 실습.pdf](https://github.com/syshin0116/Study/files/11524006/04.05.shutdwon.pdf)
[04.06.ALERT 로그 모니터링.pdf](https://github.com/syshin0116/Study/files/11524007/04.06.ALERT.pdf)
[04.07.PGA 자동관리 설정.pdf](https://github.com/syshin0116/Study/files/11524008/04.07.PGA.pdf)
[04.08.ASMM 실습.pdf](https://github.com/syshin0116/Study/files/11524009/04.08.ASMM.pdf)



## 4.1 파라미터 기본 정보 알아보기

### 실습 : 파라미터 파일 관련 정보를 확인하고 설정된 파라미터 값들을 확인한다.
1. 파라미터 파일이 위치한 디렉토리를 확인하고 숙지한다.
2. 정적, 동적 파라미터 파일을 열어보고 차이를 확인한다.
3. 현재 사용중인 파라미터 파일을 확인한다.
3.1 PFILE을 이용하여 오라클을 기동하고 사용중인 파라미터 파일을 확인한다.
4. 설정된 파라미터 값들을 조회해본다.

#### 명령어
```sql
# 파라미터 값 확인하기
SHOW PARAMETER <파라미터명>
SHOW PARAMETER <파라미터명의 일부문자열>
# 명시적으로 PFILE을 지정하여 구동
startup pfile = 'PFILE 경로/ init<\SID>.ora
```
#### 파라미터 파일 기본 위치
유닉스/리눅스 : $ORACLE_HOME/dbs
윈도우 : $ORACLE_HOME/database
#### 파라미터 파일명의 규칙
PFILE: init<\SID>.ora
SPFILE : spfile<\SID>.ora
SID는 데이터베이스 생성시 설정한 인스턴스 이름을 의미한다.
#### 파라미터 파일 편집 시 주의사항
PFILE은 텍스트 형식이기 때문에 편집기로 수정 가능하나
**SPFILE은 바이너리 형식이기 때문에 편집기로 수정하면 사용할 수 없다**.
SPFILE은 PFILE로 변경 후 수정하거나 아래와 같은 SQL 명령어로 수정해야 한다.
```ALTER SYSTEM SET <파라미터명> = <값> SCOPE = [SPFILE | MEMORY | BOTH];```

#### 1. SPFILE을 통해서 PFILE을 생성한다.
오라클 설치후에는 initORA19C.ora 파일이 없어서 정적 파라미터 파일을 생성한다.
SYS 계정 SQL Developer에서 실행한다.
SQL> create pfile from spfile;
#### 2. 파라미터 파일이 위치한 디렉토리를 확인하고 숙지한다.

```shell
[/home/oracle]$ echo $ORACLE_HOME
/app/oracle/product/19.3/db_1

[/home/oracle]$ cd $ORACLE_HOME/dbs

[/app/oracle/product/19.3/db_1/dbs]$ pwd
/app/oracle/product/19.3/db_1/dbs
# init<\SID>.ora, spfile<\SID>.ora 형식으로 파일명이 형성된 것을 확인 할 수 있다.
[/app/oracle/product/19.3/db_1/dbs]$ ls -l
-rw-r-----. 1 oracle dba 1098 Mar 10 20:59 initORA19C.ora
-rw-r-----. 1 oracle dba 2560 Mar 17 20:35 orapwORA19C
-rw-r-----. 1 oracle dba 3584 Mar 17 21:38 spfileORA19C.ora
```
#### 3. 정적, 동적 파라미터 파일을 열어보고 차이를 확인한다.
```shell
# 정적 파라미터 파일 확인, 텍스트 형식
[/app/oracle/product/19.3/db_1/dbs]$ vi initORA19C.ora
ORA19C.__data_transfer_cache_size=0
ORA19C.__db_cache_size=1241513984
ORA19C.__oracle_base='/app/oracle'#ORACLE_BASE set from environment
…
# spfile은 바이너리 파일이기 때문에 절대로 편집하면 안된다. 오라클 작동이 안 될 수도 있다.
# view 는 읽기모드로 파일을 오픈하는 명령어이다.
[/app/oracle/product/19.3/db_1/dbs]$ view spfileORA19C.ora
C"^@^@^A^@^@^@^@^@^@^@^@^@^A^D<97>,^@^@^@^@^@^@^@^@^@^@^
@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^G^@^@^@^@^B^@^@^@^@^@
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@.
...
```
#### 4. 현재 사용중인 파라미터 파일을 확인한다.
SYS 계정 SQL Developer에서 실행한다.
```sql
# 현재 사용중인 파라미터 파일은 spfile임을 확인 할 수 있다.
SQL> show parameter spfile;
SQL> select name, value
from v$parameter
where name = 'spfile';
NAME VALUE
------- -----------------------------------------------------------
spfile /app/oracle/product/19.3/db_1/dbs/spfileORA19C.ora
```
#### 4.1 pfile을 이용하여 오라클을 기동하고 사용중인 파라미터 파일을 확인한다.
```sql
# 오라클을 종료하고 정적 파라미터 파일을 이용하여 startup 한다.
SQL> shutdown immediate;
SQL> startup pfile='/app/oracle/product/19.3/db_1/dbs/initORA19C.ora';
# 현재 사용중인 파라미터 파일이 pfile인 경우 value값이 없다.
SQL> select name
 , value
from v$parameter
where name = 'spfile';
# pfile을 사용하고 있는 경우에는 value 값이 없다.
NAME VALUE
------- -------------------------------------------------
spfile
```
#### 5. 설정된 파라미터 값들을 확인한다.
```shell
  
# v$parameter 에서 조회된 값은 현재 DB에 설정된 파라미터 값
SQL>select name, value from v$parameter;
# v$spparameter 에서 조회된 값은 SPFILE에 저장된 값
SQL>select name, value from v$spparameter;
show parameter spfile;
show parameter service_names;
show parameter instance_name;
show parameter listener;
show parameter block;
show parameter pga;
show parameter sga;
show parameter remote_login_passwordfile
show parameter control_files;
show parameter cache;
show parameter session;
show parameter undo;
show parameter sga_max_size;
show parameter pga_aggregate_limit;
show parameter pga_aggregate_target
show parameter workarea_size_policy;
```

# 5. Oracle 네티워크 환경 구성

## 목표
이 단원을 마치면 다음을 수행할 수 있습니다.
- Oracle Net Manager를 사용하여 다음 작업 수행
	– 추가 리스너 생성
	– Oracle Net 서비스 alias 생성
	– Oracle Net 리스너 제어
- Listener Control 유틸리티를 사용하여 Oracle Net 리스너 관리
- tnsping을 사용하여 Oracle Net 연결 테스트
- Shared Server를 사용하는 경우와 Dedicated Server를사용하는 경우 확인

> ### Shared Server, Dedicated Server차이
#### Shared Server:
- 멀티프로세스 아키텍처로, 한정된 수의 서버 프로세스가 여러 클라이언트 연결을 처리합니다.
서버 프로세스는 클라이언트 요청을 처리한 후에 다음 클라이언트에게 할당됩니다.
- 클라이언트는 연결을 유지하고 있지 않고, 요청할 때마다 서버 프로세스에 연결하여 작업을 처리합니다.
- 많은 클라이언트가 동시에 작업을 수행하는 경우 자원 공유를 통해 시스템 자원의 효율성을 높일 수 있습니다.
- 메모리 사용량이 적을 수 있어, 대규모 연결 수를 지원하는데 유리합니다.
#### Dedicated Server:
- 단일 프로세스 아키텍처로, 각 클라이언트 연결에 대해 별도의 서버 프로세스가 할당됩니다.
각 클라이언트는 독립적으로 서버 프로세스와 연결되어 작업을 처리합니다.
- 클라이언트 연결이 유지되므로, 서버 프로세스는 해당 클라이언트와의 상태를 유지하고, 메모리 및 세션 상태 등을 유지합니다.
- 각 클라이언트에게 더 많은 시스템 자원을 할당할 수 있으며, 개별 클라이언트에 대한 성능과 격리를 보장합니다.
- 메모리 사용량이 증가하고, 대규모 연결 수에 대한 자원 관리에 도전할 수 있습니다.

### 5.1 Oracle Net 서비스:개요
- Oracle Net Services란 오라클을 네트워크 환경에서 사용하는 데 필요한 구성품(제품군)을 부르는 총괄적인 용어
	- Oracle Net
	- Oracle Net Listener
	- Net Configuration Assistant(NetCA)
	- Net Manager
![](https://velog.velcdn.com/images/syshin0116/post/3a9f304d-d4d9-4cd2-a518-e103e065f109/image.png)
>#### /app/oracle/product/19.3/db_1/network/admin
1. listener.ora, tnsnames.ora
	- listener: server
	- tnsname: client
	- CONET_DATA = (SERVER = DEDICATED)외에 PROTOCAL, HOST, PORT 등의 정보가 담겨있음
2. sqlnet.ora
	- NAMES.DIRECTORY_PATH= (TNSNAMES, **EZCONNECT**) 
    
### 5.2 Oracle Net 리스너: 개요
![](https://velog.velcdn.com/images/syshin0116/post/efcbcfed-d0f8-46f9-ae86-9109dc5133b5/image.png)

### 5.3 오라클 네트워크 연결 설정
Oracle Net에서 클라이언트 또는 Middle-tier 연결을 설정하려면 클라이언트는 다음 사항을 알아야 합니다.
- 리스너가 실행 중인 **IP(호스트)**
- 리스너가 모니터 중인 **포트**
- 리스너가 사용 중인 **프로토콜**
- 리스너가 처리 중인 **서비스 이름**

### 5.4 이름 분석(Names Resolution)
![](https://velog.velcdn.com/images/syshin0116/post/157cb9e0-0e0e-4f82-ac40-c854270c52c2/image.png)

### 5.5 연결 설정 (순서)
1. 리스너는 CONNECT 패킷을 수신한 다음 이 CONNECT 패킷이 적합한 Oracle Net 서비스 이름을 요청하고 있는지 검사
	1.1 부적합한 서비스 이름을 요청한 경우 리스너는 User Process에 오류 코드를 전송합니다
2. CONNECT 패킷이 적합한 서비스 이름을 요청한 경우 연결을 처리할 서버 프로세스를 생성
3. 리스너는 User Process의 주소 정보를 포함하여 초기화 정보를 서버 프로세스에게 전달
4. 서버 프로세스는 유저 인증(암호) 확인 및 유저 세션 생성

### 5.5 이름 지정 방식
Oracle Net는 여러 가지 연결 정보 분석 방법을 지원합니다.
- 간단한 연결(**Easy Connect**) 이름 지정: TCP/IP 연결 문자열 사용
- 로컬 이름 지정: **로컬 구성 파일 사용(tnsnames.ora)**
- 디렉토리 이름 지정: 중앙화된 LDAP규격 디렉토리 서버 사용
- 외부 이름 지정: 지원되는 비오라클 이름 지정 서비스 사용

>sqlnet.ora에 있던 ```NAMES.DIRECTORY_PATH= (TNSNAMES, **EZCONNECT**)```
Easy Connect문자열로 쭉 나열해서 사용한다 
ex) sqlplus hr/hr@10.0.2.15:1521/ORA19c

### 5.6 간단한 연결(Easy Connect)
1. 기본적으로 활성화됨
2. 클라이언트측 구성이 필요 없음
3. TCP/IP만 지원(SSL은 지원하지 않음)
4. 다음과 같은 고급 연결 옵션은 지원하지 않음
	- Connect-time failover
	- 소스 경로 지정
	- 로드 밸런싱
```SQL> CONNECT hr/hr@db.us.oracle.com:1521/dba11g```

### 5.7 로컬 이름 지정
1. 클라이언트측 이름 분석(Names Resolution) 파일 필요
	- $ORACLE_HOME/network/admin/**tnsnames.ora**
	- **TNS_ADMIN 환경변수**를 사용하여 어느 곳 에든 배치 가능
2. 모든 Oracle Net 프로토콜 지원
3. 다음과 같은 고급 연결 옵션 지원
	- Connect-time failover
	- 소스 경로 지정
	- 로드 밸런싱
>TNS_ADMIN 환경변수 
```env | grep TNS```
```TNS_ADMIN=/app/oracle/product/19.3/db_1/network/admin```
```vi ./.bash_profile```
![](https://velog.velcdn.com/images/syshin0116/post/d9251195-6ac2-497b-8ce1-59a61b712faf/image.png)

### 5.8 Oracle Net 서비스 구성 및 관리 도구

1. Enterprise Manager Net Services Administration 페이지
2. Oracle Net Manager
	- **netmgr**
3. Oracle Net Configuration Assistant
	- **netca**
4. Listener Control 유틸리티
	- **lsnrctl**
>이런 GUI툴이 있다고만 알아 두고 실제로는 cli로 많이 쓴다

### 5.9 Oracle Net 서비스 구성 요소 정의
![](https://velog.velcdn.com/images/syshin0116/post/2c5b426c-5892-497a-ba94-b3c69df7b86e/image.png)

### 5.10 Oracle Net Manager 사용(netmgr)
![](https://velog.velcdn.com/images/syshin0116/post/d4739dd6-7079-470f-b036-92dce773fca8/image.png)

### 5.11 Oracle Net Configuration Assistant 사용(netca)
![](https://velog.velcdn.com/images/syshin0116/post/276a39d3-3348-4bcb-8a7d-b15f2ca0f940/image.png)
>최초 설치때 이미 했음

### 5.12 Listener Control 유틸리티 사용
![](https://velog.velcdn.com/images/syshin0116/post/ff1dbad7-b077-45b2-a7e7-e08f0fe7d8a7/image.png)

### 5.13 Listener Control 유틸리티 구문
Listener Control 유틸리티 명령은 명령행이나 lsnrctl 프롬프트에서 실행할 수 있습니다.
- 명령행 구문:
  ```shell
  $ lsnrctl <command name>
  $ lsnrctl start
  $ lsnrctl status
  ```

- 프롬프트 구문
	```shell
    LSNRCTL> <command name>
	LSNRCTL> start
	LSNRCTL> status
    ```

### 5.14 고급 연결 옵션
1. Oracle Net는 로컬 및 디렉토리 이름 지정과 함께 다음 고급 연결 옵션을 지원합니다.
2. Connect-time failover
	- 클라이언트가 host1로 접속을 시도할 때 허용하는 시간을 초과하여 실패한 경우 다른 host2로 접속 시도
	- 서비스를 지속하기 위하여 사용(고가용성)
3. 로드 밸런싱(LOAD_BALANCE)
	- 여러 개의 host가 있을 경우 각 host의 부하 분산 유무를 결정
4. 소스 경로 지정(SOURCE_ROUTE)
	- 라우터가 지정해주는 경로를 사용하지 않고 목적지까지의 경로를 직접 설정

>

### 5.15 Oracle Net 연결 테스트
Oracle Net 서비스 **Alias를 테스트하는 tnsping 유틸리티**:
- 클라이언트와 Oracle Net 리스너 간 연결 확인
- 요청된 서비스가 사용 가능한지 확인하지 않음
- 간단한 연결 이름 분석(Easy Connect Names Resolution) 지원
```tnsping host01.example.com:1521/orcl```
- 로컬 및 디렉토리 이름 지정 지원
```tnsping orcl```
>![](https://velog.velcdn.com/images/syshin0116/post/e91b872d-cbed-4930-87c1-9ab3f94d8f2f/image.png)


### 5.16 리스너의 동적 서비스 등록
1. 인스턴스의 정보를 LREG가 동적으로 등록
2. 리스너 시작 후 인스턴스 시작하면 바로 접속 가능
3. 인스턴스 시작한 뒤 리스너를 시작하면 약 1분내외의 시간소요
	- 수동 등록 : ALTER SYSTEM REGISTER
4. 동적 서비스 등록을 수행하는 리스너 설정
	- show parameter local_listener
	- LREG 백그라운드 프로세스가 LOCAL_LISTENER 파라미터 읽어서 동적으로 LISTENER에게 인스턴스 정보를 등록
```
# listener.ora
LISTENER =
(DESCRIPTION =
(ADDRESS = (PROTOCOL = TCP)(HOST = HORA19C)(PORT = 1521))
)
```

### 5.17 리스너의 정적 서비스 등록
- listener.ora 파일에 오라클 서버를 직접 등록하는 것
	- SID_LIST_리스너명을 작성하면 정적 등록 방식으로 작동

```
LISTENER =
(DESCRIPTION =
(ADDRESS = (PROTOCOL = TCP)(HOST = HORA19C)(PORT = 1521))
)
SID_LIST_LISTENER =
(SID_LIST =
(SID_DESC =
(SID_NAME = ORA19C)
(ORACLE_HOME = /app/oracle/product/19.3/db_1)
)
)
```

### 5.18 동적/정적 서비스 확인방법
- lsnrctl services
- 동적 서비스일때의 리스너 상태
```
Services Summary...
Service "ORA19C" has 1 instance(s).
Instance "ORA19C", status READY, has 1 handler(s) for this service...
Handler(s):
```
- 정적 서비스일때의 리스너 상태
```
Services Summary...
Service "ORA19C" has 1 instance(s).
Instance "ORA19C", status UNKNOWN, has 1 handler(s) for this
service...
Handler(s)
```

### 5.19 Dedicated Server와 Shared Server 구성 비교
• Dedicated Server 구성: 클라이언트마다 하나의 서버 프로세스(1:1)
• Shared Server 구성: 적은 서버 프로세스 풀을 많은 수의 클라이언트에 사용 가능

### 5.20 유저 세션: Dedicated Server 프로세스
![](https://velog.velcdn.com/images/syshin0116/post/cb6041dd-0a33-4bda-a3d4-b6fddb1f2d96/image.png)

### 5.21 유저 세션: Shared Server 프로세스
![](https://velog.velcdn.com/images/syshin0116/post/e78d7005-1d95-4e26-95f3-6894481b87dc/image.png)

### 5.22 SGA 및 PGA 사용
Oracle Shared Server: UGA(User Global Area)가 SGA에 저장
![](https://velog.velcdn.com/images/syshin0116/post/212c88e2-cf58-400f-bd5f-927a203bea3e/image.png)

- SGA의 크기 조정 시 Shared Server 메모리 요구 사항을 고려
- UGA는 SGA의 Large Pool, Shared Pool 순으로 존재하는 영역부터 우선적으로 자리를 차지하게 됨
- Oracle 19c에서는 스택 공간, 해시영역, 비트맵 병합영역은 PGA에 남음

### 5.23 PGA(Program Global Area)
![](https://velog.velcdn.com/images/syshin0116/post/466c1de7-fe02-4cc9-8977-992cf5503d92/image.png)

### 5.24 Shared Server 구성 고려 사항
다음은 Shared Server를 사용하여 수행하지 않아야 하는 특정 데이터베이스 작업 유형입니다.
  - 데이터베이스 관리
  - 백업 및 recovery 작업
  - 일괄 처리 및 대량 로드 작업
  - 데이터 웨어하우스 작업

### 5.25 Database link
- 여러 데이터베이스가 존재하는 **분산 데이터베이스환경**에서 사용되는 데이터 통합을 위한 기능
- 데이터베이스 링크를 사용하면 분산되어 있는 데이터를 **하나의** 데이터베이스에 있는 것처럼 처리
- 사이트 간에 데이터나 메시지를 보내려면 두 사이트 모두에 네트워크를 구성 필요
- 다음을 구성해야 합니다.
	- 네트워크 연결(예: tnsnames.ora)
	- **데이터베이스 링크**
```
CREATE [PUBLIC] DATABASE LINK <remote_global_name>
CONNECT TO <user> IDENTIFIED BY <pwd>
USING '<connect_string_for_remote_db>';
```

# 5장 실습:
## 파일 다운:
[[보조자료] 5장 데이터베이스 링크 예제.txt](https://github.com/syshin0116/Study/files/11523993/5.txt)
[05.01.리눅스 환경에서 오라클 클라이언트 설정.pdf](https://github.com/syshin0116/Study/files/11523994/05.01.pdf)
[05.02.윈도우환경에서 오라클 클라이언트 설정.pdf](https://github.com/syshin0116/Study/files/11523995/05.02.pdf)
[05.03.오라클 리스너 구동.pdf](https://github.com/syshin0116/Study/files/11523996/05.03.pdf)
[05.04.오라클 리스너 추가(정적등록).pdf](https://github.com/syshin0116/Study/files/11523997/05.04.pdf)
[05.05.오라클 서버 리스너 포트 변경(동적등록).pdf](https://github.com/syshin0116/Study/files/11523998/05.05.pdf)
[05.06.Shared Server 설정 및 구동.pdf](https://github.com/syshin0116/Study/files/11523999/05.06.Shared.Server.pdf)
[LISTENER2.txt](https://github.com/syshin0116/Study/files/11524000/LISTENER2.txt)


# 6. 유저 보안 관리(Administering User Security)

### 6.1 목표
1. 데이터베이스 유저 계정 생성 및 관리:
	- 유저 인증
	- 기본 저장 영역(테이블스페이스) 할당
2. 권한 부여 및 취소
3. 롤(role) 생성 및 관리
4. 프로파일 생성 및 관리:
	- 표준 암호 보안 기능 구현
	- 유저별 리소스 사용량 제어

### 6.2 데이터베이스 유저 계정

각 데이터베이스 유저 계정에는 다음이 포함되어 있습니다.
1. 고유 Username
2. 계정 상태(open/lock/unlock/expired등)
3. 인증 방식
4. 기본 테이블스페이스
5. 임시 테이블스페이스
6. 유저 프로파일(패스워드/자원제한)
7. 초기 Consumer Group

**스키마**
1. 데이터베이스 유저가 소유하는 데이터베이스 객체의 모음
2. 유저 계정과 동일한 이름

### 6.3 미리 정의된 관리 계정
1. SYS:
	- 데이터 딕셔너리 및 AWR(Automatic Workload Repository) 소유
	- 데이터베이스 Instance 시작 및 종료에 사용
2. SYSTEM: 추가 관리 테이블 및 뷰 소유
3. SYSBACKUP: Oracle RMAN(Recovery Manager) 백업 및 Recovery 작업 지원
	- 데이터베이스를 백업 및 복구하는 유틸리티
4. SYSDG: Oracle Data Guard 작업 지원
	- 장애가 발생 했을 때 가용성 유지
5. SYSKM: Transparent Data Encryption 전자 지갑(wallet) 작업 지원
	- TDE: 응용 프로그램의 수정 없이 DB 내부에서 컬럼, 테이블 스페이스 레벨의 암호화

### 6.4 관리 권한
![](https://velog.velcdn.com/images/syshin0116/post/f256d046-73b9-41a5-93ef-b2a4ff20da6d/image.png)

### 6.5 권한이 부여된 계정 보호
권한이 부여된 계정을 보호하는 방법:
1. 대소문자를 구분하는 암호로 이루어진 Password file 사용
	- 패스워드 파일 위치 : $ORACLE_HOME/dbs/orapw<\SID>
	- Password file의 목적
	- 원격 연결 시 권한 있는 유저를 인증하기 위함
	- 로컬은 사용되지 않음
2 패스워드 인증 방식으로 접속 가능한 계정 확인
  ```SQL> select * from $pwfile_users;```
3 관리자 롤(role)에 강력한 인증 활성화

### 6.6 유저 인증
- 암호: 유저가 데이터베이스에 로그인할 때 입력해야 하는 암호가 유저 정의에 포함됩니다.
- External: 데이터베이스 **외부의 방식으로 인증**
	(운영 체제, Kerberos, Radius)
- Global: **LDAP** 기반 디렉토리 서비스를 사용하여 **유저 인증**

### 6.7 관리자 인증
#### 운영 체제 보안:
1. DBA는 파일을 생성하고 삭제하는 OS 권한 소유
	- 데이터 파일을 생성하고 이동 등의 작업을 위해
2. 일반 유저는 데이터베이스 파일을 생성하고 삭제하는 OS 권한을 가질 수 없습니다.
	- 일반적으로 접속해서 트랜잭션을 일으키는 업무만 수행
#### 관리자 보안:
1. SYSDBA 및 SYSOPER 연결:
	- Password file 및 강력한 인증 방식에서는 DBA 유저 이름에 대한 **감사(audit) 수행**
	- OS 인증에서는 OS 계정 이름에 대한 **감사(audit)** 수행
	- 권한 있는 유저에 대해 **OS 인증**이 Password file 인증보다 우선적으로 실시(OS안에 오라클이 탑재, OS가 먼저임)
	- Password file은 **대소문자를 구분**하는 암호 사용
    
### 6.8 OS 인증과 OS 그룹
![](https://velog.velcdn.com/images/syshin0116/post/68c82f34-62ac-4f23-a9df-f011edcfdc6f/image.png)
위와 같이 dba로 설정하면 운영체제 유저 중 dba 그룹에 속하는
유저만이 해당 데이터베이스에서 dba 권한을 행사 할 수 있음
oracle 계정이 dba 그룹에 소속되어서 dba 권한을 가지고
오라클 데이터베이스를 생성했다.

### 6.9 권한
다음과 같은 두 가지 유형의 유저 권한이 있습니다.
	- 시스템 권한: 유저가 데이터베이스에서 특정 작업을 수행할 수 있도록 합니다.
	- 객체 권한: 유저가 특정 객체를 액세스 및 조작할 수 있습니다.
    
### 6.10 SQL Developer 사용자 관리
![](https://velog.velcdn.com/images/syshin0116/post/86de8c14-f56a-4756-81a9-f4fe84d623d5/image.png)

### 6.11 DBA 권한으로 접속: 
#### 메뉴 > 보기 > DBA
![](https://velog.velcdn.com/images/syshin0116/post/e45416d8-35e8-48f9-9759-70ff0fb00e38/image.png)

### 6.12 유저 생성

#### 보안 > 사용자 > 우 클릭 > 새로 만들기
![](https://velog.velcdn.com/images/syshin0116/post/49abe793-5e9c-4fa4-88d3-5d9a8526ce29/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/0b7a66b8-2b1d-4634-9769-b2ef208bf4e1/image.png)
> 주의사항: 사용자 이름은 **대문자**로 입력!!

#### 유저에게 롤 부여
![](https://velog.velcdn.com/images/syshin0116/post/5e3154f4-6924-4a33-b924-16c6317fb948/image.png)

#### 시스템권한 부여
![](https://velog.velcdn.com/images/syshin0116/post/59a8357d-a573-439b-b4ba-16b247acb802/image.png)

#### 테이블스페이스의 할당 제한(쿼터)
![](https://velog.velcdn.com/images/syshin0116/post/e9c05a6c-2892-4940-ac23-889458983232/image.png)

### 6.13 유저 생성 - SQL
![](https://velog.velcdn.com/images/syshin0116/post/0dc9c27b-e721-4713-b8b4-2a5032c8f110/image.png)

#### 접속 테스트
![](https://velog.velcdn.com/images/syshin0116/post/e4ee67b3-41c3-49f9-91d7-b92a75d05e59/image.png)

### 6.14 사용자 필터링
![](https://velog.velcdn.com/images/syshin0116/post/b03e5542-b46f-431a-8579-5a6dca3462a4/image.png)

### 6.15 사용자 편집
![](https://velog.velcdn.com/images/syshin0116/post/0b40e24c-fed3-46a2-8113-931cf290eee6/image.png)

#### 각 탭의 항목 재설정 가능
![](https://velog.velcdn.com/images/syshin0116/post/29200d6d-b18f-400f-beca-121e6e7c554e/image.png)

#### 적용 되는 SQL
![](https://velog.velcdn.com/images/syshin0116/post/2c349063-d683-4cf6-babf-8eeb6f27ef0c/image.png)

### 6.16 사용자 삭제
![](https://velog.velcdn.com/images/syshin0116/post/42c4ca16-dc4e-483e-88e5-f6b91d287d68/image.png)

### 6.17 비밀번호 만료
![](https://velog.velcdn.com/images/syshin0116/post/3f67a475-ca26-4fd5-a55e-f5e2f1605510/image.png)

### 6.18 사용자 잠금
![](https://velog.velcdn.com/images/syshin0116/post/346faeff-adb0-4615-91f1-67321c6f0dbc/image.png)

### 6.19 사용자 잠금 해제
![](https://velog.velcdn.com/images/syshin0116/post/584e3689-d325-45f9-b7ac-1eaccb0e183a/image.png)

### 6.20 롤 부여
![](https://velog.velcdn.com/images/syshin0116/post/2310c375-e5fd-40c9-9331-e042418924b5/image.png)

### 6.21 시스템 권한 부여

![](https://velog.velcdn.com/images/syshin0116/post/df4191bc-6293-4948-828a-30c8edd1f8d5/image.png)

### 6.22 객체 권한 부여
#### 접속 > HR > 테이블 > EMPLOYEES > 우 클릭 > 권한 > 권한부여
![](https://velog.velcdn.com/images/syshin0116/post/a2b3666e-26eb-4001-b665-2f2230eb7cd3/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/7d91a7b0-6635-4975-9886-a979107f1e68/image.png)

### 6.23 객체 권한 취소
#### 접속 > HR > 테이블 > EMPLOYEES > 우 클릭 > 권한 > 권한취소
![](https://velog.velcdn.com/images/syshin0116/post/5f727855-2127-4c1a-b9b2-3dcd256a1712/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/5405079f-775f-482d-b5e4-c643f70aff2b/image.png)

### 6.24 ADMIN OPTION을 사용하여 시스템 권한 취소(독립적)
![](https://velog.velcdn.com/images/syshin0116/post/b5b562fa-b48e-4c1b-bc26-13cab4b73df7/image.png)

### 6.25 GRANT OPTION을 사용하여 객체 권한 취소(연쇄적취소)
![](https://velog.velcdn.com/images/syshin0116/post/587acd63-4924-4b81-bd0c-9b112bd45f46/image.png)

### 6.26 롤(role)을 사용하여 권한 관리
1. 롤:
	- 시스템/오브젝트 권한과 롤을 그룹화하는 데 사용
	- 유저에게 여러 권한 또는 롤 부여 가능
2. 롤 사용 시의 이점:
	- 권한 관리 용이성
	- 동적 권한 관리
	- 권한의 선택적 가용성
    
### 6.27 롤(role)에 권한 할당 및 유저에게 롤(role) 할당
![](https://velog.velcdn.com/images/syshin0116/post/6de1213c-b50a-4429-9497-9a9834678c2f/image.png)


### 6.28 롤 생성
#### DBA > 보안 > 롤 > 우 클릭 > 새로 만들기
![](https://velog.velcdn.com/images/syshin0116/post/e8a702a8-f3ac-46aa-b654-faca38c67458/image.png)

    
> 롤 이름은 항상 대문자로!!소문자로 하면 만들 수는 있지만 사용이 불가하여 결국엔 지워야 한다

#### 롤을 롤에게 부여
![](https://velog.velcdn.com/images/syshin0116/post/65c7ce58-0536-445a-9362-eb004e2e1355/image.png)

#### 시스템 권한 부여
![](https://velog.velcdn.com/images/syshin0116/post/251fc299-5685-4c87-b0f4-07b2ece2131e/image.png)

#### 적용되는 SQL
```sql
--ROLE SQL
CREATE ROLE "BASIC_ROLE";

--ROLES
GRANT "RESOURCE" TO "BASIC_ROLE";

--SYSTEM PRIVILEGES
GRANT CREATE SESSION TO "BASIC_ROLE";
GRANT CREATE TABLE TO "BASIC_ROLE";
```

### 6.29 롤 삭제
#### DBA > 보안 > 롤 > 우 클릭 > 롤 삭제
![](https://velog.velcdn.com/images/syshin0116/post/762067a7-3d26-4809-b22a-c691417d3b07/image.png)

### 6.30 미리 정의된 롤(role)
![](https://velog.velcdn.com/images/syshin0116/post/752d1506-43e6-4ea4-96e2-0719adf318b4/image.png)

### 6.31 보안 롤(role)
1. 롤은 비활성화 할 수 있고 필요할 때 활성화할 수 있습니다.
```SET ROLE {vacationdba | all | none};```
2. 롤은 인증을 통해 보호할 수 있습니다.
3. pl/sql로 만든 프로그램을 이용한 롤 사용 가능
```
CREATE ROLE secure_application_role
IDENTIFIED USING <security_procedure_name>;
```

### 6.32 권한 분석
- 미사용 권한을 취소하기 위해 사용된 권한을 분석합니다.
- DBMS_PRIVILEGE_CAPTURE 패키지를 사용합니다.
![](https://velog.velcdn.com/images/syshin0116/post/09f0cd75-cb45-408e-8602-49824b285f5d/image.png)


### 6.33 권한 분석 흐름
![](https://velog.velcdn.com/images/syshin0116/post/64316894-68a2-46b4-853d-56c478351653/image.png)

### 6.34 프로파일 및 유저
![](https://velog.velcdn.com/images/syshin0116/post/cecfc247-26c0-422d-8546-6bc6ef09c70d/image.png)

> 주의: RESOURCE_LIMIT가 TRUE로 설정되어야 프로파일에서 리소스 제한을
적용할 수 있다

### 6.35 프로파일 
#### 패스워드 정책

1. FAILED_LOGIN_ATTEMPTS
- 로그인 실패 가능 횟수
2. PASSWORD_LOCK_TIME
- 로그인 가능 시도 횟수 초과 시 잠기는 일수
3. PASSWORD_LIFE_TIME
- 암호의 만료 기간을 일 수로 설정
4. PASSWORD_GRACE_TIME
- 만료 후 설정한 값 동안 경고 메시지 발생(유예기간, 단위:일)
5. PASSWORD_REUSE_TIME
- 설정된 기간에는 동일 암호 사용불가 (단위:일)
6. PASSWORD_REUSE_MAX
- 이전 암호가 재사용 가능한 최대 횟수
7. PASSWORD_VERIFY_FUNCTION
- 암호를 할당하기 전 복잡성 검사 함수
8. INACTIVE_ACCOUNT_TIME
- 지정된 일 수 후에 계정을 자동으로 잠금

#### 리소스 제한
1. SESSIONS_PER_USER
- 동시에 접속 가능한 사용자수 설정
2. CPU_PER_SESSION
- 한 세션에서 사용 가능한 CPU 시간(단위:1/100초)
3. CPU_PER_CALL
- 한 문장에서 사용 가능한 CPU 시간(단위:1/100초)
4. LOGICAL_READS_PER_SESSION
- 한 세션에서 논리적 읽기 가능한 블록 수
5. LOGICAL_READS_PER_CALL
- 한 문장에서 논리적 읽기 가능한 블록 수
6. IDLE_TIME
- 일정 시간동안 아무런 작업이 없을 때 세션을 종료 (단위:분)
7. CONNECT_TIME
- 접속 유효시간(단위:분)
8. PRIVATE_SGA
- shared server에서 해당 세션에서 사용 가능 SGA 사용량 설정
9. COMPOSITE_LIMIT
- connect_time, private_sga, cpu_per_session, read_per_session 등과 같은 값을 통합해서 제한


#### DBA > 프로파일 > 우 클릭 > 새로 만들기
![](https://velog.velcdn.com/images/syshin0116/post/84539790-1330-4a2f-a74d-121d2f135aba/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/d2529af7-e676-45b2-80f5-fd3224bc33de/image.png)
> 주의사항: 프로파일 이름은 대문자로 입력

#### 프로파일 편집
![](https://velog.velcdn.com/images/syshin0116/post/ea1f14de-3cd2-42aa-bf3b-3b4d1501acaf/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/b2c05ee7-caca-4358-bacd-54020f14e890/image.png)

#### 프로파일 삭제
![](https://velog.velcdn.com/images/syshin0116/post/cceaf3df-43f4-44b9-a5ec-a07905828207/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/4ab5eced-f327-429f-bd36-d29ff0a6fdb3/image.png)
현재 사용자에게 할당되어 있는 프로파일은 기본적으로 삭제가 불가능 하나
CASCADE 옵션을 사용하면 가능
삭제된 프로파일 사용자는 DEFAULT 프로파일로 변경됨

### 6.36 암호 보안 기능 구현
![](https://velog.velcdn.com/images/syshin0116/post/c500ff46-7bb9-4601-a9f7-4f768fa66968/image.png)

### 6.37 복잡한 암호 적용을 위한 함수제공
$ORACLE_HOME/rdbms/admin/utlpwdmg.sql 스크립트에 의해 아래 함수가 생성됩니다.
	- ORA12C_VERIFY_FUNCTION
	- ORA12C_STRONG_VERIFY_FUNCTION
이 함수는 암호에 대한 다음 조건을 필요로 합니다.
    - 최소 문자 수
    - username, 숫자가 추가된 username 역으로 바뀐 username 불가
    - 데이터베이스 이름 또는 숫자가 추가된 데이터베이스 이름 불가
    - 한 개 이상의 영문자 및 한 개 이상의 숫자 포함
    - 직전의 암호와 세 자 이상 달라야 함
    
### 6.38 기본 프로파일 수정
utlpwdmg.sql 스크립트는 다음과 같이 DEFAULT 프로파일을
수정합니다.
```sql
ALTER PROFILE DEFAULT LIMIT
PASSWORD_LIFE_TIME 180 -- 패스워드 사용기간 180일 제한
PASSWORD_GRACE_TIME 7 -- 만료 후 7일동안 경고 메시지 발생(유예기간)
PASSWORD_REUSE_TIME UNLIMITED -- 설정된 기간에는 동일 암호 사용불가
PASSWORD_REUSE_MAX UNLIMITED -- 동일 암호 사용 최대 횟수
FAILED_LOGIN_ATTEMPTS 10 -- 로그인 시도 10회 실패 시 1일 잠김
PASSWORD_LOCK_TIME 1 -- 로그인 시도 10회 실패 시 1일 잠김
PASSWORD_VERIFY_FUNCTION -- 복잡한 암호를 위한 함수 적용
ora12c_verify_function;
```

### 6.39 유저에게 할당량 지정
UNLIMITED TABLESPACE 시스템 권한이 없는 유저는 테이블스페이스에 객체를 생성하려면 할당량이 있어야 합니다.
	- 유저에게 SYSTEM 및 SYSAUX를 포함한 모든 테이블스페이스에 대해 무제한 할당량을 부여
	- 이 권한은 신중하게 부여해야 함

할당량은 다음과 같이 지정할 수 있습니다.
	- 특정 값(MB 또는 KB)
	- Unlimited
```sql
ALTER USER "HR" QUOTA 100M ON "USERS";
ALTER USER "HR" QUOTA UNLIMITED ON "USERS";

GRANT UNLIMITED TABLESPACE TO HR;
REVOKE UNLIMITED TABLESPACE FROM HR;
```

### 6.40 최소 권한의 원칙 적용 + α
1. 최소 권한의 원칙
	- 유저의 작업에 꼭 필요한 권한만 부여한다는 의미
	- 실수 또는 악의적으로 수정 불가하도록 예방
2. PUBLIC(전체사용가능)권한 **제한**
3. 네트워크 액세스 **제어**에 ACL(Access Control List) 사용
4. 유저가 액세스할 수 있는 **디렉토리 제한**
5. 관리 권한을 갖는 **유저 제한**
6. 원격 데이터베이스 인증 제한(패스워드 인증 방식으로 사용)
	```REMOTE_OS_AUTHENT=FALSE```
7. 최소 권한의 원칙 적용 뿐만 아니라 **다양한 관점으로 제한과 보호**를 권장

### 6.41 요약
1. 데이터베이스 유저 계정 생성 및 관리:
	- 유저 인증
	- 기본 저장 영역(테이블스페이스) 할당
2. 권한 부여 및 취소
3. 롤(role) 생성 및 관리
4. 프로파일 생성 및 관리:
	- 표준 암호 보안 기능 구현
	- 유저별 리소스 사용량 제어
    
### 6.42 연습: 개요
1. 리소스 소비를 제한하는 프로파일 생성
2. 다음과 같은 두 가지 롤(role) 생성:
	- HRCLERK
	- HRMANAGER
3. 네 명의 새 유저 생성:
	- 한 명의 관리자 및 두 명의 직원
	- 후속 연습 세션을 위한 한 명의 스키마 유저
    
## 6장 실습
[01.유저 생성 및 삭제, 시스템 권한부여.pdf](https://github.com/syshin0116/Study/files/11523990/01.pdf)
[02.시스템 권한 부여 및 회수, with admin option.pdf](https://github.com/syshin0116/Study/files/11523991/02.with.admin.option.pdf)
[03.오브젝트 권한 부여 및 회수, with grant option.pdf](https://github.com/syshin0116/Study/files/11523992/03.with.grant.option.pdf)
[04.롤(ROLE) 생성과 권한 할당.pdf](https://github.com/syshin0116/Study/files/11523988/04.ROLE.pdf)
[05.프로파일 생성 및 적용.pdf](https://github.com/syshin0116/Study/files/11523989/05.pdf)
