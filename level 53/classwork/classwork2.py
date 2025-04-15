def apply_to_list(func, values):
    return [func(value) for value in values]

def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_list(square, numbers)
print(squared_numbers)  