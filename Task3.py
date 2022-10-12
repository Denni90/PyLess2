'''
Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072
'''

def create_sequence(n):
    result = []
    for i in range(1, n + 1):
        result.append((1 + 1 / i) ** i)
    return result

def sum_of_list(origin_list):
    sum = 0
    for number in origin_list:
        sum += number
    return sum

num = int(input('Введите число: '))
print("Сумма: ", round(sum_of_list(create_sequence(num)), 3))