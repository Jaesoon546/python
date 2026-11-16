-- 원본: 쿼리 #6.sql
-- EMP/DEPT 조회 문제 (정렬, 조건, BETWEEN, LIKE), 문자열·숫자 함수,
-- GROUP BY / HAVING, JOIN, 이벤트 스케줄러

# 테이블이름과 필드이름은 대소문자 구분
SELECT * FROM DEPT;
SELECT * FROM EMP;
SELECT * FROM SALGRADE;

SELECT empno, ename, job FROM EMP;

-- 문제1 --
# EMP 테이블에서 사원번호, 급여, 부서번호를 출력하시오,
# 단 급여가 많은 순서대로 출력
SELECT empno, sal, deptno FROM EMP ORDER BY sal DESC;

# EMP 에서 직업과 급여를 출력하시오,
# 단 직업명은 오름차순, 급여는 내림차순으로 정렬
SELECT job, sal FROM EMP ORDER BY job ASC, sal DESC;

# EMP 에서 부서번호가 10번인 사원들의 급여를 출력하되
# 10% 인상된 금액으로 출력
SELECT sal * 1.1 FROM EMP WHERE deptno = 10;

# EMP 에서 급여가 3000 이상인 사람들의 모든 정보 출력
SELECT * FROM EMP WHERE sal >= 3000;

# 부서번호가 30번이 아닌(!=) 사람들의 이름과 부서번호를 출력
SELECT ename, deptno FROM EMP WHERE deptno != 30;

# emp 테이블에서 부서번호가 10번이고
# 급여가 3000이상인 사원들의 이름과 급여 출력
SELECT ename, sal FROM EMP WHERE deptno = 10 AND sal >= 3000;

# 직업이 salesman이거나 manager 인 사람의 사원번호와 부서번호 출력
SELECT empno, deptno FROM EMP WHERE job = 'SALESMAN' OR job = 'MANAGER';
SELECT empno, deptno FROM EMP WHERE job IN ('SALESMAN', 'MANAGER');

# 급여가 1000과 2000사이인 사원들의 사원번호와 이름 그리고 부서번호 출력
SELECT ename, empno, deptno FROM EMP WHERE sal >= 1000 AND sal <= 2000;
SELECT ename, empno, deptno FROM EMP WHERE sal BETWEEN 1000 AND 2000;

# 사원이름이 'FORD'와 'SCOTT' 사이의 사원들의 사원번호와 이름 출력
SELECT empno, ename FROM EMP WHERE ename>='FORD' AND ename<='SCOTT';
SELECT empno, ename FROM EMP WHERE ename BETWEEN 'FORD' AND 'SCOTT';

# 사원이름이 'J' 로시작하는 사원의 사원이름과 부서번호를 출력
SELECT ename, deptno FROM EMP WHERE ename LIKE 'J%';

# 입사일이 81년 생인 사원의 입사일과 사원번호를 출력하시오
SELECT empno , hiredate FROM EMP WHERE hiredate LIKE '1981%';

-- 함수 --
SELECT CHAR(65);
SELECT LOWER('HELLOW');
SELECT LPAD('HI', 10, '*');
SELECT LENGTH('국어');
SELECT LEFT('abcde',3); # 추출
SELECT RIGHT('abcde',3); # 추출
SELECT SUBSTRING('abcde', 2, 2); # 추출
SELECT ename, IFNULL(comm, 0) FROM EMP;
SELECT ABS(-10);
SELECT CEIL(3.1234); # 올림
SELECT FLOOR(3.6241); # 내림
SELECT ROUND(3.22645,2);

# 급여를 부서별로 합계를 내어서 부서번호와 급여합계를 출력하시오
# group by 할 때는 그룹대상 변수와 집계함수(sum, avg ...)만 가능함
SELECT deptno, SUM(sal) AS 급여합계 FROM EMP GROUP BY deptno;

# 부서별로 평균급여를 구해 그룹번호와 평균을 출력하시오
SELECT deptno, round(AVG(sal),2) AS 평균급여 FROM EMP GROUP BY deptno;

# 직업별로 최고 급여를 출력하시오
SELECT job, MAX(sal) AS 최고급여
FROM EMP
GROUP BY job;

# 급여가 1000이상인 사원들의 부서별 평균 급여의 반올림값을 부서번호로 내림차순 정령해서 출력
SELECT deptno, ROUND(AVG(sal),2) AS 평균급여
 FROM EMP
 WHERE sal >= 1000
 GROUP BY deptno
 ORDER BY deptno DESC;

# 각 부서별로 같은 업무를 하는 사람의 인원수를 구해서 부서번호, 업무, 인원수를
# 부서번호에 대해서 오른차순으로 정렬
SELECT deptno, job, COUNT(*) AS 인원수
 FROM EMP
 GROUP BY deptno, job
 ORDER BY deptno;

# 급여가 1000이상인 사원들의 부서별 평균 급여를 출력
# 단 부서별 평균 급여가 2000이상 (>=)인 부서만 출력하시오 (having)
SELECT deptno, ROUND(AVG(sal),2) AS 평균급여
 FROM EMP
 WHERE sal >= 1000
 GROUP BY deptno
 HAVING ROUND(AVG(sal),2) >= 2000;

# EMP 테이블의 모든 사원들의 이름, 부서번호, 부서명을 출력
SELECT e.ename, e.deptno, d.dname
 FROM EMP e
 JOIN DEPT d ON e.deptno = d.deptno;

-- event --
# 1. 테스트 데이터
INSERT INTO sensor_data(id, description, counter, last_updated)
VALUES (1, '초당 방문자 수', 0, NOW())
ON DUPLICATE KEY UPDATE counter = 0, last_updated = NOW();

# 2. 스케줄러 켜기
SET GLOBAL event_scheduler = ON;
SHOW VARIABLES LIKE 'event_scheduler';

# 3. 이벤트 활성화
ALTER EVENT sp_increment_counter ENABLE;

# 4. 몇 초 뒤에 여러 번 실행해서 counter가 오르는지 확인
SELECT * FROM sensor_data;
