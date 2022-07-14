#  Напишите программу, которая по заданному номеру четверти, 
#  показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Enter number of quarter of axis:  "))

if   a == 1: print(" The first axis: x from 0 to + ∞, y from 0 to + ∞") 
elif a == 2: print(" The second axis: x from 0 to  - ∞, y from 0  to + ∞ ")  
elif a == 3: print(" The third axis: x from 0 to  - ∞, y from 0  to - ∞ ")
elif a == 4: print(" The four axis: x from 0 to  + ∞, y from 0  to - ∞ ")
else:        print("Error, try again") 