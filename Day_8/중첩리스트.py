list_in_list = [1, [2,3], "hello", [True,False]]

print(list_in_list[1][1])

python_class = [
    ["철수", "영희", "민수"],
    ["지수", "현우", "나영"],
    ["동현", "수진", "소영"]
]

print(python_class[0])
print(python_class[1])
print(python_class[2])

print(python_class[2][1])

python_class[1][0] = "제니"
print(python_class[1][0])