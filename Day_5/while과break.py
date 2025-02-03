'''
시작 숫자 0, 30까지 증가
5의 배수와 짝수는 출력하지 않음
27 전까지만 출력
break continue 둘 다 사용
'''

num = 0
while num < 30 :
    num += 1
    if num % 5 == 0 or num % 2 == 0 :
        continue
    print(num, end = " ")
    if num == 27 :
        break