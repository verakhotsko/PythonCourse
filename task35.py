"""Напишите функцию, которая принимает одно число
и проверяет, является ли оно простым"""

def simpleNum(number):
    
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'    

num = int(input())
print(simpleNum(num))          