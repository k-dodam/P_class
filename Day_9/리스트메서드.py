'''
리스트 추가
1. append() : 리스트 마지막 새 요소 추가
2. insert() : 리스트 중간 새 요소 추가

리스트 삭제
1. remove() : 특정 값을 가진 요소를 삭제
2. pop() : 특정 위치의 요소 삭제

리스트 정렬
1. sort() : 오름차순 정렬 (리스트 원본 변경됨)
2. sort(reverse = True) : 내림차순 정렬 (리스트 원본 변경됨)
3. sorted() : 정렬된 리스트를 새 리스트로 반환 (리스트 원본 유지됨)

리스트 반전
1. reverse() : 역순으로 변경 (리스트 원본 변경됨)

리스트 문자열
join() : 리스트 요소에 연결 문자를 추가해 하나의 문자열로 결합
'''

# append()
append_nums = [1,2,3]
print(f"append(4) 추가 전 : {append_nums}")
append_nums.append(4)
print(f"append(4) 추가 후 : {append_nums}")
print()

# insert()
alphabet = ['a', 'b', 'c']
print(f"insert(1, 'm') 추가 전 : {alphabet}")
alphabet.insert(1, 'm')
print(f"insert(1, 'm') 추가 후 : {alphabet}")
print()

# remove() - remove(요소값)
remove_nums = [1,2,3,4]
print(f"remove(1) 추가 전 : {remove_nums}")
remove_nums.remove(1)
print(f"remove(1) 추가 후 : {remove_nums}")
print()

# pop - pop(인덱스 번호)
colors = ["red", "black", "yellow", "black"]
print(f"pop(3) 추가 전 : {colors}")
colors.pop(3)
print(f"pop(3) 추가 전 : {colors}")
print()

# reverse()
reverse_num = [2,6,1,176,5,13,744]
print(f"reverse() 추가 전 : {reverse_num}")
reverse_num.reverse()
print(f"reverse() 추가 후 : {reverse_num}")
print()

# join()
join_text = ["I", "love", "dog"]
print(f"\"-\".join() 추가 전 : {join_text}")
join_result = "-".join(join_text)
print(f"\"-\".join() 추가 후 : {join_result}")
print()