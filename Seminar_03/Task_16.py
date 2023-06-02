# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых 
# чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

my_list = []

for i in range(int(input('Введите колличство элементов в списке: '))):
    my_list.append(randint(0, 10))

number = int(input('Введите чило: '))
count_number = 0

for i in range(len(my_list)):
    if number == my_list[i]:
        count_number += 1

print(f'Список: {my_list}')
print(f'Число: {number}')
print(f'Встречается: {count_number}')

