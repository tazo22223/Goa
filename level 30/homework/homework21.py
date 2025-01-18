def check_all_lowercase(input_string):
    """
    Checks if all characters in a given string are lowercase.

    Parameters:
    input_string (str): The string to check

    Returns:
    bool: True if all characters are lowercase, False otherwise
    """
    return input_string.islower()

# Example usage
input_string = "hello world"
result = check_all_lowercase(input_string)
print("All characters in the string are lowercase:", result)
