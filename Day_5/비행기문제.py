'''
비행기는 총 3대 운행
프로그램을 실행하면 "1번째 비행기 탑승 준비!" 출력
비행기는 여권을 가진 사람 2명 탑승 시에만 출발
-> n번째 고객님 여권 있나요? (Y/N)
N-> "여권이 없어요! 다음 승객 기다리기... 출력
Y-> "n번째 승객이 탑승했습니다!" 출력 후 반복
Y 2 -> "1번째 비행기 출발!" 출력 후 다음 비행기
'''

airplane = 0

while airplane < 3 :
    passenger = 0
    enter = 0
    airplane += 1
    print(f"{airplane}번째 비행기 탑승 준비!")
    while enter < 2 :
        passenger += 1
        passport = input(f"{passenger}번째 고객님 여권 있나요? (yes/no)")
        if passport == "yes" :
            enter += 1
            print(f"{enter}번째 승객이 탑승했습니다")
        else :
            print("여권이 없어요! 다음 승객 기다리기...")
        if enter == 2 :
            print(f"{airplane}번째 비행기 출발!")