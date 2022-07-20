# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)

def dif(list):
    dif_max_min =[]
    for i in range(len(list)):
        dif_max_min.append(list[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(round(dif(list),2))
