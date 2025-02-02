def find_maximum(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Call the function with a list of numbers
maximum = find_maximum([10, 3, 6, 1, 9, 4, 7])
print("The maximum number is:", maximum)
