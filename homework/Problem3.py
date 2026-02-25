arr = [1, 4, 3, 5, 8, 6]
res = []
res.append(min(arr))
res.append(max(arr))
print(res)

def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]

print(kthSmallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4))
