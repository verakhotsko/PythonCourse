"""Даны два массива чисел. Выведите элементы массива, 
которых нет во втором массиве. Пользователь вводит число - 
количество элементов массива, затем сами элементы."""

n = int(input('Введите количество элементов первого массива: '))
numbersN = [int(numbersN) for numbersN in input().split()][:n]
print(numbersN)

m = int(input('Введите количество элементов второго массива: '))
numbersM = [int(numbersM) for numbersM in input().split()][:m]
print(numbersM)

result = list()
for num in numbersN:
    if num not in numbersM:
        result.append(num)
        #print(num, end=' ')       
print(result)   