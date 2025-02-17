
my_tuple = (10, 20, 30, 40, 50)

try:
    my_tuple[1] = 99
except TypeError as e:
    print(f"Error: {e}")
