def three_way_partition(arr, a, b):
    n = len(arr)
    low = 0
    high = n - 1
    
    for i in range(n):
        if arr[i] < a:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
    
    for i in range(low, n):
        if arr[i] > b:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1

    return arr

arr = [1, 4, 3, 6, 2, 1]
a = 1
b = 3

print(three_way_partition(arr, a, b))
