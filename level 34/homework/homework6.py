def outer_function():
    def inner_function():
        print("Hello from the inner function!")

    # Call the inner function
    inner_function()

# Call the outer function
outer_function()
