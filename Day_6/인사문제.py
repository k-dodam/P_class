'''
정수 입력받아서 입력받은 횟수만큼 n번째 안녕하세요 출려
0보다 작은 수 입력시 "잘못된 입력" 출력
if, for 사용
'''

num = input("정수 입력 : ")

if  num < 0 :
    print("잘못된 입력")
else :
    for nums in range(num) :
