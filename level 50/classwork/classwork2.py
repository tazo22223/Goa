try:
    # მომხმარებლის მიერ მონაცემის შემოტანა
    user_input = input("შეიყვანეთ თქვენი სახელი ან გვარი: ")
    
    # სხვა ტიპის ერორების პროვოცირების ილუსტრაცია
    if not user_input.isalpha():
        raise ValueError("სახელი ან გვარი უნდა შეიცავდეს მხოლოდ ასოებს!")
    
    print("თქვენი მონაცემი წარმატებით შეიტანეთ:", user_input)

except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("მოხდა შეუმჩნეველი შეცდომა:", e)
