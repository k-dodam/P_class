'''
1
22
333
4444
55555
range 이용
변수 = 5 -> range 범위 지정
'''

num = 5
for nums in range(1,num + 1) :
    for nums2 in range(nums) :
        print(nums, end = "")
    print()
