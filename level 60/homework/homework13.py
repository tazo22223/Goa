def stringy(size):
    # Generate the alternating string using a list comprehension
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(size)])
