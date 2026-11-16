# Python — 대전바이오융합 직업훈련 학습 기록

Google Colab에서 작성한 수업 실습 노트북과 과제를 `.py` 코드로 정리한 섹션입니다.

- 각 파일 맨 위 docstring에 원본 노트북 이름이 적혀 있습니다.
- 노트북의 설명(마크다운) 셀은 `#` 주석으로, 코드 셀은 `# %% [번호]` 구분선으로 표시했습니다.
  (VS Code·PyCharm에서는 `# %%` 단위로 셀처럼 실행할 수 있습니다.)
- 실행 결과(출력)는 제외했고, Colab 전용 셸 명령(`!pip`, `!cat` 등)은 주석 처리했습니다.
- 노트에 붙여 넣은 이미지는 `[이미지 — 원본 Colab 노트북 참고]`로 대체했습니다.

## 수업 (`lectures/`)

| 파일 | 내용 |
|---|---|
| [01_variables.py](lectures/01_variables.py) | 변수, 데이터 타입, 형변환, 문자열, 연산자 (11/03) |
| [02_data_structure.py](lectures/02_data_structure.py) | 자료구조 — 리스트 CRUD, 큐, 딕셔너리, 정렬 (11/04) |
| [03_control_statement.py](lectures/03_control_statement.py) | 제어문 — if, for, range, 이중 for, while (11/05) |
| [04_function_method.py](lectures/04_function_method.py) | 함수 — 기본/디폴트 매개변수, 고차 함수, 재귀, 이진 검색 (11/06) |
| [05_class_object.py](lectures/05_class_object.py) | 객체 지향 — 클래스 예제, deepcopy, static 변수, classmethod (11/09) |
| [06_inheritance.py](lectures/06_inheritance.py) | 상속, 다중상속, 시계·달력 예제 (11/10) |
| [07_class_relation.py](lectures/07_class_relation.py) | 클래스 관계 — 연관·집합·포함, 디자인 패턴 (11/11) |

## 과제 (`assignments/`)

| 파일 | 내용 |
|---|---|
| [20261105_grade_program.py](assignments/20261105_grade_program.py) | 성적 프로그램 v1 — 2차원 리스트 |
| [20261106_rock_paper_scissors.py](assignments/20261106_rock_paper_scissors.py) | 가위바위보 게임 함수화 |
| [20261106_grade_program_v2.py](assignments/20261106_grade_program_v2.py) | 성적 프로그램 v2 — 함수화 (입력·출력·검색·수정·삭제) |
| [20261109_grade_program_v3_class.py](assignments/20261109_grade_program_v3_class.py) | 성적 프로그램 v3 — 클래스 |
| [20261111_team2_grade_program.py](assignments/20261111_team2_grade_program.py) | 팀과제(2회차 2조) — Student / Management / Menu 클래스 |
| [20261111_team2_grade_program_jaesoon.py](assignments/20261111_team2_grade_program_jaesoon.py) | 팀과제 개인 작업본 |

## 실행

```bash
python3 assignments/20261111_team2_grade_program.py
```

대부분의 과제는 `input()`으로 값을 받는 대화형 프로그램입니다.
