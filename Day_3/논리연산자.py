'''
1. and : 둘 다 참이어야 참
2. or : 하나만 참이어도 참
3. not : 참 거짓 반대로 (단항 연산자로 not 값 의 형식으로 작성)
'''

num1 = 10
num2 = 20
num3 = 30

num_result = num1 < num2 and num2 < num3
print(num_result)

num_result2 = num1 > num2 and num2 < num3
print(num_result2)

num_result3 = num1 > num2 or num2 < num3
print(num_result3)

num_result4 = num1 > num2 or num2 > num3
print(num_result4)

false = False
print(false)
print(not false)
print(false)

'''
빈 문자열을 선언 후
해당 문자열로 True를 출력하는 프로그램 만들기
(빈 문자열은 False를 출력함)
'''

a = ""
print(not a)
not_a = not a

'''
15라는 숫자가 10 이상 20 이하 인지 확인
'''

fifteen = 15
check_fifteen = 10 <= fifteen <= 20
print(check_fifteen)