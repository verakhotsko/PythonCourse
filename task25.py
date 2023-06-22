"""Программа, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью
постфикса формата _n.
input: a a a b c a a d c d d
output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"""
"""
string = input('Введите строку: ').split()
result = {}
for letter in string:
    if letter in result:
        print(f'{letter}_{result[letter]}', end=' ')
    else:
        print(letter, end=' ')
    result[letter] = result.get(letter, 0) + 1  """ 


string = input('Введите строку: ').split()
result = {}
for letter in string:
    if letter in result:
        print(f'{letter}_{result[letter]}', end=' ')
        result[letter] += 1
    else:
        print(letter, end=' ')
        result[letter] = 1                      
