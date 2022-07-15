# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

num = input("Enter the number: ")
sum = 0
for i in num:
    if i!=".":
        sum = sum + int(i)
print(f"The sum of the {num} is: ", sum)
