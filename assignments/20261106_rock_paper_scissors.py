"""
과제: 20261106_박재순_가위바위보게임.ipynb
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# # 과제
# + 가위, 바위, 보 게임을 함수화 하시요 ( 입력, 처리, 출력 )
# + 20261106_박재순_가위바위보게임


# %% [1]
import random
rsp = ['가위', '바위', '보']
judge = ['이김','짐','비김']
score = [
    2, 1, 0,
    0, 2, 1,
    1, 0, 2
]

def is_scan():
  user = input("입력하시요 : (0:가위, 1:바위, 2:보)")
  user = int(user) % 3
  return user

def rsp_game(user):
  com = random.randint(0,2) % 3
  result_index = user * 3 + com
  f_result = judge[score[result_index]]
  return com, result_index, f_result

def is_print(user, com, result_index, f_result):
    print(f'당신은 {rsp[user]}을 선택 하였고 컴퓨터는 {rsp[com]}을 선택 하였습니다. 당신은 {f_result} 했습니다')


def main():
    while True:
        user = is_scan()
        com, result_index, f_result = rsp_game(user)
        is_print(user, com, result_index, f_result)

        if score[result_index] == 0:
            print('당신이 이겼습니다. 게임을 종료합니다.')
            break

main()
