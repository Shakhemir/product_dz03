"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

def drobnchast(float_number):
    result = float_number - int(float_number)
    return result if result != 0 else None


spisok = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in spisok:
    drobn = drobnchast(i)
    if drobn is None:
        continue
    if drobn < min:
        min = drobn
    if drobn > max:
        max = drobn
print(max - min)