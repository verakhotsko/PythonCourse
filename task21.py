"""Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"},
{"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII
":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}"""
# Словари
"""
age = {'Anna': 25, 'Andrey': 33, 'Ivan': 45, 'Alexander': 38}
print(age['Alexander']) # обращение к возрасту по ключу имени
# Словарь в списке:
age = [{'Anna': 25, 'Andrey': 33, 'Ivan': 45, 'Alexander': 38}] #словарь в списке из одного элемента
print(age[0]['Andrey'])  # 1-ый аргумент - обращение к элементу списка(словарю), 2-й  - обращ. по ключу к элементу словаря
# Два словаря в списке:
age = [{'Anna': 25, 'Andrey': 33}, {'Ivan': 45, 'Alexander': 38}]
print(age[1]['Ivan'])"""
"""
data = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"},
        {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, 
        {"VIII":"S007"}]
values = set()
for i in data:
    #print(list(i.values())) # функция возвращает список значений
    values.add(list(i.values())[0]) # добавляем конкретное значение в множество
print(values)    """

data = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"},
        {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, 
        {"VIII":"S007"}]
values = set()
for i in data:
    for key in i:
        values.add(i[key])
print(values)
