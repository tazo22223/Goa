def first_n_multiples(x, n):
    return [x * i for i in range(1, n + 1)]

# Example usage
number = 3
count = 5

result = first_n_multiples(number, count)
print(result)  # Output will be [3, 6, 9, 12, 15]
