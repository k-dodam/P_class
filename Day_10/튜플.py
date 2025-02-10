'''
튜플 > 변수명 : (요소 1, 요소 2, 요소 3) // # 튜플의 특성 : 불변
리스트 > 변수명 : [요소 1, 요소 2, 요소 3]
'''
from Day_5.무한루프 import count

alphabet = ('a', 'b', 'c') # 문자
color = ("red", "yellow", "orange") # 문자열
bool_type = (True, False, True) # 논리값
mix_tuple = ("red", 'g', 3, True) # 혼합

name = ("Kwon", "Min", "Ji")
first_name = name[0]
second_name = name[1]
third_name = name[2]
print(first_name)
print(second_name)
print(third_name)
print()

first_name2 = name[-3]
print(first_name2)
print()

num_list = [1,2,3]
num_tuple = (1,2,3)
print(num_list)
print(num_tuple)
print()

num_list[0] = 100
print(num_list)
print()

# num_tuple[0] = [100]
# print(num_tuple)

num_list.append(4)
print(num_list)
print()

# num_tuple.append(4)
# print(num_tuple)

'''
1. 데이터 손상 방지
2. 코드 안전성 향상
'''

# 튜플 중첩
multi_tuple = (1,(2,3), [4,5])
print(multi_tuple[2])
print(multi_tuple[1][1])
print(multi_tuple[2][1])
print(multi_tuple[0])
print()

# 튜플 속 리스트 수정 가능
multi_tuple[2][0]= 3
print(multi_tuple[2])
multi_tuple[2].append(7)
print(multi_tuple)

# 튜플 슬라이싱
slice_tuple = (3,10,"파이썬", True, "cat", 23)
print(slice_tuple[1:4:])
print(slice_tuple[:5:])
print(slice_tuple[:8:])
print(slice_tuple[300:200:100])
print()

### 튜플 메서드
'''
1. count() : 튜플 속 특정 값 등장 수 셈
2. index() : 튜플 속 특정 값 처음 등장 위치(인덱스) 반환
'''

my_tuple = (1,2,3,2,2,4)

print(my_tuple.count(2))
count_of_2 = my_tuple.count(2)
print(count_of_2)
print()

my_tuple2 = (10,20,30,40,20,50)

print(my_tuple2.index(20))
index_of_20 = my_tuple2.index(20)
print(index_of_20)
print()

'''
자주 사용하는 것
1. len() : 길이
2. in : 요소 포함 여부 확인
3. + : 튜플 병합 연산자
4. * : 튜플 반복 연산자
'''

my_tuple3 = (1,2,3,4)
t1 = (1,2)
t2 = (3,4)
t3 = t1 * 3
print(f"len(my_tuple3) : {len(my_tuple3)}")
print(f"2 in my_tuple3 ? : {2 in my_tuple3}")
print(f"5 in my_tuple3 ? : {5 in my_tuple3}")
print(t1 + t2)
print(t3)
print()

a = 10
b = 20
print(f"교환 전 -> a : {a}, b : {b}")
(a,b) = b,a
print(f"교환 후 -> a : {a}, b : {b}")
# 튜플 < 데이터 변경 및 추가 불가능 but 데이터 교환 등 변수 변경에 활용 가능