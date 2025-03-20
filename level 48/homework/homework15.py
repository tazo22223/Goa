def feast(beast, dish):
    # Check if the first and last letters of the beast match those of the dish
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# Examples:
print(feast("great blue heron", "garlic naan"))  # Output: True
print(feast("chickadee", "chocolate cake"))     # Output: True
print(feast("brown bear", "bear claw"))         # Output: False
