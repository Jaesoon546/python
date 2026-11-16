"""
05_Class Object.ipynb — 클래스와 객체
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# # 객체 지향 프로그래밍


# ## 객체 지향 프로그래밍 4개 개념
# - 파이썬은 기본적으로 완전 객체 지향언어
#   - 함수( 일급객체 )도 객체다. 객체도 함수가 될 수 있다.
#   - 변수에 대입이 가능하고 매개변수로 전달, 함수의 리턴값으로 사용이 된다.
# - 전역변수와 이를 처리하는 함수가 흩어져 있어 debugging의 어려움을 해결
# - 캡슐화 ( 데이터를 보호 : public, private( __ ) -> 파이썬은 pubilc이 기본 )
# - 추상화 ( 구현추상화, interface ( 함수의 몸체만 선언 -> 재정의 사용 ))
# - 다형성
#   - overloading ( 함수 이름은 같은데 매개변수의 타입과 개수가 다르면 다른 함수로 인식
#     - 파이썬에서는 오버로딩이 언어 차원에서 해결
#     - 연산자 오버로딩은 object에 구현되어 있음 )
#   - overrding ( 재정의 )
#     - 상속받은 함수를 재정의 해서 행동을 정의
#     - 함수 이름은 같은데 함수가 각기 다른 행을 한다
#
# - 상속성 : 파이썬의 모든 클래스는 최고 부모인 object를 상속
#   - JAVA는 object에 최소기능만 있는데 파이썬의 obdect는 다양한 기능
#   - __class__
#
# - 클래스의 문법
#   - 멤버변수는 함수안에서만 선언 : self 만 붙이면 멤버변수
#   - 멤버함수는 self가 처음 매개변수에 선언되어야 함
#   - 변수 종류
#     - 함수 : 지역변수와 전역변수
#     - 클래스 : class변수( 공유변수 ), static 변수( 정적변수 ), instance 변수( 클래스 메모리 확보 )


# ## 클래스 예제 1


# %% [1]
# class = 멤버변수 + 멤버변수
# self를 붙인 변수 : 멤버변수
# 메모리 공간을 확보하는 것이 instance
# 파이썬에서 기본적으로 모든 객체는 object를 상속
# __가 앞에 붙으면 private 변수
class C: # object
  def __init__(self):     # 초기화 : 생성자 -> __init__ => 재정의 ( object )
    self.__x = None       # 멤버변수

  def getx(self):         # 함수는 첫 매개변수가 반드시 self
    return self.__x

  def setx(self, value):
    self.__x = value

  def delx(self):
    del self.__x          # 메모리에서 변수 삭제

test = C()                # 인스턴스
test.setx(100)
test.getx()


# %% [2]
# class = 멤버변수 + 멤버변수
# self를 붙인 변수 : 멤버변수
# 메모리 공간을 확보하는 것이 instance
# 파이썬에서 기본적으로 모든 객체는 object를 상속
class D: # object
  def __init__(self):     # 초기화 : 생성자 -> __init__ => 재정의 ( object )
    self.__y = None       # 멤버변수

  def gety(self):         # 함수는 첫 매개변수가 반드시 self
    return self.__y

  def sety(self, value):
    self.__y = value

  def dely(self):
    del self.__y

test = C()                # 인스턴스
test.setx(100)
test.getx()

test_y = D()
test_y.sety(100)
test_y.gety()


# ## 클래스 예제 2


# %% [3]
class MyClass(object):    # 명시적으로 object 상속
  '''클래스의 예'''
  i = 12345               # class 변수 ( 공유변수 : 여러번 인스턴스 해도 한번만 메모리 구성 )
  def __init__(self):
    self.i = 54321        # 멤버변수
    num = 100             # 함수의 지역변수 ( stack에 만들어졌다 없어짐 )
  def f(self):
    return self.i
print(MyClass.__doc__)    # object를 상속받아 선언하지 않아도 사용 가능 print()-> 1
print(MyClass.i)          # 인스턴스 하지 않고 바로 사용가능            print()-> 2

myclass = MyClass()       # __init__는 클래스 인스턴스 할 떄 자동실행 - 멤버변수 초기화
myclass = MyClass()
print(myclass.i)
myclass.f()


# ## 클래스 예제3


# %% [4]
# import time 도 가능 but 메모리 낭비
# 클래스는 생성자로 초기화하고 소멸자로 주소 해제 할당된 메모리 해제는 GC가
from time import time, ctime, sleep # 로딩
print(time())                       # timestamp linux의 -> 1970년 이후로 지난시간을 초로 표현
class Life:

  def __init__(self):               # 생성자
    self.birth = ctime()            # character 문자
    print("생성", self.birth)

  def __del__(self):                # 소멸자
    print("사망",ctime())

  def test(self):
    print("3초 동안 sleeping")
    sleep(3)                        # 정지

li = Life()                         # 인스턴스 : 메모리 확보 ( heap )
li.test()
del li                              # 주소해제 : 확보된 메모를 해제하는 것은 GC(garbage collection) -> 자동으로 해제
print(time())


# ## 클래스 예제 4


# %% [5]
class Employee:

  empCount = 0                                              # 공유변수 - 한번의 메모리 확보 -> 누적

  def __init__(self, name, salary):
    self.name = name                                        # 멤버변수
    self.salary = salary
    Employee.empCount += 1                                  # 생성할 때 마다 추가

  def displayCount(self):
    print("직원 수 = %d" %Employee.empCount)
    return " 몰라 "

  def displayEmployee(self):
    print("이름 : ", self.name, ", 급여 : ", self.salary)

  def __call__(self, *pargs, **kargs):                      # 오버라이딩 ( 클래스를 함수처럼 )
    print("Called : ", pargs, kargs)


# %% [6]
emp = Employee('박재순', 500)
emp.displayCount()
emp1 = Employee("이대한", 500)
emp1.displayCount()
emp.displayCount()


# %% [7]
emp( "빅데타", 500,100, c=100 ) # 클래스를 함수처럼 사용


# %% [8]
emp1.age = 7 # 클래스에 실시간으로 변수 추가
emp1.age = 8 # 수정


# %% [9]
hasattr(emp1, 'name')
hasattr(emp1, 'age')
getattr(emp1, 'age')
setattr(emp1, 'age',8)
delattr(emp1, 'age')


# ## 클래스 문제1


# %% [10]
# 문제 이름과 나이를 저장하는 Student class를 작성하시요

class Student:
  '''학생관리'''
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def is_print(self):
    print("이름: ", self.name, " 나이: ", self.age)

  def __repr__(self): #__repr__ 최근
    return "나의 이름: " + self.name + " 나이: " + str(self.age) + "입니다."
# 문자열 리턴 : 문자열을 요구하는 함수에서 자동실행


# %% [11]
stu = Student('다함께', 23)
stu.is_print()
print(stu)
print(stu.__doc__)
print(stu.__class__)
# 인스턴스 변수에서 초기화된 클래스 이름을 역추적
g = stu.__class__("테스트", 40)
print(g)


# ## deecopy


# %% [12]
import copy
a = [100,2,3]
b = [4,5,a]             # [4,5,[100,2,3]]
x = [a,b,100]           # [[100,2,3],[4,5,[100,2,3]],100]
# y = x
# 얕은 복사는 주소만 넘어가기 때문에 같은 곳을 가리키게 됨
y = copy.copy(x)        # 얕은 복사 [[100,2,3],[4,5,[100,2,3]],100]
a.append(2000)          # [100, 2, 3, 2000]
print("a =",a)
print(x)                # [[100, 2, 3, 2000], [4, 5, [100, 2, 3, 2000]], 100]
print(y)                # [[100, 2, 3, 2000], [4, 5, [100, 2, 3, 2000]], 100]
# 깊은복사
y2 = copy.deepcopy(x)   # x = [[100, 2, 3, 2000], [4, 5, [100, 2, 3, 2000]], 100]
                        # y2 = [[100, 2, 3, 2000], [4, 5, [100, 2, 3, 2000]], 100]
                        # -> 별도의 공간 복산
a[0] = 200
print(y)                # [[200, 2, 3, 2000], [4, 5, [200, 2, 3, 2000]], 100]
                        # -> 주소복사로 인해 값 변경
print(y2)               #[[100, 2, 3, 2000], [4, 5, [100, 2, 3, 2000]], 100]


# ## Chaining


# %% [13]
class Person:                                           # 생성자가 없음 -> 멤버변수가 없는가? self가 붙은 변수는 모두 멤버변수

  def name(self, value):
    self.name = value
    return self                                         # self를 리턴하면 chaining으로 호출이 가능

  def age(self, value):
    self.age = value
    return self

  def introduce(self):
    print("이름 : ", self.name, ", 나이 : ", self.age)

person = Person()
person.name("융합교육원").age(21).introduce()


# ## static 변수


# %% [14]
# static 변수 : 파이썬에서는 class 변수가 static 변수
# staticmethod : 함수를 정적호출이 가능하게 해줌 -> 정적함수
# 정적 함수 : 인스턴스하지 않고 호출이 가능

class StaticTest():

  def spam(x, y):
    print("정적함수", x, y)
  spam = staticmethod(spam)

  @staticmethod             # 장식자
  def spam1(x, y):
    print("일반함수", x, y)

'''st = StaticTest() # 인스턴스 '''
StaticTest.spam(1,2)
StaticTest.spam1(1,2)
# math는 전부 정적함수들만 모아 놓고 있음


# ## classmethod


# %% [15]
from datetime import date
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod                                        # 초기화 방법을 변경하고자 할 때
  def fromBirthYear(cls, name, birthYear):            # Person
    return cls(name, date.today().year - birthYear)   # 나이계산

  def display(self):
    print(self.name + "의 나이는 : " + str(self.age))

person = Person("강감찬", 19)
person.display()
person1 = Person.fromBirthYear("을지문덕", 1985)
person1.display()


# ## 셔플


# %% [16]
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)


# ## 로또 프로그램 만들기


# %% [17]
import random
# 단일 책임의 원칙 ( 하나의 기능을 구현 )
# 비교가 가능하게 ( 클래스를 비교  -> 연산자 오버로딩 )
class LottoBall:                          # 상속관계

  def __init__(self, num):
    self.num = num
  # 연산자 오버로딩 ( class에서 꼭 필요한 작업 )
  def __lt__(self, other):                # <: less then >: greater then
    if isinstance(other, LottoBall):      # 로또볼만 비교 가능
      return self.num < other.num         # 참인경우
    return NotImplemented                 # 다른 것은 구현이 안되어 있다.

  def __repr__(self):                     # 문자열을 요구하는 함수안에서 자동 작동
    return str(self.num)

class LottoMachine:

  def __init__(self):
    self.ballList = []                    # ball의 주소를 담은 리스트
    for i in range(1,46):
      self.ballList.append(LottoBall(i))

  def selectBalls(self):
    random.shuffle(self.ballList)
    return sorted(self.ballList[0:6])

# LottoBall과 LottoMachine 의 관계는 Component 포함관계
# 상속관계와 포함관계
# 인터페이스를 이용한 출력
class LottoUI:

  def __init__(self):
    self.machine = LottoMachine()

  def playLotto(self):
    input("로또를 뽑을까요?")
    selectedBalls = self.machine.selectBalls()
    for ball in selectedBalls:
      print(ball, end=" ")


# %% [18]
lo = LottoUI()
lo.playLotto()


# ## class 이등변삼각형


# %% [19]
width = 10
height = 20
area = width * height / 2
print("삼각형의 넓이는", area)


# %% [20]
# 클래스로 작성

class WH:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height / 2

  def __repr__(self):
    return "높이: " + str(self.width) + " 밑변:" + str(self.height) + " 면적:" + str(self.area())


# %% [21]
tri1 = WH(10,20)
print(tri1)


# ## 클래스 문제 2


# %% [22]
# Point Class를 작성하시오
# x, y 두개의 좌표를 관리합니다 .
# 두 점과의 거리를 구하는 함수를 작성하시요
# 두 점의 거리가 3보다 작으면 충돌하는 것을 체크하는 함수를 작성하시요
# 충돌 여부를 출력하는 함수를 작성하시요

import math

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getx(self):
    return self.x

  def gety(self):
    return self.y

  def setx(self, value):
    self.x = value

  def sety(self, value):
    self.y = value

  def __repr__(self):
    return f"좌표는 ({self.x}, {self.y})"

  def distance(self, other):
      dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
      return dist

  def collection(self, other):
    return self.distance(other) < 3

  def collectionUI(self, other):
    if self.collection(other):
      print("충돌하였습니다.")
    else:
      print("충돌하지 않았습니다.")


# %% [23]
first = Point(1,1)
second = Point(2,2)

print("두점 사이의 거리는 : ", first.distance(second))

first.collection(second)


# %% [24]
first.collectionUI(second)


# ## 클래스 문제 3


# %% [25]
# 1 부터 10까지의 숫자로 random하게 좌표를 10개 생성
# 그리고 이 좌표간에 충돌 여부를 확인하시요
# randint, randint

pointlist = []
for count in range(10):
  po = Point(random.randint(1,10),random.randint(1,10))
  pointlist.append(po)
print(count)


totalcollisincount = 0
n = len(pointlist)
for count1 in range(n -1):
  for count2 in range(count1+1,n):
    if (pointlist[count1].collection(pointlist[count2])):
      print("충돌했습니다. ")
      print("충돌 인덱스 번호", str(count1), " - ", str(count2))
      print("충돌 좌표", pointlist[count1], "- ", pointlist[2])
      totalcollisincount += 1
      print(count2)
print("전체 충돌횟수 =", str(totalcollisincount))
print(pointlist)


# %% [26]
import math
import random


class Collection:

    def __init__(self):

        self.x = random.randint(1, 10)
        self.y = random.randint(1, 10)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self, value):
        self.x = value

    def sety(self, value):
        self.y = value

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return dist

    def collection(self, other):
        return self.distance(other) < 3

    def collectionUI(self, other):
        if self.collection(other):
            print(f"충돌: {self.distance(other):.2f}")
        else:
            print(f"안전: {self.distance(other):.2f}")


# 1. 10개의 랜덤 좌표를 생성하여 리스트에 저장합니다.
points = [Collection() for _ in range(10)]

for i, point in enumerate(points):
    print(f"점 {i+1}: {point}")

# 2. 모든 좌표 간의 충돌 여부를 확인합니다. (이중 루프 사용)
# 중복 검사를 피하기 위해 j는 i+1부터 시작합니다.

collection_count = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]

        print(f"[점 {i+1} {p1}] : [점 {j+1} {p2}] -> ", end="")
        p1.collectionUI(p2)

        if p1.collection(p2):
            collection_count += 1

print(f"총 충돌 횟수: {collection_count}번")


# ## 클래스 문제 4


# %% [27]
import math

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getx(self):
    return self.x

  def gety(self):
    return self.y

  def setx(self, value):
    self.x = value

  def sety(self, value):
    self.y = value

  def __repr__(self):
    return f"좌표는 ({self.x}, {self.y})"

  def distance(self, other):
      dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
      return dist

  def collection(self, other):
    return self.distance(other) < 3

  def collectionUI(self, other):
    if self.collection(other):
      print("충돌하였습니다.")
    else:
      print("충돌하지 않았습니다.")


# %% [28]
import math
import random
# Point class 이용해서 Circle class 를 작성하시요
# Point : 중심점, Radius 반지름 지정
# 원의 면적을 구하는 함수를 작성하시오
# 원의 둘레를 구하는 함수를 작성하시오
# 두 원의 중심점 간의 거리를 구하는 함수를 작성하시오
# 두 원이 충돌했는지 여부를 구하는 함수를 작성하시오 ( 두원의 반지름 보다 작으면 충돌 )

class Circle:

  def __init__(self, point, radius):
    self.point = point                                # Point class를 입력받는 다고 설정
    self.radius = radius

  def r_area(self):
    return math.pi * float(self.radius ** 2)

  def r_perimeter(self):
    return 2 * math.pi * self.radius

  def r_distance(self, other_circle):
    return self.point.distance(other_circle.point)

  # 두 원이 충돌했는지 여부를 구하는 함수 (두 원의 중심 간 거리가 두 원 반지름의 합보다 작으면 충돌)
  def r_collection(self, other_circle):
    dist = self.r_distance(other_circle)
    if dist < (self.radius + other_circle.radius):
      print("충돌하였습니다. ")
    else :
      print("충돌하지 않았습니다. ")

  def __str__(self):
    return "원의 중심은 " + str(self.point) + "반지름은 " + str(self.radius)

  def print_repr(self):
    print(self.__str__)


# %% [29]
# 중심점 인스턴스
first = Point(7,3)
second = Point(4,7)

# 원을 인스턴스 ( 원이 중심점을 포함 : 포함관계 )
cir = Circle(first, 1)
cir2 = Circle(second, 5)

print(cir)
print(cir2)

print(cir.r_collection(cir2))
print(cir.r_distance(cir2))
cir.print_repr()


# ## 클레스 문제 5


# %% [30]
# Rectangle class 를 작성하시오
# Point class 2개로 구성
# 둘레, 면적, 대각선의 길이를 구하는 함수를 작성하시요
# 사각형 좌표
# p1, p2 ,width, height

# 둘레 -> re_perimeter = width * 2 + height * 2
# 면적 -> re_area = width * height
# 대각선 -> re_diagonal = math.sqrt((self.width ) ** 2 + (self.height) ** 2)

class Rectangle:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.width = abs(p2.x - p1.x)         # 절대값 고려
    self.height = abs(p2.y - p1.y)

  def re_perimeter(self):
    return (self.width + self.height) * 2

  def re_area(self):
    return self.width * self.height

  def re_diagonal(self):
    return math.sqrt(self.width ** 2 + self.height ** 2)

  def __repr__(self):
    return f"{self.p1} , {self.p2} 둘레 :{self.re_perimeter()}, 면적:{self.re_area()}, 대각선의 길이:{self.re_diagonal()}"


# %% [31]
point1 = Point(2,4)
point2 = Point(3,6)

rec = Rectangle(point1, point2)
print(rec)


# ## Vector Class 생성


# %% [32]
# Vector class 생성
# 요소연산, 내적연산
# x,y를 요소로 하는 vector를 구성하고 요소연산과 내적연산을 실행하는 클래스를 작성
# 요소연산
# Vector (10, 2), Vector (20,2) +-*/ => Vector (10 + 20, 2 + 2)
# 내적연산
# 내적연산은 요소끼리 곱해서 다 더해주는 계산
# Vector(2, 3) = Vector(2/3.605...., 3/3.605....) -> 3.605... 는 norm값( 점까지의 길이 )
# normalize : 방향만 남음 ( 사이즈는 1이 됨 : 정규화 )

class Vector:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)
  def __mul__(self, other):
    return Vector(self.x * other.x, self.y * other.y)
  def __truediv__(self, other):
    return Vector(self.x / other.x, self.y / other.y)
  def __floordiv__(self, other):
    return Vector(self.x // other.x, self.y // other.y)

  def norm(self):
    return math.sqrt(self.x**2 + self.y**2)
  def normalize(self):                      # 벡터에 있는 값을 norm으로 나눈 벡터 ( 크기가 1인 벡터 )
    return Vector(self.x/self.norm(), self.y/self.norm())
  def dot (self, other):
    return self.x * other.x + self.y * other.y
  def costheta(self, other):
    return self.dot(other) / (self.norm() * other.norm())
  def theta(self, other):
    costh = self.costheta(other)
    return math.acos(costh) * (180/math.pi)
  def theta_2(self, other):
    thetaradion = self.costheta(other)
    theta_2 = math.degrees(thetaradion)
    return theta_2
  # thetaradion = math.acos(costheta)# cos 벗기기
  # theta = math.degrees(thetaradion)# θ 값 구하기
  # return theta
  def __repr__(self):
    return f"(좌표는 ({self.x}, {self.y}))"


# %% [33]
f = Vector(100, 23)
g = Vector(20, 27)

print(f)
print(f+f)
print(f + g)
print(f * g)
print(f - g)
print(f / g)
print(f // g)
print(f.theta(g))
print(f.theta_2(g))


# ## 문제 6


# %% [34]
# 다차원 벡터로 변경

import math


class Vector_m:

  def __init__(self, x):
    self.x = x

  def __repr__(self):
    return f"(좌표는 {self.x})"

  def __add__(self, other):
    return Vector_m([self.x[i] + other.x[i] for i in range(len(self.x))])

  def __sub__(self, other):
    return Vector_m([self.x[i] - other.x[i] for i in range(len(self.x))])

  def __mul__(self, other):
    return Vector_m([self.x[i] * other.x[i] for i in range(len(self.x))])

  def __truediv__(self, other):
    return Vector_m([self.x[i] / other.x[i] for i in range(len(self.x))])

  def __floordiv__(self, other):
    return Vector_m([self.x[i] // other.x[i] for i in range(len(self.x))])

  def norm(self):
    return math.sqrt(sum([x * x for x in self.x]))

  def normalize(self):
    n = self.norm()
    return [x / n for x in self.x]

  def dot(self, other):
    return sum([x * y for x, y in zip(self.x, other.x)])

  def costheta(self, other):
    dot_val = self.dot(other)
    norm1 = self.norm()
    norm2 = other.norm()
    return dot_val / (norm1 * norm2)

  def theta(self, other):
    costh = self.costheta(other)
    # acos의 입력값 범위(-1 ~ 1)가 오차로 인해 벗어나는 경우 방지
    costh = max(-1.0, min(1.0, costh))
    return math.acos(costh) * (180 / math.pi)


# %% [35]
vec1 = Vector_m([100,80,70,60,100,80,90])
vec2 = Vector_m([100,81,72,65,99,82,91])

print(vec1)
print(vec2)
print(vec1 + vec2)
print(vec1 - vec2)
print(vec1 * vec2)
print(vec1 / vec2)


# %% [36]
print(vec1.dot(vec2))
print(vec1.costheta(vec2))
print(vec1.theta(vec2))


# ## 클래스 리스트


# %% [37]
class Student:

  def __init__(self, name, age, major):
    self.name = name
    self.age = age
    self.major = major

  def __str__(self):
    return f"이름: {self.name}, 나이: {self.age}, 전공: {self.major}"


# %% [38]
students = [
    Student("김대한", 20, "컴퓨터공학"),Student("김민국", 21, "전자공학"),
    Student("김만세", 22, "정보공학"),
]

students[1].name


# %% [39]
import pickle
# write/binary ( 2진 - 가독성이 없음 )
# 파일 관리는 os이 함 : 반드시 해제
# 데이터베이스 연결, 네트워크 연결, 파일처리는 반드시 해제
with open("students.pk", "wb") as file: # 자동 해제
  pickle.dump(students, file)


# %% [40]
with open("students.pk", "rb") as file:
  loaded_students = pickle.load(file)


# %% [41]
for student in loaded_students:
  student.age += 1
  print(student)
