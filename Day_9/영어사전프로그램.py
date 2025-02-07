'''
딕셔너리 생성
영어 : 뜻  / 4쌍

사용자에게 영어 입력받기
1. 입력 단어가 딕셔너리에 있는지 확인
2. 있다면 영어 : 뜻 출력
3. 없다면 단어 뜻 입력받기
            입력한 영어 : 뜻 딕셔너리에 추가
            영어 : 뜻 (사전에 추가되었습니다) 출력
'''
dict = {
    "flower" : "꽃",
    "food" : "음식",
    "math" : "수학",
    "english" : "영어"
}

eng = input("영어 입력 : ")
if eng in dict :
    print(dict[eng])
else :
    kor = input("뜻 입력 : ")
    dict[eng] = kor
    print(f"{eng} : {kor} (사전에 추가됨)")