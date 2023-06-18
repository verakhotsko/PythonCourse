"""Дана последовательность из N целых чисел и 
число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]"""

list1 = [int(i) for i in input().split()]
step = int(input("Введите количество сдвигов: "))
step = step % len(list1)
resultList = list()
for i in range(len(list1)):
    resultList.append(list1[i - step])
print(resultList)