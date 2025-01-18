# შექმენით სია 10 ელემენტით
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი
num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

# შეამოწმეთ პირობები და გააკეთეთ slicing
if num1 > num2:
    sliced_list = my_list[num2:num1]
elif num2 > num1:
    sliced_list = my_list[num1:num2]
else:
    sliced_list = []

# დაბეჭდეთ ახალი სია
print("ახალი სია:", sliced_list)
