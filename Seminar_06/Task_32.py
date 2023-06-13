# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

min_range = int(input('Диапозон, от: '))
max_range = int(input('          до: '))
print(my_list := [randint(0, 20) for _ in range(10)])

print([item for item in range(len(my_list)) 
      if min_range <= my_list[item] <= max_range])
