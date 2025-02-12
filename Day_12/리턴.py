'''
def 함수 이름( 매개 변수 1, 매개 변수 2, ... )
    코드
    return 함수 밖으로 전달할 값
'''

def plus(a, b):
    return (a + b)

sum = plus(10,20)
print(sum)

def multiply(num):
    result = num * 7
    return result

print(multiply(3))

print()

'''
7의 배수라면 True 반환
아니라면 False 반환
'''
def bool(num):
    if num % 7 == 0:
        return True
    else :
        return False

print(bool(9))