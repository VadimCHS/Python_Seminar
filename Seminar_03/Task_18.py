# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых
# чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

my_list = [1,2,4,5]

# for i in range(int(input('Введите колличство элементов в списке: '))):
#     my_list.append(randint(0, 10))

number = int(input('Введите чило: '))
near_number = [my_list[0]]

delta = abs(number - my_list[0])

for i in range(len(my_list)):
    if abs(number - my_list[i]) == delta and near_number[0] != my_list[i]:
        if len(near_number) > 1:
            near_number[1] = my_list[i]
        else:
            near_number.append(my_list[i])

    if abs(number - my_list[i]) < delta:
        near_number[0] = my_list[i]
        delta = abs(number - my_list[i])
    
    if near_number[0] == number and len(near_number) > 1:
        near_number.pop()

print(f'Список: {my_list}')
print(f'Число: {number}')
print(f'Ближайшие числа: {near_number}')
