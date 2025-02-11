'''
요소 추가
1. add() : 한 번에 요소 하나 추가
2. update() : 여러 요소 한 번에 추가 ( 세트가 아닌 자료형(리스트 튜플 등)도 인자로 받음 )

요소 삭제
1. remove() : 특정 요소 제거 ( 없는 요소일 시 오류 발생 )
2. discard() : 특정 요소 제거 ( 없는 요소 실행 가능 )
3. pop() : 임의 요소 제거 및 반환 ( 순서 없음 )
4. clear() : 모든 요소 제거
'''

# 요소 추가

set_a = {1,2,3}

set_a.add(4)
print(set_a)

set_a.update({5,6})
print(set_a)
print()

# 요소 삭제

set_b = {"a","s","d","y","o","q","n","c","z","m","h"}
set_b.remove("a")
print(set_b)
# set_b.remove("강아지") > "강아지"는 없는 요소 > 오류
set_b.discard("고양이")
print(set_b) # "고양이"는 없는 요소 > 오류 X

set_red = {'r', 'e', 'd'}
print(set_red)
print(set_red.pop())
print(set_red)

set_blue = {'b', 'l', 'u','e'}
set_blue.clear()
print(set_blue)