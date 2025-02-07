'''
list[start:stop:step]
start : 슬라이싱 시작 인덱스 (시작점 포함)
stop : 슬라이싱 종료 인덱스 (종료점 미포함)
step : 건너뛰는 간격 (기본값 : 1)
'''

nums = [10,20,30,40,50]

print(nums[0:3])

print(nums[1:4])

print(nums[-2:])

print(nums[:-1])

print(nums[::2])

print(nums[::-1])

nums[:2] = [100, 200]
print(nums)

nums[:2] = []
print(nums)