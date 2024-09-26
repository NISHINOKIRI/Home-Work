word = input('Введите слово для проверки: ')

while True:
    if word == ''.join(reversed(word)):
        print('Палиндром')
        break
    if word != ''.join(reversed(word)):
        print('Не палиндром\nПопробуй ещё раз')
        break
