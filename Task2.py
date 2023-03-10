# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

from random import randrange

n = int(input('Введите количество монеток на столе: '))

tails = randrange(n)
heads = n - tails

if (tails < heads): print (f'Нужно перевернуть {tails} монет!')
else: print (f'Нужно перевернуть {heads} монет!')