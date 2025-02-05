'''
무한반복하는 반복문을 생성하여 커피 자판기 만들기!
커피 한잔 : 300원
사용자에게 넣을 돈 액수 n 입력받기
300원 이하의 입력 시 "300원 이상 넣어주세요" 출력
입력받은 돈이 300원 이상이라면 "n원으로는 x잔 뽑을 수 있어요." 출력 및 사용자에게 커피를 몇 잔 뽑을 건지 입력받기
x잔 이상의 입력 시 다시 "n원으로는 x잔 뽑을 수 있어요." 출력
0이하의 잔 입력 시 "1잔 이상 입력해주세요" 출력
사용자가 넣은 돈에서 뽑은 커피 잔수와 커피 값을 연산하여 차감(잔돈 계산) 후 커피를 y잔 뽑았어요. 남은 돈 z원" 출력
남은 돈이 300원 이상이라면 자판기 반복
300원 미만이라면 종료
'''

'''
change = 0
while True :
    money = int(input(f"얼마를 넣겠습니까? (현재 잔돈 {change}원)  : "))
    if money < 300 :
        print("300원 이상 넣어주세요")
        continue
    else :
        while True :
            coffee = int(input(f"{money}원으로는 커피를 {int(money / 300)}잔 뽑을 수 있습니다. 몇 잔 뽑겠습니까? : "))
            if coffee <= 0 :
                print("1잔 이상 입력해주세요")
                continue
            elif coffee > money / 300 :
                continue
            else :
                change = money - 300 *  coffee
                print(f"커피를 {coffee}잔 뽑았어요. 남은 돈 : {money - 300 * coffee}")
            if money - 300 * coffee >= 300 :
                continue
            else :
                print("잔돈이 부족하여 종료합니다")
                break
'''

change = 0
while True:
    money = int(input(f"얼마를 넣겠습니까? (현재 잔돈{change}원) : "))
    change += money
    coffee_price = 300
    max_coffee = change // coffee_price  # 최대 커피 잔 수

    if change < 300:
        print("300원 이상 넣어주세요")
        continue

    while True:
        coffee_count = int(input(f"{change}원으로는 {max_coffee}잔 뽑을 수 있습니다. 몇 잔 뽑겠습니까? : "))
        if coffee_count > max_coffee:
            print(f"{change}원으로는 {max_coffee}잔 뽑을 수 있습니다.")
        elif coffee_count <= 0:
            print("1잔 이상 입력해주세요")
        else:
            break

    change -= coffee_price * coffee_count
    print(f"커피{coffee_count}잔을 뽑았습니다. 남은 잔돈 : {change}")

    if change < 300:
        print("잔돈이 부족하여 종료합니다.")
        break
