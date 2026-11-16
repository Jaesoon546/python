"""
01_variables.ipynb — 변수 (2026/11/03 직업훈련 1회차)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# 2026/11/03 화요일 직업훈련 1회차


# # Ubuntu linux system : 가상 컴퓨터 ( 웹으로 제어 )
# - version 24.04
# - 운영체제 ( operation system ) : window(GUI : graphic user interface), linux (server) - service
# - colab : python 기반


# %% [1]
# 리눅스 + 출력 + 파일 경로
# / root 경로 , 하위 폴더를 /로 구분
# cell
# etc -> 윈도우에서의 제어판 역할
# !cat /etc/*release


# # 연습


# %% [2]
# !uname -a


# %% [3]
# 드라이브와 colab 연결
from google.colab import drive
drive.mount('/content/drive')


# %% [4]
# !pwd # 주석 : present working directory 작업디렉토리


# %% [5]
# cd -> Change directory
# %cd /content/sample_data


# %% [6]
# !pwd


# %% [7]
# %cd /content


# %% [8]
#mk - make directory
# !mkdir test


# %% [9]
# list
# !ls


# # Python
# - 객체지향 프로그래밍 언어
# - 기계어(2진수로 프로그래밍), assembly (기계어와 1:1로 매핑)  -> C(고급언어)
# - C ( 메모리 동적할당 : malloc, free ) -> C++ (데이터 + 함수 => class 객체) -> JAVA ( 함수 하나를 만들려고 해도 class로 만들어야 함 + 기본데이터타입 )
# - 고급언어 ( python : 모든 것을 객체 지향언어로 함수까지도 객체로 만듬 )
# - Interpreter 언어 ( 해석 ) : 컴파일러 ( C, C++, JAVA )
# - Interactive 언어 : 대화형 언어
# - scripting 언어 : javascript ( html안에서 동작 )


# # 문법적 특징
# - 데이터 타입을 지정하지 않음 : 변수가 주소만 가지기 때문 ( pointer )
# - 데이터 타입을 확인 ( type ) -> 프로그램하는 사람이 책임
# - 메모리에 데이터를 저장하면 반드시 데이터 타입을 알아야 함
#   - A : 65
#   - 65 : 65 -> 데이터 타입을 알아야 데이터 해석 가능
# - 메모리 해제 : GC( garbage collection 참조(reference)하는것이 없으면(주소가 없어지고 데이터만 있을때) ) 이 자동으로 해제(데이터삭제)


# ## 변수와 주소


# %% [10]
# 변수 -> 메모리 주소 = 데이터 주소( heap ) -> 데이터를 가리킴
a = 10
b = a # a의 주소가 b로
print(a)
print(b)
print("주소값 대입", id(a)), print(id(b)) #id : 주소를 가리킴
a = 20
print(a)
print(b)
print("주소값 대입", id(a)), print(id(b))


# ## 데이터 타입


# %% [11]
# 자동으로 데이터 타입을 지정
a = 10  # 1010 : 데이터 표현 비트개수
print(type(a)) # 데이터 타입도 객체 => 파이썬에서는 모든 것이 객체이다.
a.bit_length() # 4 비트


# ## 타입변환


# %% [12]
# 입출력은 text로 함, 네트워크 전송 : text로 함
problem = input("수식을 입력하시요")
print(problem) # int, str 숫자형인가 문자형인가
print(type(problem)) # str
print(eval(problem))
print(type(eval(problem))) # 타입 변환 : 수치 연산은 test는 불가 -> 형변환 ( typecasting )


# ## 형변환


# %% [13]
# 형변환
print(int("23"))
print(float("23.5")) # 부동소수점 : 소수점이 있는 데이터 0.235 * 10**2( 10^2 )로 만듬 지수부2 + 가수부 235 => 많은수를 저장하기위함
print(eval("23"))
print(eval("23.5"))
x = 5
print(eval("23 + (2 * x)")) # eval : 수식으로 변환하여 사용가능하기에 사용
x = 5.0
print(eval("23 + (2 * x)"))


# %% [14]
a3 = 4.24e-3 # exponent 지수형 0.00424
a4 = 0o177   # octal 8진수
print(a3)
print(a4)
# 단항연산자가 우선
print((1* 8**2) + (7* 8**1) + (7* 8**0))
64 + 56 + 7 # => 127


# ## 문자열


# %% [15]
# 문자열
#string integer( 정수 )
#입출력은 문자열을 생성
print('My name is %s and I am from %s , %i .' % ('AI', '4차산업혁명', 10))# % format : C 방식
print('My name is {1} and I am from {0} and I like {thing}'.format('딥러닝', 'AI', thing='cats')) # C# 방식
name = '박재순'
age = 27
print(f"이름은 {name} 나이는 {age}") #최근방식 : f 문자열


# ## 문자열 배열


# %% [16]
# 문자열 배열 , 공백도 문자열, 배열은 인덱싱으로 위치를 가리킬 수 있음
# 인덱스는 0부터 시작
fullName = input("이름을입력하세요: ") # 문자열 변수
# 파이썬은 문자열 변수도 객체 ( 데이터 + 함수 )
n = fullName.rfind(" ") # reverse 거꾸로 , 공백또한 문자열
                   # 0 1 2 3
print(fullName[0]) # 박 재순 문자열은 배열에 저장 : 인덱스 0 부터 시작
print(fullName[1])
print(fullName[2])
print(n)
print("이름:", fullName[n+1:]) # 인덱싱 범위(:)  ~ 끝까지
print("성(s)", fullName[:n])   # 없으면 처음부터 *끝은 포함이 되지않음


# ## 문자열 연산과 인덱싱


# %% [17]
# 문자열 연산과 인덱싱
# 10 + 10 => 20
s = 'korea'
print(s + s) # 연산자의 의미가 오버로딩
print(s * 3) # 반복
print(s[0:]) # 끝까지
print(s[4])  #
print(s[-1]) # 뒤에서 부터 시작해서
print(s[1:3])# 뒤에 것은 제외하고

print(s[-2:])
print(s[-2:5])
print(s[3:-1])
print(len(s)) # 문자개수
s.split('r')  # r을 중심으로 나누기 ( 파이선에서 기본적인 데이터 처리는 [] 리스트로 함 )
# () : 함수,tuple , {} : dict, set , [] : 리스트, 문자열 배열
# 파이썬 자료구조
# () : tuple : list와 같지만 불변
# {} : dict(key data), set(key) 형태로 저장(검색이 빠름)
# [] : list : 주소를 담고있는 자료구조 -> 이질적 데이터 저장이 가능 문자 + 숫자 혼합
# 자료구조 : 대량의 데이터


# %% [18]
# 처리한 결과의 데이터타입 체크
t = 'Seoul, Incheon, won'.split(",")
print(t) # 리스트
print(','.join(t)) # 문자열
type(','.join(t))


# %% [19]
# 데이터 타입도 객체 ( int, float, str )
s = 'korea'
print(s.capitalize()) # original은 변하지 않음 -> 대입해야 변형
#s = print(s.capitalize()) 변화는 대입을 통해서
print(s.find('r'))    # 정방향
print(s.count('re'))  # 카운트
print(s.isalpha())    # 문자 확인
print(s.isdigit())    # 숫자 확인
print('0123'.isdigit())
print(s.replace('r', 'R')) # 크롤링 ( 원하지 않는 문자가 출력되는걸 방지 )
print(s.startswith('K'))
print(s.endswith('a'))


# %% [20]
# 숫자에서 문자로 캐스팅 ( 타입변환 )
f = 1.23
g = str(f)
h = repr(f) # 숫자를 문자로 만들 때 더 정교하다
print(g, "   ", h)

print(type(f))
print(type(g))
print(type(h))


# ## 연산자


# %% [21]
a = 3
b = 4

print(a + b, a - b, a * b, a / b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # % 나머지 연산자 -> 경우의 수를 만들 때 사용
# 컴퓨터 프로그래밍은 가능한 경우 다 처리 -> 완벽한 프로그램 ( 경우의 수 만큼으로 나누어주면됨 )


# ## 자료구조 : 리스트


# %% [22]
# 자료구조 : 리스트
# 숫자 = > +-*/
# 문자 = > ** 오버로딩
li = [4,7,8]
lj = [5,6,7]
print(li+lj)
# sum(1.2) C언어 에서는 해당만 가능
print(sum(li)) # 함수의 매개변수로 리스트를 받는다.
print(type(li))
li * 3


# %% [23]
# indent 들여쓰기 : 블록을 의미함
num1 = input("정수를 입력하시오: ") # 데이터 입력시 데이터 타입 : str 10, 5
num2 = input("정수를 입력하시오: ")
hab = int(num1) + int(num2) # 타입변환
quotuent = hab // 2 # 몫 연산자
remainder = hab % 2 # 나머지 연산자
print("입력된 수를 2로 나눈 결과 몫 = ", quotuent, "나머지 = ", remainder)

if remainder == 0:
  print("짝수입니다. ")
else:
  print("홀수입니다. ")


# ## 전역변수 지역변수


# %% [24]
# 전역변수
x = 300 # 함수밖에서 선언 ( 전역변수 )
def myfunc(): # 함수는 어디에서 실행 : stack에서 실행
  # 함수 안에서 선언된 변수는 지역변수 , 지역변수가 우선 , 지역변수는 함수와 수명을 같이함
  x = 200; # 세미콜론 문장의 종료점 : 생략가능 ( c언어는 필수 )
  print(x)
myfunc()
print(x)


# %% [25]
# LEGB 규칙 : 변수를 local,  enclosing, global, builtt-in( 파이썬 기본 명령어 ) 에서 찾음
x = 300
def myfunc(): # local에 변수가 없으면 global ( 전역 )에서 찾는다
  print(x)
myfunc()
print(x)


# %% [26]
globals()
