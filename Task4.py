# Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# Пример 10: 0, 1, 2, 3

n = int(input('Введите натуральное целое число: '))

i = 0
array = list()
while (i < n):
    if (2**i > n): break
    array.append(i)
    i += 1

print (f'{n}: {array}')