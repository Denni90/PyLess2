'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.
'''

def massive_():
    for i in range(-number, number+1):
        lst.append(i)
    print("Вывод массива: ", lst)

def operation():
    if ((a > len(lst) and b > len(lst)) or (a <= 0 and b <= 0)):
        print('Таких позчий нет в списке')
    elif (a > len(lst) or b > len(lst) or a <= 0 or b <= 0):
        if ( a > len(lst) or a <= 0 ):
            print('Позиции под номером 1 нет в списке')
        else:
            print('Позиции под номером 2 нет в списке')
    else:
        print(f"Произведение позиций {a} и {b} равна: ", int(lst[a-1]) * int(lst[b-1]))


number = int(input('Введите число элементов: '))
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
lst = []
massive_()
operation()
