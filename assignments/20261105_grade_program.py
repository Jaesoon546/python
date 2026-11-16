"""
과제: 20261105_박재순_성적프로그램.ipynb
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# %% [1]
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
