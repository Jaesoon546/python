-- 원본: 쿼리 #5.sql
-- 병원 / 환자 / 진단 다대다 관계 (chaintable 연결 테이블, GROUP_CONCAT 조회, 중복 제거)

INSERT INTO hospital VALUES ('H1', '충주병원'), ('H2', '서울병원');

INSERT INTO patient VALUES
('P0001', '박재순', 'M', 27), ('P0002', '박지희', 'F', 24),
('P0003', '김성민', 'F', 30), ('P0004', '김현준', 'M', 36), -- ← 쉼표 추가
('P0005', '박재순순', 'M', 28), ('P0006', '박지희희', 'F', 25),
('P0007', '김성민민', 'F', 31), ('P0008', '김현준준', 'M', 37), -- ← 쉼표 추가
('P0009', '박박재순', 'M', 29), ('P0010', '박박지희', 'F', 26);

INSERT INTO diagnosis VALUES
('D001', '감기'), ('D002', '비염'), ('D003', '위염'),
('D004', '역류성식도염'), ('D005', '고혈압'), ('D006', '당뇨병'),
('D007', '고지혈증'), ('D008', '요통'), ('D009', '대상포진'),
('D010', '코로나');


-- 3. 조회
SELECT h.name AS 병원, p.name AS 환자, p.sex AS 성별, p.age AS 나이,
 GROUP_CONCAT(d.dxname SEPARATOR ', ') AS 병명
FROM chaintable c
JOIN hospital h ON c.hospitalid = h.hospitalid
JOIN patient p ON c.patientid = p.patientid
JOIN diagnosis d ON c.dxcode = d.dxcode
GROUP BY h.hospitalid, h.name, p.patientid, p.name, p.sex, p.age
ORDER BY h.hospitalid, p.patientid;

/*
INSERT INTO chaintable (hospitalid, patientid, dxcode) VALUES
('H1', 'P0001', 'D001'), ('H1', 'P0002', 'D002'),
('H1', 'P0003', 'D003'), ('H2', 'P0004', 'D004'),
('H2', 'P0005', 'D005'), ('H1', 'P0006', 'D006'),
('H1', 'P0007', 'D007'), ('H1', 'P0008', 'D008'),
('H2', 'P0009', 'D009'), ('H2', 'P0010', 'D010');
*/

INSERT INTO chaintable (hospitalid, patientid, dxcode) VALUES
('H1', 'P0001', 'D002'),
('H1', 'P0001', 'D005');

SELECT * FROM chaintable;

SELECT p.name AS 환자,
 GROUP_CONCAT(d.dxname) AS 병명
FROM chaintable c
JOIN patient p ON c.patientid = p.patientid
JOIN diagnosis d ON c.dxcode = d.dxcode
GROUP BY p.patientid, p.name;

/* #중복제거
DELETE c1
FROM chaintable c1
JOIN chaintable c2
 ON c1.hospitalid = c2.hospitalid
 AND c1.patientid = c2.patientid
 AND c1.dxcode = c2.dxcode
 AND c1.no > c2.no;
#중복되면 오류 발생하게 하기
ALTER TABLE chaintable
 ADD CONSTRAINT uq_chaintable UNIQUE (hospitalid, patientid, dxcode);
*/
