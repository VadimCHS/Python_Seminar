# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponentiation (number, exp):
    if exp == 0:
        return 1
    return number * exponentiation(number, exp - 1)

input_number = int(input('Введите число: '))
input_exp = int(input('Введите степнь: '))

print(exponentiation(input_number, input_exp))