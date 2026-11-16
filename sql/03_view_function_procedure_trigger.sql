-- 원본: 쿼리 #3.sql
-- 뷰, 날짜 함수, 사용자 정의 함수, 프로시저, 트리거 호출

-- view --
SELECT * FROM student_view;
SELECT * FROM student_rank;

-- print --
SELECT NOW();

-- current date, time --
SELECT CURDATE();
SELECT CURTIME();

# 날짜 데이터는 입력은 문자열 -> 계산은 특별한 수식에 의해 계산
SELECT DATE_SUB("2016-02-08", INTERVAL 60 DAY);
SELECT DATEDIFF("2016-01-01 23:59:59", "2016-01-03");
SELECT DATE_ADD("2016-01-04 23:59:59", INTERVAL 22 SECOND);

SELECT calc(10,20,'+');
SELECT calc_distance(90,80,70,80,80,80);
SELECT calc_distance(90,80,70,80,90,70);
SELECT calc_grade(90,80,70);

-- procedure --
CALL student_select();
CALL student_multi_select();

-- trigger --
INSERT INTO student(NAME, kor, mat, eng, schoolcode) VALUES ("트리거", 90,90,90,'CH00000001');
UPDATE student SET kor=100, mat=100, eng=100 WHERE NAME = '트리거';

-- insert 호출 --
/*
SET @abc = 0;
CALL student_insert("테스트", 90, 80, 100, 'CH00000001',@abc);
SELECT @abc;
CALL student_insert("테스트", 90, 80, 100, 'AB00000001',@result);
SELECT @result; -> 결과값 = -1

*/
CALL student_insert("테스트", 90, 80, 100, 'CH00000001',@result);
SELECT @result;
