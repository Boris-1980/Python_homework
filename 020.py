# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')




# sum_of_poly = (list_of_poly_1), '+' (list_of_poly_2)




# if len(poly_1) > len(poly_2):
#     help_poly = poly_1
#     poly_1 = poly_2
#     poly_2=help_poly
# poly_1 = poly_1.split(' + ')
# poly_2 = poly_2.split(' + ')
# print(poly_1,poly_2)

# count1 =0
# count2=len(poly_2)-len(poly_1)
# new_poly = ''
# for i in range(count2):
#     new_poly += poly_2[i] + '+'

# ind1 = ''
# ind2 = ''

# for i in range(len(poly_2) - len(poly_1), len(poly_2)):
#     result = 0 
#     if i == len(poly_2) - 1:
#         result += int(poly_1[-1][:-4]+poly_2[-1][:-4])
#         new_poly += str(result) + poly_1[-1][-4:]
#     elif i == len(poly_2) - 2:
#         result += int(poly_1[-2][:-2]+poly_2[-2][:-2])
#         new_poly += str(result) + poly_1[-2][-2:] + ' + ' 
#     else:
#         result += int(poly_1[count1][:-4]+poly_2[count2][:-4])
#         new_poly += str(result) + poly_1[count1][-4:] + ' + ' 
#         count1 += 1
#         count2 += 2
# print(new_poly)




