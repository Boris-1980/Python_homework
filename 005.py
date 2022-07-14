# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Enter coordinate х1: '))
y1 = int(input('Enter coordinate y1: '))
x2 = int(input('Enter coordinate х2: '))
y2 = int(input('Enter coordinate y2: '))
import math
sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
print(f'Distance: (A - ({x1}, {y1}) between B - ({x2}, {y2}) = {sqrt}')