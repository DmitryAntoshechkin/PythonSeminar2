# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import choice
try:
    number = int (input('Введите количество монет: '))
    if number < 2:
        print('Введено некорректное число')
    else:
        coins = list()
        for i in range(number):
            coins.append(choice([0,1])) 
        print(coins)
        zero_sum = 0
        for i in range(number):
            if coins[i] == 0:
                zero_sum +=1
        if zero_sum < number/2:
            print(f'Надо перевернуть {zero_sum} монеток')
        else:
            print(f'Надо перевернуть {number - zero_sum} монеток')
except:
        print('Введены некорректные данные')

