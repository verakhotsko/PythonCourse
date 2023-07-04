"""посчитать количество гласных в словах фразы и сравнить 
с эталоном"""

text = input().lower().split()
vowels = 'ёуеыаоэяию'
result = set()
for word in text:
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    result.add(count)
if len(result) == 1:
    print(True)
else:
    print(False)    
