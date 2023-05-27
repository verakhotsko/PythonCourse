"""Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9"""

n = int(input("Введите количество арбузов: "))
maxWeight = 0
minWeight = 1000
for i in range(n):
    x = int(input("Введите массу арбуза: "))
    if x > maxWeight:
        maxWeight = x
    if x < minWeight:
        minWeight = x
print(minWeight, maxWeight)            