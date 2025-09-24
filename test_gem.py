import copy


nums = [1, 2, 3, 4, 5]
vals = copy.copy(nums)
del vals[1:2]
print(nums)
print(vals)