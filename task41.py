"""Дан массив из целых чисел. Выведите количество
элементов, у которых два соседних и при этом оба
соседних элемента меньше данного."""

n = int(input('Введите количество элементов массива: '))
numbers = [int(numbers) for numbers in input().split()][:n]
print(numbers)

count = 0
for num in range(1, n - 1):
    if numbers[num - 1] < numbers[num] > numbers[num + 1]:
        count += 1
print(count)
