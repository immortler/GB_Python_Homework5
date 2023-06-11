"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех
арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*
2 2
    4
"""

def sum(a, b):
    if b > 0:
        b -= 1
        a += 1
        return sum(a, b)
    return print(f'Sum of these numbers is {a}.')


number_a = int(input('Enter first integer non-negative number (a): '))
number_b = int(input('Enter second integer non-negative number (b): '))
if number_a >= 0 and number_b >= 0:
    sum_of_numbs = sum(number_a, number_b)
else:
    print('You entered negative number, try again.')
