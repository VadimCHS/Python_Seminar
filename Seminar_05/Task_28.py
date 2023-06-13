# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2 -> 4
import sys

sys.setrecursionlimit(10000)

def sum_numbers(a, b):
    if b == 0:
        return a
    return sum_numbers(a + 1, b - 1)

number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))

print('Сумма чисел равна: ', end = '')
print(sum_numbers(number_one, number_two))

