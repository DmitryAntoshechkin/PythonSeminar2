# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.


try:
    number = int (input('Введите число больше 1: '))
    if number < 1:
        print ('Введено неверное число')
    else:
        pow = 1
        while pow <= number:
            print(pow, end = ' ')
            pow *=2
except:
    print('Введены некорректные данные')