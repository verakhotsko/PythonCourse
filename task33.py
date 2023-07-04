"""Программа, которая заменяет все максимальные 
числа на минимальные и наоборот"""

def changeValue(list):
    minValue = list[0]
    maxValue = list[0]
    for i in list:
        if minValue > list[i]:
            minValue = list[i]
        elif maxValue < list[i]:
            maxValue = list[i]    
    for i in range(len(list)): # указываем длину списка иначе не напечатает новый список
        if list[i] == maxValue:
            list[i] = minValue
        elif list[i] == minValue:
            list[i] = maxValue    
    return list                


countGrades = int(input('Введите количество оценок: '))
grades = [int(grade) for grade in input().split()][:countGrades]
print(changeValue(grades))  
       
