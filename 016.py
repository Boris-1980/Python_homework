# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

pi = math.pi
print('Pi = ', pi)
d = 0.001
print(f'Accuracy = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print(round(pi, count))
