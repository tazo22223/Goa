def no_duplicates(user_list):
    return list(set(user_list))
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = ['a', 'b', 'b', 'c', 'd', 'd']
list3 = [10, 20, 20, 30, 40, 40, 50]

print(no_duplicates(list1))  
print(no_duplicates(list2))  
print(no_duplicates(list3)) 