# Найти сумму чисел списка стоящих на нечетной позиции

a = [4, 6, 7, 9, 12, 4, 1, 9, 6]
lst = [a[index] for index in range(0, len(a), 2)]
print(a)
print(lst)
print(f'{sum(lst)}')
