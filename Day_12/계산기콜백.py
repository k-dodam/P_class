'''
숫자 2개와 연산자(함수)를 받는 함수 생성 -> 연산자(매개 변수 1, 매개 변수 2)

1. 더하기
2. 빼기
3. 곱하기
4. 나누기
'''

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 + num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "나누는 수(분모)가 0일 수는 없습니다."
    return num1 / num2

def arithmetic(operator,num1,num2):
    return operator(num1,num2)

print(arithmetic(divide,1312345,4128356832))