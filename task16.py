"""Требуется вычислить, сколько раз встречается 
некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит 
натуральное число N – количество 
элементов в массиве. В последующих  
строках записаны N целых чисел Ai. 
Последняя строка содержит число X"""

num = int(input("Введите целое число: "))
numberList = [number for number in range(1, num + 1)]
#numberList = [1, 2, 2, 3, 6, 5, 7, 7, 7, 8]
print(numberList)
findNum = int(input("Введите искомое число: "))
count = 0
for number in numberList:
    if findNum == number:
        count += 1
print(count)        
