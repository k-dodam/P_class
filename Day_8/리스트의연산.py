'''
리스트 결합
1. + 연산자
2. extend()
'''

list1 = ['a', 'b', 'c']
list2 = ['d', 'e']

list3 = list1 + list2 # + 연산자 -> 대입할 새로운 리스트 필요 (기존 리스트 변화 X)
print(list3)

print(list1)
list1.extend(list2) # extend() -> 기존 리스트 원본을 변경 및 대입
print(list1)

list4 = list2 * 3
print(list4)

result = len(list4)
print(result)

# in 연산자 - True / False
print('d' in list4)

result2 = list4.count('e')
print(result2)

list5 = [99, 55, 12, 469, 72, 3, 2, 14, 6, 8]
print(max(list5))
print(min(list5))

