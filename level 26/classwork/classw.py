def manual_len(input_list):
    length = 0 # ვაწყობთ სიის სიგრძის დაწყებითი მნიშვნელობა ნულის
    for item in input_list:
        length += 1 # ვზრდით სიგრძის ცვლადს თითოეული ელემენტის მიღებისას
        return length
        # ფუნქციის გამოძახება და სიის სიგრძის დაბეჭდვა
        sample_list = [1, 2, 3, 4, 5]
        print(f"სიის სიგრძეა: {manual_len(sample_list)}")
        