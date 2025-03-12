def replace_digits(input_string):
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character in the input string
    for char in input_string:
        # Convert the character to an integer
        digit = int(char)
        # Replace digits below 5 with '0' and digits 5 and above with '1'
        if digit < 5:
            result += '0'
        else:
            result += '1'
    
    return result

# Example usage
input_string = "273845"
output_string = replace_digits(input_string)
print(output_string)  # Output will be '001101'
