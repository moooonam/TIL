# DB...

> ## SQL
<br>

- "Structured Query Language"
- RDBMS(관계형 데이터베이스 관리 시스템)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어 
- SQL은 데이터베이스와 상호작용하는 방법
- SQL commands 종류
  1. DDL(Data Definition Language)
  2. DML(Data Manipulation Language)
  3. DCL(Data Control Language)


|분류|개념|SQL키워드|
|------|---|---|
|DDL-데이터 정의 언어|관계형 데이터베이스 구조를 정의(생성, 수정 및 삭제)하기 위한 명령어|CREATE,DROP,ALTEL|
|DML-데이터 조작 언어|데이터를 조작(추가,조회,변경,삭제)하기 위한 명령어|INSERT,SELECT,UPDATE,DELETE|
|DCL-데이터 제어 언어|데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어|GRANT,REVOKE,COMMIT,ROLLBACK|

- CREATE TABLE

```SQL
CREATE TABLE table_name(
    column_1 data_type constraints,
    column_2 data_type constraints,
    column_2 data_type constraints,
);

-- DDL.sql

CREATE TABLE contacts(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE,
);
```
- Data Types 종류
  1. NULL
     - 정보가 없거나 알 수 없음을 의미
  2. INTEGER
     - 정수
     - 크기에 따라 0,1,2,3,4,6또는 8바이트와 같은 가변 크기를 가짐
  3. REAL
     - 실수
     - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
  4. TEXT
     - 문자 데이터
  5. BLOB(Binary Large Object)
     - 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
     - 바이너리 등 멀티미디어 파일(이미지 데이터 등등)
  - SQLite에는 별도의 Bollean 타입이 없음
  - 대신 Boolean 값은 정수 0(false)과 1(true)로 저장됨
  
- SQLite Datatypes 특징
  - 동적 타입 시스템(dynamic type system)을 사용  
  - 컴럼에 선언된 데이터 타입에 의해서가 아니라 컬럼에 저장된 값에 따라 데이터 타입이 결정됨
  - 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 되지만 데이터 타입을 지정하는 것을 권장

- Constraints
  - "제약조건"
  - 입력하는 자료에 대해 제약을 정하고 제약에 맞지 않다면 입력이 거부됨 
  - 데이터 무결성
    - 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
    - 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적
- Constraints 종류
  1. NOT NULL
     - 컬럼이 NULL값을 허용하지 않도록 지정
     - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함 
  2. UNIQUE
       - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
  3. PRIMARY KEY
       - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
       - 각 테이블에는 하나의 기본 키만 있음
       - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
       - 
  4. AUTOINCREMENT
       - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
- ALTER TABLE
  - "Modify the structure of an existing table."
  - 기존 테이블의 구조를 수정
  - Rename, Add, Delete 등등

```SQL
-- DDL.sql

ALTER TABLE contacts RENAME TO new_contacts;
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
ALTER TABLE new_contacts DROP COLUMN address;
-- 삭제는 컬럼이 다른 부분에서 참조되는경우,PK값인경우, UNIQUE 제약 조건이 있는 경우 삭제하니 못함
```

```SQL

-- DML.sql
-- 이름과 나이 조회
SELECT first_name, age FROM users;

-- 이름과 나이를 나이가 어린 순서대로 조회하기
SELECT first_name, age FROM users ORDER BY age ASC;

-- 이름과 나이를 나이가 많은 순서대로 조회하기
SELECT first_name, age FROM users ORDER BY age DESC;

-- 이름,나이,계좌 잔고를 나이가 어린순으로, 만약 같다면 계좌 잔고가 많은 순으로 조회
SELECT first_name, age FROM users ORDER BY age ASC, balance DESC;

-- 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;

-- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users;

-- 나이가 30살 이상인 사람들의 이름 나이 계좌잔고 조회하기
SELECT DISTINCT first_name, age, balance FROM users WHERE age >= 30;

```
- % wildcard
  - "영%" 영으로 시작하는 모든 문자열과 일치
  - "%도" 도로 끝나는 모든 문자열과 일치
  - "%강원%"패턴은 강원을 포함하는 모든 문자열과 일치
- '_' wildcard
  - '영_' 영으로 시작하고 총 2자리인 문자열과 일치
  - '_도' 도로 끝나고 총 2자리인 문자열과 일치

```SQL

-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT DISTINCT first_name, last_name FROM users WHERE first_name LIKE '%호%';

-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users WHERE country IN ('경기도', '강원도');

-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT DISTINCT first_name, age FROM users WHERE age >= 20 AND age <= 30;

-- 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name FROM users LIMIT 10;
```

- INSERT statement
```SQL

INSERT INTO table_name (col1, col2, ...)
VALUES (value1, value2, ...);
-- 컬럼 목록을 생략하는 경우 값 목록의 모든 칼럼에 대한 값을 지정해야함
```
- UPDATE
```SQL
-- 2번 데이터의 이름을 '김철수' 주소를 '제주도'로 수정하기
UPDATE classmates
SET name='김철수', 
    address='제주도'
WHERE rowid =2;
```
<br>
<hr>
<br>
