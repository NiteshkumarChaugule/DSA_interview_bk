
nums = [3, 0, 1]

print(list(set(range(len(nums)+1))-set(nums))[0])
nums = [0, 1]
print(list(set(range(len(nums)+1))-set(nums))[0])

nums = [0, 1, 2, 4, 5, 6, 7, 9, 8, 10]
print(list(set(range(len(nums)+1))-set(nums))[0])
