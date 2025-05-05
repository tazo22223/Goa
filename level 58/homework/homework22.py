names = ["Alice", "Bob", "Amanda", "Charlie", "Alex", "David"]
names_starting_with_A = list(filter(lambda name: name.startswith("A"), names))

print(names_starting_with_A)