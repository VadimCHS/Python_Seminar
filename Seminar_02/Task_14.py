# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

limitation = int(input('Введите число: '))
number_of_degree = 2
result = 1
while result < limitation:
    print(result)
    result *= number_of_degree