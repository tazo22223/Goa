def access_list():
    my_list = ["apple", "banana", "cherry", "date"]
    
    try:
        index = int(input(f"Enter an index (0-{len(my_list)-1}): "))
        print(f"Item at index {index}: {my_list[index]}")
    
    except ValueError:
        print("Error: Please enter a valid integer.")
    except IndexError:
        print("Error: Index out of range. Please enter a number between 0 and", len(my_list)-1)
    finally:
        print("Operation complete.")


access_list()