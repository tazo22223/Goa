def remove_one_element(lst, index):
    # ვამოწმებთ, რომ ინდექსი სიის ფარგლებს შიგნითაა
    if 0 <= index < len(lst):
        lst.pop(index)
    else:
        print("არასწორი ინდექსი")

    print(lst)

# მაგალითი გამოყენება:
my_list = [10, 20, 30, 40, 50, 60]
index = 3

remove_one_element(my_list, index)
# შედეგი: [10, 20, 30, 50, 60]