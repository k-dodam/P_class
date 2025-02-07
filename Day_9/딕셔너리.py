'''
딕셔너리 : 키와 쌍으로 이뤄진 데이터 구조

key1 : value1,
key2 : value2
'''

me = {
    "name" : "KwonMinJi",
    "age" : 20, # 숫자나 불리언 값은 따옴표 없이 사용 가능
    "phone" : "010-1234-5678",
    "class" : ["C언어", "Python", "Java"] # 리스트 작성 가능
}
print(me)
print(me["phone"])
print(me["class"])
print(me["class"][0])

'''
phone에 대한 딕셔너리 생성
# key : name / price / color / storage
'''

my_phone = {
    "name" : "Iphone",
    "price" : "1,400,000",
    "color" : "white",
    "storage" : "256GB"
}

print(my_phone["color"])

friends = {}
friends["도현"] = 19
friends["길동"] = 27
print(friends)

print(friends["길동"])

friends["도현"] = 29
print(friends)

del friends["길동"]
print(friends)

friends.clear()
print(friends)