'''
num = 7
nums = [1,2,3,4,]
'''
number = [0,1,2,3] # 숫자 리스트
alphabet = ['a', 'b', 'c'] # 문자 리스트
bools = [True,False,True] # 논리값 리스트
greetings = ["hello", "오늘은", "파이썬", "8일차"] # 문자열 리스트
mixed = [1, "apple", 3.14, True] # 혼합 리스트

print(mixed)

print(f"mixed[1] : {mixed[1]}")

mixed[1] = "mango"
print(f"change_mixed[1] : {mixed[1]}")

print(mixed[-1])

num_list = [9,8,6,7,4,5,3,1,2]

num_list.sort() # 오름차순
print(num_list)

num_list.sort(reverse=True) # 내림차순
print(num_list)

korean = ['가', '다', '라', '사', '나', '바', '마']
print(sorted(korean)) # 리스트 원본을 건들지 않고 오름차순!
print(korean)

korean.sort() # 리스트 원본을 오름차순으로 변경
print(korean)

korean.sort(reverse=True) # 리스트 원본을 내림차순으로 변경
print(korean)

minji = ["minji", "minji", "kwonminji"]
print(set(minji)) # 중복 없앰
# append() : 리스트 끝에 요소 추가 메서드