# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, 
# сами значения предикатов случайные, проверяем это утверждение 100 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа. 
# В конце вывести результат проверки истинности этого утверждения.

from random import choice, randint
from datetime import datetime
TESTS = 100
start_time = datetime.now()
result = True
for i in range(TESTS):
    left_side = choice([True, False])
    right_side = not left_side
    for j in range(randint(4,24)):
        predicat = choice([True, False])
        left_side = left_side or predicat
        right_side = right_side and (not predicat)
    left_side = not left_side
 #   print(f'Тест {i}, предикатов {j+2}, левая часть : {left_side} правая часть : {right_side}')
    if left_side != right_side:
        result = False
stop_time = datetime.now()    
print(f'На {TESTS} тестах результат проверки - {result}')
print(f'Время работы программы: {stop_time - start_time}')









