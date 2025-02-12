'''
정해진 아이디 비밀 번호 설정
함수 생성 > 두 개의 매개 변수 받기 (아이디 비밀 번호)
함수 역할 <<
받은 아이디 == 설정 아이디 && 받은 비밀 번호 == 설정 비밀 번호 >> 로그인 성공
받은 비밀 번호 != 설정 비밀 번호 >> 비밀 번호 불일치
받은 아이디 != 설정 아이디 >> 아이디 불일치
'''

id = "abcd"
password = 1234

def login(id_check, password_check):
    if id_check == id and password_check == password :
        print("로그인 성공")
    elif id_check != id and password_check == password:
        print("아이디 불일치")
    elif id_check == id and password_check != password :
        print("비밀번호 불일치")
    else :
        print("아이디, 비밀번호 모두 불일치")


login(input("아이디 입력 : "), int(input("비밀번호 입력 : ")))