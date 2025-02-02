def filter_positive_numbers(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers

# Call the function with a list of integers
positive_list = filter_positive_numbers([-10, 3, -6, 1, -9, 4, 7])
print("The positive numbers are:", positive_list)
