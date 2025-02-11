'''
함수의 장점
1. 반복 코드 제거 및 재사용 원활
2. 코드 가독성 및 유지 보수 향상
3. 오류 추적 및 디버깅 용이

def 함수이름() :
    코드 1
    코드 2
    코드 3
'''

def hello():
    print("안녕하세요")
    print("저는 민지입니다.")
    print("파이썬 수업중입니다.")

hello()

colors = ["red", "orange", "yellow", "green", "blue"]
index = 0

def change_color():
    global index
    if index >= len(colors):
        index = 0
    print(f"배경색을 {colors[index]}로 변경합니다.")
    index += 1

change_color()
change_color()
change_color()
change_color()
change_color()
change_color()