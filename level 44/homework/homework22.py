def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# Example usage
print(is_divisible(3, 1, 3))    # Output: True
print(is_divisible(12, 2, 6))   # Output: True
print(is_divisible(100, 5, 3))  # Output: False
print(is_divisible(12, 7, 5))   # Output: False
