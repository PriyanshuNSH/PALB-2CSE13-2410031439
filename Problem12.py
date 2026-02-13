def smallest_subarray(x, arr):
    n = len(arr)
    
    min_length = n + 1
    current_sum = 0
    start = 0
    
    for end in range(n):
        
        current_sum += arr[end]
        
        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1
    
    if min_length == n + 1:
        return 0
    
    return min_length

print(smallest_subarray(51, [1, 4, 45, 6, 0, 19]))  
print(smallest_subarray(100, [1, 10, 5, 2, 7]))     
