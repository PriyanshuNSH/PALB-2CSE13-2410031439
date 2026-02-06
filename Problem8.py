nums = [1, 3, 5, 6]
target = 5

index = len(nums)
for i in range(len(nums)):
    if nums[i] >= target:
        index = i
        break

print("Index =", index)