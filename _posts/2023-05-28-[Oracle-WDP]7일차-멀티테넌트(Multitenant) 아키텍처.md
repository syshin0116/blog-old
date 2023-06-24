---
title: "[ORACLE-WDP]7일차-3멀티테넌트(Multitenant) 아키텍처"
date: 2023-05-28 20:00:00 +0900
categories: [Database, ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---


<!--#### 공유url: http://naver.me/xoKMlnp5
#### -->


# 멀티테넌트(Multitenant) 아키텍처
1. [@멀티테넌트 아키텍처.pdf](https://github.com/syshin0116/Study/files/11583309/%40.pdf)
2. [multitenant-administrators-guide-19c.pdf](https://github.com/syshin0116/Study/files/11583308/multitenant-administrators-guide-19c.pdf)

>#### 톰 카이트의 한 마디
- 현재 오라클 데이터베이스 12c 릴리스에서는 기존의 아키텍처뿐만 아니라, 멀티테넌트 아키텍처도 지원하지만 향후에는 이전 아키텍처 지원은 중단될 것이다.(오라클 멀티테넌트 라이선스 별도 구매 필요)
- 따라서 DBA가 이 멀티테넌트 아키텍처에 익숙해지는 것이 앞으로 도움이 될 것으로 생각된다.
- 멀티테넌트 아키텍처는 DBA에게만 변화가 있지 개발자나 애플리케이션의 관점에서는 변화가 없다.
- 멀티테넌트 아키텍처의 궁극적인 목표는 기존에 존재하는 애플리케이션의 영향 없이 리소스를 좀 더 효과적으로 사용하는 데 있다.

>![](https://velog.velcdn.com/images/syshin0116/post/9f4ac850-13a6-48c2-9b16-c02effe9f12a/image.png)




>## Oracle VM VirtualBox
### 한대의 컴퓨터안에 여러개의 OS를 동시에 구동
1. 통합, CPU/MEMORY(HW) 공유
2. 가져오기/내보내기를 통해 OS 이미지의 이동 용이
3. 해당 OS를 복제하여 사용가능
GUEST OS(Linux)
\---------------------
HOST OS(Windows)
\---------------------
CPU/MEMORY(HardWare)
\---------------------

>## 오라클 멀티테넌트 아키텍처
1. 여러 데이터베이서들을 하나의 컴퓨터 통합!
	- CPU/MEMORY를 공유하여 사용 -> 1개의 인스턴스 공유
2. PDB(Pluggable) 데이터베이스 plug/unplug (가져오기/내보내기)
3. 기존 데이터베이스를 복제해서 사용가능

### 1. 멀티테넌트(Multitenant) 아키텍처 소개
1. 주요 목표는 **애플리케이션의 영향 없이 리소스(CPU/MEMORY등)를 효과적으로 사용**하는 것
	- 계정계 : 주간에 트랜잭션이 많이 발생함
	- 정보계(DW) : 야간에 대량의 배치작업이 많이 발생함
2. 개발자나 애플리케이션의 관점에서는 변화가 없음
3. 관리적인 관점에서 **최적화된 통합 DBMS 환경**
4. 복제
	- 여러 단계를 거쳐 DB 복제 및 DB 이동(non-CDB 아카텍처)
	- 한 단계로 즉시 DB 복제 및 용이한 DB 이동
5. 백업
	- 다수의 DB에 대한 백업 실행(non-CDB 아카텍처)
	- 하나의 멀티테넌트 컨테이너 DB에 대한 백업 실행
6. 패치
	- 여러 DB에 대한 패치 및 업그레이드 수행(non-CDB 아카텍처)
	- 하나의 멀티테넌트 컨테이너 DB에 대한 패치 및 업그레이드 수행
7. 클라우드 아키텍처 개념을 접목
8. 전통적인 서버 아키텍처의 문제점인 자원의 비효율적 사용, 자원의 낭비를 해결하기 위해 탄생
9. 여러 개의 DB를 관리하면서 **프로세스나 메모리 등의 자원은 공유하지만 각 시스템(PDB)의 데이터는 개별로 저장**
	– **OS 자원을 낭비 없이 효율적으로 사용**
	– 각각의 시스템의(PDB) 데이터 독립성 보장
	– DBA가 각 DB별로 관리하는 부담 감소, 운영비용 감소
10. CDB라 불리는 통합용 데이터베이스에 여러 대의 데이터 베이스(PDB)를 통합시키는 방식
11. CDB에 통합된 여러 대의 PDB는 **CDB 인스턴스 하나로 관리**
	– CDB : Container Database (통합용/관리용 데이터베이스)
	– PDB : Pluggable Database (업무용 데이터베이스)
    
> 계정계와 정보계를 통합해서 사용하여 효율적인 자원관리 가능

- CDB : Container Database (통합용/관리용 데이터베이스)
	- CDB 내부에는 총 252개의 PDB 관리 가능
	- Physical Level에 데이터베이스 Instance와 데이터베이스 파일존재
- PDB : Pluggable Database (업무용 데이터베이스)
	- 플러그/언 플러그 가능 데이터베이스, **유연성 제공**
	- 데이터베이스 스키마의 집합이며, 유저와 응용 프로그램에는 논리적으로 별도의 데이터베이스로 인식됨, **독립성 보장**
- 컨테이너 타입
	- Root 컨테이너, CDB$ROOT
	- Seed 컨테이너, PDB$SEED
		- 내부적으로 생성해 놓은 기본 데이터베이스 이미지(템플릿), PDB 생성시 사용
	- PDB 컨테이너
- PDB 생성방법
	- 기존 DB(Non-CDB)를 CDB에 통합할 때는 PDB 형태로 변환
	- PDB$SEED로 부터 생성
	- 기존 PDB를 복제해서 다른 PDB를 생성
	- 임의의 CDB에서 PDB를 언플러그 해서 다른 CDB에 플러그 가능

> CDB 구조
![](https://velog.velcdn.com/images/syshin0116/post/f79c9bd8-85bb-40ec-b279-9cb78b10b0bb/image.png)
![](https://velog.velcdn.com/images/syshin0116/post/c6a6b372-a17b-4639-a4a4-e7dab5a05a85/image.png)


>### 모든 PDB는 같은 형태일까?
#### 톰 카이트의 한 마디
- CDB를 업그레이드/패치할 때 동시에 관련된 PDB를 모두 적용하거나 선택해서 일부만 적용할 수 있다.
패치를 적용하거나 다음 릴리스로 업그레이드할 때 기존에 존재했던 데이터베이스를 업그레이드하는 대신에 새로운 멀티테넌트 DB 인스턴스를 구성하도록 선택할 수 있다.
- 그런 다음 PDB를 업그레이드/패치하고 기존의 CDB로부터 간단히 몇 초 안에 언플러그해서 새로운 CDB로 플러그 할 수 있다.
- 이 방식으로 새로운 릴리스에서 각각의 애플리케이션을 테스트하는 목적으로 며칠 또는 몇 주 간의 과정을 통해 PDB를 업그레이드/패치 할 수 있다.
> 
| 	| PDB, CDB	|
|---|---|
| Seed PDB                             | CDB는 새로운 PDB를 만드는데 사용되는 PDB\$SEED라는 PDB를 가지고 있다. PDB\$SEED 내에 오브젝트를 추가하거나 변경할 수 없다.                                                                                                                                                             |
| PDB                                  | 사용자 스키마, 데이터, 코드와 기타 데이터베이스 관련 오브젝트를 담고 있는 유저가 만든 개체이다. PDB는 CDB 내에서 고유하고 독립된 데이터베이스 환경을 가진다. 하나의 CDB는 복수 개의 PDB를 가질 수 있다.                                                                              |
| CDB 인스턴스                         | 인스턴스 파라미터, SGA, 백그라운드 프로세스와 같이 일반적인 인스턴스 항목이 포함된 구조이다.                                                                                                                                                                                         |
| 하나 이상의 컨트롤 파일              | non-CDB와 같이 컨트롤 파일을 다중화 한다. 이 컨트롤 파일은 CDB와 연결된 PDB를 모두 지원한다.                                                                                                                                                                                         |
| 온라인 리두 로그 파일                | non-CDB와 같이 여러 그룹을 생성하고 다중화 한다. 이 리두 로그가 전체 CDB와 연결된 PDB를 같이 지원한다. 온라인 리두 로그는 루트 컨테이너의 일부로서 저장되는 것으로 간주한다. CDB가 ARCHIVELOG 모드인 경우 아카이브 파일도 생성한다. ARCHIVELOG 모드의 변경은 CDB레벨에서만 수행한다. |
| 하나 이상의 Temporary 파일 집합      | CDB는 디폴트로 TEMP라는 단일 Temporary 테이블 스페이스를 최소한 한 개를 가진다. 이 테이블 스페이스는 CDB와 PDB에 대한 임시 작업에 대한 요청을 처리한다. CDB는 추가로 Temporary 테이블 스페이스를 생성하거나 정의할 수 있고, PDB마다 Temporary 테이블 스페이스를 생성할 수 있다.      |
| Undo 테이블 스페이스와 관련 Tempfile | 하나의 UNDO 테이블 스페이스와 tempfile이 non-RAC인 CDB의 루트 컨테이너에 위치한다. 이 UNDO 테이블 스페이스는 CDB와 PDB를 모두 지원한다. RAC 구성에서 각 노드별로 Undo 테이블 스페이스를 가진다.                                                                                      |
| SYSTEM과 SYSAUX                      | CDB의 시스템 테이블 스페이스의 데이터 파일에는 루트 컨테이너에 관한 데이터 딕셔너리와 PDB와 관련된 데이터 딕셔너리에 대한 Pointer를 가진다. CDB는 유저 테이블 스페이스나 유저에 관련되는 데이터 파일을 가지지 않는다.                                                                |

![](https://velog.velcdn.com/images/syshin0116/post/d9c9c690-c71e-4e83-aa3a-1313013ef314/image.png)

### 2. 오라클 서버 아키텍처(non-CDB 아키텍처)
![](https://velog.velcdn.com/images/syshin0116/post/08ae617e-d777-4d16-a898-1ba7db5b43c2/image.png)

### 3. CDB(Container Database) PDB(Pluggable Database)
![](https://velog.velcdn.com/images/syshin0116/post/ac161bc2-23ab-437a-ab14-2e0f98133b4f/image.png)
> 기본적인 형태가 정해져있기 때문에 명령어 하나로 쉽게 생성 가능함

### 4. PDB$SEED를 통해 PDB 생성
![](https://velog.velcdn.com/images/syshin0116/post/9ac6344e-524a-4834-b07a-97eeebbfe6de/image.png)

새로운 PDB 생성
```sql
CREATE PLUGGABLE DATABASE NewPDB
ADMIN USER dba1 IDENTIFIED BY password;
```

### 5. 기존 PDB를 복제하여 PDB 생성
![](https://velog.velcdn.com/images/syshin0116/post/0263e81b-994e-4e4d-9b31-be1af0bbb3de/image.png)

기존 PDB 복사
```sql
CREATE PLUGGABLE DATABASE NewPDB FROM SourcePDB;
```

### 6. Plugging In an Unplugged PDB
![](https://velog.velcdn.com/images/syshin0116/post/de9273f4-af13-4e6c-bbab-bf613d40ff0a/image.png)

```sql
CREATE PLUGGABLE DATABASE salespdb
USING '/disk1/usr/salespdb.xml’ NOCOPY;
```

### 7. 멀티테넌트(Multitenant) 아키텍처 소개
1. 오라클에서는 기존에 사용해 오던 데이터베이스 아키텍처에서 멀티테넌트 아키텍처로 일원화할 것이라고 발표
2. 멀티테넌트 아키텍처가 확산 중이고 더욱 확산될 예정
3. Multitenant Administrators Guide 19c
4. multitenant-administrators-guide-19c.pdf 참고
5. [https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/index.html](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/index.html)

# 오라클 중요 개념- Redo, Undo

## Redo log, Undo segment(Rollback segment)

호칭: 
- Redo log = Redo data = Redo record = 변경이력
- Undo = Rollback

많이 쓰이는 상황:
- 리두 데이터: 백업/복구(RAMN, DATAPUMP)
- 언두 데이터: 플래쉬백 (논리적인 복구)

```sql
select empno, ename, sal
from scott.emp
where ename= 'KING';
```
5000

```sql
update scott.emp set sal = 10000
where ename = 'KING'
```
5000 -> 10000

- 리두 = 재실행 (10000으로 변경)
- 언두 데이터: 변경 이전의 값: 5000

#### 메모리 관점(비영구적, 휘발성 -> 장애 발생시 데이터 유지안됨)
1. SGQ의 어떤 메모리 공간에 변화가 일어나는가?
2. 어떤 순서로 메모리 공간의 변화가 일어나는가?
3. 해당 메모리 공간의 변화를 일으키는 프로세스는 어떤것인가?
	- 이해를 돕기 위한 가정
    => 커밋된 데이터가 디스크에 기록되는것이 늦게 일어나는 경우
4. 해당하는 파일에 기록 혹은 기록하게 하는 프로세스는?


1. 해당 세션, 트랜잭션이 발생, 언두 세그먼트를 할당
2. 해당 데이터 파일에서 해당 블록을 데이터 버퍼 캐시 로딩
3. 변경 이력을 리두로그 버퍼에 저장(선 로그 기법)
4. 언두 데이터를 언두 세그먼트에 저장
5. 변경이력에 해당하는 데이터를 데이터 버퍼캐시에 저장
=> 서버 프로세스

> ### 버퍼 캐시란?
- SGA의 일부로서 데이터 파일에서 읽은 데이터 블록 복사본을 보관한다
- 오라클이 데이터를 읽고 수정하기 위해 디스크에 존재하는 데이터를 읽어 저장하는 메모리 공간이다
![](https://velog.velcdn.com/images/syshin0116/post/07602f01-1fcf-4e92-afe0-6c90315563a1/image.png)


```sql
commit;
```
1. 언두 세그먼트 할당 해제
2. 리두로그 버퍼내용을 리두로그 파일에 즉시 기록(LGWR)
	- 리두로그 파일에 기록되는 조건은 다양함
3. commit 완료 메세지를 사용자에게 전달

#### 변경된 데이터를 디스크에 기록하는 대표적인 경우: 체크포인트 이벤트 발생시
1. CKPT(체크포인트) 프로세스가 DBWR(DB writer) 프로세스에게 신호 전달
2. DBWR가 더티버퍼를 데이터파일에 기록
	- 모아서 한꺼번에 기록(버퍼역할, I/O 횟수 감소)
3. 데이터 파일의 헤더와 컨트롤 파일에 체크포인터를 저장 => 커밋된 데이터를 어디까지 디스크에 기록했느냐의 정보

```sql
ROLLBACK;
```

# 인스턴스 크래쉬/인스턴스 복구

### CKPT, 체크포인트 이벤트

```shutdown abort``` = 정전 => 비정상 종료
- 커밋된 데이터를 디스크에 기록하지 못하고 비정상 종료
- 커밋되지 않은 데이터가 디스크에 반영된 상태로 비정상 종료
- 인스턴스 크래쉬라고 부른다


```shutdown normal/transactional/immediate``` => 정상 종료 

#### 데이터베이스 일관성이란?
커밋된 트랜잭션의 변경 데이터만! 디스크에 반영된 상태

- DBWR에 의해 더티버퍼가 데이터 파일에 기록된다
- 여기서 더티 버퍼에는 두가지 종류가 있다
	1. 커밋된 더티버퍼
	2. 커밋되지 않은 더티버퍼\
    
#### startup -> SMON(System Monitor)
- 인스턴스 크래쉬(일관성 깨짐, 비정상 종료)
	- 롤포워드, 롤백(일부)
	- 오픈 후 롤백(나머지)
    
> ### Roll Forward 란 ?
- 트랜잭션 로그에는 데이터 변경 처리가 완벽히 끝난 것으로 기록되어 있으나 해당 내용이 데이터 파일에 미처 반영되지 못했을 때 트랜잭션 로그 내용을 참조해 데이터 변경 작업이 실제 데이터 파일에 반영된다.

> ### Rollforward 와 Rollback 차이
- ROLLBACK : 복구시 로그파일을 이용해서 COMMIT 이전 상태로 데이터 복구
- ROLLFORWARD : 복구시 로그 파일을 이용해서 COMMIT 상태로 데이터 복구