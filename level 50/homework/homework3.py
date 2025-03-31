try:
    # Attempt to add an integer to a string
    result = "Hello" + 5
except TypeError:
    # Handle the TypeError
    print("Error: You cannot add an integer to a string.")