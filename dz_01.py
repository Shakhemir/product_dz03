"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

spisok = [1, 4, 5, 7, 2, 8, 10, 23, 11]
summ = 0
for i in range(1, len(spisok), 2):
    summ += spisok[i]
print(summ)
