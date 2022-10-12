'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
'''

number = input("Введите число: \n x = ")
suma = 0
suma = sum(int(digit) for digit in number if digit.isdigit())
print(f"Сумма чисел равна: {suma}")
