# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

a = int(input('Enter the number: '))
list =[]
for i in range(1,a+1):
    if(a%i==0):
      list.append(i)
print(f'{a} = {list}')