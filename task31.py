"""Задача на фибоначчи"""
def fibonacchi(a):
    if a == 0 or a == 1:
        return 1
    return fibonacchi(a - 1) + fibonacchi(a - 2)
a = int(input('Введите число Фибоначчи: '))
print(fibonacchi(a))