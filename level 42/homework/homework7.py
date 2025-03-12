# Creating a dictionary with at least five key-value pairs
my_dictionary = {
    "name": "John",
    "age": 25,
    "city": "Tbilisi",
    "country": "Georgia",
    "occupation": "Engineer"
}

# Retrieving a value using the get() method
key_to_retrieve = "city"
value = my_dictionary.get(key_to_retrieve, "Key does not exist")

print(value)
