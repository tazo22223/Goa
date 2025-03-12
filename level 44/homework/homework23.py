def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

# Example usage
number_of_sheep = 3
result = count_sheep(number_of_sheep)
print(result)  # Output will be "1 sheep...2 sheep...3 sheep..."
