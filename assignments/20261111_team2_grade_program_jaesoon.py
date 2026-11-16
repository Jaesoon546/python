"""
팀과제: 20261111__박재순_2회차2조_성적프로그램.ipynb
(Google Colab 노트북에서 변환 — 실행 결과는 제외)
"""


# # 팀과제
# Class는 3개로 작성
#  - Student : 1 인분의 데이터를 처리 ( CRUD, 합계, 평균, 학점 )
#  - Management : 여러명의 학생을 관리 ( CRUD, 등수처리 )
#  - Menu : 입력, 출력, 성적계산, 학생 검색, 수정, 삭제, 과목별 합계와 평균,프로그램 종료


# %% [1]
class Student:

  def __init__(self, name='', kor=0, eng=0, mat=0):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.mat = mat
    self.rank = 1

  def total(self):
    return self.kor + self.eng + self.mat

  def avg(self):
    return self.total() / 3

  def grade(self):
    avg = self.avg()
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'


# %% [2]
class Management:

  def __init__(self):
    self.studentlist = []

  def add_student(self, name, kor, eng, mat):
    student = Student(name, kor, eng, mat)
    self.studentlist.append(student)
    print(f"'{name}' 학생이 추가되었습니다.")

  def calc_ranks(self):
    for student in self.studentlist:
      rank = 1
      for j in self.studentlist:
        if student.avg() < j.avg():
          rank += 1
      student.rank = rank

  def view_all(self):
    if not self.studentlist:
        print("등록된 학생이 없습니다.")
        return

    print("\n이름\t국어\t영어\t수학\t총점\t평균\t학점\t등수")
    self.calc_ranks()
    for student in self.studentlist:
      print(
            f"{student.name}\t"
            f"{student.kor}\t"
            f"{student.eng}\t"
            f"{student.mat}\t"
            f"{student.total()}\t"
            f"{student.avg():.2f}\t"
            f"{student.grade()}\t"
            f"{student.rank}"
          )


# %% [3]
class Menu:

  def __init__(self, manager):
    self.manager = manager

  def input_data(name=None):
    if name is None:
      name = input('이름을 입력하세요 : ')
    kor = int(input('국어성적을 입력하세요 : '))
    eng = int(input('영어성적을 입력하세요 : '))
    mat = int(input('수학성적을 입력하세요 : '))
    return name, kor, eng, mat

  def print_menu():
    print("\n--- 학생 성적 관리 프로그램 ---")
    print("1. 학생 추가")
    print("2. 전체 학생 보기")
    print("3. 학생 검색")
    print("4. 학생 성적 수정")
    print("5. 학생 삭제")
    print("6. 과목 합계")
    print("7. 과목 평균")
    print("8. 프로그램 종료")
    return input("원하는 메뉴 번호를 선택하세요: ")

  def search_student(self, name):
    studentlist = self.manager.studentlist
    for student in studentlist:
        if student.name == name:
            return student
    return None

  def modify_student(self, name, kor, eng, mat):
    student = self.search_student(name)
    if student:
      student.kor = kor
      student.eng = eng
      student.mat = mat
      print(f"'{name}' 학생의 성적이 수정되었습니다.")
    else:
      print("학생 이름이 검색되지 않습니다.")

  def pop_student(self, name):
    student = self.search_student(name)
    if student:
      self.manager.studentlist.remove(student)
      print(f"'{name}' 학생의 데이터가 삭제되었습니다.")
    else:
      print(f"'{name}' 학생을 찾을 수 없습니다.")

  def subject_tot(self):
    studentlist = self.manager.studentlist
    if not studentlist:
        print("등록된 학생이 없습니다.")
        return

    tot_kor = sum(student.kor for student in studentlist)
    tot_eng = sum(student.eng for student in studentlist)
    tot_mat = sum(student.mat for student in studentlist)

    print("\n=== 과목별 총점 ===")
    print(f"국어 총점: {tot_kor}점")
    print(f"영어 총점: {tot_eng}점")
    print(f"수학 총점: {tot_mat}점")

  def subject_avg(self):
    studentlist = self.manager.studentlist
    if not studentlist:
        print("등록된 학생이 없습니다.")
        return

    count = len(studentlist)
    tot_kor = sum(student.kor for student in studentlist)
    tot_eng = sum(student.eng for student in studentlist)
    tot_mat = sum(student.mat for student in studentlist)

    print("\n=== 과목별 평균 ===")
    print(f"국어 평균: {tot_kor / count:.2f}점")
    print(f"영어 평균: {tot_eng / count:.2f}점")
    print(f"수학 평균: {tot_mat / count:.2f}점")


# %% [4]
manager = Management()
menu = Menu(manager)

while True:
  choice = Menu.print_menu()

  if choice == '1':
    name, kor, eng, mat = Menu.input_data()
    manager.add_student(name, kor, eng, mat)

  elif choice == '2':
    manager.view_all()

  elif choice == '3':
    name = input("검색할 학생의 이름을 입력하세요 : ")
    student = menu.search_student(name)
    if student:
      print(f"\n[검색 결과] 이름: {student.name}, 총점: {student.total()}, 평균: {student.avg():.2f}, 학점: {student.grade()}")
    else:
      print("해당 학생을 찾을 수 없습니다.")

  elif choice == '4':
    name = input("수정할 학생의 이름을 입력하세요 : ")
    student = menu.search_student(name)
    if student:
      print(f"'{name}' 학생의 새로운 성적을 입력합니다.")
      name, kor, eng, mat = Menu.input_data()
      menu.modify_student(name, kor, eng, mat)
    else:
      print("학생 이름이 검색되지 않습니다.")

  elif choice == '5':
    name = input('삭제할 이름을 입력하세요 : ')
    menu.pop_student(name)

  elif choice == '6':
    menu.subject_tot()

  elif choice == '7':
    menu.subject_avg()

  elif choice == '8':
    print("프로그램을 종료합니다.")
    break

  else:
    print("잘못된 입력입니다. 1~8 사이의 숫자를 입력해주세요.")


# %% [5]
class Student:
    def __init__(self, name='', kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.rank = 1

    def total(self):
        return self.kor + self.eng + self.mat

    def avg(self):
        return self.total() / 3

    def grade(self):
        avg = self.avg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'


class Management:
    def __init__(self):
        self.studentlist = []

    def add_student(self, name, kor, eng, mat):
        student = Student(name, kor, eng, mat)
        self.studentlist.append(student)
        print(f"'{name}' 학생이 추가되었습니다.")

    def calc_ranks(self):
        for student in self.studentlist:
            rank = 1
            for j in self.studentlist:
                if student.avg() < j.avg():
                    rank += 1
            student.rank = rank

    def view_all(self):
        if not self.studentlist:
            print("등록된 학생이 없습니다.")
            return

        print("\n이름\t국어\t영어\t수학\t총점\t평균\t학점\t등수")
        self.calc_ranks()
        sorted_list = sorted(self.studentlist, key=lambda s: s.avg(), reverse=True)
        for student in sorted_list:
            print(
                f"{student.name}\t"
                f"{student.kor}\t"
                f"{student.eng}\t"
                f"{student.mat}\t"
                f"{student.total()}\t"
                f"{student.avg():.2f}\t"
                f"{student.grade()}\t"
                f"{student.rank}"
            )

    def search_student(self, name):
        for student in self.studentlist:
            if student.name == name:
                return student
        return None

    def modify_student(self, name, kor, eng, mat):
        student = self.search_student(name)
        if student:
            student.kor = kor
            student.eng = eng
            student.mat = mat
            print(f"'{name}' 학생의 성적이 수정되었습니다.")
        else:
            print("학생 이름이 검색되지 않습니다.")

    def pop_student(self, name):
        student = self.search_student(name)
        if student:
            self.studentlist.remove(student)
            print(f"'{name}' 학생의 데이터가 삭제되었습니다.")
        else:
            print(f"'{name}' 학생을 찾을 수 없습니다.")

    def subject_tot(self):
        if not self.studentlist:
            print("등록된 학생이 없습니다.")
            return

        tot_kor = sum(s.kor for s in self.studentlist)
        tot_eng = sum(s.eng for s in self.studentlist)
        tot_mat = sum(s.mat for s in self.studentlist)
        print("\n=== 과목별 총점 ===")
        print(f"국어 총점: {tot_kor}점")
        print(f"영어 총점: {tot_eng}점")
        print(f"수학 총점: {tot_mat}점")

    def subject_avg(self):
        if not self.studentlist:
            print("등록된 학생이 없습니다.")
            return

        count = len(self.studentlist)
        tot_kor = sum(s.kor for s in self.studentlist)
        tot_eng = sum(s.eng for s in self.studentlist)
        tot_mat = sum(s.mat for s in self.studentlist)
        print("\n=== 과목별 평균 ===")
        print(f"국어 평균: {tot_kor / count:.2f}점")
        print(f"영어 평균: {tot_eng / count:.2f}점")
        print(f"수학 평균: {tot_mat / count:.2f}점")


class Menu:
    def __init__(self, manager):
        self.manager = manager

    @staticmethod
    def input_score(subject):
        while True:
            try:
                score = int(input(f"{subject} 성적을 입력하세요 (0~100) : "))
                if 0 <= score <= 100:
                    return score
                print("0에서 100 사이의 점수를 입력해주세요.")
            except ValueError:
                print("유효한 숫자를 입력해주세요.")

    @classmethod
    def input_data(cls, name=None):
        if name is None:
            name = input('이름을 입력하세요 : ')
        kor = cls.input_score('국어')
        eng = cls.input_score('영어')
        mat = cls.input_score('수학')
        return name, kor, eng, mat

    @staticmethod
    def print_menu():
        print("\n--- 학생 성적 관리 프로그램 ---")
        print("1. 학생 추가")
        print("2. 전체 학생 보기")
        print("3. 학생 검색")
        print("4. 학생 성적 수정")
        print("5. 학생 삭제")
        print("6. 과목 합계")
        print("7. 과목 평균")
        print("8. 프로그램 종료")
        return input("원하는 메뉴 번호를 선택하세요: ")

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == '1':
                name, kor, eng, mat = self.input_data()
                self.manager.add_student(name, kor, eng, mat)

            elif choice == '2':
                self.manager.view_all()

            elif choice == '3':
                name = input("검색할 학생의 이름을 입력하세요 : ")
                student = self.manager.search_student(name)
                if student:
                    print(f"\n[검색 결과] 이름: {student.name}, 총점: {student.total()}, 평균: {student.avg():.2f}, 학점: {student.grade()}")
                else:
                    print("해당 학생을 찾을 수 없습니다.")

            elif choice == '4':
                name = input("수정할 학생의 이름을 입력하세요 : ")
                student = self.manager.search_student(name)
                if student:
                    print(f"'{name}' 학생의 새로운 성적을 입력합니다.")
                    _, kor, eng, mat = self.input_data(name)
                    self.manager.modify_student(name, kor, eng, mat)
                else:
                    print("학생 이름이 검색되지 않습니다.")

            elif choice == '5':
                name = input('삭제할 이름을 입력하세요 : ')
                self.manager.pop_student(name)

            elif choice == '6':
                self.manager.subject_tot()

            elif choice == '7':
                self.manager.subject_avg()

            elif choice == '8':
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 1~8 사이의 숫자를 입력해주세요.")


if __name__ == "__main__":
    manager = Management()
    menu = Menu(manager)
    menu.run()
