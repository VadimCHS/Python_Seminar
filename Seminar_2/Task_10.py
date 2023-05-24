# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

number_of_coins = int(input('Введите число монеток: '))
eagle = 0
tails = 0

for i in range(number_of_coins + 1):
    position = randint(0, 1)
    print (f'{i}: {"орел" if position == 0 else "решка"}')
    if position == 0:
        eagle += 1
    else:
        tails += 1

if eagle <= tails:
    print (f'Минимальное число монет: {eagle}')
else:
    print (f'Минимальное число монет: {tails}')

