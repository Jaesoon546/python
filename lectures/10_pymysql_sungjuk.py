"""
10_pymysql-sungjuk.ipynb — PyMySQL로 MySQL(성적 DB) 연동 (2026/11/16 10회차)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# #pymaysql
# 20261116 직업훈련 10회차


# %% [1]
# !pip install pymysql


# %% [2]
# transaction 대상 : insert into, update, delete - commit
# ASCII code : 256가지 -> utf8 표준화
# 연결 -> 커서 얻기 -> sql 실행
# Database -> 중간객체(Resultset) -> python 자료구조
import pymysql
import os

# 접속 정보는 코드에 직접 쓰지 않고 환경변수로 받습니다 (공개 저장소 보호용).
#   export DB_HOST=<서버 IP>  DB_PASSWORD=<비밀번호>
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)
# conn2 = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
#                        db = 'project1', charset = 'utf8', autocommit=True)
# 예외처리
try:
  with conn.cursor() as cur: # 생성 인스턴스 자동 폐기 (자동해제)
    cur.execute("select * from student") # sql 실행
    rows = cur.fetchall() # 중간 만들어진 쿼리 결과에서 파이썬이 읽을 수 있도록 리턴
    desc = cur.description # 테이블에 대한 설명 (필드이름)
    for row in rows:
      print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')
finally: # try가 정상이던 비정상이던 마무리
  conn.close()
# 데이터베이스 객체, 네트워크 객체 -> OS에서 관리 -> 반드시 해제
print(desc)
print([i[0] for i in cur.description])


# %% [3]
# fetchone(1), fetchmany(여러개), fetchall(전부)
# DB형식 -> 리스트로 변경
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)
# resultset (DB와 형식 같음 )
try:
  with conn.cursor() as cur:
    cur.execute('SELECT * FROM student WHERE bunho in (5, 6, 7)')
    bunho, name, kor, mat, eng, total, average, grade, ranks, schoolcode = cur.fetchone()
    print(bunho, name, kor, mat, eng, total, average)
    # 갯수 일치
    bunho, name, kor, mat, eng, total, average, grade, ranks, schoolcode = cur.fetchone()
    print(bunho, name, kor, mat, eng, total, average)
    print(cur.fetchone()) # tuple로 리턴
    print(cur.fetchone()) # None 리턴
    print(cur.fetchone())
finally:
  conn.close()


# %% [4]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)
person = ("테스트", 80,90,100,'CH00000001')
try:
  with conn.cursor() as cur:
    cur.execute("""INSERT INTO student(name, kor, mat, eng, schoolcode)
    VALUES(%s, %s, %s, %s, %s)""",
    (person[0],person[1],person[2],person[3],person[4]))
    conn.commit()
    print("새로운 학생이 등록되었습니다. ")
finally:
  conn.close()


# %% [5]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)
person = ("typoon", 100,100,100,'CH00000001')
try:
  with conn.cursor() as cur:
    cur.execute("""INSERT INTO student(name, kor, mat, eng, schoolcode)
    VALUES(%s, %s, %s, %s, %s)""",
    (person[0],person[1],person[2],person[3],person[4]))
    conn.commit()
    print("새로운 학생이 등록되었습니다. ")
finally:
  conn.close()


# %% [6]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)

try:
  with conn.cursor() as cur:
    cur.execute("""UPDATE student SET name = %s WHERE name = %s""",('korea', 'typoon'))
    conn.commit()
    print("학생 이름이 korea로 변경되었습니다. ")
finally:
  conn.close()


# %% [7]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)
try:
  with conn.cursor() as cur:
    cur.execute("""DELETE FROM student WHERE name = %s""",('korea',))
    conn.commit()
    print("학생 데이터가 삭제되었습니다. ")
finally:
  conn.close()


# %% [8]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True)
try:
  with conn.cursor() as cur:
    cur.callproc('student_select')
    if(cur.rowcount): # 영향받은 행수 리턴
      print(cur.fetchall()) # tuple로 리턴
finally:
  conn.close()


# %% [9]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
# DictCursor : 데이터가 dict 형태로 리턴
data = ('둔산골', 90, 80, 100, 'CH00000001',0)
try:
  with conn.cursor() as cur:
    cur.callproc('student_insert', data)
    cur.execute('SELECT @_student_insert_5') # 성공실패확인
    conn.commit()
    result = cur.fetchone()
    print(result['@_student_insert_5']) # 1이면 성공, -1이면 실패
finally:
  conn.close()


# %% [10]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
# data = (7,'에이콘', 100, 90, 80,0)
data = ("둔산골","둔산동",0)
try:
  with conn.cursor() as cur:
    cur.callproc('student_update', data)
    cur.execute('SELECT @_student_update_2') # 자동으로 결정
    conn.commit()
    result = cur.fetchone()

    print(result['@_student_update_2'])
    if result['@_student_update_2'] == 2:
      print("수정할 이름이 없습니다.")
    elif result['@_student_update_2'] == -1:
      print("에러가 발생하였습니다.")
    elif result['@_student_update_2'] == 1:
      print("수정 성공하였습니다. ")
    else:
      print("알 수 없음")
finally:
  conn.close()


# %% [11]
conn = pymysql.connect(host=DB_HOST,port=3306,user='root',passwd=DB_PASSWORD,
                       db = 'jsdb', charset = 'utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
data = ("테스트",0)
try:
  with conn.cursor() as cur:
    cur.callproc('student_delete', data)
    cur.execute('SELECT @_student_delete_1') # 자동으로 결정
    conn.commit()
    result = cur.fetchone()

    print(result['@_student_delete_1'])
    if result['@_student_delete_1'] == 2:
      print("삭제할 이름이 없습니다.")
    elif result['@_student_delete_1'] == -1:
      print("에러가 발생하였습니다.")
    elif result['@_student_delete_1'] == 1:
      print("삭제완료")
    else:
      print("에러 발생")
finally:
  conn.close()


# %% [12]
# 2tier c/s programming (오늘한 것)
# cliet / server

# 내일 : html, 다음날 javascript, flask (3tier programming)
# 3tier는 client -> wepserver (html) -> DB
# R
# 머신러닝
# 딥러닝
# LLM
# 기타 등등
