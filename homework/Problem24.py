def min_swaps(arr, k):
    n = len(arr)
    
    # Step 1: Count elements <= k
    count = 0
    for num in arr:
        if num <= k:
            count += 1
    
    # If no or all elements <= k
    if count == 0 or count == n:
        return 0
    
    # Step 2: Count bad elements in first window
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    ans = bad
    
    # Step 3: Slide the window
    for i in range(count, n):
        
        # Remove left element from window
        if arr[i - count] > k:
            bad -= 1
        
        # Add new element to window
        if arr[i] > k:
            bad += 1
        
        ans = min(ans, bad)
    
    return ans


# Example Tests
print(min_swaps([2, 1, 5, 6, 3], 3))          # Output: 1
print(min_swaps([2, 7, 9, 5, 8, 7, 4], 6))    # Output: 2
print(min_swaps([2, 4, 5, 3, 6, 1, 8], 6))    # Output: 0
