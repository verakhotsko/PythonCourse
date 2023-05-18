#print(5, 8, 6)
#n = 5    # none - пустое значение
#print(n)

#print(type(n))  
"""
a = 5
b = 5.89
c = "Hello"
print(a, b, c)
print(a,'-', b, '-', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a, b, c))
"""
# Ввод данных:
"""
print('Введите первое число: ') # приглашение к вводу
a = input()                     # ввод данных (на разных строках)
b = input('Введите второе число: ') # совмещеннное приглашение и ввод данных
print(a, '+', b, '=', a + b) # сложение строк
"""


# Приведение типов:
"""
c = 5.89
print(c)
print(type(c))
n = int(c)
print(n)
print(type(n))
d = str(c)
print(d)
print(type(d))
print(c + n)
#print(c + d)        # ошибка - нельзя складывать числа со строками

f = 1
print(f)
print(type(f))
s = bool(f)
print(s)
"""
# Арифметические операции:
"""
a = int (input('Введите первое число: '))                     
b = int (input('Введите второе число: ')) 
print(a, '+', b, '=', a + b) # сложение
print(a*b) # умножение
"""
"""
c = float (input('Введите первое число: '))
d = float (input('Введите второе число: '))
print(c*d)
print(round(c*d, 3))    # округление вещественных чисел
"""
# сокращённые присваивания:
"""
iter = 2    # 
iter += 3   # iter = iter + 3
iter -= 4   # iter = iter - 4
iter *= 5   # iter = iter * 5
iter /= 5   # iter = iter / 5   деленние вещественных чисел
iter //= 5  # iter = iter  // 5 целочисленное деление
iter %= 5   # iter = iter % 5   остаток от деления
iter **= 5  # iter = iter ** 5  возведение в степень
"""
# Операторы if, elif, else:
"""
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топчик)')
else:
    print('Привет, ', username)            
"""
# Операторы while (flag):
"""
n = int(input())
flag = True       # прерывающий цикл оператор
i = 2
while flag:
    if n % i == 0: # если остаток от деления равен 0
        flag = False
        print(i)
    elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
        print(i)
        flag = False
    i += 1    
"""    
# Цикл for, функция range():
"""
for i in 1, -2, 30, 4:
    print(i)           # i будет последовательно принимать перечисленные значения
"""
# range выдает занчения с шагом 1 по умолчанию
# 1-й и 2-й аргументы это диапазон не вклющающий 2-й
# 3-й аргумент это шаг
"""
for i in range(5, 50, 10):
    print(i)

for i in range(100, 0, -20):
    print(i)    
"""    
# для строк:
#for i in 'dfjvhr':
#    print(i)
"""
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)    
"""
# Работа с текстом:
"""
text = 'СъЕшь ещё эТих булочек!'
print(len(text))     # len чтобы узнать размер
print('ещё' in text) # булевая проверка
print(text.lower())  # переводит буквы в нижний регистр 
print(text.upper())  # переводит буквы в верхний регистр
print(text.replace('СъЕшь', 'Схомячь')) # изменяет текст
"""
# Срезы:
"""
text = 'СъЕшь ещё эТих булочек!'
print(text[0])            # C
print(text[1])            # ъ
print(text[len(text)-1])  # !
print(text[-5])           # o
print(text[:])            # СъЕшь ещё эТих булочек!
print(text[len(text)-2:]) # к!
print(text[2:9])          # Ешь ещё
print(text[1:-18])        # ъЕшь
print(text[0:len(text):6])# Сеио (каждую 6-ю)
print(text[::6])          # Сеио
text = text[2:9] + text[-5] + text[:2]
print(text)               # Ешь ещёоСъ
"""
n = int(input())
m = int(input())
#import math
#print(math.ceil(m/n))
print((m + n - 1)//n)