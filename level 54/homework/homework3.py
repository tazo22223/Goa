def access_dictionary():
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    
    try:
        key = input("Enter a key to access: ")
        print(f"Value: {my_dict[key]}")
    except KeyError:
        print("Error: Key not found in dictionary.")
    finally:
        print("Operation complete.")


access_dictionary()