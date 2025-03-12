def manual_list(start, end, step, user_num):
    numbers = list(range(start, end, step))

    result = [num for num in numbers if num > user_num]
    return result

print(manual_list(1, 10, 1, 5)) 
print(manual_list(0, 20, 2, 10)) 
print(manual_list(-10, 10, 3, 0)) 