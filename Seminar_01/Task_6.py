# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма 
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

print('Проверка счастливости номера билета')
number = int(input('Введите номер билета: '))
firstNumber = number//1000
secondNumber = number%1000
firstSum = 0
secondSum = 0
while firstNumber != 0:
    firstSum += firstNumber%10
    firstNumber //= 10
while secondNumber != 0:
    secondSum += secondNumber%10
    secondNumber //= 10 
if firstSum == secondSum:
    print (f'{number} -> счастливый')
else:
    print (f'{number} -> не счастливый')
