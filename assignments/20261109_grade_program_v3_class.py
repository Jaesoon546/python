"""
과제: 20261109_박재순_성적프로그램_V3_Class.ipynb
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# # 과제
#
# + 성적 프로그램을 클래스로 작성하시오
# + 데이터는 클래스 1인분으로 작성 (이름, 국어, 영어, 수학)
# + 함수 : 입력, 처리(합계, 평균), 출력


# %% [1]
class Grade:
    def __init__(self, name="", kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def is_scan(self):
        self.name = input('이름을 입력하세요 : ')
        self.kor = int(input('국어성적을 입력하세요 : '))
        self.eng = int(input('영어성적을 입력하세요 : '))
        self.mat = int(input('수학성적을 입력하세요 : '))

    def is_total(self):
        return self.kor + self.eng + self.mat

    def is_avg(self):
        return self.is_total() / 3


students = []

while True:
    print("\n성적 관리 프로그램 메뉴")
    print("1. 입력 2. 출력 3. 종료")
    ch = input("원하는 메뉴 번호를 입력하세요: ")

    if ch == '1':
        student = Grade()
        student.is_scan()
        students.append(student)
        print(f"'{student.name}' 학생의 성적이 입력되었습니다.")

    elif ch == '2':
        if not students:
            print("입력된 성적 정보가 없습니다.")
            continue
        print("번호\t이름\t국어\t영어\t수학\t총점\t평균")
        for i, x in enumerate(students):
            print(f"{i+1}\t{x.name}\t{x.kor}\t{x.eng}\t{x.mat}\t{x.is_total()}\t{x.is_avg():.2f}")

    elif ch == '3':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~3 사이의 번호를 입력해주세요.")
