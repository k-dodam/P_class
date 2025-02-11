# 세트의 교집합
'''
1. &연산자 사용 : 두 세트를 & 연산자로 연결 후 새 세트를 만들며, 이때 중복되는 요소는 제거
2. intersection() : 두 세트를 인자로 전달 후 교집합 반환
'''

print("합집합")

set_a = {1,2,3,4}
set_b = {3,4,5,6}

intersection_a_b = set_a.intersection(set_b)
print(intersection_a_b)

a_and_b = set_a & set_b
print(a_and_b)
print()

'''
과일바구니 : strawberry orange cherry
내가 좋아하는 과일 : strawberry grape orange
'''
fruits = {"strawberry", "orange", "cherry"}
my_fruits = {"grape", "strawberry", "orange"}
print(fruits & my_fruits)

fruits_and_my_fruits = fruits & my_fruits
intersection_fruits_my_fruits = fruits.intersection(my_fruits)
print()

# 세트의 합집합
'''
1. |
2. union()
'''

print("교집합")

set_c = {1,2,3}
set_d = {3,4,5}

pipe_set =set_c | set_d
print(pipe_set)

union_set = set_c.union(set_d)
print(union_set)

print()

'''
수학반 : 엘사, 모아나, 라푼젤
과학반 : 엘사, 안나, 모아나
학원생 전원의 명단 뽑기
'''

math_class = {"엘사", "모아나", "라푼젤"}
science_class = {"엘사", "안나", "모아나"}
print(math_class | science_class)

pipe_class = math_class | science_class
union_class = math_class.union(science_class)
print()

# 세트의 차집합
'''
1. -
2. difference()
'''

print("차집합")

set_e = {1,2,3,4}
set_f = {3,4,5,6}

minus_set = set_e - set_f
print(minus_set)

diff_set = set_e.difference(set_f)
print(diff_set)

'''
음악반 : 알라딘 오로라 자스민
역사반 : 오로라 자스민
음악만 공부하는 학생 출력
'''

music_class = {"알라딘", "오로라", "자스민"}
history_class = {"오로라", "자스민"}
print(music_class - history_class)

only_music_minus = music_class - history_class
only_music_diff = music_class.difference(history_class)