'''
사용자에게 키와 나이 입력받기
키가 120이상이고 나이가 10살 이상이어야만 놀이기구 탑승 가능
출력 : 놀이기구를 탈 수 있나요? True of False
'''

height = int(input("키를 입력하세요 :"))
age = int(input("나이를 입력하세요 :"))
check = 120 <= height and 10 <= age
print("놀이기구를 탈 수 있나요?", check)
print(f"놀이기구를 탈 수 있나요? {check}")