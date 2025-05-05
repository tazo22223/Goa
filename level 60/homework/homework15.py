def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"

# Example usage
print(mouth_size("alligator"))  # Output: "small"
print(mouth_size("frog"))       # Output: "wide"