-- 원본: 쿼리 #2.sql
-- school / student 테이블: WHERE, LIKE, IN, 서브쿼리, JOIN, 집계함수, GROUP BY,
-- 사용자 변수, 테이블 백업, CASE / IF 로 학점 계산

-- SELECT * FROM school;
-- SELECT * FROM student;

INSERT INTO school(schoolname, address, schoolcode, studentcount)
VALUES("충주여자고등학교", "충주시", "CH00000001",360);

INSERT INTO school(schoolname, address, schoolcode, studentcount)
VALUES("서울여자고등학교", "서울시", "SE00000001",1200);

INSERT INTO school(schoolname, address, schoolcode, studentcount)
VALUES("대전고등학교", "대전시", "IC00000001",560);

-- SELECT * FROM school;
# 입력이 안됨 -- 유일 코드가 중복
-- INSERT INTO school(schoolname, address, schoolcode, studentcount) VALUES("천안고등학교", "아산시", "IC00000001",560);

SELECT * FROM school;
SELECT * FROM school WHERE schoolcode = "CH00000001";

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('김만덕', 100,99,99,"CH00000001");

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('고려인', 100,99,99,"CH00000001");

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('전공인', 81,81,81,"SE00000001");

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('전공이', 81,81,81,"SE00000001");

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('전공삼', 91,100,100,"CH00000001");

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('전공사', 100,100,100,"CH00000001");

INSERT INTO student(NAME, kor, mat, eng, schoolcode)
VALUES('종로구', 100,81,71,"IC00000001");

-- SELECT * FROM student;

SELECT NAME, kor, mat, eng FROM student WHERE NAME='김만덕';
# 별칭
SELECT NAME AS '이름', kor AS '국어', mat AS '수학', eng AS '영어'
FROM student WHERE NAME = '김만덕';
SELECT NAME, schoolcode FROM student WHERE NAME='고려인';

# in 연산자 ( 포함 )
SELECT NAME, kor, mat, eng FROM student
WHERE schoolcode IN ("SE00000001","IC00000001")

# subquery ( 괄호로 묶어줌 )
SELECT NAME, kor, mat, eng FROM student WHERE schoolcode IN (SELECT schoolcode FROM school);

# 문자검색 ( r%:전문자, _단일문자에 대응 )
SELECT NAME, kor, mat, eng FROM student WHERE NAME LIKE '김%';
SELECT NAME, kor, mat, eng FROM student WHERE NAME LIKE '%종%';
SELECT NAME, kor, mat, eng FROM student WHERE NAME LIKE '_종_';

# 논리연산자
SELECT * FROM student WHERE kor > 90 AND mat > 90 AND eng > 90;
SELECT * FROM student WHERE kor > 90 or mat > 90 or eng > 90;

# 출력 수를 제한
SELECT * FROM student WHERE kor between 60 AND 90 LIMIT 2;

# 중복을 제거하고
SELECT DISTINCT NAME FROM student;

# 함수의 사용
SELECT COUNT(*) AS '학생수' FROM student;
SELECT CONCAT(NAME, '님') AS '이름', kor AS '국어', mat AS '수학', eng AS '영어' FROM student WHERE NAME='전공인';

-- 문제 --

# 전체 학생을 이름 기준으로 내림차순으로 출력
SELECT * FROM student ORDER BY NAME DESC;

# 이름 중복을 제외하고 2명만 출력
SELECT DISTINCT NAME FROM student LIMIT 2;

# 모든 학생의 이름과 합계점수와 평균점수를 출력하시요
SELECT NAME, (kor+mat+eng), ROUND((kor+mat+eng)/3,2) FROM student;

# 학생의 이름, 평균, 학교이름을 출력하시요 (join)
SELECT st.NAME, ROUND((st.kor+st.mat+st.eng)/3,2), sc.schoolname FROM student st INNER JOIN school sc
ON st.schoolcode = sc.schoolcode; -- join의 조건은 ON

# 국어평균, 수학평균, 영어평균
SELECT SUM(kor), SUM(mat), SUM(eng) FROM student;
SELECT AVG(kor), AVG(mat), AVG(eng) FROM student;
SELECT SUM(kor+mat+eng), AVG(kor + mat + eng) FROM student;

-- 연산의 원칙에 연산시 NULL이 하나라도 있으면 결과는 NULL
-- 10 + 20 + NULL -> 결과 NULL

# 변수와 초기값
SELECT NAME, IFNULL(kor,0) + IFNULL(mat,0) + IFNULL(eng,0) FROM student;

# 학교별로 과목별 합계
SELECT SUM(kor), SUM(mat), SUM(eng) FROM student GROUP BY schoolcode;

# 학교별로 총점의 합계 ( 시험안본 학생(NULL) 고려 )
SELECT schoolcode, SUM(IFNULL(kor,0) + IFNULL(mat,0) + IFNULL(eng,0)) FROM student GROUP BY schoolcode;

# 학교 이름별로 총점의 합계 ( 시험안본 학생(NULL)을 고려 )
SELECT sc.schoolname, IFNULL(SUM(IFNULL(st.kor,0) + IFNULL(st.mat,0) + IFNULL(st.eng,0)), 0) AS total_sum
FROM school sc JOIN student st ON st.schoolcode = sc.schoolcode
GROUP BY sc.schoolcode, sc.schoolname;

# 위 계산을 충주여자고등학교에 적용하시요
SELECT sc.schoolname,
IFNULL(SUM(IFNULL(st.kor,0) + IFNULL(st.mat,0) + IFNULL(st.eng,0)), 0) AS total_sum
FROM school sc
JOIN student st ON st.schoolcode = sc.schoolcode
WHERE sc.schoolname = '충주여자고등학교'
GROUP BY sc.schoolcode, sc.schoolname;

-- 변수 사용법
-- @@ : 시스템변수, @ : 사용자 변수
SELECT schoolcode INTO @abc FROM school WHERE schoolname = '충주여자고등학교';
SELECT SUM(kor), SUM(mat), SUM(eng) FROM student WHERE schoolcode = @abc;

SELECT SUM(kor), SUM(mat), SUM(eng) FROM student
 WHERE schoolcode = ( SELECT schoolcode FROM school
 WHERE schoolname = '충주여자고등학교');

-- 테이블 백업
CREATE TABLE if NOT EXISTS se_backup AS
 SELECT * FROM student
 WHERE schoolcode = ( SELECT schoolcode FROM school
 WHERE schoolname = '충주여자고등학교');

ALTER TABLE se_backup ADD PRIMARY KEY (bunho);
ALTER TABLE se_backup;

-- 빈 필드 채우기 ( 합계와 평균 )
-- 모든 필드에 적용
UPDATE student SET total = IFNULL(kor, 0) + IFNULL(mat, 0) + IFNULL(eng, 0);
UPDATE student SET average = round(total/3,2);

-- 이름과 학점을 출력
SELECT NAME , (case when (average >= 90) then 'A'
 when (average >= 80 AND average < 90) then 'B'
 when (average >= 70 AND average < 80) then 'C'
 when (average >= 60 AND average < 70) then 'D'
 ELSE 'F' END) AS '등급' FROM student;

-- ADD CONSTRAINT fk_student_schoolcode
-- FOREIGN KEY (schoolcode) REFERENCES school(schoolcode)
-- ON UPDATE CASCADE
-- ON DELETE RESTRICT;

-- 3항 연산자 (if 조건, 참일때, 거짓일 때)
-- if 조건, 참일때, if 조건, 참일때, if 조건, 참일때, 거짓일 때
SELECT NAME , ( if(average >= 90,'A',
 if(average >= 80,'B',
 if(average >= 70,'C',
 if(average >= 60,'D', 'F'))))) AS '학점' FROM student;

-- 문제 2 --

# 학점을 평균으로 판정해서 수정하시요
-- ALTER TABLE student ADD COLUMN `학점` CHAR(1); -- 학점 = `학점` 동일
-- ALTER TABLE student DROP COLUMN `학점`;
UPDATE student
SET grade = IF(average >= 90, 'A',
 IF(average >= 80, 'B',
 IF(average >= 70, 'C',
 IF(average >= 60, 'D', 'F'))));

SELECT * FROM student;

-- 문제 3 --

# 학교 이름을 출력하고 학생들의 이름, 총점, 평균, 학점이 입력된
# 국어, 영어, 수학 점수로 부터 계산해서 출력
/*
SELECT st.name AS 이름, sc.schoolname AS 학교이름, (IFNULL(st.kor,0) + IFNULL(st.mat,0) + IFNULL(st.eng,0)) AS 총점,
 ROUND((IFNULL(st.kor,0) + IFNULL(st.mat,0) + IFNULL(st.eng,0))/3,2) AS 평균,
 IF(st.average >= 90, 'A',
 IF(st.average >= 80, 'B',
 IF(st.average >= 70, 'C',
 IF(st.average >= 60, 'D', 'F')))) AS '등급'
 FROM student st INNER JOIN school sc
ON st.schoolcode = sc.schoolcode;
*/
