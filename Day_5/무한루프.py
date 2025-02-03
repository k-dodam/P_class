'''
count = 0
while count < 3 :
    print(count)
'''

# break : while문을 강제로 종료
# continue : while문 다음에 오는 코드를 무시하고 조건을 검사

count = 0
while count < 10 :
    print(count)
    count += 1

while count == 5 :
    break

print()
print()

#continue
num = 0
while num < 20 :
    num += 1
    if num == 5 :
        continue #실행됐다면 다음에 오는 코드를 무시하고 다음 반복을 실행
    print(num, end = " ")