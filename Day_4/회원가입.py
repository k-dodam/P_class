ID = "kwonminji"
password = 1234

input_ID = input("아이디 입력 : ")
input_password = int(input("비밀번호 입력 : "))

if ID == input_ID and password == input_password:
    print("로그인 성공")
elif ID != input_ID and password == input_password:
    print("아이디가 잘못되었습니다.")
elif ID == input_ID and password != input_password:
    print("비밀번호가 잘못되었습니다.")
else :
    print("회원가입 하러 가기")