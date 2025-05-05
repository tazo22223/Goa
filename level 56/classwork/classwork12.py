def find_multiples(n, limit):
    return [i for i in range(n, limit + 1, n)]

# Example usage
print(find_multiples(2, 6))  # Output: [2, 4, 6]