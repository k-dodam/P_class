'''
문자열의 특징
1. 순서(인덱스) 존재 -> 0부터 시작
'''

'''
대소문자 변환
1. upper() : 대소문자로 변환
2. lower() : 소문자로 변환
3. capitalize() : 첫 글자만 대문자로 변환

문자열 찾기
1. find() : 특정 글자가 어디에 있는지 찾기
2. count() : 특정 글자가 몇 번 등장하는지 찾기

문자열 변경하기
1. replace() : 특정 글자를 다른 글자로 변경

문자열 나누고 합치기
1. split() : 특정 기준으로 문자열 나누기 (리스트로 변환)
2. join() : 리스트를 문자열로 합치기

공백 제거 함수
1. strip() : 양쪽 공백 제거
2. lstrip() : 왼쪽 공백 제거
3. rstrip() : 오른쪽 공백 제거

문자열의 특정 조건 만족 여부 확인
1. startswith() : 특정 문자로 시작하는지 확인
2. endswith() : 특정 문자로 끝나는지 확인
3. isdigit() : 숫자로만 이루어져 있는지 확인 
4. isalpha() : 알파벳으로만 이루어져 있는지 확인

문자열 길이 구하기
1. len() : 문자열의 글자 개수 구하기
'''

#upper
hello = "hello"
print(hello.upper())

#lower
python = "PYTHON"
print(python.lower())

#capitalize
money = "money"
print(money.capitalize())

#find
find_text = "find text"
print(find_text.find("text"))
print(find_text.find("java"))

#count
banana = "banana"
print(banana.count("a"))

#replace
replace_text = "I like dog"
print(replace_text.replace("like","love"))

#split
split_text = "apple, pizza, pasta"
print(split_text.split(","))

#join
words = ["apple, pizza, pasta"]
print(",".join(words))

#strip


#lstrip


#rstrip


#startswith
swith_text = "start swith"
print(swith_text.startswith("start"))
print(swith_text.startswith("swith"))

#endswith
print(swith_text.endswith("start"))
print(swith_text.endswith("swith"))

#isdigit
isdigit_text = "12345"
isdigit_texts = "12345abc"
print(isdigit_text.isdigit())
print(isdigit_texts.isdigit())

#isalpha
isalpha_text = "python"
isalpha_texts = "python123"
print(isalpha_text.isalpha())
print(isalpha_texts.isalpha())

#len
len_text = "minji"
len_texts = "min ji"
print(len(len_text))
print(len(len_texts))