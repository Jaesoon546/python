"""
06_inheritance.ipynb — 상속 (2026/11/10 6회차)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# 20261110 직업훈련 6회차


# 20261110 직업훈련 6회차


# # 상속


# ## 부모와 자식 method


# %% [1]
class Parent():           # 부모 클래스
  def myMethod(self):
    print("부모메쏘드")

class Child(Parent):
  def myMethod(self):
    print("자식메쏘드")

ch = Child()              # 인스턴스
ch.myMethod()             # 재정의한 자식 메쏘드 우선 ( MRO )


# ## Point class


# %% [2]
# 2차원
# 함수는 선언하고 바로 사용이 가능
# 클래스는 멤버변수들 ( 사용자 정의 데이터 타입 )의 메모리 공간을 확보 : 인스턴스( instance )

import math
class Point:
  def __init__(self, x, y):       # 생성자에서 데이터 초기화
    self.x = x
    self.y = y

  def translate(self, dx, dy):
    self.x += dx
    self.y += dy


# %% [3]
class Point3D(Point):             # 3차원 클래스 확장
  def __init__(self, x, y, z):
    Point.__init__(self, x, y)    # 부모의 생성자 호출
    self.z = z

  def translate(self, dx, dy, dz):
    Point.translate(self, dx, dy)
    self.z += dz


# ## Shape Class


# %% [4]
class Shape:
  def __int__(self):
    print("부모 클래스")
  def area(self):
    print("면적")
  def perimeter(self):
    print("둘레")


# %% [5]
import math
class Point:
  def __init__(self, x, y):       # 생성자에서 데이터 초기화
    self.x = x
    self.y = y

  def translate(self, dx, dy):
    self.x += dx
    self.y += dy


# %% [6]
# 문제 Triangle class ( 이등변 삼각형 )를 Shape를 상속받아서 구현
# width, height 로 초기화
class Triangle(Shape):

  def __init__(self, width, height):
    Shape.__init__(self)
    self.width = width
    self.height = height

  def area(self):
    print("삼각형의 넓이는=", self.width * self.height / 2)

  def perimeter(self):
    print(
        "삼각형의 둘레는=",
        self.width
        + math.sqrt(
            math.pow(self.width / 2, 2) + math.pow(self.height, 2)
        )
        * 2,
    )


# %% [7]
class Circle(Shape):

  def __init__(self, center, radius):
    Shape.__init__(self)
    self.center = center
    self.radius = radius

  def area(self):
    print("원의 넓이는=", math.pi * self.radius ** 2)

  def perimeter(self):
    print("원의 둘레는=", 2 * math.pi * self.radius)


# %% [8]
# Rectangle class를 shape를 상속받아서 구현하시요
# 사각형 밑변 * 높이  = 넓이
# 2 * ( 밑변 + 높이 ) = 둘레

# Rectangle 클래스 구현
class Rectangle(Shape):

  def __init__(self, p1, p2):
    Shape.__init__(self)
    self.p1 = p1
    self.p2 = p2

  def area(self):
    print(
        "사각형의 넓이는=",
        abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y),
    )

  def perimeter(self):
    print(
        "사각형의 둘레는:",
        (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y)) * 2,
    )


# ## Class 통합 출력 - 리스트화


# %% [9]
# import random
# shape_list = [] # 클래스 리스트 ( 2차원 : 클래스 자체가 1차원의 효과 )

# for i in range(10):
#   rand = random.randint(0,10)
#   if rand%3 == 0:
#     width = random.randint(1,10)
#     height = random.randint(1,10)
#     tri = Triangle(width, height)
#     shape_list.append(tri)
#   elif rand%3 == 1:
#     x = random.randint(1,10)
#     y = random.randint(1,10)
#     rect = Rectangle(Point(10,20), Point(x,y))
#     shape_list.append(rect)
#   else :
#     r = random.randint(1,10)
#     ci = Circle(Point(10,20), r)
#     shape_list.append(ci)

# for i in range(10):             # 재정의를 이용한 처리
#   shape_list[i].area()
# #   shape_list[i].perimeter()


# %% [10]
import math
import random

shape_list = []

for i in range(10):
  rand = random.randint(0, 10)
  if rand % 3 == 0:
    width = random.randint(1, 10)
    height = random.randint(1, 10)
    tri = Triangle(width, height)
    shape_list.append(tri)
  elif rand % 3 == 1:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    rect = Rectangle(Point(10, 20), Point(x, y))
    shape_list.append(rect)
  else:
    r = random.randint(1, 10)
    ci = Circle(Point(10, 20), r)
    shape_list.append(ci)

for i in range(len(shape_list)):
  shape_list[i].area()
  shape_list[i].perimeter()


# ## Delegate


# %% [11]
# 부모는 자식을 가리킬 수 있다. ( 자식이 추가한 함수는 부모가 모른다. )

class Evaluation:
  def printcalcGrade(self,average):
    pass

class Hakjum(Evaluation):
  def printcalcGrade(self, average):
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else : return "F"

class Pass_Fail(Evaluation):
  def printcalcGrade(self, average):
    if average >= 60: return "합격"
    else :  return "불합격"

class Element_Evaluation(Evaluation):
  def printcalcGrade(self, average):
    if average >= 90: return "수"
    elif average >= 80: return "우"
    elif average >= 70: return "미"
    elif average >= 60: return "양"
    else : return "가"

# 처리하고 출력을 분리
class Evaluation_print:
  def print_evaluation(self, evaluation): # 평가 방법을 매개변수로 전달하면 대리자가 받음
    jumsu = eval(input("점수를 입력하시요 "))
    print(evaluation.printcalcGrade(jumsu))


# %% [12]
ha = Hakjum()
ev = Evaluation_print()
ev.print_evaluation(ha)
pass_fail = Pass_Fail()
ev.print_evaluation(pass_fail)
element = Element_Evaluation()
ev.print_evaluation(element)


# ## 다이아몬드 문제 ( 상속 ) 해결


# %% [13]
# C -> 다중상속 불가 : 에러 , JAVA -> 단일상속만 가능
class A:
  def m(self):
    print("A.m()호출 ")

class B(A):
  def m(self): # 오버라이딩
    print("B.m()호출 ")

class C(A):
  def m(self): # 오버라이딩
    print("C.m()호출 ")
# 다중상속
class D(B,C): # MRO 우선순위에 의해 B가 우선  ( 자식이 우선, 처음 지정한 클래스가 우선 )
  pass

dinc = D()
dinc.m()
# 같은 이름으로 함수를 정의하면 : 나중 선언한 함수가 우선함


# ## 문제1 시계 클래스


# %% [14]
class Clock():

  def __init__(self, hours=0, minutes=0, seconds=0):
    self.__hours = hours     # private 변수 ( 외부접근이 불가 )
    self.__minutes = minutes
    self.__seconds = seconds

  def set(self, hours=0, minutes=0, seconds=0):
    self.__hours = hours     # private 변수 ( 외부접근이 불가 )
    self.__minutes = minutes
    self.__seconds = seconds

  def tick(self):
    if self.__seconds == 59:
      self.__seconds = 0
      if (self.__minutes == 59):
        self.__minutes = 0
        if (self.__hours == 23):
          self.__hours = 0
        else :
          self.__hours += 1
      else :
        self.__minutes += 1
    else :
      self.__seconds += 1

  def display(self):
    print(f"{self.__hours}:{self.__minutes}:{self.__seconds}")

  def __str__(self):
    return  "%2d:%2d:%2d" % (self.__hours, self.__minutes, self.__seconds)

  def check(self):
    if self.__hours == 0 and self.__seconds == 0 and self.__minutes == 0:
      return True


# %% [15]
# 16시 47분을 만들어 보시요
x = Clock()
print(x)

for i in range(16*60*60 + 47*60):
  x.tick()
print(x)


# %% [16]
# 18시 46분 32초 만들어 보시오
y = Clock()
for i in range(18*60*60 + 46*60 + 32):
  y.tick()
print(y)


# ## 달력 만들기


# %% [17]
class Calendar():
  months = (31,28,31,30,31,30,31,31,30,31,30,31)       # Class 변수 ( 공유변수 ) : 정적변수

  def __init__(self, day = 1, month = 1, year = 1900): # 년월일
    self.__day = day
    self.__month = month
    self.__year = year

  def leapyer(self, y): # 윤년 계산
    if y % 4:
      return 0          # 윤년이 아님
    else :              # 4로 나누어서 떨어진 것 중에
      if y % 100:       # 100으로 나누어서 떨어지지 않으면 윤년
        return 1
      else :            # 100으로 나누어 떨어진 것 중에
        if y % 400:     # 떨어지지 않으면 윤년이 아님
          return 0
        else :
          return 1      # 400으로 나누어서 떨어지면 윤년

  def set(self, day, month, year):
    self.__day = day
    self.__month = month
    self.__year = year

  def advance(self):
    months = Calendar.months
    max_days = months[self.__month-1]      # 인덱스(0) == 월(1)을 일치
    if self.__month == 2:                  # 윤년 계산
      max_days += self.leapyer(self.__year)
    if self.__day == max_days:             # 최종일을 지나가야 월이 바뀜
      self.__day = 1
      if (self.__month == 12):             # 마지막 달에는 년도가 바뀜
        self.__month = 1
        self.__year += 1
      else :
        self.__month += 1
    else :
      self.__day += 1

  def __str__(self):
    return str(self.__year) + "/" + str(self.__month) + "/" + str(self.__day)

  # def control(self):
  #   self.tick()
  #   if self.check(): # 모두가 0이면 그 때 날짜가 하루 감
  #     self.advance()


# %% [18]
cal = Calendar(10, 11, 2026)
print(cal)  # 출력: 2023/12/31
cal.advance() # 다음 날로 이동
print(cal)  # 출력: 2024/1/1


# %% [19]
x = Calendar()
for i in range(365*126+30*11+14):
  x.advance()
print(x)


# ## 문제2 시계와 달력 연결


# %% [20]
# class CalendarClock(Clock, Calendar): # 다중상속

#   def __init__(self, year = 1900, month = 1, day = 1, hours=0, minutes=0, seconds=0):
#     Calendar.__init__(self, day, month, year)
#     Clock.__init__(self, hours, minutes, seconds)

#   def __str__(self):
#     return Calendar.__str__(self) + ", " + Clock.__str__(self)

#   def tick_advance(self):
#     self.tick()
#     if self.check():
#       self.advance()


# %% [21]
class Clock:

  def __init__(self, hours=0, minutes=0, seconds=0):
    self.__hours = hours
    self.__minutes = minutes
    self.__seconds = seconds

  def set(self, hours=0, minutes=0, seconds=0):
    self.__hours = hours
    self.__minutes = minutes
    self.__seconds = seconds

  def tick(self):
    self.__seconds += 1
    if self.__seconds == 60:
      self.__seconds = 0
      self.__minutes += 1
      if self.__minutes == 60:
        self.__minutes = 0
        self.__hours += 1
        if self.__hours == 24:
          self.__hours = 0
          return True  # 24시간이 경과하여 날짜 변경 필요
    return False

  def display(self):
    print(f'{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}')

  def __str__(self):
    return '%2d:%2d:%2d' % (self.__hours, self.__minutes, self.__seconds)

  def check(self):
    return self.__hours == 0 and self.__minutes == 0 and self.__seconds == 0


class Calendar:
  months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

  def __init__(self, day=1, month=1, year=2000):
    self.__day = day
    self.__month = month
    self.__year = year

  def leapyer(self, y):
    if y % 4:
      return 0
    elif y % 100:
      return 1
    elif y % 400:
      return 0
    else:
      return 1

  def set(self, day, month, year):
    self.__day = day
    self.__month = month
    self.__year = year

  def advance(self):
    months = Calendar.months
    max_days = months[self.__month - 1]
    if self.__month == 2:
      max_days += self.leapyer(self.__year)

    if self.__day == max_days:
      self.__day = 1
      if self.__month == 12:
        self.__month = 1
        self.__year += 1
      else:
        self.__month += 1
    else:
      self.__day += 1

  def __str__(self):
    return str(self.__year) + '/' + str(self.__month) + '/' + str(self.__day)


class CalendarClock(Calendar, Clock):  # MRO(Method Resolution Order) 고려한 다중상속

  def __init__(
      self, year=2000, month=1, day=1, hours=0, minutes=0, seconds=0
  ):
    Calendar.__init__(self, day, month, year)
    Clock.__init__(self, hours, minutes, seconds)

  def __str__(self):
    return Calendar.__str__(self) + ', ' + Clock.__str__(self)

  def tick_advance(self):
    # tick()이 True를 반환(자정 넘어감)하거나, check()가 True일 때 advance() 호출
    if self.tick():
      self.advance()


# %% [22]
x = Calendar()
for i in range(365*26+30*11+11):
  x.advance()
print(x)

y = Clock()
for i in range(18*60*60 + 46*60 + 32):
  y.tick()
print(y)


# %% [23]
x = CalendarClock(2020, 1,1,0,0,0)
for i in range((60*60*24)*(365*6+30*11+11)+(18*60*60 + 46*60 + 32)):
  # 60*60*24 -> 하루가 흘러가는 전체 시간 1일
  x.tick_advance()
print(x)


# ## 병원 클래스 상속


# %% [24]
# 클래스 리스트, 리스트를 멤버변수로 포함 , 클래스 함수의 매개변수로 리스트
# 클래스는 객체 : 변수에 대입, 매개변수 전달, 함수 리턴값으로 사용
# a = 10
# a = Hospical() # 클래스 인스턴스
class Hospiltal:

  def __init__(self, name):
    self.name = name
    self.patients = []                      # 리스트를 멤버변수

  def add_patient(self, patient):
    self.patients.append(patient)

class Patient:
  def __init__(self, name, diagnosis_list): # 매개변수도 리스트
    self.name = name
    self.diagnosis = diagnosis_list

# 사용 예

hospital = Hospiltal("대전의료원")
hospital.add_patient(Patient("트럼팡",['고혈압','협심증']))
hospital.add_patient(Patient("트럼풍",['천식']))

for p in hospital.patients:
  print(f"{p.name}:{p.diagnosis}")
