# Creating two dictionaries
original_dictionary = {
    "name": "John",
    "age": 25,
    "city": "Tbilisi"
}

update_dictionary = {
    "age": 26,  # This will update the age
    "country": "Georgia",  # This will add a new key-value pair
    "occupation": "Engineer"  # This will add a new key-value pair
}

# Updating the original dictionary with the update dictionary
original_dictionary.update(update_dictionary)

# Printing the updated dictionary
print(original_dictionary)
