# Creating a dictionary with at least five key-value pairs
my_dictionary = {
    "name": "John",
    "age": 25,
    "city": "Tbilisi",
    "country": "Georgia",
    "occupation": "Engineer"
}

# Checking if a specific key exists using the in operator
key_to_check = "city"

if key_to_check in my_dictionary:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
