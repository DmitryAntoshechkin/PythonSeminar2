# задача 4 необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

try:
    number = int (input('Введите положительное число: '))
    if number < 1:
        print('Введено некорректное число')
    else:
        seq = [0] * (2 * number + 1)
        seq[number + 1] = 1
        seq[number - 1] = 1
        for i in range(2,number+1):
            seq[number + i] = seq[number+i-1] + seq[number+i-2]
            seq[number - i] = -seq[number-i+1] + seq[number-i+2]
        print (seq)      
except:
        print('Введены некорректные данные')