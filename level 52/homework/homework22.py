def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:
            return arr[i]
    return None  # Return None if all elements are consecutive

# Example usage:
print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))  # Output: 6
print(first_non_consecutive([-3, -2, -1, 0, 1, 3, 4]))  # Output: 3
print(first_non_consecutive([10, 11, 12, 13]))  # Output: None