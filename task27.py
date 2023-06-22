"""Пользователь вводит текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены
одним пробелом. Определите, сколько различных слов содержится
в тексте."""

print(len(set(input('Введите текст: ').lower().split())))


#She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells