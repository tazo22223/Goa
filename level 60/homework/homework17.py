def replace(s):
    return s.translate(str.maketrans("aeiouAEIOU", "!!!!!!!!!!"))

# Example usage
print(replace("Hi!"))       # Output: "H!!"
print(replace("!Hi! Hi!"))  # Output: "!H!! H!!"
print(replace("aeiou"))     # Output: "!!!!!"
print(replace("ABCDE"))     # Output: "!BCD!"