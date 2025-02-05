'''
영화 이름 입력받기
영화 평점 입력받기 (1~5점)
영화 평점이 1~5가 아닐 시 "1부터 5까지의 숫자를 입력하세요"출력
영화 이름의 평점 : ***
continue, break 모두 사용
'''

name = input("영화 이름 입력 : ")
while True :
    score = int(input("영화 평점 입력 : "))

    if score < 1 or score > 5 :
        print("평점은 1에서 5사이로 입력")
        continue

    else :
        print(f"{name}의 평점 : ", end = "")
        for i in range(1, score + 1):
            print("*", end="")
        break