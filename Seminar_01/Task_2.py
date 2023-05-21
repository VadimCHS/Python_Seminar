# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Нахождение суммы цифр трехзначного числа.')
number = int(input('Введите число: '))
result = 0
n = 10
if number//1000 != 0 or number//100 == 0:
    print('Введено неверное чило!!!')
else:
    while number != 0:
        result += number % n
        number = number//n
    print(f'Сумма цифр равна: {result}')
