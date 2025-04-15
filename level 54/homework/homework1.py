def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        
        result = num1 / num2
        print(f"Result: {result}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Error: Please enter valid numbers.")
    finally:
        print("Operation complete.")
divide_numbers()