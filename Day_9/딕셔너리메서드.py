'''
1. keys() : 딕셔너리의 모든 key를 반환
2. values() : 딕셔너리의 모든 값을 반환
3. items() : 딕셔너리의 모든 쌍(key값과 value값)을 반환 *튜플
4. update(other_dictionary) : 딕셔너리에 다른 딕셔너리의 key 추가 혹은 덮어씀
'''

my_dict = {
    "name" : "Kelly",
    "age" : 25,
    "city" : "New York"
}

# keys
print("keys()")
keys = my_dict.keys()
print(keys)
list = list(my_dict.keys())
print(list)
print()

# values()
print("values()")
values = my_dict.values()
print(values)
print()

# items
print("items()")
items = my_dict.items()
print(items)
print()

# update()
print("update()")
my_dict.update({"age" : 26, "hobby" : "free diving"})

# key값 기준 정렬
print(sorted(my_dict))
print(sorted(my_dict,reverse=True))
print(sorted(my_dict.items()))