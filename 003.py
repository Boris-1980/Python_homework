# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x=int(input('Enter coordinate - x: '))
y=int(input('Enter coordinate - y: '))

if  x > 0 and y > 0:
    print(f'Point({x}, {y}) is located in 1 quarter  of the coordinate axis')
elif x < 0 and y > 0:
    print(f'Point({x}, {y}) is located in 2 quarter  of the coordinate axis')    
elif x < 0 and y < 0:
    print(f'Point({x}, {y}) is located in 3 quarter  of the coordinate axis')    
elif x > 0 and y < 0:
    print(f'Point({x}, {y}) is located in 4 quarter  of the coordinate axis')  