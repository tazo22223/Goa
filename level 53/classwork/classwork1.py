def division_calculator():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        if denominator == 0:
            raise ValueError("Division by zero is not allowed.")
        
        result = numerator / denominator
        print(f"Result: {result}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception:
        print("Error: Please enter valid numbers.")
    finally:
        print("Operation complete.")

# Run the function
division_calculator()