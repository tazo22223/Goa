user_input = int(input("შეიყვანეთ რიცხვი: "))


total_sum = 0

for number in range(0, user_input + 1):
    total_sum += number


print(f"დიაპაზონის რიცხვების ჯამი არის: {total_sum}")

