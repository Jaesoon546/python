"""
02_data structure(자료구조).ipynb (2026/11/04 2회차)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# 2026/11/04 수요일 직업훈련 2회차


# # List 기본


# %% [1]
# 파이선의 리스트는 주소를 저장
a = [1,2,3,4,5]       # 리스트 초기화 + 데이터주소 + 데이터는 heap
b = a[0:2]            # 마지막은 제외
print(b)
print(type(b))

a = [1,2,3]
b = str(a[2]) + "hi"  # 타입이 일치해야 함 : type casting (형변환), + * str사용
print(b)
# ['a','b','c'] 별도 저장
a = [1,2,3,['a','b','c'], 4, 5]
print(a[2:5])
print(a[3][:2])                    # 2차원 인덱싱

a = [1,2,['a','b',['Life', 'is']]]
print(a[0])
print(a[2][2][0])                  # 3차원 인덱싱
print(len(a))
len(a[2])


# # for 문


# %% [2]
# 전통적 for문 for ( int i = 0, i < 10, i++) 인덱싱 오류가 많이 발생
# 현대적인 for 문 : for in 파이썬에서 사용
a = [1,2,3,4,5]
b = range(1,5,1) # 초기값, 한계값, 증강값 인덱스 세팅
print(b)
print(list(b))   # 캐스팅
for i in a: # 인덱싱 오류 발생 x
  print(i)
for i in b: # 인덱스 숫자 발생
  print(a[i])


# #Python의 리스트


# %% [3]
# 파이썬의 리스트는 이질적 데이터가 가능하다
# 파이썬의 배열은 동질적이다
# 파이썬의 리스트는 동적 배열이다
a = [1,2,3]
a[2] = 4
print(a)

a[1:2] = ['a','b','c']      # 요소로 입력 (인덱스 범위로 줄시)
print(a)

a[2] = ['하나', '둘', '셋'] # 모양을 유지하고 입력 (인덱스 하나로 줄시)
print(a)

mat = [['김',1,2,3],['이',4,5,6],['박',7,8,9]] # 이차원리스트
print(mat)


# # Create Read Update Delete


# %% [4]
# CRUD (Create, Read, Update, Delete)
# stack 자료구조 (list 로 stack을 구현)
a = [10,20,30,40,50]
a.append(60)
print(a)
print(a.pop())
a.append(70)
a.append(80)
print(a)
print(a.pop())
print(a)


# # Queue


# %% [5]
# Queue n(큐) FIFO(first in first out) 선입선출
from collections import deque  # 양방향 큐
myStack = deque()   # 클래스 인스턴스 ( 메모리에 저장공간을 확보 )
myStack.append('a')
myStack.append('b')
myStack.append('c') # [a, b, c]
myStack.appendleft('d') # [d, a, b, c]
print(myStack)
print(myStack.pop())
print(myStack)
myStack.popleft()
print(myStack)
# append, popleft를 사용하면 queue
# append, appendleft, pop, popleft


# # if 문


# %% [6]
# 상태 : 참인 상태와 거짓상태
# 자료구조에서의 거짓상태는 리스트 [], dict {}, tuple (), 0, ""
printer = [] # 리스트, 거짓상태
if not printer: # 조건문 참상태
  print("리스트가 비어 있습니다. ")
printer.append(60) # [60]
printer.append(50) # [60, 50]
if not printer:    # 작동 X
  printer.pop()
print(printer)     # [60, 50]
printer.append(40) # [60, 50, 40]
print(printer)
print(printer.pop(0)) # 후입선출의 특성으로 [40]이 빠져야 정상이나, 값을 0을 주어서 인덱스 값 0의 값인 [60] pop
print(printer)


# # 함수


# %% [7]
# 함수
# stack 에서 동작함 ( 필요한 데이터는 stack에 저장 but 저장공간이 작으니까 -> heap에 데이터를 저장하고 주소만 전달해도 됨 )
# 포인터가 필요한 이유
# define 정의하다.

# 숫자를 사용하겠다는 목적
def calc(a,b):     # parameter 매개변수
  return a+b, a*b  # 파이썬의 함수는 멀티리턴이 가능
                   # 리턴하는 값은 tuple로 전달
x, y = calc(3,4)   # 7 , 12
print(x, y)
print(x)
print(y)
args = (4,5)      # tuple 현재값 1개
calc(*args)       # 파이썬의 * = 변수 나누기 원래 * = 포인터


# # dictionary


# %% [8]
# dictionary : {}
# 입력형태가 key : data `key는 불변  :=colon으로 분리
# dict는 입력되는 순서대로 저장되지 않음

d = {'one':1 , 'two':2}
print(d.items()) # key 데이터의 tuple 조합을 list 로 출력
print(d.keys())  # key 만 list 로 출력
print(d.values())       # data 만 list 로 출력
print(d['one'])


# # 문자열 리스트


# %% [9]
cities = ['seoul', 'incheon', 'suwon'] # 문자열 리스트
print(cities.index('suwon'))
print('incheon' in cities)             # 포함연산자 ( True/False ) => true/false
print(cities.count('seoul'))
print(sorted(cities))                  # 정렬 : 오름차순 ( 작은 것 -> 큰 것 ) : A : 75, 76(B), a : 97
print(sorted(cities, reverse=True))    # 역순으로 정렬
cities.insert(0, 'daegu')
print(cities)
cities.append(['daegu', 'ulsan'])      # 모양유지
print(cities)
cities.extend(['jeju', 'kwangju'])     # 풀어져서
print(cities)
cities


# #Enumerate


# %% [10]
# enumerate
seasons = ('Spring', 'Summer', 'Fall', 'Winter') # tuple 초기화
print(enumerate(seasons))                        # enumerate 객체
print(list(enumerate(seasons)))                  # 순서가 필요로 할 때
print(list(enumerate(seasons, start=1)))         # 시작 번호를 지정
print(seasons[1])


# # 정렬


# %% [11]
# 정렬 : 클래스 매소드와 별도의 sorted 는 영향력이 다름
listexam =[('대한',1),('민국',3),('만세',6),('야호',1)]
listexam.sort() # 원본에 영향을 미침 , 첫 데이터를 중심으로 정렬
print(listexam)
# lambda 함수 ( 무명함수 : 이름이 없다 -> 한번 쓰고 버리는 )
# def name(row) :
#    return row[1] -> lambda row: row[1] 동일
listexam.sort(key=lambda row: row[1])               # 두번째 요소 숫자를 중심하고 정렬
print(listexam)

listexam.sort(key=lambda row: row[1], reverse=True) # 역순으로 정렬 (내림차순)
print(listexam)


# # 문제


# %% [12]
# 만세를 대군으로 변경
listexam =[('대한',1),('민국',3),('만세',6),('야호',1)]
x = list(listexam[2])
x[0] = '대군'
listexam[2] = tuple(x)
print(listexam)


# %% [13]
# 만세를 대군으로 변경
listexam =[('대한',1),('민국',3),('만세',6),('야호',1)]
for index, data in enumerate(listexam):
  print(data)
  listexam[index] = list(data)
listexam[2][0] = "대군"
listexam


# %% [14]
# 만세를 대군으로 변경
listexam =[('대한',1),('민국',3),('만세',6),('야호',1)]
for index, data in enumerate(listexam):
  if listexam[index][0] == "만세":
    listexam[index] = list(data)
    listexam[index][0]="대군"
listexam


# %% [15]
# 문제 : (이름과 국어점수)를 입력 받아 school 이라는 리스트 변수에 3개를 입력하고 점수를 내림차순으로 정렬해서 출력하세요
# input, school = []

# 이름 : 대한, 민국, 만세
# 국어점수 : 90,70,80
# 입력 -> 처리 -> 출력
# 데이터 저장공간 : 자료구조 (여러개인 경우)

school = []

name = input("이름을 입력하시요: ")
kor = eval(input("국어점수를 입력하시오: "))
school.append([name,kor])

name = input("이름을 입력하시요: ")
kor = eval(input("국어점수를 입력하시오: "))
school.append([name,kor])

name = input("이름을 입력하시요: ")
kor = eval(input("국어점수를 입력하시오: "))
school.append([name,kor])

school.sort(key=lambda row: row[1], reverse=True)
print(school)


# %% [16]
# 반복문으로 코드길이 짧게
school = []
for i in range(3):
  name = input("이름을 입력하시오 : ")
  kor = eval(input('국어점수를 입력하시오 : '))
  school.append([name, kor])

school.sort(key=lambda row: row[1], reverse=True)
print(school)


# # 이중 for 문


# %% [17]
# 이중 for문, 중첩 for 문
for i in range(3):   # 3번 실행 : 0, 1, 2
  print("외부", i)
  for j in range(2): # 2번 실행 : 0, 1
    print(j, end=' ')
  print()


# %% [18]
# 이중 for문, 중첩 for 문
for i in range(3):      # 3번 실행 : 0, 1, 2
  print("외부", i)
  for j in range(2):    # 2번 실행 : 0, 1
    print("내부", j)
    for z in range(2):  # 2번 실행 : 0, 1
      print(z, end=' ')
    print()
  print()


# %% [19]
for i in range(5):
  print(" ")
  for j in range(5):
    if i >= j :
      print("*", end="")
# i = 0 ~ 4 , j = 0 ~ 4


# %% [20]
for i in range(5):
  print(" ")
  for j in range(5):
    if i <= j :
      print("*", end="")
# i = 0 ~ 4 , j = 0 ~ 4


# #무한 반복문


# %% [21]
# while True:
#     val = input("종료하려면 'exit'를 입력하세요: ")
#     if val == "exit":
#         print("반복을 종료합니다.")
#         break  # 반복문 탈출


# # 문제 2


# %% [22]
# 둔산중학교는 3학년으로 이루어져 있고
# 한 학년은 2개반으로 구성되어 있다
# 한 반의 학생은 3명씩이다.
# 이 데이터를 list에 입력하시오

# school = 1, 2, 3
# grade = 1, 2
# ban = 1, 2, 3

total = []
school = []
grade = []
ban = []

for i in range(3):
  school = eval(input("몇학년: "))
  for j in range(2):
    grade = eval(input("몇반: "))
    for z in range(3):
      ban = input("이름: ")
      total.append([school, grade, ban])
print(total)


# %% [23]
# school = []
# for i in range(3):
#     grade = []
#     for j in range(2):
#         ban = []
#         for k in range(2):
#             name = input("이름을 입력하시오: ")
#             kor = input("국어점수를 입력하시오: ")
#             ban.append([name, kor])
#         grade.append(ban)
#     school.append(grade)

# print(school)


# %% [24]
for i in range(3):
  print(i+1, " 학년")
  for j in range(2):
    print(" ", j+1, "반")
    for k in range(2):
      print(school[i][j][k], end=" ")
    print()
  print()


# Tuple


# %% [25]
tupl = (0,1,2)            # 초기화
tupl = tuple((0,1,2))
tupl = (0,1,2)
print(tupl[1])            # 인덱스 참조
tupl = (0,1,"korea",3, 4) # 이질적 데이터를 저장
tupl = ((0,1,2),(3,4,5))  # 다차원 배열
print(tupl[0][1])


# # 문제 3


# %% [26]
# 행열 3행/4열
# ['하하하', 100, 100, 100]
# ['유재석', 99, 99, 98]
# ['추신수', 90, 98, 91]
# 각 학생의 점수를 합계를 내서 마지막에 추가하시요
# sungjuk = [['하하하', 100, 100, 100, 300],['유재석', 99, 99, 98, 296],['추신수', 90, 98, 91, 279]]
# 총점을 기준으로 정렬해서 출력하시오 (오름차순으로 정렬)
# 내림차순으로 정렬해 놓고 등수를 만들어 입력 하시오
# 출력은 이름을 기준으로 해서 오름차순으로 정렬해서 출력

sungjuk = [['하하하', 100, 100, 100],['유재석', 99, 99, 98],['추신수', 90, 98, 91]]


# %% [27]
# sungjuk_2 = [['하하하', 100, 100, 100],['유재석', 99, 99, 98],['추신수', 90, 98, 91]]

# for i in range(len(sungjuk_2)):
#   total = 0 # total 초기화
#   for j in range(3):
#     #total = total + sungjuk_2[i][j+1]
#     total += sungjuk_2[i][j+1]
#   average = int(total/3 *100)/100
#   sungjuk_2[i].append(total)
#   sungjuk_2[i].append(average)
# print(sungjuk_2)


# %% [28]
# 각 학생의 점수를 합계를 내서 마지막에 추가하시요
sungjuk = [['하하하', 100, 100, 100],['유재석', 99, 99, 98],['추신수', 90, 98, 91]]

for i in range(len(sungjuk)):
  total = sungjuk[i][1] + sungjuk[i][2] + sungjuk[i][3]
  average = int(total/3 *100)/100
  sungjuk[i].append(total)
  sungjuk[i].append(average)
print(sungjuk)

# 총점을 기준으로 정렬해서 출력하시오 (오름차순으로 정렬)
sungjuk.sort(key=lambda row: row[4])
print(sungjuk)
# 내림차순으로 정렬해 놓고 등수를 만들어 입력 하시오
sungjuk.sort(key=lambda row: row[4], reverse=True)
for z in range(len(sungjuk)):
  sungjuk[z].append(z+1)
print(sungjuk)

# 출력은 이름을 기준으로 해서 오름차순으로 정렬해서 출력
sungjuk.sort(key=lambda row: row[0])
print(sungjuk)


# %% [29]
# 각 학생의 점수를 합계를 내서 마지막에 추가하시요
sungjuk = [['하하하', 100, 100, 100],['유재석', 99, 99, 98],['추신수', 90, 98, 91]]

for i in range(len(sungjuk)):
  total = sungjuk[i][1] + sungjuk[i][2] + sungjuk[i][3]
  average = int(total/3 *100)/100
  sungjuk[i].append(total)
  sungjuk[i].append(average)
print(sungjuk)

# 총점을 기준으로 정렬해서 출력하시오 (오름차순으로 정렬)
def getKey(a1):
  return a1[4]
sungjuk.sort(key = getKey)
print(sungjuk)
# 내림차순으로 정렬해 놓고 등수를 만들어 입력 하시오
sungjuk.sort(key=lambda row: row[4], reverse=True)
print(sungjuk)
for z in range(len(sungjuk)):
  sungjuk[z].append(z+1)
print(sungjuk)
sungjuk.sort(key=lambda row: row[0])
print(sungjuk)

for i in range(len(sungjuk)): #학생수
  for j in range(len(sungjuk[i])):
    print(sungjuk[i][j], end=' ')
  print()


# # 문제 4


# %% [30]
# 어떤 수를 입력 받아서 0:가위, 1:바위, 2:보 로 출력하시요
# % 연산자를 활용해 경우의 수 압축
num = int(input("수를 입력하시오 : "))%3

#while True:
if num == 0:
  print("가위")
elif num == 1:
  print("바위")
else :
  print("보")


# %% [31]
indata = input("정수를 입력하시오")
select = int(indata)%3
if select == 0:
  print("가위")
if select == 1:
  print("바위")
if select == 2:
  print("보")


# #Escape 문자


# %% [32]
# escape문자 ( 문자열 )
print("a\tb\tc\nkorea")
print("abc\tbd\tc".expandtabs(10))
print("abc\tbd\tc".expandtabs(20)) # expendtabs 간격조절


# # 줄맞춤


# %% [33]
print("Rank", "Player", "HR", sep="") #seperrator 분리자
print("Rank", "Player", "HR", sep=" -> ")
print("Rank", "Player", "HR", sep=" \t ")
print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
print("1".center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")


# #연산자


# %% [34]
# 연산자
# 대입연산자 =, +=, -+, *=, /=   ex) total += 1 증가연산자 total += count 누적연산
# 논리연산자 AND->논리곱 OR->논리합 NOT->부정
# 관계연산자 ( >, >=, <, <=, == )


# %% [35]
total = 0
for count in range(10):
  total += count
print(total)


# %% [36]
a = 20
b = 10
print(a>b)
c = a > 10 and b < 50
print(c)
c = 10 < a < 50
print(c)


# #Swaping


# %% [37]
x = 5
y = 10

# C나 JAVA에서 이용
temp = x # 백업
x = y
y = temp
print(x, y)

#스와핑
x ,y = y, x
print(x, y)


# # None


# %% [38]
# 변수는 주소 : 포인터 변수 -> 초기화되지 않은 변수를 사용하면 에러가 발생 ( 주소가 없어서 )
alist = None # 단하나 뿐인 상수 객체 null
print(alist)


# #Magic 명령어 파일분리


# %% [39]
# magic 명령어
# cell magic
# %%writefile mymodule.py

def greet(name):
  return f"hello, {name}!"

PI = 3.141592

# 클래스함수의 첫번째 매개변수는 self
# 함수베이스로 작동 -> 전역변수
class Circle:  # 불문률 대문자 시작  : class = 데이터 + 함수
  def __init__ (self, radius): # 매개변수  , __init__ 시스템이 사용하는 함수 ( 데이터 초기화 )
    self.radius = radius       # self가 붙으면 멤버변수

  def area(self):
    return PI * self.radius ** 2 # 원의 면적
  def perimeter(self):
    return 2 * PI * self.radius # 원 둘레


# %% [40]
import mymodule # 모듈 임포트

print(mymodule.greet("Park"))
print(mymodule.PI)
c = mymodule.Circle(3) # 클래스 인스턴스 ( 메모리를 확보 )
print(c.area())
print(c.perimeter())


# %% [41]
from mymodule import greet, PI
print(greet("Park"))
print(PI)


# #dict 형태 데이터


# %% [42]
person = {
    "name" : "대한이",
    "age" : 30,
    "skulls" : ["Python", "AI"],
    "method" : lambda x: x**2 # 함수도 데이터로 넣기 가능
}

print(person["name"])
person["age"] = 31        # 수정 가능
person["city"] = "Seoul"  # key 추가 가능
print("city" in person)
print(person)
person['method'](2)


# %% [43]
import hashlib
a = "대한민국"
print(hash(a)) # 최대한으로 중복되지 않는 키값 출력
print(id(a))   # 주소


# # Set


# %% [44]
s1 = set([1,2,3,3,4,2,1])
print(s1)
print(type(s1))
#s1[2] # 'set' object is not subscriptable 인덱싱이 안됨
2 in s1


# # 계산기 만들기
# 오늘 배운것들을 활용해서


# %% [45]
# 계산기 만들기

# 덧셈, 뺄셈, 나누기, 곱하기, 나머지, 루트  등등 여러가지 옵션이 있는 계산기를 만들어보자

# 1. 함수를 이용하여 각각 나누어 만들어보기
# sum(). sub(), div(), mul(), squ() ,root()

# 덧셈
def my_sum(x, y):
  return x + y

# 뺄셈
def my_sub(x, y):
  return x - y

# 나누기
def my_div(x, y):
  return x / y

# 곱하기
def my_mul(x, y):
  return x * y

# 제곱
def my_squ(x, y):
  return x**y

# 루트
def my_root(x):
  return x ** 0.5


# %% [46]
print(my_sum(5,5))
print(my_sub(5,5))
print(my_div(5,5))
print(my_mul(5,5))
print(my_squ(5,5))
print(my_root(5))


# %% [47]
# 2. 입력값을 받아서 계산기 출력해보기

num1 = int(input("정수를 입력하시오 : "))
num2 = int(input("정수를 입력하시오 : "))

print(my_sum(num1,num2))
print(my_sub(num1,num2))
print(my_div(num1,num2))
print(my_mul(num1,num2))
print(my_squ(num1,num2))
print(my_root(num1))


# %% [48]
# 3. 반복문을 활용해서 끝내고 싶을때 까지 계산 해보기

while True:
  num1 = int(input("정수를 입력하시오 : "))
  num2 = int(input("정수를 입력하시오 : "))

  print(my_sum(num1,num2))
  print(my_sub(num1,num2))
  print(my_div(num1,num2))
  print(my_mul(num1,num2))
  print(my_squ(num1,num2))
  print(my_root(num1))

  val = input("종료하려면 'exit'를 입력하거나, 계속진행하려면 엔터를 입력하세요 : ")
  if val == "exit":
      print("반복을 종료합니다.")
      break  # 반복문 탈출
  elif val == '':
      print("계속 진행합니다")
