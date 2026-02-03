def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]

print(kthSmallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10],4))