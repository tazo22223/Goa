# Create a list
my_list = [10, 20, 30, 40, 50]

try:
    # Attempt to access an index that doesn't exist
    print(my_list[10])
except IndexError:
    # Handle the IndexError
    print("Error: You tried to access an index that doesn't exist in the list.")