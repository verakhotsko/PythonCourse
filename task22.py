"""Даны два неупорядоченных набора целых чисел. 
Выдать без повторений в порядке возрастания 
все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств."""

listN = []
for num in range(int(input())):
    listN.append(int(input()))
print(listN)   
listM = []
for num in range(int(input())):
    listM.append(int(input()))
print(listM)
setResult = set(listN) & set(listM)  # пересечение множеств 
#setResult = set(listN).intersection(set(listM))

#sets = set() 
#setResult = sets.union(listN, listM) # объединение множеств
#setResult = set(listN).union(set(listM))

#setResult = set(listN) - set(listM)   # разность множеств 
#setResult = set(listN).difference(set(listM))

listResult = list(setResult)  # сортировка только списков не множеств
listResult.sort()
#listResult.sort(reverse=True) # обратная сортировка
print(listResult)
#sortListResult = sorted(listResult)
#print(sortListResult)