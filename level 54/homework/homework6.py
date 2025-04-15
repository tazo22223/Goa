def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

# Example usage:
double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(4))  # Output: 12