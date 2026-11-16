-- 원본: 쿼리.sql
-- person_info 테이블 기본 CRUD (INSERT / SELECT / UPDATE / DELETE)

-- SHOW DATABASES;
-- USE person_info;
-- SHOW TABLES;

INSERT INTO person_info(NAME, age, address, job, phone) VALUES
('홍길동', 35, '서울특별시 강남구', '개발자', '010-1234-5678'),
('김영희', 28, '부산광역시 해운대구', '디자이너', '010-2345-6789'),
('이철수', 42, '대구광역시 수성구', '마케터', '010-3456-7890'),
('박민정', 31, '서울특별시 송파구', '교사', '010-4567-8901'),
('최강현', 55, '경기도 성남시 분당구', '의사', '010-5678-9012');
INSERT INTO person_info(NAME, age, address) VALUES('김대한', 130, '대전');
INSERT INTO person_info(NAME, age, address) VALUES("김만세대한민국영원하다", 17, "대전");
-- 필드 이름을 comma로 분리
SELECT id, NAME, age, address, job, phone FROM person_info;
SELECT id, NAME, phone FROM person_info;
SELECT * FROM person_info;
SELECT NAME, age, address FROM person_info WHERE address LIKE '서울%';
SELECT NAME, age, job FROM person_info WHERE age >= 55;
SELECT COUNT(*) FROM person_info; -- 데이터 베이스에도 함수가 있음
SELECT "김종호";

SELECT job, COUNT(*) AS 인원수 FROM person_info GROUP BY job;
SELECT NAME, age FROM person_info ORDER BY age; -- ascending 오름차순
SELECT NAME, age FROM person_info ORDER BY age DESC;
-- 업데이트 조건이 중요하다 ex where name = '홍길동'
UPDATE person_info SET phone='010-0000-0000' WHERE NAME = '홍길동';
-- 박민정을 찾아서 주소를 "서울특별시 서초구" 로 변경하시오
UPDATE person_info SET address='서울특별시 서초구' WHERE NAME = '박민정';
-- 40세 이상은 직업을 고문으로 수정하시요
UPDATE person_info SET job='고문' WHERE age >= 40;

DELETE FROM person_info WHERE NAME = '홍길동';
DELETE FROM person_info WHERE age > 50;

-- DELETE FROM person_info; -- 구조는 남고 데이터만 삭제
SELECT * FROM person_info;

-- DROP TABLE person_info;
SELECT * FROM person_info;
-- unique key는 값이 유일해야 함
-- INSERT INTO person_info(NAME, age, address, job, phone) VALUESjsjs
-- ('오중복', 35, '서울특별시 강남구', '개발자', '010-1234-5678')
-- NULL을 허용하지 않는 데이터가 입력되지 않았기 때문 (address가 없음)
-- 필드 사이즈보다 크면 입력 불가
