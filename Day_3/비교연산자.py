'''
1. a > b
2. a < b
3. a >= b
4. a <= b
5. a == b
6. a != b
맞으면 true, 틀리면 false
'''

a = 10
b = 7

ab_result = a > b
print(ab_result)

ab_result2 = a < b
print(ab_result2)

ab_result3 = a >= b
print(ab_result3)

ab_result4 = a <= b
print(ab_result4)

ab_result5 = a == b
print(ab_result5)

ab_result6 = a != b
print(ab_result6)

# 문자열 비교

string1 = "Python"
string2 = "P" + "y" + "t" + "h" + "o" + "n"

string_result = string1 == string2
print(string_result)

# 문자열, 숫자형 비교
one = 1
first = "1"

type_result = one == first
print(type_result)

# 다중 연산자
x = 1
y = 2
z = 3

xyz_result = x < y < z
print(xyz_result)