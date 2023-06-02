# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
one = 1000
two = -1000

sum_numbers = one + two                  #int(input('Сумма чисел: '))
product_numbers =  one*two             #int(input('Произведение чисел: '))
discriminant = sum_numbers * sum_numbers - 4 * product_numbers
print(discriminant)
root_of_disc = 1
while root_of_disc * root_of_disc < discriminant:
    root_of_disc += 1
if root_of_disc * root_of_disc > discriminant:
    print('Введены не коректные данные!!!')
else:
    print(f'Перво число: {int((sum_numbers + root_of_disc)/2)}') 
    print(f'Второе число: {int((sum_numbers - root_of_disc)/2)}')
