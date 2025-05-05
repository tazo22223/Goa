strings = ["apple", "", "banana", " ", "cherry", "", "date"]
filtered_strings = list(filter(lambda s: s.strip() != "", strings))

print(filtered_strings)