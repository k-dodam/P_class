'''
세트
1. 순서 x / 중복 x

변수명 = {요소 1, 요소 2, 요소 3}
set(세트로 바꾸고 싶은 다른 자료 구조)
'''

my_str = "apple"
my_list = [1,2,3]
my_tuple = (1,2,3)
print("각각의 자료 구조들")
print("str : ", my_str)
print("list : ", my_list)
print("tuple : ", my_tuple)
print()

set_str = set(my_str)
set_list = set(my_list)
set_tuple = set(my_tuple)
print("set로 바꾼 각각의 자료 구조들")
print("str : ", set_str)
print("list : ", set_list)
print("tuple : ", set_tuple)
print()

str_banana = "banana"
set_banana = set(str_banana)
print(str_banana[0])
# print(set_banana[0]) >>> X 세트의 특성 탓에 인덱스 등 사용 불가

print()

list_banana = list(set_banana)
tuple_banana = tuple(set_banana)
print(list_banana)
print(tuple_banana)
# 세트 속 요소에 접근 => 리스트 or 튜플로 변환 후 접근