"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

def fibonacci(number):
    fib = [0, 1]
    negafib = [-1]
    if number < 1:
        return [0]
    for index in range(2, number + 1):
        fib.append(fib[index-1]+fib[index - 2])
        negafib = [(-1 if index % 2 == 0 else 1) * fib[index]] + negafib
    return negafib + fib

print(fibonacci(int(input("Введите число: "))))