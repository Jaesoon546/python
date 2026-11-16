"""
04_Function_method.ipynb — 함수/메서드
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# 2026/11/06 직업훈련 4회차


# # 함수 기본


# %% [1]
# 코드 중복
a = 10
b = 20
result = a + b
print(result)

a = 30
b = 40
result = a + b
print(result)

def addvalue(a, b): # 입력 -> 매개변수
  return a + b

result = addvalue(10, 20)
print(result)
result = addvalue(30, 40)
print(result)
print(addvalue(30, 40))
# addvalue <= 함수의 주소
adddata = addvalue # 함수는 일급객체` ( 변수에 대입이 가능하고, 매개변수 전달이 가능, 함수의 리턴값으로 사용 )
print(adddata(100, 200))
# 파이썬은 오버로딩의 해결이 언어차원에서 해결 ( 데이터 타입을 지정하지 않음 )
print(addvalue([10,20,30],[30,40,50]))
print(addvalue("abc","def"))
# 데이터 타입을 확인하는 것은 프로그래머의 책임


# %% [2]
def sqr_list(list):       # Coolections
  emp_list = []
  for i in list:
    emp_list.append(i**2)
  print(emp_list)

lista = [1,2,3,4]
sqr_list(lista)
# sqr_list(100) error 발생


# # default parameter


# %% [3]
# default parameter
def student(name, age=21, weight=10):
  print("이름:", name)
  print("나이:", age)
  print("체중", weight)
student(name="김이", age=25, weight=80)
student("김이", 25)
student("김이")

def student_2(name, age=21):
  print("이름:", name)
  print("나이:", age)
student_2("김이", 25)
#print(student_2("김이", 25, 80))


# #수학 함수


# %% [4]
# y = ax + b 선형방정식
# 치역 정의역
# 종속변수 독립변수
def reg(x, a=10, b=20):
  return a*x + b
reg(10)


# #Swap 함수


# %% [5]
# 파이썬의 함수는 멀티 리턴( tuple ) -> Casthing 에서 변경해야 함
a = 10
b = 20
def swap(x,y): # 두 수를 교환 ( C or JAVA 에서는 temp 를 사용해야 함 )
  return y,x
a,b = swap(b,a)
x = swap(a,b)
print(x)


# # 고차 함수


# %% [6]
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b

print("add의 결과 : ", add(10,20))
addition = add
print("addition의 결과 : ", addition(10,20))
# if 문이 불필요
# 유지보수가 유리
def changefun(g, a, b): # g 함수를 매개변수로 전달
  return g(a,b)
print("결과 : ", changefun(add, 10, 20))
print("결과 : ", changefun(multiply, 10, 20))


# #Pass


# %% [7]
def func_test4(): # 정상작동 : 협업할때 사용
  pass


# %% [8]
# 파이썬에서는 함수도 객체
result = func_test4() # None 상수 객체
# 숫자 비교 10 == 20, == 숫자 문자 비교
result is None # 객체 비교 'is'


# %% [9]
# __class__ object가 가지고 있는 멤버변수
# 파이썬은 기본적으로 상속에 의해서 구현 모든 객체는 object를 상속
result.__class__ #NoneType


# # Call by reference 참조에 의한 값 전달
# Call by value 값


# %% [10]
# a = 10
# b = a  # 주소가 같음
# print(b) -> 10
# mylist2 = mylist
def changeme( mylist2 ): # list 입력
  mylist2.append([1,2,3,4])
  print("함수 내부에서 출력 : ", mylist2)
  return
# 파이썬의 변수는 주소
# 원본에 변화를 주는
mylist = [10,20,30] # 초기화
changeme( mylist ) # 주소로 넘어가서 append 해서 원본에 영향을 미침
changeme(mylist)
changeme(mylist)
changeme(mylist)
print("함수 외부에서 출력 : ", mylist)


# #변동 매개변수


# %% [11]
def func1(*args): # tuple 로 받음
  for i in args:
    print(i, end='.')
  print()
print('시작')

func1(1,2,3)
func1(1,2,3,4,5)
func1(1,2,3,4,5,6,7)

print(type(func1))
import inspect
inspect.signature(func1)


# %% [12]
def variable(**names): # 딕셔너리 형태로 받음
  for key,value in names.items():
    print(key,value)
variable(name="대한", Age = 25, Salary=34000, Contury = "korea")


# %% [13]
def var_parameter(*args, **kwargs):
  print(" tuple 매개변수들 ", args)
  print(" key매개변수는 ", kwargs)
  return
var_parameter(1,2,3, z=5.)


# # 함수 호출


# %% [14]
##### 이해 잘 안됨 한번더 확인하기 #####
def say__hello_then_call(f, *args, **kwargs):
  print(" tuple 매개변수들 ", args)
  print(" key매개변수는 ", kwargs)
  print(" 함수를 호출 %s"%f) # 주소 출력 <function g at 0x7c7d6f5a6480>
  return f(*args, **kwargs) # 함수 호출 f(1,2, z=6)

def g(x,y,z=1):
  print(x)
  print(y)
  print(z)
  return (x+y) / z

say__hello_then_call(g , 1,2, z=6)


# %% [15]
def func_test3(a, b):
  return a + b, a-b, a*b

a = func_test3(10,5)        # 단독변수 tuple
print(a)
a, b, c = func_test3(10,5) # 개별값 : 갯수 일치
print(a,b,c)


# #제곱 함수


# %% [16]
def power(r, n):
  value = 1
  for i in range(1, n + 1): # 횟수로 사용
    value = r * value # 2, 4, 8 ....
  return value
print(power(2,3))


# # 재귀호출


# %% [17]
# 트리 구조, 그래프 탐색, 하노이의 탑, 퀵sort/합병정렬 등 구조가 재귀적이거나 분할 정복을 이용하는 문제일 때
# 코드를 선언적이고 가독성 좋게 작성하고 싶을 때
def power(r, n): # 2, 4
  if n == 1: # 종료조건 1 종료
    return r
  else :                     # ... 4  3  2   1 ->  리턴
    return r * power(r, n-1) # 2 * (2  * (2 * ) * (2 ... )))
print(power(2,4))


# #문제 1


# %% [18]
# 스택을 이용한
# factorial -> 재귀함수로 구현
# 5! = 5*4*3*2*1

def fact(r):
  if r == 1:
    return r
  elif r > 1:
    return r * fact(r - 1)
  else:
    return 0

print(fact(0))
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))


# # 이진 검색


# %% [19]
name_list = ['진정인', '원하는대로', '희망이','협동인','통일대박','딥러닝','다함께','대한인']
name_list.sort() # 오름차순
print(name_list)
# key는 검색단어
# 다함께, 원하는대로, 통일대박, 희망이 X
def binary_search_recursive(search_list, key, lower_bound, upper_bound):
  # 종료시점
  if lower_bound > upper_bound: # 교차
    print("찾는 데이터가 없습니다.")
    return
  middle_pos = (lower_bound + upper_bound) // 2 # 몫 연산자
  #종료시점 2 # too much
  if middle_pos <= lower_bound or middle_pos >= upper_bound:
    print("찾는 데이터가 없습니다. ")
    return
  if search_list[middle_pos] < key: # 정렬오른쪽에 데이터 존재
    binary_search_recursive(search_list, key, middle_pos + 1, upper_bound)
  elif search_list[middle_pos] > key:
    binary_search_recursive(search_list, key, lower_bound, middle_pos) # 오류 middle_pos -1
  else:
    print("데이터가 있는 인덱스", middle_pos)

lower_bound = 0
upper_bound = len(name_list)  # len(name_list) - 1
search_word = input("검색하고자 하는 단어를 입력하시요")
binary_search_recursive(name_list, search_word, lower_bound, upper_bound)


# %% [20]
name_list = ['진정인', '원하는대로', '희망이','협동인','통일대박','딥러닝','다함께','대한인']
name_list.sort() # 오름차순
print(name_list)
# key는 검색단어

def binary_search_recursive(search_list, key, lower_bound, upper_bound):
  # 종료시점
  if lower_bound > upper_bound: # 교차
    print("찾는 데이터가 없습니다.")
    return
  middle_pos = (lower_bound + upper_bound) // 2 # 몫 연산자
  # 종료시점 2 # too much
  # if middle_pos <= lower_bound or middle_pos >= upper_bound:
  #   print("찾는 데이터가 없습니다. ")
  #   return
  if search_list[middle_pos] < key: # 정렬오른쪽에 데이터 존재
    binary_search_recursive(search_list, key, middle_pos + 1, upper_bound)
  elif search_list[middle_pos] > key:
    binary_search_recursive(search_list, key, lower_bound, middle_pos-1)
  else:
    print("데이터가 있는 인덱스", middle_pos)

lower_bound = 0
upper_bound = len(name_list) -1
search_word = input("검색하고자 하는 단어를 입력하시요")
binary_search_recursive(name_list, search_word, lower_bound, upper_bound)


# #Generator


# %% [21]
import random
def gaus_dist(n):
  while n > 0:
    yield random.random() # 멈춤  #함수 안에서 값을 반환하고, 함수의 실행을 완전히 끝내는 것이 아니라 그 자리에 일시 정지(State 유지)
    n -= 1 #4 , 3 , 2, 1
gd = gaus_dist(5)
for i in gd: #generator
  print(i)


# #Closure


# %% [22]
def make_closere(a): # 외부함수
  b = 10
  def closure():     # 내부함수
    print('나는 호출한 함수의 매개변수와 지역변수를 알고 있다. : %d %d' % (a, b))
  return closure     # 함수 리턴

# 함수를 실행을 하면 stack에서 정리
closure = make_closere(5) # 실행완료후에도 stack에 남아 있게됨
closure()
closure()


# %% [23]
# closure를 이용한 장식자( decorator )
# 파이썬은 decorator 발달 => class base
def cookbook(name) : # 매개변수도 지역변수
  def recipe(no) :
    print("%s's 호출번호 .%d" % (name, no))
  return recipe
python_recipe = cookbook('python')
python_recipe(1)
python_recipe(2)
perl_recipe = cookbook('javascript')
perl_recipe(1)
perl_recipe(2)


# #lambda 함수


# %% [24]
# lambda 함수도 함수 ( 무명함수 : 간단한 함수를 한번쓰고 버릴 때 )
# 함수는 일급객체 ( 변수에 대입, 매개변수 전달, 리턴값 )
g = lambda x, y: x + y
g(1,2)


# %% [25]
# default parameter 사용
incr = lambda x, incr = 1 : x+incr #incr -> default 값 부여
print(incr(10))
print(incr(10,5))


# %% [26]
#변동 매개변수 가능
varge = lambda x, *args:args
print(varge(1,2,3,4,5))


# %% [27]
strings = ['foo', 'card','bar','aaaa','abab']
strings.sort(key=lambda x : len(set(list(x)))) # set -> 중복제거 집합
print(strings)


# %% [28]
# 함수 배열
func_choice = [lambda x, y: x**y, lambda x, y:x / y]
print(func_choice[0](10,2))
print(func_choice[1](10,2))


# #문제 2


# %% [29]
from itertools import count
# 나이를 입력받아 짝수인 사람은 "나는 귀중한 사람이다"
# 홀수인 사람은 "나는 행복 합니다." 를 출력
# 함수 배열을 이용하여

func_age = [lambda : print("나는 귀중한 사람입니다."),
            lambda : print("나는 행복한 사람입니다.")]

condition = eval(input("숫자를 입력하시오"))
condition %=2
func_age[condition]()


# #문제 3


# %% [30]
def pay(wage, hours, basictime = 40, multiple = 2):
  if hours <= basictime:
    amount = wage * hours
  else :
    amount = (wage * basictime) + (wage * multiple * (hours - basictime))
  return amount

hourlywage = eval(input("시간당 급여는 : "))
hoursworked = eval(input("주간 총 근무 시간 : "))
earnings = pay(hourlywage, hoursworked)
print("주간 수입은 : {0:,.2f} 원".format(earnings))


# %% [31]
# 복리
# 이자율이 주어졌을 때 (3.2%)
# 원금과 거치 기간을 입력받아 기간 거치후 총액과 이자수익을 출력하시오
# 원금 *( 1 + 이자율 )**거치기간

def balanceAndinterest(principal, numYears, INTEREST_RATE = 3.2/100):
  balance = principal * ((1+INTEREST_RATE)**numYears)
  interestEarned = balance - principal
  return balance, interestEarned

def main():
  origin = eval(input("예금액 : "))
  numberOfYears = eval(input("기간 : "))
  (bal, intEarned) = balanceAndinterest(origin, numberOfYears)
  print("총금액 : {0:,.2f}원  이자수익: {1:,.2f} 원".format(bal, intEarned))

main()


# %% [32]
# 위 프로그램을 입력, 처리 , 출력 함수로 분할해서 처리 하시요
# 최소 단위의 함수를 작성하시오


def is_scan():
    origin = eval(input("예금액 : "))
    numberOfYears = eval(input("기간 : "))
    return origin, numberOfYears

def balanceAndinterest(principal, numYears, INTEREST_RATE = 3.2/100):
    balance = principal * ((1+INTEREST_RATE)**numYears)
    interestEarned = balance - principal
    return balance, interestEarned

def is_print(bal, intEarned):
    print("총금액 : {0:,.2f}원  이자수익: {1:,.2f}원".format(bal, intEarned))

def main():
    principal, numYears = is_scan()
    balance, interestEarned = balanceAndinterest(principal, numYears)
    is_print(balance, interestEarned)

main()


# # 문제 4


# %% [33]
# def main():
#     principal, numYears = is_scan()
#     balance, interestEarned = balanceAndinterest(principal, numYears)
#     is_print(balance, interestEarned)
# 한줄의 명령으로 줄여보기
# 최소 단위 함수로 만들고 순수함수( 상태를 가지지 않는 함수 )

def main():
  is_print(*balanceAndinterest(*is_scan())) # * 찢어서 넣기

main()


# # 거리 구하는 함수


# %% [34]
# 2차원 좌표의 거리값을 구하는 함수

import math
# 대수연산 ( +=*/** )
# 초월함수( 비선형 ) : math 함수안에 저장
# 삼각함수, 지수함수, 로그함수
def distance_between_points(x1,y1,x2,y2):
  """두 점 사이의 거리를 구하는 함수,
  입력은 모두 두점의 x, y좌표임"""

  dx = x1 - x2
  dy = y1 - y2
  dist = math.sqrt(dx**2 + dy**2)
  dist = math.sqrt( math.pow(dx,2) + math.pow(dy,2))
  return dist

print(distance_between_points(1,1,2,2))
a = (1,1)
b = (2,2)
print(distance_between_points(*a,*b))
print()
#?distance_between_points #닥스트링
distance_between_points


# [이미지: image.png — 원본 Colab 노트북 참고]


# [이미지: image.png — 원본 Colab 노트북 참고]


# [이미지: image.png — 원본 Colab 노트북 참고]


# %% [35]
# vector는 데이터를 크기와 방향으로 판단
# 피타고라스 정리, 내적
import math
def theta_between_points(x1,y1,x2,y2):
  """두 점 사이의 사이각을 구하는 함수,
  입력은 모두 두점의 x, y좌표임"""
  dot = x1 * y1 + x2 * y2          # 내적
  norm1 = math.sqrt(x1**2 + y1**2) # 점 까지의 길이 (x1, y1)
  norm2 = math.sqrt(x2**2 + y2**2) # 점 까지의 길이 (x2, y2)
  costheta = dot/(norm1 * norm2)   # 내적 / 두점의 길이의 곱 -> cosθ
  thetaradion = math.acos(costheta)# cos 벗기기
  theta = math.degrees(thetaradion)# θ 값 구하기
  return theta

print(theta_between_points(1,0,1,1))
a = (1,0)
b = (0,1)
print(theta_between_points(*a, *b))


# %% [36]
# 라디안 ( 원주율 ) 3.141592(파이) * 2


# #문제 5


# %% [37]
# 3차원
import math

def theta_between_points_3(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    # 벡터 BA = A - B
    BA = (x1 - x2, y1 - y2, z1 - z2)
    # 벡터 BC = C - B
    BC = (x3 - x2, y3 - y2, z3 - z2)
    print(BA)
    print(BC)
    # 두 벡터의 내적
    dot_product = BA[0] * BC[0] + BA[1] * BC[1] + BA[2] * BC[2]

    # 각 벡터의 크기(노름)
    norm_BA = math.sqrt(BA[0]**2 + BA[1]**2 + BA[2]**2)
    norm_BC = math.sqrt(BC[0]**2 + BC[1]**2 + BC[2]**2)

    # 길이가 0인 경우 방지
    if norm_BA == 0 or norm_BC == 0:
        return 0.0

    costheta = dot_product / (norm_BA * norm_BC)

    # 부동소수점 오차로 인한 도메인 에러 방지 (-1.0 ~ 1.0 범위 클리핑)
    costheta = max(-1.0, min(1.0, costheta))

    theta_radian = math.acos(costheta)
    theta_degree = math.degrees(theta_radian)

    return theta_degree

# 테스트
print(theta_between_points_3(1, 0, 1, 1, 2, 2, 3, 1, 0))

a = (1, 0, 1)
b = (1, 2, 2)
c = (3, 1, 0)
print(theta_between_points_3(*a, *b, *c))


# # 수정사항


# %% [38]
# # 위 코드 3차원으로 확장
# import math
# def theta_between_points_3(x1,y1,z1,x2,y2,z2,x3,y3,z3):
#   """세 점 사이의 사이각을 구하는 함수,
#   입력은 모두 두점의 x, y좌표임"""
#   dot = x1 * y1 * z1 + x2 * y2 * z2 + x3 * y3 * z3         # 내적
#   norm1 = math.sqrt(x1**2 + y1**2 + z1**2) # 점 까지의 길이 (x1, y1, z1)
#   norm2 = math.sqrt(x2**2 + y2**2 + z2**2) # 점 까지의 길이 (x2, y2, z2)
#   norm3 = math.sqrt(x3**2 + y3**2 + z3**2) # 점 까지의 길이 (x3, y3, z3)
#   costheta = dot/(norm1 * norm2 * norm3)   # 내적 / 두점의 길이의 곱 -> cosθ
#   thetaradion = math.acos(costheta)# cos 벗기기
#   theta = math.degrees(thetaradion)# θ 값 구하기
#   return theta

# print(theta_between_points_3(1,0,1,1,2,2,3,1,0))
# a = (1,0,1)
# b = (1,2,2)
# c = (3,1,0)
# print(theta_between_points_3(*a, *b, *c))


# %% [39]
# import math
# import numpy as np


# def get_angle(pA, pB, pC):
#   # numpy 배열로 변환
#   a = np.array(pA)
#   b = np.array(pB)
#   c = np.array(pC)

#   # 벡터 BA와 벡터 BC 생성
#   vec_ba = a - b
#   vec_bc = c - b

#   # 내적 계산
#   dot_product = np.dot(vec_ba, vec_bc)

#   # 크기(Norm) 계산
#   norm_ba = np.linalg.norm(vec_ba)
#   norm_bc = np.linalg.norm(vec_bc)

#   # cos(theta) 값 구하기 (부동소수점 오차 방지를 위해 -1~1 범위 클립)
#   cos_theta = dot_product / (norm_ba * norm_bc)
#   cos_theta = np.clip(cos_theta, -1.0, 1.0)

#   # 라디안 -> 각도(Degree) 변환
#   angle_rad = math.acos(cos_theta)
#   angle_deg = math.degrees(angle_rad)

#   return angle_deg


# # 사용 예시 (점 B가 꼭짓점)
# pt_A = (1, 2)
# pt_B = (0, 0)
# pt_C = (2, 0)

# angle = get_angle(pt_A, pt_B, pt_C)
# print(f"사이각: {angle:.2f}도")


# # 문제6


# %% [40]
# 변동 매개변수로 4차원 만들기
import math


def theta_between_points_4(*pointlist):
    count = len(pointlist)
    if count % 2 != 0:
      print("두 포인트 좌표 개수는 짝수가 되어야 합니다.")

    vc = count // 2
    val1 = pointlist[:vc]
    val2 = pointlist[vc:]

    print("첫 번째 벡터:", val1)
    print("두 번째 벡터:", val2)

    dot = 0
    for point in range(len(val1)):
      dot += val1[point] * val2[point]

    norm1 = 0
    for point in range(len(val1)):
      norm1 += val1[point] ** 2
    norm1 = math.sqrt(norm1)

    norm2 = 0
    for point in range(len(val2)):
      norm2 += val2[point] ** 2
    norm2 = math.sqrt(norm2)

    costheta = dot / (norm1 * norm2)
    thetaradian = math.acos(costheta)
    theta = math.degrees(thetaradian)

    return theta
theta_between_points_4(0, -2, -1, 2, -1, -2)


# #문제7


# %% [41]
# user 가위 바위 보    게임
# com  가위 바위 보
# 가위 비김 이김 짐
 #바위   짐 비김 이김
#   보 이김   짐 짐

# 계산 (3가지 경우)
# 비김, 이김(x + 1), 짐(그 외)

# if문 없이 인덱스 번호로 찾기


# ## 문제7 - 1
# 단순 가위바위보 프로그램 (경우의 수 9가지)


# %% [42]
import random
rsp = ['가위', '바위', '보']
judge = ['이김','짐','비김']
com = random.randint(0,2) % 3
user = input("입력하시요 : (0:가위, 1:바위, 2:보)")
user = int(user) % 3

result = 0

if user == 0:
  if com == 0 :
    result= 2
  elif com == 1:
    result = 1
  else :
    result = 0
elif user == 1:
  if com == 0 :
    result= 1
  elif com == 1:
    result = 2
  else :
    result = 0
elif user == 2:
  if com == 0 :
    result= 1
  elif com == 1:
    result = 0
  else :
    result = 2

print("당신은 "+ rsp[user] + " 을 선택 하였고 " + " 컴퓨터는 " +rsp[com] + " 을 선택 하였습니다."+ " 당신은 "+judge[result] + " 했습니다")


# ## 문제7 - 2
# 단순 가위바위보 프로그램 (경우의 수 3가지 압축)


# %% [43]
# 계산 (3가지 경우)
# 비김, 이김(x + 1), 짐(그 외)

import random
rsp = ['가위', '바위', '보']
judge = ['이김','짐','비김']
com = random.randint(0,2) % 3
user = input("입력하시요 : (0:가위, 1:바위, 2:보)")
user = int(user) % 3

result = 0

if com == (user%3):
  result = 2
elif com == (user + 1)%3:
  result = 1
else :
  result = 0

print("당신은 "+ rsp[user] + " 을 선택 하였고 " + " 컴퓨터는 " +rsp[com] + " 을 선택 하였습니다."+ " 당신은 "+judge[result] + " 했습니다")


# ## 문제7 - 3
# 단순 가위바위보 프로그램 (if 문 없이 벡터로)


# %% [44]
# if문 없이 인덱스 번호로 찾기
# 벡터로 가위바위보 게임
import random
rsp = ['가위', '바위', '보']
judge = ['이김','짐','비김']
score = [
    2, 1, 0,
    0, 2, 1,
    1, 0, 2
]

# (user - com) % 3

com = random.randint(0,2) % 3
user = input("입력하시요 : (0:가위, 1:바위, 2:보)")
user = int(user) % 3

result_index = user * 3 + com
f_result = judge[score[result_index]]

print("당신은 "+ rsp[user] + " 을 선택 하였고 " + " 컴퓨터는 " +rsp[com] + " 을 선택 하였습니다."+ " 당신은 "+ f_result + " 했습니다")


# ## 문제7 - 4


# %% [45]
# 게임을 무한루프로 변경하고 승패를 종료시 출력
# if문 없이 인덱스 번호로 찾기
# 벡터로 가위바위보 게임
import random
rsp = ['가위', '바위', '보']
judge = ['이김','짐','비김']
score = [
    2, 1, 0,
    0, 2, 1,
    1, 0, 2
]

# (user - com) % 3

while True:
#     if val == "exit":
#         print("반복을 종료합니다.")
#         break  # 반복문 탈출
  com = random.randint(0,2) % 3
  user = input("입력하시요 : (0:가위, 1:바위, 2:보)")
  user = int(user) % 3

  result_index = user * 3 + com
  f_result = judge[score[result_index]]

  print("당신은 "+ rsp[user] + " 을 선택 하였고 " + " 컴퓨터는 " +rsp[com] + " 을 선택 하였습니다."+ " 당신은 "+ f_result + " 했습니다")

  if score[result_index] == 0:
    print("당신이 이겼습니다. 게임을 종료합니다.")
    break


# %% [46]
#과제
# 1) 가위, 바위, 보 게임을 함수화 하시요 ( 입력, 처리, 출력 )
# 성적프로그램을 함수화 하시요 ( 입력, 출력, 검색, 수정, 삭제. 종료) : 무한루프로 관리
# 20261106_박재순_성적프로그램
# 20261106_박재순_가위바위보게임
