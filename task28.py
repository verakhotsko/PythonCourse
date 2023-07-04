"""Вводится десятичное число. Реализовать алгоритм его
перевода в двоичную систему счисления через рекурсию. 
Нельзя использовать функцию bin()"""
"""
n = int(input())
result = ''
while n > 0:
    result = str(n % 2) + result
    n //= 2
print(result)    """

def binary(n):
    if n == 0 or n == 1:
        return f'{n}'
    return binary(n // 2) + f'{n % 2}'

n = int(input())
print(binary(n))