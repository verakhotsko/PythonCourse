"""Петя и Катя – брат и сестра. 
Петя – студент, а Катя – школьница. Петя помогает 
Кате по математике. Он задумывает два натуральных 
числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет 
сумму этих чисел S и их произведение P. Помогите 
Кате отгадать задуманные Петей числа."""

sumNum = int(input("Введите сумму чисел: "))
productNum = int(input("Введите произведение чисел: "))
for firstNum in range(sumNum):
    for secondNum in range(productNum):
        if sumNum == firstNum + secondNum and productNum == firstNum * secondNum:
            print(firstNum, secondNum)
