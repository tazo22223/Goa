words = ["apple", "banana", "cherry", "date", "elephant"]
long_words = list(filter(lambda s: len(s) > 5, words))

print(long_words)