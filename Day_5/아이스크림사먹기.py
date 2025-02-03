'''
우리가 가진 돈 : 5000원
아이스크림 : 1000원
아이스크림을 2번 사먹을 거임
아이스크림 1번 사먹었다! 남은 돈 4000원
아이스크림을 2번 사먹었다! 남은 돈 3000원
'''

money = 5000
icecream = 1000
times = 1
while times <= 2 :
    print(f"아이스크림을 {times}번 사먹었다! {money - icecream * times}원 남았다!")
    times += 1

