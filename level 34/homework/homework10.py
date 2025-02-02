def sum_divisible_by_three(start, end):
    total_sum = 0
    for number in range(start, end + 1):
        if number % 3 == 0:
            total_sum += number
    return total_sum

# Call the function with the range 1 to 100
result = sum_divisible_by_three(1, 100)
print("The total sum of numbers divisible by 3 is:", result)
