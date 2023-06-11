"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""

def power(num, pow):
    if pow > 1:
        num = num*number
        pow -= 1
        print(f'{num} , {pow}')
        return power(num, pow)
    return num


number = int(input('Enter a number: '))
power_on_numb = int(input('Enter a power of that number: '))
if power_on_numb < 0:
    print('Error: negative power entered. Calculation of negative powers will be added in future versions.')
elif power_on_numb == 0:
    print(f'Any number to the power of zero is equal to 1.')
else:
    result = power(number, power_on_numb)
    print(f'{number} to the power of {power_on_numb} is {result}.')
