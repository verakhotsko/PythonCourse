"""
Создать словарь из строки, где буква - ключ,
а количество повторений ее - значение"""

string = input('Введите строку: ')
result = {}
for letter in string:
    result[letter] = result.get(letter, 0) + 1
print(letter, result)