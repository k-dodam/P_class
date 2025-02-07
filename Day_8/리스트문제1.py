'''
여러 숫자가 있는 리스트 내에 5 이상인 숫자만 빈 리스트에 추가 및 오름차순으로 출력
3, 7, 8, 6, 10, 4, 2, 5, 0, 1
'''

'''
list = [3, 7, 8, 6, 10, 4, 2, 5, 0, 1]
empty_list = []

for i in list :
    if i >= 5 :
       empty_list.extend([i])

empty_list.sort()
print(empty_list)
'''

list = [3, 7, 8, 6, 10, 4, 2, 5, 0, 1]
empty_list = []

for i in list :
    if i >= 5 :
        empty_list.append(i)

empty_list.sort()
print(empty_list)