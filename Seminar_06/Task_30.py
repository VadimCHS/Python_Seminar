# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input('        Первый элемент: '))
difference = int(input('              Разность: '))
size = int(input('Коллдичество элементов: '))

print([first_el + el * difference for el in range(size)])