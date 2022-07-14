#  Напишите программу, которая принимает на вход цифру,
#  обозначающую день недели, и проверяет,
#  является ли этот день выходным.

a = int(input('Enter day number (1-7): '))
week = ['Monday', 'Tuesday', 'Wendsday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
if a in range(1, 8):
    if a in range(1, 6):
        print(week[a-1], ' - Its a workday today(')
    else:
        print(week[a-1], ' - Your lucky, its a holiday!')
else:
    print('Your make mistake, try another number.')
