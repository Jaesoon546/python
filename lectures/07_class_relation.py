"""
07_ClassRelation.ipynb — 클래스 관계 (2026/11/11 7회차)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# 20261111 직업훈련 7회차


# # 클래스 관계


# %% [1]
# 리스트 요소로서의 class
class Patient:                      # 자료구조 ( 이질적 데이터 ) : 사용자 정의 데이터 타입
  def __init__(self, name, age, diagnosis):
    self.name = name
    self.age = age
    self.diagnosis = diagnosis

patients = [                        # 클래스 리스트 : 2차원 리스트와 같은 역할
    Patient("김철수", 70,"고혈압"), # instance
    Patient("이영희", 65,"당뇨병"),
    Patient("박민수", 60,"심부전")
]

for p in patients:
  print(f"{p.name} ({p.age})세: {p.diagnosis}")


# ## 클래스가 리스트를 멤버로 보유


# %% [2]
class MedicalRecord:

  def __init__(self, patient_name):
    self.patient_name = patient_name
    self.diagnosis = []               # 리스트 ( 병명관리 )

  def add_diagnosis(self, diagnosis):
    self.diagnosis.append(diagnosis)

record = MedicalRecord("홍길동")
record.add_diagnosis("고혈압")
record.add_diagnosis("당뇨병")

print(f"{record.patient_name}의 진단 내역: {record.diagnosis}")


# ## Dependency 클래스 관계


# %% [3]
# 종속 관계
class ReportFormatter:                            # 출력
  def format(self, report):
    return f"Formatted Report: {report.content}"

class ReportGenerator:                            # 객체 생성  Factory pattern
  def generate(self, content):
    report = Report(content)                      # 인스턴스
    return report

class Report:                                     # 데이터를 저장
  def __init__(self, content):
    self.content = content



report = ReportGenerator().generate("Annual Financial Report")
formatter = ReportFormatter()
formatted_report = formatter.format(report)
print(formatted_report)


# ## Association


# %% [4]
# 서로 독립적 관계

class Student:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.add_teacher(self) # 학생 객체에도 교사(self)를 자동으로 추가

t = Teacher("김 교사")
s1 = Student("김대한")
s2 = Student("김민국")

t.add_student(s1)
t.add_student(s2)

print([s.name for s in t.students])
print([tc.name for tc in s1.teachers])


# # Aggregation


# %% [5]
# 집합관계
# Association과 개념적으로 차이를 보임
# 두 객체가 서로 독립

class Engine:

  def __init__(self, number):
    self.number = number

  def start(self):
    print(f"Engine {self.number} is starting")

class Car:

  def __init__(self, make, engine):
    self.make = make
    self.engine = engine            # 멤버변수 : 인스턴스 한 다음 전달

  def start(self):
    print(f"The {self.make} car is starting")
    self.engine.start()

# Assocition 과 Aggregation은 외부에서 인스턴스
engine = Engine(number = 1) # 외부에서 인스턴스하고 Car의 매개변수로 전달
# 서로 독립
car = Car(make = "Toyota", engine = engine)
car.start()


# ## Composition


# %% [6]
# 포함관계 : 생사를 같이함
class Student:

  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

class Management:

  def __init__(self):
    self.student = []

  def add_student(self, name, age, grade):
    # student 지역변수 : GC가 참조되지 않는 데이터는 메모리 해제
    student = Student(name, age, grade)   # 함수 내부에서 instance
    self.student.append(student)

  def display_students(self):
    for student in self.student:
      print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

manager = Management()
manager.add_student("대한", 20, "A")
manager.add_student("민국", 22, "B")
manager.display_students()


# ## dependenct, Association, Aggregation, Composite, inheritance, realize 실현(추상클래스)


# %% [7]
# 상속과 재정의
# 상속하면 공통부분을 부모로 하고 상속받은 메쏘드를 재정의

import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:

    def __init__(self):
        print('부모 클래스 ')

    def area(self):
        print('면적')

    def perimeter(self):
        print('둘레')

class Triangle(Shape):

    def __init__(self, width, height ):
        self.width = width
        self.height = height

    def area(self):
        print("삼각형의 넓이는 = ", self.width * self.height / 2)

    def perimeter(self):
        print("삼각형의 둘레는 = ", self.width + math.sqrt(math.pow(self.width/2,2) + math.pow(self.height,2)) * 2 )

class Rectangle(Shape):

    def __init__(self, po1, po2):
        self.po1 = po1
        self.po2 = po2

    def area(self):
        print("사각형의 넓이는 = ", abs(self.po1.x - self.po2.x) *
              abs(self.po1.y- self.po2.y))

    def perimeter(self):
        print("사각형의 둘레는 = ", abs(self.po1.x - self.po2.x) * 2 +
               abs(self.po1.y- self.po2.y) * 2 )

class Circle(Shape) :

    def __init__(self, po1, r):
        self.po1 = po1
        self.radius = r

    def area(self):
        print("원의 넓이는 = ", math.pi * math.pow(self.radius, 2))

    def perimeter(self):
        print("원의 둘레는 = ", 2 * math.pi * self.radius)


# ## facade pattern


# %% [8]
class ShapeMaker:

  def __init__(self):
    po = Point(10,10)                   # 기능
    po2 = Point(20,20)
    self.circle = Circle(po,10)
    self.rectangle = Rectangle(po,po2)
    self.triangle = Triangle(10,20)

  def drawCircle(self):
    self.circle.area()

  def drawRectangle(self):
    self.rectangle.area()

  def drawTriangle(self):
    self.triangle.area()


# ## Factory pattern


# %% [9]
class ShapeFactory: # 생성 패턴 - factory 패턴

  def getShape(self, shapeType):
    if(shapeType == None):
      return
    if(shapeType=="CIRCLE"):
      po = Point(10,20)
      return Circle(po,5)
    elif(shapeType=="RECTANGLE"):
      po = Point(10,20)
      po2 = Point(30,30)
      return Rectangle(po,po2)
    elif(shapeType=="TRIANGLE"):
      return Triangle(10,20)
    else :
      return


# %% [10]
class FactoryPatternDemo:
  ShapeFactory = ShapeFactory()
  shape1 = ShapeFactory.getShape("CIRCLE")
  shape1.area()
  shape2 = ShapeFactory.getShape("RECTANGLE")
  shape2.area()
  shape3 = ShapeFactory.getShape("TRIANGLE")
  shape3.area()
demo = FactoryPatternDemo()


# # Singleton pattern


# %% [11]
# cls를 매개변수로 받는 경우 : classmethod ( 초기화 방법을 달리하고자 할 때 )
# 한번만 인스턴스 되는 객체
class Person():
  __instance = None                   # static 공유변수 ( class 변수 )

  def __new__(cls, *args, **kwargs):  # 인스턴스 하기 전에 호출 되는 함수
    if not cls.__instance:            # cls.__instance 거짓은 초기화가 안되었을 때
      cls.__instance = super(Person, cls).__new__(cls) # 인스턴스가 됨
    return cls.__instance

  def  __init__(self, name):          # 멤버변수를 초기화
    self.name = name

dunsan = Person("초등학교")
chumgnam = Person("대학교")

print(dunsan.name)
print(chumgnam.name)


# # 팀과제 : 클래스 베이스 성적 프로그램 작성
# Class는 3개로 작성
#  + Student : 1 인분의 데이터를 처리 ( CRUD, 합계, 평균, 학점 )
#  +  Management : 여러명의 학생을 관리 ( CRUD, 등수처리 )
#  + Menu : 입력, 출력, 성적계산, 학생 검색, 수정, 삭제, 과목별 합계와 평균,프로그램 종료
