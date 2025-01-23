name1 = "kwon"
name2 = 'min ji'
name3 = '''kwonminji'''
name4 = """kwon min ji"""

null_string = "" # false로 간주

str = "minji's book"
str2 = 'minji says "happy"'
print(str2)

# 문자열 연산
first_name = "kwon"
last_name = " min ji"
full_name = first_name + last_name
print(full_name)

class_name = 'python '
print(class_name)
print(class_name * 5)
# 문자열 연산은 +와 *만 가능

# 문자열 인덱스
a = "apple"
first_char = a[0]
third_char = a[3]
print(first_char)
print(third_char)

# 마이너스 인덱스 : 문자열의 마지막에서부터 인덱스 번호 부여
last_char = a[-1]
char = a[-3]
print(last_char)
print(char)

# 문자열 슬라이싱 : 변수명[start;stop;step]
'''
start(시작 인덱스) : 슬라이싱을 시작할 위치 정하기 (생락시 0)
stop(종료 인덱스) : 슬라이싱을 종료할 인덱스 번호 + 1 (생략시 마지막 인덱스 + 1)
step(증감폭) : 인덱스의 증가 or 감소값 을 지정 (기본 값은 1, 생략시 1씩 증감)
'''
text = "I Love Pasta"
slicing1 = text[2:6] # start 2(L), stop 6 - 1(e)
print(slicing1)
slicing2 = text[7:12]
print(slicing2)

step = text[7:12:2]
print(step)

first_lost = text[:6]
print(first_lost)
last_lost = text[6:]
print(last_lost)

# 문자열 길이 구하기
python_text = "python"
python_length = len(python_text)
print(python_text)
print(python_length)
print(len(python_text))

'''
유용한 함수
1. 문자열을 대문자로 변환 upper()
2. 문자열을 소문자로 변환 lower()
3. 양 끝 공백 제거 strip("여기 적히는 걸 양 끝 제거, 생략시 공백")
'''

pizza = "i love pizza"

upper_pizza = pizza.upper()
print(upper_pizza)

lower_pizza = upper_pizza.lower()
print(lower_pizza)

coffee = "          This is coffee"
strip_coffee = coffee.strip()
print(strip_coffee)

coffee1 = "---------This is coffee"
strip_coffee1 = coffee1.strip("-")
print(strip_coffee1)