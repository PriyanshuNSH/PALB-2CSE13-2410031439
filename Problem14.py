def min_swaps(arr, k):
    n = len(arr)
    
    count = 0
    for num in arr:
        if num <= k:
            count += 1
    
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    min_swaps = bad
    
    i = 0
    j = count
    
    while j < n:
        
        if arr[i] > k:
            bad -= 1
        
        if arr[j] > k:
            bad += 1
        
        min_swaps = min(min_swaps, bad)
        
        i += 1
        j += 1
    
    return min_swaps

print(min_swaps([2, 1, 5, 6, 3], 3))        
print(min_swaps([2, 7, 9, 5, 8, 7, 4], 6))  
print(min_swaps([2, 4, 5, 3, 6, 1, 8], 6))  
