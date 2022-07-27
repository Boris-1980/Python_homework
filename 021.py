# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('incoming_text_021.txt','w', encoding='UTF-8' ) as file:
    file.write(input('Введите первоночальный текст: '))
with open('incoming_text_021.txt','r') as file:
    my_text = file.readline()
    change_text = my_text.split()
print()
print(my_text)
print()

del_text = input('Введите  набор букв, который нужно удалить из слов содержащие данную последовательность :  ')
print(del_text)

result = ' '.join(filter(lambda x: del_text not in x, change_text))
with open('format_text_021.txt','w', encoding='UTF-8') as file:
    file.write(f'{result}')
print(result)
