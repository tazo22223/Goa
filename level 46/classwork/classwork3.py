palindromic_numbers = [num for num in range(10, 201) if str(num) == str(num)[::-1]]
print(palindromic_numbers)