---
title: "[ORACLE-WDP]3일차-함수, GROUP BY, JOIN, SEBQUERY"
date: 2023-05-13 21:00:00 +0900
categories: [Database, ORACLE-WDP]
tags: [oracle, wdp, database]     # TAG names should always be lowercase
---

# Oracle Database 19c SQL.pdf

## 4. 함수(Function) 활용
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
	to_char(sysdate, 'YYYY-MM-DD HH24)
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
- 99, 
#### 함수 중첩
![](https://velog.velcdn.com/images/syshin0116/post/6bfbb71e-dffd-4811-8b4e-177246ddc379/image.png)
```sql
-- 중첩된 함수를 분석할때는 안쪽부터 나누어서 구문을 따로 입력하여 분석
SELECT last_name
    , SUBSTR (LAST_NAME, 1, 8) F1
    , CONCAT(SUBSTR (LAST_NAME, 1, 0), '_US')F2
    , UPPER(CONCAT(SUBSTR (LAST_NAME, 1, 0), 'US_')) F3
FROM employees
WHERE department_id = 60;
```
![](https://velog.velcdn.com/images/syshin0116/post/84fa282d-5d3d-4c04-b1a1-02990f327b6e/image.png)

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
- COALESCE 함수의 인수의 개수는 동적으로 입력 가능(여러개 입력 가능)
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
CASE 컬럼	WHEN 조건1	THEN 값1
		WHEN 조건2	THEN 값2
		ELSE 값3
```
```sql
SELECT last_name, job_id, salary,
	CASE job_id WHEN 'IT_PROG' THEN 1.10*salary
		WHEN 'ST_CLERK' THEN 1.15*salary
		WHEN 'SA_REP' THEN 1.20*salary
	ELSE salary END "REVISED_SALARY"
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/7a39fc12-7dd7-4a94-bebd-622b754e1192/image.png)

#### CASE와 DECODE와 다른 점은 조건비교에 있어서 크다(>), 작다(<), 같다(=) 로직이 가능
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
타입에 맞는 데이터만 갖지만, 가상 컬럼은 여러 개의 데이터를 연산한 결과값을 저장하는 컬럼 (11g NF)
- 새로운 데이터가 들어와도 
```shell
orcl@SCOTT> create table copy_emp as select * from emp;
orcl@SCOTT> alter table copy_emp
 				add (sal_grade varchar2(6)
 					as (CASE
 						WHEN sal between 1 and 1000 THEN 'LOW'
 						WHEN sal between 1001 and 2000 THEN 'MEDIUM'
 						WHEN sal between 2001 and 3000 THEN 'HIGH'
 						ELSE 'ULTRA'
 						END) virtual );
orcl@SCOTT> select ename, sal, sal_grade from copy_emp;
orcl@SCOTT> insert into copy_emp (empno, ename, sal) values (9999,'LEE',4000);
orcl@SCOTT> select table_name, column_name, data_type, data_default
 			from user_tab_columns
 			where table_name='COPY_EMP';
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
![](https://velog.velcdn.com/images/syshin0116/post/b6e6a669-c02b-4e29-9d00-8bcb655d030d/image.png)

#### 11g 부터는 PIVOT 와 UNPIVOT 절을 통해서 보다 쉽게 구현 가능
```sql
SELECT *
FROM ( SELECT department_id, job_id, salary
FROM employees )
PIVOT ( SUM(salary) FOR job_id IN ( 'IT_PROG' AS "IT MAN"
                                    ,'SA_REP' AS "SALES MAN"
                                    ,'ST_CLERK' AS "STOCK MAN")) ;
```

'''sql
-- * 추가예제
-- SCOTT PIVOT 예제
SELECT DEPTNO,JOB ,SUM(SAL)
FROM EMP
GROUP BY DEPTNO, JOB
ORDER BY DEPTNO, JOB;

SELECT distinct JOB FROM EMP;
SELECT distinct DEPTNO FROM EMP order by 1;

SELECT DEPTNO, CLERK, MANAGER, PRESIDENT, ANALYST, SALESMAN
FROM (SELECT DEPTNO, JOB, SAL FROM EMP)
PIVOT (
    SUM(SAL)
    FOR JOB IN('CLERK'     as CLERK
              ,'MANAGER'   as MANAGER
              ,'PRESIDENT' as PRESIDENT
              ,'ANALYST'   as ANALYST
              ,'SALESMAN'  as SALESMAN)
)
order by 1,2,3;

SELECT JOB , D10, D20, D30
FROM(SELECT DEPTNO, JOB, SAL FROM EMP)
PIVOT (
    SUM(SAL) 
    FOR DEPTNO IN (10 as D10, 20 as D20, 30 as D30)
)
ORDER BY JOB;


-- PIVOT <=> UNPIVOT 
select deptno, job_type, sal_sum
from
(
    SELECT DEPTNO, CLERK, MANAGER, PRESIDENT, ANALYST, SALESMAN
    FROM(SELECT DEPTNO, JOB, SAL FROM EMP)
    PIVOT (
        SUM(SAL)
        FOR JOB IN('CLERK'     as CLERK
                  ,'MANAGER'   as MANAGER
                  ,'PRESIDENT' as PRESIDENT
                  ,'ANALYST'   as ANALYST
                  ,'SALESMAN'  as SALESMAN)
    )
    order by 1,2,3
)
unpivot 
(
	sal_sum for job_type in (CLERK, MANAGER, PRESIDENT, ANALYST, SALESMAN)
)
order by 1,2,3
;

select job, deptno_type, sal_value
from
(
    SELECT JOB , D10, D20, D30
    FROM(SELECT DEPTNO, JOB, SAL FROM EMP)
    PIVOT (
        SUM(SAL) 
        FOR DEPTNO IN (10 as D10, 20 as D20, 30 as D30)
    )
    ORDER BY JOB
)
unpivot
(
    sal_value for deptno_type in (D10, D20, D30)
)
order by job, deptno_type, sal_value;


-- PIVOT 은 decode, case 문으로 구현가능
select deptno
 , sum(case when job = 'CLERK' then sal end) CLERK
 , sum(case when job = 'MANAGER' then sal end) MANAGER 
 , sum(case when job = 'PRESIDENT' then sal end) PRESIDENT 
 , sum(case when job = 'ANALYST' then sal end) ANALYST
 , sum(case when job = 'SALESMAN' then sal end) SALESMAN 
FROM EMP
group by deptno
order by deptno;


select job
 , sum(case when DEPTNO = 10 then sal end) D10
 , sum(case when DEPTNO = 20 then sal end) D20
 , sum(case when DEPTNO = 30 then sal end) D30
FROM EMP
group by job
order by job;
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

```sql
-- 기본 SQL 이해 - 기본 함수 사용(연습문제)
desc employees;
-- Exam1) 각 사원에 대해 다음과 같은 문장으로 출력하고자 한다. 
-- <사원의 last name> earns <salary> monthly but wants <3 times salary.> 의 문자열을 “Dream Salaries” Alias로 지정 하십시오.
SELECT LAST_NAME || ' earns ' || TO_CHAR(SALARY, '$99,999.00') ||' monthly but wants ' || TO_CHAR(3*SALARY, '$99,999.00') as "Dream Salaries" 
FROM employees;
-- Exam2) 각 사원의 성, 채용 날짜, 입사 6개월 후의 첫 번째 월요일에 해당하는 날짜를 출력 하십시오. 
-- Alias는 after6m 적용 : alter session set nls_date_format = 'YYYY-MM-DD’; 
alter session set nls_date_format = 'YYYY-MM-DD';

SELECT LAST_NAME, HIRE_DATE, NEXT_DAY(ADD_MONTHS(HIRE_DATE, 6), '월요일') as "after6m"
FROM employees;

-- Exam3) 사원의 성과 커미션 금액을 출력. 
-- 사원이 커미션을 받지 않으면 "No Commission"을 표시. 
-- 커미션의 포맷은 ‘90.99’ Alias를 COMM으로 지정.
SELECT LAST_NAME, COMMISSION_PCT, COALESCE(TO_CHAR(COMMISSION_PCT, '$90.99'), 'No Commission') AS "COMM"
FROM employees;

SELECT last_name, 
       NVL(TO_CHAR(commission_pct, 90.99), 'No Commission') COMM 
FROM   employees; 
```
```sql
--Exam4) 라스트 네임, 급여, 커미션, 새 급여를 출력 하십시오.
--커미션을 받지 않는 사원에게는 $2,000의 급여 인상을 하고
--커미션을 받는 사원의 경우에는 기존 급여에
--커미션 금액을 추가한 새 급여를 출력 하시오.

-- COALESCE 함수는 NULL이 아닌 첫번째 인수의 값을 반환함
-- NULL, VAL, VAL : 커미션이 없는 사람들
-- VAL, VAL, VAL : 커미션이 있는 사람들
-- NULL, NULL, NULL : salary가 NULL이면 NULL 반환
SELECT last_name
      , salary
      , commission_pct
      , COALESCE((salary+(commission_pct*salary)), salary+2000, salary) as "New Salary"
FROM employees;
```
```sql
-- Exam5) 다음 데이터를 사용하여 DECODE/CASE 함수를 통해
-- JOB_ID 열의 값을 기반으로 모든 사원의 등급을 출력하시오.
-- 업무별 등급을 산정
SELECT job_id
     , decode (job_id, 
               'AD_PRES',   'A', 
               'ST_MAN',    'B', 
               'IT_PROG',   'C', 
               'SA_REP',    'D', 
               'ST_CLERK',  'E',  '0') AS GRADE 
FROM employees
order by job_id, GRADE;

SELECT job_id
     , CASE job_id WHEN 'ST_CLERK' THEN 'E' 
                   WHEN 'SA_REP'   THEN 'D' 
                   WHEN 'IT_PROG'  THEN 'C' 
                   WHEN 'ST_MAN'   THEN 'B' 
                   WHEN 'AD_PRES'  THEN 'A' 
                   ELSE '0'  
       END AS GRADE 
FROM employees
order by job_id, GRADE;

```

### [보조자료] 4장_함수(SQL예제,연습문제답)

[[보조자료] 4장_함수(SQL예제,연습문제답).txt](https://github.com/syshin0116/Study/files/11468951/4._.SQL.txt)
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
- COUNT(NULL)은 NULL값의 개수를 반환
- COUNT(컬럼명)은 NULL값을 제외한 값의 개수 반환
- COUNT(*)을 자주 쓰지만 뭐가 들어가도 상관없다

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

#### Quiz) 사원 테이블에서 업무에 REP가 포함된 것은 제외하고 업무별 전체 급여 합계를 구하고 업무별 전체 급여 합계 중 $13000 보다 큰 것만 조건으로 전체 급여 합계로 오름차순 정렬해서 출력 하시오.
```sql
SELECT job_id, SUM(salary) PAYROLL
FROM employees
WHERE job_id NOT LIKE '%REP%'
GROUP BY job_id
HAVING SUM(salary) > 13000
ORDER BY SUM(salary) ASC;
```
####  Group 함수를 중첩하는 경우 반드시 Group by 절을 사용해야 한다
```sql
SELECT MAX(AVG(salary))
FROM employees
GROUP BY department_id;
```
### 생각해봅시다(1)
- 가능하면 GROUP BY보다는 WHERE 절에 조건을 주는 것이 효율적이다
![](https://velog.velcdn.com/images/syshin0116/post/4912f6ec-63e4-4310-aaef-d30de77c0ff7/image.png)
비효율적:
```sql
SELECT 		EMPLOYEE_ID, HIRE_DATE, SUM(SALARY)
FROM 		EMPLOYEES
GROUP BY	EMPLOYEE_ID, HIRE_DATE
GAVING		HIRE_DATE BETWEEN TO_DATE('2005/01/01', 'YYYY/MM'DD')
			AND TO_DATE('2009/12/31', 'YYYY/MM/DD');
```
효율적:
```sql
SELECT EMPLOYEE_ID, HIRE_DATE, SUM(SALARY)
FROM EMPLOYEES
WHERE HIRE_DATE BETWEEN TO_DATE('2005/01/01', 'YYYY/MM/DD')
AND TO_DATE('2008/12/31', 'YYYY/MM/DD')
GROUP BY EMPLOYEE_ID, HIRE_DATE;
```

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
#### Exam4) 관리자 번호 및 해당 관리자에 속한 사원의 최저 급여를 출력. 관리자를 알 수 없는 사원 및 최저 급여가 $6,000 미만인 그룹은 제외시키고, 최저급여에 대한 내림차순 정렬 하시오.
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

#### Exam6) 업무별 급여 합계 및 평균급여를 $표시와 함께 출력하시오. 단, 80번 부서에 대한 정보만 출력하고, 업무별로 오름차순 정렬하시오.
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

헷갈리기 쉬움!!
> GROUPING + CUBE를 썼을 때, 
	- 값이 0: 사용
    - 값이 1: 미사용
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

### [보조자료] 5장_그룹데이터 처리(SQL예제,연습문제답)

[[보조자료] 5장_그룹데이터 처리(SQL예제,연습문제답).txt](https://github.com/syshin0116/Study/files/11468952/5._.SQL.txt)

## 6. 테이블 조인

### 6.1 목표
- JOIN 이란
- 다양한 JOIN 방식
- [연습문제]


### 6.2 JOIN이란?
#### RDBMS에서 JOIN은 왜 사용해야 하는 것인가?
#### JOIN은 언제 사용 하는가?
- 관계형 데이터베이스는 **중복 데이터를 피하기 위해서 데이터를 여러개의 테이블로 나눠서 저장**하게 된다. 이렇게 분리되어 저장된 데이터를 사용자가 원하는 데이터 집합으로 추출하기 위해서는 **여러 테이블을 조합**해야 한다. 이때 SQL의 JOIN을 사용하게 된다.

#### JOIN의 잘못된 고정관념
- **Join은 성능 저하 발생?**
- **데이터베이스의 크기 감소**: 테이블의 분리(정규화)는 중복된 데이터를 감소시키기 때문에 전체 데이터베이스의 크기를 감소 시킨다
- **데이터의 정합성**: 테이블 분리를 통해 중복된 데이터가 제거되어 데이터는 감소하게 된다. 중복된 데이터가 제거되므로 데이터의 정합성은 더욱 확고해질 수 있다.

### 6.3 Table JOIN
#### 조인을 사용하여 둘 이상의 테이블에서 데이터를 한번에 쿼리 할 수 있다.
#### 오라클 10g부터 표준 SQL(ANSI SQL)을 사용 가능하게 되었다.
#### 다음은 표준 SQL:1999에서 제공하는 조인 기법이다.

```sql
SELECT 	table1.column, table2.column
FROM 	table1
[NATURAL JOIN table2] |
[JOIN table2 USING (column_name)] |
[JOIN table2
	ON (table1.column_name = table2.column_name)]|
[LEFT|RIGHT|FULL OUTER JOIN table2
	ON (table1.column_name = table2.column_name)]|
[CROSS JOIN table2];
```

![](https://velog.velcdn.com/images/syshin0116/post/3eeda871-46b3-4584-899d-d79ad01bf93b/image.png)

#### 여러 테이블에서 데이터 가져오기
![](https://velog.velcdn.com/images/syshin0116/post/6894c0f1-66fb-47e0-8ba9-91a2432a59a6/image.png)

#### Join 처리 시 Alias 사용
- 테이블 Alias를 사용하여 긴 테이블명을 축약하여 사용 가능
	– SQL 코드 크기를 줄여 메모리를 적게 사용
- 중복된 컬럼명을 갖는 테이블을 JOIN 하여도 오류가 발생하지 않음
- Alias는 FROM절에서 미리 정의하고 SELECT절에서 사용함
- 유의사항
  – 테이블 Alias 는 30자까지 사용할 수 있지만 길이는 짧을수록 좋다
  – FROM 절의 특정 테이블 이름에 대해 테이블 Alias가 사용될 경우 ELECT 문 전체에서 테이블 이름 대신 해당 테이블 Alias를 사용해야 한다
  – 테이블 Alias 는 의미 있는 단어 선택
  – 테이블 Alias 는 현재 SELECT 문에 대해서만 유효

```sql
SELECT 	e.employee_id, e.last_name,
		d.location_id, department_id
FROM 	employees e JOIN departments d
USING 	(department_id) ;
```

- 반드시 Alias를 사용해야 하는 경우 (양 테이블에 같은 컬럼 존재하여 구분해야 할 때)
```sql
SELECT 		e.employee_id, e.last_name ln, d.location_id,
			e.department_id, d.department_id
FROM 		employees e
JOIN 		departments d
			on e.department_id = d.department_id
ORDER BY 	ln;
```
#### Natural Join
- 두개의 테이블 에서 동일한 컬럼명으로 조인이 이루어지는 것
- 여러 개의 동일한 컬럼명이 존재하면 모두 조인에 사용됨
- 동일한 컬럼명이 서로 다른 데이터 타입을 가지면 오류 발생

```sql
SELECT 	department_id, department_name,
		location_id, city
FROM 	departments
NATURAL JOIN locations ;
```
![](https://velog.velcdn.com/images/syshin0116/post/5e24a34e-c333-44c8-b2f3-58c6e621888e/image.png)

#### Using절을 이용한 Join
- USING 절에 조인 대상이 되는 칼럼을 지정
- 여러 개의 동일한 컬럼명이 있는 경우 컬럼명을 지정하여 하나만 조인조건으로 사용 할 수 있다.
- USING절을 통해 명시한 컬럼은 Alias를 사용할 수 없다.
```sql
SELECT 	employee_id, last_name,
		location_id, department_id
FROM 	employees JOIN departments
USING 	(department_id) ;
```

![](https://velog.velcdn.com/images/syshin0116/post/6dd770a3-b607-45b7-88fe-8f87af3e5b08/image.png)

#### ON 절로 Join 생성
- ON 절을 사용하여 임의 조건을 지정하거나 조인할 컬럼을 지정
- 조인 조건만을 ON절에 기술하고 다른 검색이나 필터 조건은 WHERE절에 분리해서 기술할 수 있다.

```sql
SELECT 		e.employee_id, e.last_name, e.department_id,
			d.department_id, d.location_id
FROM 		employees e JOIN departments d
ON 			(e.department_id = d.department_id);
```
![](https://velog.velcdn.com/images/syshin0116/post/eb50a20d-2055-4ff0-99c0-ab8f66cbeff4/image.png)

#### ON 절로 3-way Join 생성
```sql
SELECT 		employee_id, city, department_name
FROM 		employees e
JOIN 		departments d
ON 			d.department_id = e.department_id
JOIN 		locations l
ON 			d.location_id = l.location_id;
```
![](https://velog.velcdn.com/images/syshin0116/post/cb55d2c1-2a9a-4a3b-ab8a-700de66d7628/image.png)

#### 특정 사원(&)에 대해 아래의 결과를 산출하는 쿼리를 작성해 보시오
![](https://velog.velcdn.com/images/syshin0116/post/d7f7e5ae-4340-4b5d-8e69-1a2fd744c38c/image.png)
```sql
select 		a.employee_id, a.last_name, d.job_title,
			b.start_date, b.end_date, c.department_name
	from 	employees a,
			job_history b,
			departments c,
			jobs d
	where 	a.employee_id 			= b.employee_id
			and b.department_id 	= c.department_id
			and b.job_id 			= d.job_id
			and a.employee_id 		= 101;
```
![](https://velog.velcdn.com/images/syshin0116/post/388aa6f2-a91a-4512-8130-2810c54591ed/image.png)

#### Self Join
![](https://velog.velcdn.com/images/syshin0116/post/d12e089f-1ba4-4a19-883d-96123488479f/image.png)

```sql
SELECT 	worker.last_name emp, manager.last_name mgr
FROM 	employees worker JOIN employees manager
ON 		(worker.manager_id = manager.employee_id);
```
![](https://velog.velcdn.com/images/syshin0116/post/b357c18f-1bc4-4221-907e-e3d1919aae23/image.png)

사원의 사번, 성명과 해당 사원을 담당하고 있는 매니저의 사번, 성명을 출력
사원명과 담당 매니저명 출력

#### Non-equiJoins (비 동등 조인)
- BETWEEN 조인

![](https://velog.velcdn.com/images/syshin0116/post/e0b568f1-e697-4597-ae4b-68c057f6d277/image.png)

```sql
SELECT 	e.last_name, e.salary, j.grade_level
FROM 	employees e JOIN job_grades j
ON 		e.salary
		BETWEEN j.lowest_sal AND j.highest_sal;
```
![](https://velog.velcdn.com/images/syshin0116/post/7a20f22a-e80f-43b1-b84b-e57dd82bd7d3/image.png)

#### Outer Join으로 직접 일치하지 않는 행 반환
![](https://velog.velcdn.com/images/syshin0116/post/86e233e9-bab8-4eec-9dd7-e43e5101cf74/image.png)

#### Left Outer Join
```sql
SELECT 	e.last_name, e.department_id, d.department_name
FROM 	employees e LEFT OUTER JOIN departments d
ON 		(e.department_id = d.department_id) ;
```
![](https://velog.velcdn.com/images/syshin0116/post/09330ebf-973a-451a-a530-c9adec90daf1/image.png)

- Left Outer Join 예제
기준 테이블을 좌측에 두면 LEFT OUTER KOIN
사원 테이블에는 있고 부서 테이블에는 없는것은 NULL 출력

```sql
SELECT  e.employee_id
		, e.LAST_NAME
        , d.department_id
        , d.department_name
        , count(*) over() 총사원수
FROM employees e
LEFT OUTER JOIN departments d
ON e.department_id = d.department_id
ORDER BY d.department_id nulls first;
```
![](https://velog.velcdn.com/images/syshin0116/post/553a8b94-8713-4da9-89cf-2bc48e8f4c55/image.png)

#### RIGHT Outer Join
```sql
SELECT e.last_name, e.department_id, d.department_name
FROM employees e RIGHT OUTER JOIN departments d
ON (e.department_id = d.department_id) ;
```
![](https://velog.velcdn.com/images/syshin0116/post/4da5f612-b1d2-4791-8106-22ea2d5cd9d3/image.png)

#### Full outer Join
```sql
SELECT e.employee_id, e.last_name, d.department_id, d.department_name
FROM employees e FULL OUTER JOIN departments d
ON (e.department_id = d.department_id) ;
```
![](https://velog.velcdn.com/images/syshin0116/post/e2cd5861-9f2e-4c5e-8012-dbd49874f61a/image.png)

- 오라클 형식으로 구현한 FULL OUTER JOIN
- 오라클은 FULL OUTER JOIN을 지원하지 않아서 UNION을 사용함(?)
#### Cartesian Product = Cross Join
- 다음과 같은 경우 Cartesian Product 생성
	– 조인 조건에 연결 조건이 없는 경우
	– 조인 조건에 연결 조건은 없고 다른 조건이 있는 경우
	– 조인 조건이 잘못된 경우
- Cartesian Product가 생성되지 않게 하려면 반드시 유효한 조인 조건을 포함해야 한다.

```sql
SELECT 	last_name, department_name
FROM 	employees
CROSS 	JOIN departments ;
```
![](https://velog.velcdn.com/images/syshin0116/post/0a7b5881-3ca5-4463-85f8-222e6e1ba50a/image.png)

### 6.4 Table Join (연습문제, HR ERD를 보면서 실습하세요.)
[[보조자료] 6장_테이블 조인(SQL예제,연습문제답).txt](https://github.com/syshin0116/Study/files/11469053/6._.SQL.txt)

![](https://velog.velcdn.com/images/syshin0116/post/6023951c-94ff-43bc-aebc-22161bfb8fd0/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/071ddf98-538f-4d4a-91a1-552eeb92df2d/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/0e0e0f50-ba5f-49b2-864e-bcaf5257a115/image.png)


![](https://velog.velcdn.com/images/syshin0116/post/8f29e367-9db6-485e-bdc4-46fec965280d/image.png)



#### Exam 1) 
전체사원에 대해서 사원번호, 성명, 직무타이틀, 부서명, 부서의 도시,나라,대륙을 출력하시오. 단 부서가 할당되지 않은 사원도 출력, 사원ID로 정렬

```sql
SELECT      e.employee_id, 
            e.last_name, 
            j.job_title, 
            e.department_id, 
            l.city, 
            c.country_name, 
            r.region_name,
            COUNT(*) OVER() total
FROM        employees e
LEFT OUTER JOIN        jobs j
ON          e.job_id = j.job_id
LEFT OUTER JOIN        departments d
ON          e.department_id = d.department_id
LEFT OUTER JOIN        locations l
ON          d.location_id = l.location_id
LEFT OUTER JOIN        countries c
ON          l.country_id = c.country_id
LEFT OUTER JOIN        regions r
ON          c.region_id = r.region_id
ORDER BY    e.employee_id;
```
![](https://velog.velcdn.com/images/syshin0116/post/9da840ae-b88e-4e4e-8bb0-f23b31f1020a/image.png)

#### Exam2) 
직무이력이 있는 사원의 사원번호, 성, 직무ID, 직무타이틀, 직무 시작/종료일자를 출력하시오. 사원ID, 직무시작일자 정렬

```sql
SELECT      e.employee_id, 
            e.last_name, 
            e.job_id, 
            j.job_title, 
            h.start_date, 
            h.end_date, 
            COUNT(*) OVER() 개수
FROM        employees e
JOIN        jobs j
ON          e.job_id = j.job_id
JOIN        job_history h
ON          j.job_id = h.job_id
ORDER BY    e.employee_id, h.start_date;
```
![](https://velog.velcdn.com/images/syshin0116/post/22872ab9-f4c0-4a57-b209-f35f997dc54c/image.png)


#### Exam3) 
모든 사원의 사원아이디, 사원성명, 부서아이디, 부서명을 출력하시오. 단, 소속된 부서가 없는 사원도 출력하시오. 부서 아이디 NULL을 첫번째로 정렬

```sql
SELECT      e.employee_id, 
            e.last_name, 
            e.department_id, 
            d.department_name
FROM        employees e
LEFT OUTER JOIN        departments d
ON          e.department_id = d.department_id
ORDER BY    e.department_id NULLS FIRST;
```
![](https://velog.velcdn.com/images/syshin0116/post/4514cced-2390-4ff5-86fa-6f0efce8b272/image.png)



#### Exam4) 
모든 부서의 부서 아이디, 부서명, 매니저 아이디, 매니저 성명을 출력하시오. 단, 부서의 매니저가 없는 부서도 출력, 부서 아이디로 정렬

```sql

```


#### Exam5) 
**NATURAL JOIN**을 사용하여 LOCATIONS 및 COUNTRIES 테이블에서 지역ID, 주소, 도시명, 국가명, 시/도/구/군을 출력하시오.
![](https://velog.velcdn.com/images/syshin0116/post/337e984e-d984-49da-86b6-29c5db109ffb/image.png)

#### Exam6) 
HR 부서에서 Toronto에 근무하는 사원에 대한 보고서를 요구한다. Toronto에서 근무하는 모든 사원의 성, 직무ID, 부서 ID 및 부서 이름을 출력하시오. (add : 도시명을 입력(&) 받을 수 있도록 구성)
![](https://velog.velcdn.com/images/syshin0116/post/4ae0fff5-fd23-42e3-a1f4-57104f4d1360/image.png)

#### Exam7) 
동일한 부서에 근무하는 모든 사원의 동료를 출력하시오. (부서ID, 사원의이름, 동료의 이름)
![](https://velog.velcdn.com/images/syshin0116/post/056d496d-b136-4a26-863c-0396d87946f7/image.png)

#### Exam8) 
HR 부서에서 직책 등급 및 급여에 대한 보고서를 요구한다. JOB_GRADES 테이블에 익숙해지도록 먼저 JOB_GRADES 테이블의 구조를 표시하고, 모든 사원의 이름, 직무, 부서 이름, 급여 및
등급을 출력하시오.

### 6.5 노트
- JOIN 할때 기준컬럼에 NULL 값이 없는지 확인해야함 (NULL값이면 제외되고 JOIN됨)
	- count(*) over() 총수 를 사용하여 쉽게 확인 가능 (아직 안배움)
- ALIAS를 사용하는 습관을 들이는것이 바람직하다
- JOIN은 기본값으로 INNER JOIN으로 진행된다

![](https://velog.velcdn.com/images/syshin0116/post/9bedc676-7897-429a-988f-74a9a2bcfc3a/image.png)

#### 오라클 형식의 JOIN
WHERE 절에 ON절 쿼리를 쓸 수 있다
```sql
SELECT 	employee_id, city, department_name
FROM 	employees e, departments d, locations
WHERE 	d.department_id = e.departemnt_id
AND 	d.location = l.location_id;
```

## 7. 서브쿼리 활용

### 7.1 목표
- SUBQUERY 이해
- 단일 행 SUBQUERY
- 다중 행 SUBQUERY
- INLINE VIEW 활용
- [연습문제]

### 7.2 What is a Subquery?
#### - 서브 쿼리
	- **서브 쿼리란 하나의 SQL문안에 포함되어 있는 또 다른 SQL**
	- 서브 쿼리는 반드시 **괄호 ()** 로 감싸져 있어야 한다
#### - 장점
	- 쿼리를 구조화 시키므로 **쿼리의 각 부분들을 명확히 구분**할 수 있다
	- JOIN, UNION 보다 **가독성**이 좋다
#### - 서브 쿼리 종류 ( 쿼리 위치에 따라 종류가 나뉜다 )
	- 서브쿼리 or 중첩 서브쿼리 ( Neseted Subquery) : WHERE 에서 사용
	- 인라인 뷰 ( Inline View ) : FROM 에서 사용
	- 스칼라 서브쿼리 ( Scalar Subquery) : SELECT 에서 사용
#### - 서브 쿼리 실행 순서
	- 서브 쿼리가 실행 된 후에 메인 쿼리가 실행됨
    
### 7.3 Using Subquery
#### Subquery를 사용한 문제 해결 > Unknown condition
- **“Abel보다 급여를 더 많이 받는 사원은 누구입니까?”** 라는 문제

![](https://velog.velcdn.com/images/syshin0116/post/e790724e-25d9-4316-83a7-6282627f68dc/image.png)
    
#### Subquery를 사용한 문제 해결
- **조회할 때마다 **알 수 없는 값을 서브쿼리로 구해서 **WHERE절에서 메인쿼리의 조건으로 사용**된다.
```sql
SELECT 	last_name, salary
FROM 	employees
WHERE 	salary > 
			(SELECT 	salary
			FROM 	employees
			WHERE 	last_name = 'Abel');
```
![](https://velog.velcdn.com/images/syshin0116/post/d75ac935-9129-4ba9-b171-de7885f0d031/image.png)
#### Subquery Type
- Single-row subquery
- Multiple-row subquery

![](https://velog.velcdn.com/images/syshin0116/post/118bd813-d9d9-415b-8cb6-0b9df000dd4e/image.png)
### 7.4 Using Subquery – single row subquery
#### 단일 행 Subquery
- 한 행만 반환
- 단일 행 비교 연산자를 사용
![](https://velog.velcdn.com/images/syshin0116/post/d7f1a3a7-6247-4cab-a7c0-8b953afa1a1e/image.png)

#### Exam)
141번 사원의 직무 ID와 동일한 직무 ID를 가진 사원을 출력하시오.
![](https://velog.velcdn.com/images/syshin0116/post/6f5a90eb-bd54-4652-b1fd-da97748f6d72/image.png)

#### Subquery Exam : Abel 과 직무가 같고, 급여는 더 많은 사원을 출력. Taylor 와 직무가 같고, 급여는 더 많은 사원을 출력.

```sql
SELECT 		last_name, job_id, salary
FROM 		employees
WHERE 		job_id =
				(SELECT 	job_id
				FROM 		employees
				WHERE 	last_name = Abel')
AND salary >
				(SELECT 	salary
				FROM 		employees
				WHERE 		last_name = Abel');
```
![](https://velog.velcdn.com/images/syshin0116/post/12dad93d-0211-4797-9517-f6889ca5cc7b/image.png)

#### 수업중 서브쿼리 연습문제1
#### LAST_NAME 이 Zlotkey(즐로키)와 동일한 부서에 근무하는 모든 사원들의 사번 및 고용날짜를 조회한다.
단, 결과값에서 Zlotkey 는 제외한다.
```sql
SELECT 	employee_id, hire_date
FROM 	employees
WHERE 	department_id = 
                    (SELECT department_id
                    FROM employees
                    WHERE last_name = 'Zlotkey')
and last_name <> 'Zlotkey';
```
#### Subquery Exam: 전체 사원의 최저 급여와 똑같은 급여를 받는 모든 사원의 성, 직무 ID 및 급여를 출력.

```sql
SELECT 	last_name, job_id, salary
FROM 	employees
WHERE 	salary =
			(SELECT MIN(salary)
FROM 	employees);
```
![](https://velog.velcdn.com/images/syshin0116/post/2977e185-dc4b-4635-be54-a57d47c9f687/image.png)


#### Subquery Exam: 부서ID 50의 최저급여 보다 최저 급여가 큰 모든 부서를 출력
```sql
SELECT 		department_id, MIN(salary)
FROM 		employees
GROUP BY 	department_id
HAVING 		MIN(salary) >
				(SELECT MIN(salary)
				FROM employees
				WHERE department_id = 50)
```
![](https://velog.velcdn.com/images/syshin0116/post/44463ce7-a7dd-4480-9efd-48b0963e9cb0/image.png)

#### 수업중 서브쿼리 연습문제2
#### 회사 전체 평균 급여 보다 더 많이 받고 LAST_NAME 에 u 가 있는 사원들이 근무하는 부서에서 근무하는 사원들의 사번, LAST_NAME 및 급여를 조회한다.

```sql
SELECT  employee_id, last_name, salary
FROM    employees
WHERE   department_id IN (
                        SELECT department_id
                        FROM employees
                        WHERE last_name LIKE '%u%' )
        AND salary > 
                    (SELECT AVG(salary)
                    FROM employees);
```
![](https://velog.velcdn.com/images/syshin0116/post/47182529-cde4-499f-87c6-1a16c25e2034/image.png)



#### Subquery Quiz : 평균 급여가 가장 낮은 직무를 찾습니다.
![](https://velog.velcdn.com/images/syshin0116/post/0ad33997-1d1d-4e8a-ae8a-e13d490fbb54/image.png)

```sql
SELECT 		job_id, AVG(salary)
FROM 		employees
GROUP BY 	job_id
HAVING 		AVG(salary) = (SELECT MIN(AVG(salary))
							FROM employees
							GROUP BY job_id);
```
평균 급여가 가장 높은 부서의 부서 번호와
해당 부서의 최저 급여를 표시하는 보고서를 작성하시오.
![](https://velog.velcdn.com/images/syshin0116/post/5a7f77a9-9d2a-48d9-9992-43152e5c76e3/image.png)

![](https://velog.velcdn.com/images/syshin0116/post/2bc5138f-a151-4eb7-9386-423ea1b3e68a/image.png)

### 7.5 Using Subquery – multi row subquery
#### 다중 행 Subquery
- 두 개 이상의 행을 반환
- 여러 행 비교 연산자 사용

![](https://velog.velcdn.com/images/syshin0116/post/ef31e735-7eb2-469a-b0f3-96bca8c794b3/image.png)


#### 다중 행 Subquery : ANY 연산
- IT 프로그래머가 아닌 사원 중 급여가 IT 프로그래머보다 적은 사원은?
```sql
SELECT 		employee_id, last_name, job_id, salary
FROM 		employees
WHERE 		salary < ANY
					(SELECT 	salary
					FROM 	employees
					WHERE 	job_id = 'IT_PROG')
					AND 	job_id <> 'IT_PROG';
```
![](https://velog.velcdn.com/images/syshin0116/post/7325c7dd-2244-43d7-a7a2-63762675b714/image.png)

- any: OR의 의미 (하나만 만족하면 됨)
- all: AND의 의미 (모두 만족해야 됨)

#### 다중 행 Subquery : ALL 연산
- 직무 ID가 IT_PROG인 모든 사원보다 급여가 적고 직무가 IT_PROG가 아닌 사원은?
```sql
SELECT 	employee_id, last_name, job_id, salary
FROM 	employees
WHERE 	salary < ALL
				(SELECT 	salary
				FROM 	employees
				WHERE 	job_id = 'IT_PROG')
				AND 	job_id <> 'IT_PROG';
```
![](https://velog.velcdn.com/images/syshin0116/post/436b9ff8-2b14-458d-86c1-860a82c12130/image.png)

### 7.6 Using the EXISTS Operator

#### 다중 행 Subquery : EXISTS 연산
- EXITS연산자는 **서브 쿼리 내에서 집합의 존재 여부만 판단.**
- 존재 여부만을 판단하므로 연산 시 부하가 많이 줄어든다
```sql
SELECT 	* 	
FROM 	departments
WHERE 	NOT EXISTS
		(SELECT 	1 
        FROM 		employees
		WHERE 		employees.department_id = departments.department_id);
```
- 부서 테이블에서 사원 테이블의 부서ID가 존재하지 않는 것만 출력 
	- **즉, 사원이 없는 부서들만 출력됨**
- EXISTS 연산자는 JOIN으로도 구현 할 수 있음
- EXISTS 연산자는 교집합을 NOT EXISTS 연산자는 차집합을 표현 가능

- 메인 쿼리서 사용하는 테이블을 서브쿼리에서 사용할 수 있다


### 7.7 Using Inline view
#### Inline view

- **FROM 절에 있는 서브쿼리**를 인라인 뷰라고 한다.
- **해당 쿼리의 구문 안에서만 사용 가능한 가상의 테이블**이란 의미
- FROM 절에 있는 인라인뷰는 자주 **별칭을 사용**
- 효율적인 검색 가능

#### Exam) 
20번 부서의 평균급여보다 큰 급여를 갖는 사원이고 매니저인 사원
단 20번 부서의 사원은 출력 하지 않음

```sql
SELECT 	b.employee_id, b.last_name, b.salary, b.department_id
FROM 	(SELECT employee_id
		FROM 	employees
		WHERE salary >	(SELECT AVG(salary)
						FROM employees WHERE department_id = 20)) a
JOIN 	employees b -- 매니저 테이블로 사용
ON 		a.employee_id = b.employee_id
AND 	b.manager_id is NOT NULL
AND 	b.department_id <> 20;
```
![](https://velog.velcdn.com/images/syshin0116/post/504136dc-80fe-466b-a432-f16385b133f7/image.png)

### 7.8 Top-N 구문
![](https://velog.velcdn.com/images/syshin0116/post/ff5b8ed8-1b43-4e8c-bf5f-bec587ea8255/image.png)

### 7.9 Top-N 절의 Analyze Function 적용
```sql
SELECT employee_id, last_name, salary,
		RANK() OVER(ORDER BY salary DESC) AS RANK,
		DENSE_RANK() OVER(ORDER BY salary DESC) AS DENSE_RANK,
		ROW_NUMBER() OVER(ORDER BY salary DESC) AS ROW_NUMBER
FROM employees;
```
![](https://velog.velcdn.com/images/syshin0116/post/cef61300-e659-4df5-b21d-72e0b9579d48/image.png)

### 7.10 Top-N 절의 Analyze Function 적용
```sql
SELECT DEPARTMENT_ID,
		RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS RANK,
		DENSE_RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS DENSE_RANK,
		ROW_NUMBER() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS ROW_NUMBER,
        SALARY
FROM 	EMPLOYEES
ORDER BY 1;
```

![](https://velog.velcdn.com/images/syshin0116/post/105ef22a-b098-4b4c-b1db-0285037c65d5/image.png)


### 7.11 Subquery Exam

#### 6~10위 사이의 급여 랭킹을 구하시오.
(1. Top-N절 사용 2.분석함수 사용)
```sql
-- Top-N
SELECT ranking, employee_id, last_name, salary
FROM (SELECT rownum ranking, employee_id, last_name, salary
FROM (SELECT employee_id, last_name, salary
FROM employees order by salary desc))
WHERE ranking between 6 and 10;

-- Analyze Function
SELECT rank, employee_id, last_name, salary
FROM (SELECT employee_id, last_name, salary
, row_number() over(order by salary desc) as rank
FROM employees)
WHERE rank between 6 and 10;
```

![](https://velog.velcdn.com/images/syshin0116/post/1c991e83-941c-496d-80df-598673013f28/image.png)

#### Q) 사원명, 급여, 부서번호와 해당 부서의 평균급여를 사번, 부서순으로출력하시오 (대기 발령자 제외)
```sql
SELECT 	e1.last_name, e1.salary, e1.department_id,
		TO_CHAR(AVG(e2.salary), '$999,999.0') as avg_sal
FROM 	employees e1 JOIN employees e2
ON 		e1.department_id = e2.department_id
GROUP BY e1.employee_id, e1.last_name, e1.salary, e1.department_id
ORDER BY e1.department_id, e1.employee_id;
```
![](https://velog.velcdn.com/images/syshin0116/post/13602641-07e8-4269-85db-5274f4926ebf/image.png)

#### Q) 사원 테이블에 사원명과 급여, 급여등급을 출력하려고 한다. 급여등급은 월급이 상위 25% 까지는 A 등급, 25% ~ 50% 까지는 B 등급, 50% ~ 75% 까지는 C 등급, 75% ~ 100% 까지는 D 등급

```sql
select last_name, salary
		, case 	when rownum between 0 and g1 then 'A'
				when rownum between g1 + 1 and g2 then 'B'
				when rownum between g2 + 1 and g3 then 'C'
				when rownum between g3 + 1 and g4 then 'D'
		end sal_grade, rownum, t_cnt, g1, g2, g3, g4
From (
		select * from employees
		order by salary desc) e
cross join (
		SELECT count(*) t_cnt
			, round((count(*) / 4)) g1
			, round((count(*) / 4) * 2) g2
			, round((count(*) / 4) * 3) g3
			, round((count(*) / 4) * 4) g4
FROM employees ) m
order by salary desc;
```
![](https://velog.velcdn.com/images/syshin0116/post/6354dc49-06a2-456f-9988-c038925dc310/image.png)

### 7.12 Using Subquery (연습문제)
#### Exam1) 
전체사원의 평균급여보다 큰 급여를 받는 사원에 대해서 사번, 성, 급여를 급여 오름차순으로 출력

#### Exam2) 
전체사원의 평균급여보다 큰 급여를 받고 성에 'u'가 들어간 부서의 사원에 대해서 사번, 성, 급여를 급여 오름차순으로 출력

#### Exam3) 
King(사번100)에게 보고하는 모든 사원의 성과 급여를 출력하시오

#### Exam4)
부서 60의 사원보다 급여가 많은 모든 사원 리스트를 출력하시오.

#### Exam5) 
도시 이름이 'T' 로 시작하는 지역에 사는 사원들의 사번, LAST_NAME 및 부서 번호를 조회하시오. 단, join을 사용하지 말고 subquery로 작성하시오.

#### Exam6) 
요일 (월,화,수요일...) 별 고용된 인원이 가장 많은 요일(들)과 동일한 요일에 고용된 모든 사람들의 LAST_NAME 및 요일을 조회 하시오.

#### Exam7) 
가장 많은 인원을 보유하고 있는 부서의 인원수와 동일한 부서의 부서번호, 부서이름 및 부서 별 인원수를 조회하시오.

#### Exam8) 
미국에서 근무하고 있는 사원들의 평균급여 보다 많은 사원에 대한 성명, 직무타이틀을 출력하시오.

#### Exam9) 
모든 사원의 사번, 성, 급여, 부서ID, 해당 부서의 평균 급여를 출력하시오.추가적으로 대기 발령중인 사원 정보를 포함 하시오. 사번으로 정렬 하시오.

#### Exam10) 
자신이 근무하는 부서의 평균급여보다 급여를 많이 받는 사원의 성, 급여, 부서ID, 해당부서의 평균급여를 출력하시오. (from절 상의 subquery)

#### Exam11) 
모든 사원의 사번, 성, 부서 이름 출력하시오. 단, 부서가 없는 사원도 출력, 사번으로 정렬, 스칼라 subquery를 사용하여 SELECT 문에서 부서 이름을 검색

### [보조자료] 7장 서브쿼리(SQL예제,연습문제답)
[[보조자료] 7장 서브쿼리(SQL예제,연습문제답).txt](https://github.com/syshin0116/Study/files/11469194/7.SQL.txt)

### Notes
#### RANK, DENSE_RANK, ROWNUM 차이점(SQLD에 자주 나옴!!)
```sql
-- RANK, DENSE_RANK, ROWNUM 차이점

SELECT employee_id, last_name, salary,
    RANK()      OVER(ORDER BY salary DESC) AS RANK,
    DENSE_RANK()    OVER(ORDER BY salary DESC) AS DENSE_RANK,
    ROW_NUMBER()    OVER(ORDER BY salary DESC) AS ROW_NUMER
FROM employees;
```

![](https://velog.velcdn.com/images/syshin0116/post/f42c8adb-ef9d-4255-8d3e-497f34d909f2/image.png)

#### 부서별 급여가 많은 순으로 정렬하여 출력
```sql
-- 부서별 급여가 많은 순으로 정렬하여 출력
SELECT DEPARTMENT_ID,
        RANK()          OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS RANK,
        DENSE_RANK()    OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS DENSE_RANK,
        ROW_NUMBER()    OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS ROW_NUMBER,
        SALARY
FROM    EMPLOYEES
ORDER BY 1;
```
![](https://velog.velcdn.com/images/syshin0116/post/68dc2041-c667-416d-aed5-b64e560b1e11/image.png)


