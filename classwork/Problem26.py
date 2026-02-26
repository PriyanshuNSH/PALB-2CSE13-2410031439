def find_median(arr):
    arr.sort()
    n = len(arr)
    
    # Odd length
    if n % 2 != 0:
        return arr[n // 2]
    
    # Even length
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Examples
print(find_median([90, 100, 78, 89, 67]))  # Output: 89
print(find_median([56, 67, 30, 79]))       # Output: 61.5
print(find_median([1, 2]))                 # Output: 1.5
