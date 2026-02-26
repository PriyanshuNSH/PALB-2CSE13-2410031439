def is_palindrome_number(num):
    return str(num) == str(num)[::-1]


def all_palindromes(arr):
    for num in arr:
        if not is_palindrome_number(num):
            return False
    return True


# Example 1
print(all_palindromes([111, 222, 333, 444, 555]))  # Output: True

# Example 2
print(all_palindromes([121, 131, 20]))  # Output: False
