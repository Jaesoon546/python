-- 원본: 쿼리 #7.sql
-- UNION 으로 과목별 통계, 백업 테이블에서 복원 (INSERT ... SELECT), 업데이트 백업 트리거 테스트

SELECT '국어' AS 과목,
 AVG(kor) AS 과목평균,
 MAX(kor) AS 과목최고,
 MIN(kor) AS 과목최소
FROM student
UNION
SELECT '영어', AVG(eng), MAX(eng), MIN(eng) FROM student
UNION
SELECT '수학', AVG(mat), MAX(mat), MIN(mat) FROM student;

# esxape 문자열 (\n, \t) heidisql에서 적용안됌
SELECT '국어', AVG(kor), MAX(kor), MIN(kor), "\n",
 '영어', AVG(eng), MAX(eng), MIN(eng), "\n",
 '수학', AVG(mat), MAX(mat), MIN(mat) FROM student;

CREATE TABLE student_backup LIKE student;

SELECT * FROM student_backup;
DELETE FROM student WHERE NAME = "종로구";
SELECT * FROM student_backup;

# values 없이 사용
INSERT INTO student (name, kor, mat, eng, schoolcode)
 SELECT name, kor, mat, eng, schoolcode
 FROM student_backup
 WHERE name = '종로구';

SELECT * FROM student WHERE NAME = '종로구';

-- 문제 2 --
# 업데이트를 백업하는 trigger 를 작성하시오

# trigger test
SELECT * FROM student LIMIT 5;
SELECT * FROM student_backup;
UPDATE student SET kor = kor + 1 WHERE bunho = 5;
SELECT * FROM student_backup WHERE action_log = 'UPDATE';
SELECT * FROM student WHERE bunho = 5;
UPDATE student SET kor = kor + 1 WHERE bunho = 7;

/*
SHOW KEYS FROM student_backup WHERE Key_name = 'PRIMARY';
ALTER TABLE student_backup
 MODIFY bunho INT NOT NULL,
 DROP PRIMARY KEY,
 ADD COLUMN log_id INT AUTO_INCREMENT PRIMARY KEY FIRST;
*/
