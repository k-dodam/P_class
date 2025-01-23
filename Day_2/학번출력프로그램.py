# 학번 입력 받기

# 첫번째 숫자 : 학년
# 두번째 숫자 : 반
# 세번째 숫자 : 번호
# 첫번째 숫자 학년 두번째 숫자 반 세번째 숫자 번 출력
'''
student_grade = input("학년을 입력하세요 : ")
student_class = input("반을 입력하세요 : ")
student_number = input("번호를 입력하세요 : ")

print(f"{student_grade}학년 {student_class}반 {student_number}번")
'''

student_id = input("4자리 학번을 입력하세요 : ")
print(f"{student_id[:1]}학년 {student_id[1:2]}반 {student_id[2:4]}번")