def largest(arr):
    max_ele = arr[0]
    for i in arr:
        if i > max_ele:
            max_ele = i
    return max_ele

arr = [1, 8, 7, 56, 90]
print(largest(arr))