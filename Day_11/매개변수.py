'''
매개변수
def 함수이름(매개변수 1, 매개변수 2 ...):
    기능 코드 작성
'''

def candy_fluff(count):
    print("오늘은 솜사탕을 " + str(count) + "개 만들어야 합니다.")

candy_fluff(15)
candy_fluff(3)
# 매개 변수가 있는 함수를 선언 시 호출할 때 매개 변수값 지정 필수

print()

'''
블랙핑크 자기 소개 함수
'''

def blackpink_hello(black_pink):
    print("안녕하세요 블랙핑크 " + black_pink + "입니다.")

blackpink_hello("제니")
blackpink_hello("로제")
blackpink_hello("리사")
blackpink_hello("지수")

print()

def plus(a,b):
    print(a + b)

plus(10, 20)
plus(5, 20)