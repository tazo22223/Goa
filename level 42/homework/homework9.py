# Creating a dictionary with at least five key-value pairs
my_dictionary = {
    "name": "John",
    "age": 25,
    "city": "Tbilisi",
    "country": "Georgia",
    "occupation": "Engineer",
    "hobby": "Photography"
}

# Removing a key-value pair using the pop() method
removed_value = my_dictionary.pop("city")

# Printing the updated dictionary
print(my_dictionary)

# Optionally, printing the removed value
print(f"Removed value: {removed_value}")
