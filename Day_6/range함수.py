# 1 ~ 5
# 1 + 2 + 3 + 4 + 5
'''
sum = 0
sum += 1
sum += 2
sum += 3
sum += 4
sum += 5
'''

'''
nums = [1,2,3,4,5]
sum = 0
for nums_for in nums :
    sum += nums_for
print(sum)
'''

'''
for 변수 in range(start,stop,step) :
    실행할 코드
'''

for range_for in range(5) :
    print(range_for)

print()

for range_for2 in range(2,6) :
    print(range_for2)
# 시작 기본 값 : 0
# 시작값 작성시 해당 값 포함
# 종료값은 포함하지 않음

print()

for range_for3 in range(1,10,2) :
    print(range_for3)

print()

for range_for4 in range(10,1,-1) :
    print(range_for4)

print()

# 1 ~ 5 합을 range 함수 이용하여 출력
sum = 0
for range_for5 in range(1,6) :
    sum += range_for5
print(sum)

print()

fruits = ["apple", "banana", "cherry"]
for range_for6 in range(len(fruits)) :
    print(f"인덱스 {range_for6} : {fruits[range_for6]}")