# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

my_list_one = [randint(0, 10) for _ in range(
    int(input('Размер первого набора чисел: ')))]

my_list_two = [randint(0, 10) for _ in range(
    int(input('Размер второго набора чисел: ')))]

print(f'Первый набор: {my_list_one}')
print(f'Второй набор: {my_list_two}')
print('Пересечение наборов: ', end = '')
print(sorted(set(my_list_one).intersection(set(my_list_two))))
