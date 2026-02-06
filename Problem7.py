arr = [2, 3, -8, 7, -1, 2, 3]

max_sum = curr_sum = arr[0]

for i in range(1, len(arr)):
    curr_sum = max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)

print("Maximum Subarray Sum =", max_sum)