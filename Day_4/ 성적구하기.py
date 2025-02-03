score = int(input("점수 입력 : "))

if score >= 90:
    print("A 학점, 참 잘했어요")

elif score >= 80:
    print("B 학점")

elif score >= 70:
    print("C 학점")

else :
    print("F학점, 재시험")

month = int(input("좋아하는 달은 몇 월 입니까? : "))
if 3 <= month <= 5 :
    print(f"{month}월은 봅 입니다.")
if 6 <= month <= 8 :
    print(f"{month}월은 여름 입니다.")
if 9 <= month <= 11 :
    print(f"{month}월은 가을 입니다.")
if month == 12 or 1 <= month <= 2 :
    print(f"{month}월은 겨울 입니다.")