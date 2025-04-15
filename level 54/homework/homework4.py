def convert_to_integer():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"Converted integer: {number}")
    except ValueError:
        print("Error: Please enter a valid integer.")
    finally:
        print("Operation complete.")


convert_to_integer()