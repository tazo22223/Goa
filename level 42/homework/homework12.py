def sum_of_numeric_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            total_sum += value
    return total_sum

# Example dictionary
my_dictionary = {
    "name": "John",
    "age": 25,
    "height": 1.75,  # in meters
    "city": "Tbilisi",
    "salary": 5000  # in USD
}

# Calculating the sum of all numeric values
result = sum_of_numeric_values(my_dictionary)
print(f"The sum of all numeric values in the dictionary is: {result}")
