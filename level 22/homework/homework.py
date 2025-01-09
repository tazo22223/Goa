
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
num1, num2 = int(input("Enter number: ")), int(input("Enter number: "))

if num1 > num2: print(list1[num2:num1])
elif num2 > num1: print(list1[num1:num2])
else: print([])