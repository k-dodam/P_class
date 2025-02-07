fruit_colors = {
    "Red" : "apple",
    "Yellow" : "banana",
    "Purple" : "blueberry"
}

print(fruit_colors.keys)
for i in fruit_colors.keys() :
    print(i)

list = []
for i in fruit_colors.values() :
    list.append(i)
print(list)