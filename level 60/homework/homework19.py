def add_length(sentence):
    return [f"{word} {len(word)}" for word in sentence.split()]

# Example usage
print(add_length("apple ban"))  # Output: ["apple 5", "ban 3"]
print(add_length("you will win"))  # Output: ["you 3", "will 4", "win 3"]