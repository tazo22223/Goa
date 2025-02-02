def remove_elements_by_indexes(main_list, indexes_list):
    # ინდექსების დალაგება უკუღმა, რომ წაშლისას ინდექსები არ გადანაცვლდეს
    indexes_list = sorted(indexes_list, reverse=True)
    
    # ინდექსებზე ელემენტების წაშლა pop() მეთოდით
    for index in indexes_list:
        if 0 <= index < len(main_list):  # ვამოწმებთ, რომ ინდექსი ლეგიტიმური იყოს
            main_list.pop(index)
    
    return main_list

# მაგალითი
main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]

result = remove_elements_by_indexes(main_list, indexes_list)
print(result)  # Output: [10, 30, 50]
