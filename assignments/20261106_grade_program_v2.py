"""
과제: 20261106_박재순_성적프로그램_v2.ipynb (함수화)
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# # 과제
# + 성적프로그램을 함수화 하시요 ( 입력, 출력, 검색, 수정, 삭제. 종료) : 무한루프로 관리
# + 20261106_박재순_성적프로그램


# %% [1]
# 2차원 리스트 total
# 합계 total , 평균 avg, 학점 A ~ F (90 ~)
# [num ,name, kor , ens, mat, result, rank]
# list[0] ~ list[7]
# 입력, 출력, 검색, 수정, 삭제, 종료
# is_scan (입력), is_total(총합), is_avg(평균),is_grade(학점)
# is_sorting (정렬), is_append(성적추가), is_rank(등수 추가)
# is_print (출력), is_in(검색), is_change(수정), is_pop(삭제)
# main()
total = []

def is_scan():
    name = input('이름을 입력하세요 : ')
    score_kor = int(input('국어성적을 입력하세요 : '))
    score_ens = int(input('영어성적을 입력하세요 : '))
    score_mat = int(input('수학성적을 입력하세요 : '))
    return name, score_kor, score_ens, score_mat

def is_total(score_kor, score_ens, score_mat):
    return score_kor + score_ens + score_mat

def is_avg(score_total):
    return score_total / 3

def is_grade(score_avg):
    if score_avg >= 90:
        return 'A'
    elif score_avg >= 80:
        return 'B'
    elif score_avg >= 70:
        return 'C'
    elif score_avg >= 60:
        return 'D'
    else:
        return 'F'

def is_append(total, name, score_kor, score_ens, score_mat, score_total, score_avg, result):
    total.append([name, score_kor, score_ens, score_mat, score_total, round(score_avg, 2), result])

def is_sorting(total):
    total.sort(key=lambda row: row[5], reverse=True)

def is_rank(total):
    for rank, row in enumerate(total):
        if len(row) == 8:
            row[7] = rank + 1  # 이미 등수가 있으면 수정
        else:
            row.append(rank + 1) # 없으면 추가

def is_print(total):
    print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t학점\t등수")
    for x, y in enumerate(total):
        num = x + 1
        print(f"{num}\t{y[0]}\t{y[1]}\t{y[2]}\t{y[3]}\t{y[4]}\t{y[5]}\t{y[6]}\t{y[7]}")
    print()


def is_in(total):
    search = input('검색할 이름을 입력하세요 : ')
    for x, y in enumerate(total):
        if y[0] == search:
          print("\n[검색 결과]")
          print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t학점\t등수")
          print(f"{x+1}\t{y[0]}\t{y[1]}\t{y[2]}\t{y[3]}\t{y[4]}\t{y[5]}\t{y[6]}\t{y[7]}")
          return # 밑에 print가 같이뜸
    print(f"'{search}' 학생을 찾을 수 없습니다.")

def is_change(total):
    change = input('성적을 수정할 이름을 입력하세요 : ')
    for y in total:
        if y[0] == change:
            print(f"'{change}' 학생을 찾았습니다. 새로운 성적을 입력하세요.")
            y[1] = int(input('새로운 국어성적 : '))
            y[2] = int(input('새로운 영어성적 : '))
            y[3] = int(input('새로운 수학성적 : '))
            y[4] = is_total(y[1], y[2], y[3])
            y[5] = round(is_avg(y[4]), 2)
            y[6] = is_grade(y[5])
            print(f"'{change}' 학생의 성적이 수정되었습니다.")
            return # 밑에 print가 같이뜸
    print(f"'{change}' 학생을 찾을 수 없습니다.")

def is_pop(total):
    pop = input('삭제할 이름을 입력하세요 : ')
    for x, y in enumerate(total):
        if y[0] == pop:
            del_s = total.pop(x)
            print(f"'{del_s[0]}' 학생의 데이터가 삭제되었습니다.")

            return # 밑에 print가 같이뜸
    print(f"'{pop}' 학생을 찾을 수 없습니다.")

def main():
    while True:
        print("\n성적 관리 프로그램 메뉴")
        print("1. 입력 2. 출력 3. 검색 4. 수정 5. 삭제 6. 종료")
        ch = input("원하는 메뉴 번호를 입력하세요: ")

        if ch == '1':
            name, score_kor, score_ens, score_mat = is_scan()
            score_total = is_total(score_kor, score_ens, score_mat)
            score_avg = is_avg(score_total)
            result = is_grade(score_avg)

            is_append(total, name, score_kor, score_ens, score_mat, score_total, score_avg, result)
            is_sorting(total)
            is_rank(total)
            print(f"'{name}' 학생의 성적이 입력되었습니다.")

        elif ch == '2':
            if not total:
                print("입력된 성적 데이터가 없습니다.")
            else:
                is_print(total)

        elif ch == '3':
            is_in(total)

        elif ch == '4':
            is_change(total)
            is_sorting(total)
            is_rank(total)

        elif ch == '5':
            is_pop(total)
            is_sorting(total)
            is_rank(total)

        elif ch == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~6 사이의 번호를 입력해주세요.")

main()
