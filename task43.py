"""Дан список чисел. Посчитайте, сколько пар элементов в нем 
равны друг другу."""

numbers = [int(numbers) for numbers in input().split()]
print(numbers)
count = 0
"""
for num in range(len(numbers)):
    for i in range(num + 1, len(numbers)):
        if numbers[num] == numbers[i]:
            count += 1
print(count) """

result = {}
for num in numbers:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

print(sum([num // 2 for num in result.values()]))    

