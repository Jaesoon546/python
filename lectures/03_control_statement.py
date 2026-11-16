"""
03_Control Statement.ipynb — 제어문 (2026/11/05 3회차)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# 2026/11/05 직업훈련 3회차


# # 제어문
#  + 제어문
#  + 조건문과 반복문
#  + 조건문의 거짓조건 : 0, "", [], {}. (), None ( 주소를 가지지 않은 null )
#  + if, elif, else 경우수를 판단
#  + for in
#    - collections, range, iterator, generator, zip


# %% [1]
score = 70
# 연산의 순소서 : 산술연산 -> 관계연산 -> 논리 연산
if score >= 80 + 10 and score <= 100 :     # 조건식 결과값 boolean ( True/False )
  print("80이상")
else:
  print("80이하")


# %% [2]
city=''             # False
if not city:        # 거짓이면 실행
  print("빈문자열")


# %% [3]
# 3항 연산자
x = 5
ans = '양수' if x>=0 else '음수'
print(ans)


# %% [4]
names = ['대한이', '민국이','만세야']
name = '대한이'
for name in names : # 포함 연산자의 결과값은 True/False
  print(name)


# #split


# %% [5]
# 다음 데이터에서 010만 분리하시요
tel = "010-123-4567"
print(tel.split("-"))
tel.split("-")[0]


# %% [6]
firstNumber = input().split("-")[0]
if firstNumber == "011":
  telecom = "SKT"
elif firstNumber == "016":
  telecom = "KT"
elif firstNumber == "019":
  telecom = "LGU"
else:
  telecom = "알 수 없는"
print(f"당신은 {telecom} 사용자입니다.")


# # 문제 1


# %% [7]
# 두 수를 입력해서 숫자이면 합계를 내서 출력하고 아니면 숫자가 아닌 것이 있는지 확인하시오
# 경우의 수 : 4가지
# 숫자 or 문자 isdigit, isalpha


num1 = input("숫자를 입력하세요 : ")
num2 = input("숫자를 입력하세요 : ")

if num1.isdigit() and num2.isdigit():
  print("합계는", str(eval(num1) + eval(num2)) + ".")
elif not num1.isdigit():
  if not num2.isdigit():
    print("둘 다 숫자가 아님")
  else:
    print("처음수가 숫자가 아님")
elif not num2.isdigit():
  print("두번째 수가 숫자가 아님")


# # 문제 2


# %% [8]
# 수입( income ) 과 지출( costs ) 를 입력 받아서 순수입을 출력하는 프로그램을 작성하시요
# 경우의 수 : 3가지 ( 순수익(profit), 순손실(loss), 동등 break even point )

income = eval(input("수입를 입력하세요 : "))
costs = eval(input("지출를 입력하세요 : "))
profit = income - costs
loss = income - costs

if (income - costs) > 0:
  print(f"순수익은 : {profit}")
elif (income - costs) < 0:
  print(f"순손실은 : {loss}")
elif (income - costs) == 0:
  print("수입과 지출이 같습니다.")


# %% [9]
# 수입( income ) 과 지출( costs ) 를 입력 받아서 순수입을 출력하는 프로그램을 작성하시요
# 경우의 수 : 3가지 ( 순수익(profit), 순손실(loss), 동등 break even point )

income = eval(input("수입를 입력하세요 : "))
costs = eval(input("지출를 입력하세요 : "))
profit = income - costs
loss = income - costs

if costs == income:
  result = "손익분기점입니다."
elif costs < income:
  profit = income - costs
  result = "순수익 = {0.2f}".format(profit)
else:
  loss = costs - income
  result = "순손실 = {0.2f}".format(profit)

print(result)


# # 문제 3


# %% [10]
# 반응에 따른 날씨 예측 프로그램
#                           BLUE    RED
# STEADY(안정적 기분)       화창    비오는날
# FLASHING(변덕스런 기분)   구름    눈오는날
# color와 mode를 입력 받아서 처리하는 프로그램을 작성하시오
# 경우의 수 : 4가지

color = input("색상을 입력하세요 BLUE or RED : ")
mode = input("기분을 입력하세요 STEADY or FLASHING : ")

if color == "BLUE" and mode == "STEADY":
  print("화창한 날")
elif color == "BLUE" and mode == "FLASHING":
  print("구름낀 날")
elif color == "RED" and mode == "STEADY":
  print("비오는 날")
else :
  print("눈오는 날")


# %% [11]
# chaining 연쇄
color = input("색상을 입력하세요 BLUE or RED : ")
mode = input("기분을 입력하세요 STEADY or FLASHING : ")

color = color.upper() # 대소문자 구분
mode = mode.upper()
result = ""

if color == "BLUE" and mode == "STEADY":
  result = "화창한 날"
elif color == "BLUE" and mode == "FLASHING":
  result = "구름낀 날"
elif color == "RED" and mode == "STEADY":
  result = "비오는 날"
else :
  result = "눈오는 날"
print("예측된 날씨는 ", result)


# # 문제 4


# %% [12]
# 점수 ( jumsu )를 입력받아서 A, B, C, D, F 학점으로 출력하시요
# A = 90, B = 80, C = 70, D = 60, F
jumsu = eval(input("점수를 입력하시오 : "))
result = ""
if jumsu >= 90 :
  result = "A학점"
elif jumsu >= 80 and jumsu < 90:
  result = "B학점"
elif jumsu >= 70 and jumsu < 80:
  result = "C학점"
elif jumsu >= 60 and jumsu < 70:
  result = "D학점"
else :
  result = "F학점"

print(f"점수는 {jumsu} 이고 "f"학점은 {result}입니다.")


# #문제 5


# %% [13]
# 1개의 과일 가격이 100.50 원 에 세금 12.5%를 붙여서 팔았다.
# 판매가격, 세금, 순매출액을 출력하시요

x = float(100.50)
y = float(12.5/100)

p = (x * y) + x
s = p * y
total = p - s

print(f"판매가격은 {p}")
print(f"세금은 {s}")
print(f"순매출액은 {total}")


# %% [14]
price = 100.50
tax_rate = 12.5 / 100
tax_per_one = price * tax_rate
sales_price = price * (1 + tax_rate)
print(f"1개 판매가격 = {round(sales_price, 2)}, 세금={round(tax_per_one, 2)}, 순매출액={round(sales_price - tax_per_one, 2)}")


# # 문제 5


# %% [15]
# 문제 : 제곱미터로 입력되는 아파트 면적을 평형으로 계산해서 종류로 판정하시요
# 소형( 17평이하 ) 중형 (17 ~ 30) 대형 ( 30이상 )
# 평수 = 제곱미터 / 3.305

m2 = eval(input("아파트의 면적을 입력하세요 : "))

x = m2 / 3.305

print(f"아파트의평수는 : {x}")

result = ""
if x <= 17 :
  result = "소형입니다."
elif x > 17 and x < 30:
  result = "중형입니다."
else :
  result = "대형입니다."
print(result)


# #문제 6


# %% [16]
# 문제
# 놀이 공원 매표소 단체 입장료 계산하기
# 조건 : 팀별 인원 구성을 입력 ( 초등, 청소년, 일반인, 경로대상 )하면 입장료 소견표에 따라
# 정산요금 : 초등(h1) (5000원), 청소년(h2) (10000원), 일반인(h3)(15000원), 경로대상(h4)(3000원)
# 팀별 할인 카드 확인
# 카드없음 : 할인무, 일반카드 : 10%, VIP 20% 할인
# 위의 데이터를 참조해서 총 요금 계산

team = input("총 몇명인지 입력하시오 : ") # 총인원 구하기
h1 = eval(input("초등학생의 수를 입력하시오 : "))
h2 = eval(input("청소년의 수를 입력하시오 : "))
h3 = eval(input("일반인의 수를 입력하시오 : "))
h4 = eval(input("경로대상의 수를 입력하시오 : "))

total_h = int(h1 + h2 + h3 + h4)
total_m = int(h1 * 5000) + int(h2 * 10000) + int(h3 * 15000) + int(h4 * 3000)
card = input("결제할 카드를 입력하세요(카드없음, 일반카드, VIP카드 ) : ") # 카드없음, 일반카드, VIP카드
#sel = int(input("카드없음(0), 일반카드(1), VIP(2)를 선택해 주세요"))
#if sel == 0: total_cost = total_m
#elif sel == 1: total_cost = total_m - (total_m * 0.1)
#elif sel == 2: total_cost = total_m - (total_m * 0.2)
#else: total_cost - total_m
#print("총요금은", total_cost, "원 입니다. ")

#sel = int(input("카드없음(0), 일반카드(1), VIP(2)를 선택해 주세요"))
#select = [total_m, total_m - (total_m * 0.1), total_m - (total_m * 0.2)]
#print("총요금은", select[sel], "원 입니다. ")

result = 0

if card == "일반카드":
  result = total_m - (total_m * 0.1)
elif card == "VIP카드":
  result = total_m - (total_m * 0.2)
else:
  result = total_m

print(f"총 인원은 {total_h}명 입니다.")
print(f"총 요금은 {result}원 입니다.")


# #문제 7


# 과세표준	세율	누진공제
# + 14,000,000원 이하	6%	-
# + 14,000,000원 초과 50,000,000원 이하	15%	(누진공제)1,260,000원
# + 50,000,000원 초과 88,000,000원 이하	24%	(누진공제)5,760,000원
# + 88,000,000원 초과 150,000,000원 이하	35%	(누진공제)15,440,000원
# + 150,000,000원 초과 300,000,000원 이하	38%	(누진공제)19,940,000원
# + 300,000,000원 초과 500,000,000원 이하	40%	(누진공제)25,940,000원
# + 500,000,000원 초과 1,000,000,000원 이하	42%	(누진공제)35,940,000원
# + 1,000,000,000원 초과	45%	(누진공제)65,940,000원


# %% [17]
# 소득세계산
# 소득 세율표를 보고 이를 이용해 소득을 입력받아 세금이 얼마인지 계산하는 프로그램을 작성하시오
# 입력되는 연봉을 과세표준으로 계산합니다 .
# 과세표준 - 공제액으로 계산

# 변수 x = 연봉 , y = 세율 , z = 공제액

x = int(input("연봉을 입력하세요 : "))
# income = [14000000, 50000000,88000000, 150000000, 300000000, 500000000, 1000000000] income[0] ~ income[7]
y = [0.06, 0.15, 0.24, 0.35, 0.38, 0.40, 0.42, 0.45] # y[0] ~ y[7]
z = [1260000, 5760000, 15440000, 19940000, 25940000, 35940000, 65940000] # z[0] ~ z[6]
#z = [0, 1260000, 5760000, 15440000, 19940000, 25940000, 35940000, 65940000] # z[0] ~ z[7]

if x <= 14000000:
  total = x * y[0]
elif x > 14000000 and x <= 50000000:
  total = x * y[1] - z[0]
elif x > 50000000 and x <= 88000000:
  total = x * y[2] - z[1]
elif x > 88000000 and x <= 150000000:
  total = x * y[3] - z[2]
elif x > 150000000 and x <= 300000000:
  total = x * y[4] - z[3]
elif x > 300000000 and x <= 500000000:
  total = x * y[5] - z[4]
elif x > 500000000 and x <= 1000000000:
  total = x * y[6] - z[5]
else :
  total = x * y[7] - z[6]

print(f"세금은 : {total} 원 입니다.")


# # 반복문


# %% [18]
# collections, range, iterator, generator, zip, enumerate
elements = ["earth", "air", "fire", "water"] # collections : list
for i in elements:
  print(i , end=" ")

# range로 변경해서 출력
for i in range(0,len(elements)):
  print(elements[i], end=" ")


# %% [19]
cart = [10, 20, 500, 700, 50, 60] # 500초과는 출력하지 않음 ( filtering )
for item in cart:
  if item<=500:
    print(item, end=" ")


# %% [20]
for item in cart:
  if item>500:
    #continue # 건너뛰기 할때
    break # 중지
  print(item, end=" ")


# %% [21]
for item in cart:
  if item>500:
    continue # 건너뛰기 할때
    #break # 중지
  print(item, end=" ")


# #문제 8


# %% [22]
# 다음 데이터에서 target을 검색하시오
items = [1,5,7,9,11,15]
target = 9

for item in items:
  if item == target:
    print(f"타겟을 찾았습니다 : {item}")
    break
  print(f"현재값 : {item}")


# # range 생략


# %% [23]
# 함수의 매개변수 : 일치해야 됨 ( 디폴트 매개변수 : 매개변수에 정해진 값 )
# range ( 초기값, 한계값, 증강값 )
print(list(range(10)))            # 생략된 것 range(0, 10, 1)
print(list(range(10,2)))          # 생략된 것 range(10, 2, 1)
print(list(range(1,10)))          # 생략된 것 range(1, 10, 2)
print(list(range(1,10,2)))
print(list(range(10,1,-1)))
print(list(range(1,11,-1)))
print(list(reversed(range(10))))  # 역순


# #iterator


# %% [24]
# iterator 반복자 = 포인터의 다음 주소를 가리킴
# call by reference
# 처리순서를 변경 : 제어문 ( 조건문, 반복문 ), 함수, 예외처리, 비동기
def is_iterable(obj):
  try: # 예외처리 : 프로그램은 예외를 처리하고 계속되어야 한다.
    iter(obj)       # iterator 를 구성
    return True
  except TypeError: # 예외가 발생하면 처리
    return False
print(is_iterable([1,2,3,])) # 데이터는 HEAP에 저장 주소를 변수 입력
print(is_iterable("Python")) # 문자열 -> 정적 배열
print(is_iterable(42))       # 정수 단독


# %% [25]
ra = range(4) #0, 1, 2, 3
ra = iter(ra)
print(next(ra))
print(next(ra))
print(next(ra))
print(next(ra))
# print(next(ra)) 다음은 없기에 오류 발생


# #sorted


# %% [26]
print(sorted([7,1,2,6,0,3,2])) # reverse=True, key=lambda x:x[0] : 무명함수(일회용)


# #Zip


# %% [27]
# zip : 같은 인덱스 끼리 결합
seq1 = ['a','b','c']
seq2 = ['d', 'e']
seq3 = [False, True]
zipped = zip(seq1, seq2, seq3) # 변동 매개변수
list(zipped)


# %% [28]
for i, (a, b) in enumerate(zip(seq1, seq2)):
  print("%d %a %s" %(i,a,b))
list(reversed(range(10)))


# #문제 9


# %% [29]
# 1 ~ 10까지의 합을 계산 (for)
# 변수는 초기화( 포인터가 없는 변수 -> 에러 발생 )
sum_t = 0
for i in range(1,11):
  sum_t = sum_t + i
  # sum_t+=i
print(sum_t)


# %% [30]
print(list(range(1,11)))
x = sum(list(range(1,11)))

print(x)


# %% [31]
sum(range(1,11))


# # 이중 for 문


# %% [32]
for x in range(2, 10):
  for y in range(2, 10):
    print(f"{y} * {x} = {x*y}", end="\t")
  print()


# %% [33]
for x in range(2, 10):
  for y in range(2, 10):
    print(f"{x} * {y} = {x*y}", end="\t")
  print()


# # While


# %% [34]
# while문 ( 조건이 참이면 계속 실행 )
# for ( 초기값, 한계값, 증강값 )
i = 0
sum_t = 0
while i < 10 :
  i += 1        # i = i + 1 증가변수
  sum_t += i    # 누적변수
print(sum_t)


# %% [35]
# 무한 반복문
# while True:
#     val = input("종료하려면 'exit'를 입력하세요: ")
#     if val == "exit":
#         print("반복을 종료합니다.")
#         break  # 반복문 탈출

# while 1:
#     val = input("용량을 입력하시오")
#     if val.upper() == "Q":
#         print("반복을 종료합니다.")
#         break  # 반복문 탈출


# # 문제 10


# %% [36]
#while 문을 이용해서 3,4,5,6,7 만 합계를 내시요
i = 0
sum_t = 0
while i < 10 :
  i += 1
  if i > 2 and i < 8:
    sum_t += i
print(sum_t)


# %% [37]
#while 문을 이용해서 3,4,5,6,7 만 합계를 내시요
#countinue, break
i = 0
sum_t = 0
while i < 10 :
  i += 1
  if i < 3 : continue
  if i > 7 : break
  else:
    sum_t += i
print(sum_t)


# #문제 11


# %% [38]
# 입력 형식 10k or 10M or 10G 와 같은 형식으로 입력하고
# 입력데이터의 용량을 바이트로 변환해서 출력하시요
# 입력은 무한대로 하고 Q가 입력이 되면 중지하게 하시요
# 10k = 10 * 1024(byte)
# 10M = 10 * 1024(byte) * 1024(byte)
# 10G = 10 * 1024(byte) * 1024(byte) * 1024(byte)
byte = 1024

while 1:

    D = input("용량의 크기를 입력하시오 : ")
    if D.upper() == "Q":
      print("반복을 종료합니다.")
      break
    val = eval(input("용량을 입력하시오 : "))
    if D.upper() == "K":
      K = int(val * byte)
      print(f"{val}K의 바이트는 {K} byte 입니다.")
    elif D.upper() == "M":
      M = int(val * byte * byte)
      print(f"{val}M의 바이트는 {M} byte 입니다.")
    elif D.upper() == "G":
      G = int(val * byte * byte * byte)
      print(f"{val}M의 바이트는 {G} byte 입니다.")
    else :
      print("다른문자를 입력해주세요")


# %% [39]
UNIT = 1024
criterion = ['K', 'M', 'G']  # 단위를 체크할 기준 리스트 정의

while True:
    volumein = input("용량의 크기를 입력하세요 (종료: Q): ")

    if not volumein:
        continue

    volumein = volumein.strip()

    if volumein.upper() == 'Q':
        print("프로그램을 종료합니다.")
        break

    # 마지막 글자를 단위(scale), 나머지를 숫자(num)로 분리
    num = volumein[:-1].strip()
    scale = volumein[-1]
    calcunit = scale.upper()

    # 숫자 판별 및 단위 유효성 검사
    if not num.isdigit() or calcunit not in criterion:
        print("잘못 입력하였습니다. 숫자로 입력하고 단위는 K, M, G 중 하나로 입력하세요.")
        continue

    volume = int(num)

    if calcunit == 'K':
        volume_res = volume * UNIT
    elif calcunit == 'M':
        volume_res = volume * UNIT * UNIT
    elif calcunit == 'G':
        volume_res = volume * UNIT * UNIT * UNIT
    else:
        print("계산 가능한 용량단위가 아니므로 다시 입력하시오")
        continue

    print(f"입력한 용량 {volumein} 은 {volume_res} 바이트입니다.")


# #Random


# %% [40]
# 난수 : 의사난수 출력 순서가 결정되어 있음
# seed 값 ( 시작하는 위치 )
import random
com = random.randint(1,100) # 100도 포함됨
com


# %% [41]
while 1:
    val = input("")
    if val.upper() == "Q":
        print("반복을 종료합니다.")
        break  # 반복문 탈출
    com = random.randint(1,100)
    print(com)


# # 문제 12


# %% [42]
# 컴퓨터가 상상한 값을 유저가 맞추려고 합니다 .
# computer는 난수로 결정하고 user는 입력으로 처리합니다 .
# 무한루프 동작
# Q 또는 값을 맞추면 종료 합니다.

com = random.randint(1,10)
while 1:
    val = input("Q를 입력하거나 값을 맞추면 종료합니다.")
    if val.upper() == "Q":
        print("반복을 종료합니다.")
        break  # 반복문 탈출
    user = int(val)
    if user == com:
      print("정답을 맞추었습니다. 반복을 종료합니다.")
      break
    elif user < com:
      print("입력된 값보다 큽니다.")
    else :
      print("입력된 값보다 작습니다.")
print(com)
#사람이 입력한 값과 com의 값을 비교해서 작은지 큰지 알려준다


# %% [43]
user = 2
while 1:
    com = random.randint(1,10)
    if user == com:
      print("정답을 맞추었습니다. 반복을 종료합니다.")
      break
    elif user > com:
      print("입력된 값보다 큽니다.")
    else :
      print("입력된 값보다 작습니다.")
print(com)


# %% [44]
# 사람이 8번 이상 입력하면 진 것으로 하도록 제약하시오
import sys
while(1):
  com = random.randint(1,100)
  count = 0
  while 1:
      val = input("Q를 입력하거나 값을 맞추면 종료합니다.")
      count += 1
      if val.upper() == "Q":
          print("반복을 종료합니다.")
          sys.exit()  # 반복문 탈출
      user = int(val)
      if user == com:
        print("정답을 맞추었습니다. 반복을 종료합니다.")
        sys.exit()
      elif user < com:
        print("입력된 값보다 큽니다.")
      elif user > com:
        print("입력된 값보다 작습니다.")
      if count == 8:
        print("8번 이상입력하여 게임을 다시 시작합니다")
        break
  print(com)


# #문제 13


# %% [45]
# 전체 게임 회수를 출력하고, 몇승 몇패인지 출력하시오
# 게임당 몇번 입력했는지 평균 입력점수를 출력하시오
import sys
total_count = 0
win = 0
total_apptemp = []
while(1):
  com = random.randint(1,100)
  count = 0
  total_count += 1

  while 1:
      val = input("Q를 입력하거나 값을 맞추면 종료합니다.")
      count += 1
      if val.upper() == "Q":
          print(f"전체 게임 횟수는 {total_count-1} 번 했습니다. 총 {win} 승 하셨습니다. 총 {total_count-win-1} 패 하였습니다.")
          avg = sum(total_apptemp) / (total_count-1)
          print("평균시도횟수", avg)
          sys.exit()  # 반복문 탈출
      user = int(val)
      if user == com:
        print("정답을 맞추었습니다. 반복을 종료합니다.")
        win += 1
        total_apptemp.append(count)
        break
      elif user < com:
        print("입력된 값보다 큽니다.")
      elif user > com:
        print("입력된 값보다 작습니다.")
      if count == 5:
        total_apptemp.append(count)
        print("5번 이상입력하여 게임을 다시 시작합니다")
        print(f"정답은 {com} 입니다. ")
        break
  print(f"전체 게임 횟수는 {total_count} 번 했습니다.")


# %% [46]
# list comprehenslon

a = [x * 2 for x in range(5)]    # list
b = {x * 2 for x in range(5)}    # set
c = {x: x * 2 for x in range(5)} # dict
d = (x * 2 for x in range(5))    # generator

print(a)
print(b)
print(c)
print(list(d))
print(d)


# %% [47]
gen = (x * 2 for x in range(5))  # generator 함수화

while True :
  try :
    val = next(gen)
    print(f"꺼낸 값 : {val}")
  except StopIteration:
    print("StopIteration 감지 : 순화가 완료되었습니다.")
    break


# # list comprehension


# %% [48]
result = []
for x in range(10):
  if x % 2 == 0:
    result.append(x * 2)
print(result)
result_2 = [x * 2 for x in range(10) if x % 2 == 0]
print(result_2)


# %% [49]
rows = range(1,5)
cols = range(10, 15)
# 이중 for문으로 구성된 list comprehension
vectors = [(r, c)for r in rows if r % 2 for c in cols if c % 2]
vectors


# %% [50]
#list comprehension을 이용해서 1 ~ 20까지의 수중에 2의 배수와 5의 배수만 출력하시오
val = []

for x in range(1,21):
  if x % 5 == 0 or x % 2 == 0:
    val.append(x)
print(val)


# %% [51]
val = [x for x in range(1,21) if x % 2 == 0 or x % 5 == 0]
val


# #과제
# 20261105_박재순_성적프로그램


# %% [52]
# # 반복문으로 코드길이 짧게
# school = []
# for i in range(3):
#   name = input("이름을 입력하시오 : ")
#   kor = eval(input('국어점수를 입력하시오 : '))
#   school.append([name, kor])

# school.sort(key=lambda row: row[1], reverse=True)
# print(school)


# %% [53]
# # 각 학생의 점수를 합계를 내서 마지막에 추가하시요
# sungjuk = [['하하하', 100, 100, 100],['유재석', 99, 99, 98],['추신수', 90, 98, 91]]

# for i in range(len(sungjuk)):
#   total = sungjuk[i][1] + sungjuk[i][2] + sungjuk[i][3]
#   average = int(total/3 *100)/100
#   sungjuk[i].append(total)
#   sungjuk[i].append(average)
# print(sungjuk)

# # 총점을 기준으로 정렬해서 출력하시오 (오름차순으로 정렬)
# sungjuk.sort(key=lambda row: row[4])
# print(sungjuk)
# # 내림차순으로 정렬해 놓고 등수를 만들어 입력 하시오
# sungjuk.sort(key=lambda row: row[4], reverse=True)
# for z in range(len(sungjuk)):
#   sungjuk[z].append(z+1)
# print(sungjuk)

# # 출력은 이름을 기준으로 해서 오름차순으로 정렬해서 출력
# sungjuk.sort(key=lambda row: row[0])
# print(sungjuk)

# 번호 이름   국어 수학 영어 총점 평균   학점 등수
# 1    김대한 100  90   90   280  93.33  A    1
# 2    김민국 90   80   90   260  86.67  B    2
# 3    김만세 80   80   80   240  80     B    3


# %% [54]
# for i in range(len(sungjuk)): #학생수
#   for j in range(len(sungjuk[i])):
#     print(sungjuk[i][j], end=' ')
#   print()


# %% [55]
#print(round(val, 2)) 소숫점


# %% [56]
# for x in range(2, 10):
#   for y in range(2, 10):
#     print(f"{x} * {y} = {x*y}", end="\t")
#   print()


# %% [57]
# for i, (a, b) in enumerate(zip(seq1, seq2)):
#   print("%d %a %s" %(i,a,b))


# %% [58]
# 3명분의 이름, 국어, 영어, 수학 점수를 입력받아서 2차원 list에 입력하고
# 합계와 평균을 구하고 학점을 구해서 출력하시오
# 단일 for 문에서 실행

# 2차원 리스트 total
# 합계 total , 평균 avg, 학점 A ~ F (90 ~)
# [num ,name, kor , ens, mat, result, rank]
# list[0] ~ list[7]

total = []

for i in range(3):
    name = input('이름을 입력하세요 : ')
    score_kor = int(input('국어성적을 입력하세요 : '))
    score_ens = int(input('영어성적을 입력하세요 : '))
    score_mat = int(input('수학성적을 입력하세요 : '))

    score_total = score_kor + score_ens + score_mat
    score_avg = score_total / 3

    if score_avg >= 90:
        result = 'A'
    elif score_avg >= 80:
        result = 'B'
    elif score_avg >= 70:
        result = 'C'
    elif score_avg >= 60:
        result = 'D'
    else:
        result = 'F'

    total.append([name, score_kor, score_ens, score_mat, score_total, round(score_avg, 2), result])

total.sort(key=lambda row: row[5], reverse=True)

# 정렬 후 등수 추가
for rank in range(len(total)):
    total[rank].append(rank + 1)

print("번호\t이름\t국어\t수학\t영어\t총점\t평균\t학점\t등수")
for x, y in enumerate(total):
    num = x + 1  # 번호 추가
    print(f"{num}\t{y[0]}\t{y[1]}\t{y[2]}\t{y[3]}\t{y[4]}\t{y[5]}\t{y[6]}\t{y[7]}")
