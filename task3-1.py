'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))

def division(num1, num2):
    try:
        result = num1 / num2
        return result
    except:
        return 'Деление на 0 невозможно'

print(division(number1, number2))