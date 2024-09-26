word = input('Введите слово(или вообще любые символы, я не написал тут валидацию) для проверки: ')

while True:
    if word == ''.join(reversed(word)):
        print('Палиндром')
        break
    if word != ''.join(reversed(word)):
        print('Не палиндром')
        break
