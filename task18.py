"""Требуется найти в массиве A[1..N] самый близкий 
по величине элемент к заданному числу X. 
Пользователь в первой строке вводит 
натуральное число N – количество 
элементов в массиве. В последующих  
строках записаны N целых чисел Ai. 
Последняя строка содержит число X"""

num = int(input("Введите количество элементов: "))
numberList = [int(number) for number in input('Введите значения массива: ').split()]
print(numberList)
findNum = int(input("Введите число: "))
count = findNum - numberList[0]
if count < 0:
    count *= (-1)
numbers = numberList[0]    
for i in range(1, num):
    temp = findNum - numberList[i]
    if temp < 0:
        temp *= (-1)
    if count > temp:
        count = temp    
        numbers = numberList[i]
print(numbers)