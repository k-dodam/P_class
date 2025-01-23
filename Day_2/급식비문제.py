'''
학생 한명당 필요한 급식비 = 8,000원
선생님 = 6,000원

학생 23명과 선생님 2명이 급식을 먹음
급식비 계산
'''

s_price = 8000
t_price = 6000
students = 23
teachers = 2

print(s_price * students + t_price * teachers)

s_total = s_price * students
t_total = t_price * teachers
total = s_total + t_total
print(total)
