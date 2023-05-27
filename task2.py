"""Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)"""

number = int(input("Введите трёхзначное число: "))

digit1 = number % 10
digit2 = number // 100
digit3 = ( number // 10) % 10
if number < 100 or number > 999:
    print("Введённое число не трёхзначное. Повторите ввод.")
else:
    print(f"Сумма всех цифр в числе {number} равна {digit1 + digit2 + digit3}")     
"""
while number < 100 or number > 999:
    number = int(input("Это не трёхзначное число. Повторите ввод: "))
print(number)"""