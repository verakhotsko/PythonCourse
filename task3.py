"""В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них."""
# Input: 20 21 22(ввод чисел НЕ в одну строку)
class1 = int(input("Количество учеников в А классе: "))
class2 = int(input("Количество учеников в Б классе: "))
class3 = int(input("Количество учеников в В классе: "))
print((class1//2 + class1%2) + (class2//2 + class2%2) + (class3//2 + class3%2))