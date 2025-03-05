def remove_duplicates(original_list):
  
    unique_set = set(original_list)
    
    unique_list = list(unique_set)
    
    return unique_list

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
result = remove_duplicates(my_list)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
