def check_even_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

# Call the function with a list of numbers
check_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
