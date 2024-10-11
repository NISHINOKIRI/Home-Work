field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

# Заполняем поле звездочками
def filing():
    for l in range(len(field)):
        for w in range(len(field[l])):
            field[l][w] = '*'

# Удаляем звёздочку из центра
def del_center():
    # Центр для 3x3 поля
    l = 1
    w = 1
    field[l][w] = ' '

# Выводим поле в строку
def answer():
    for row in field:
        print('|', ' | '.join(row), '|') # Добавляем рамку, и центрируем символы(костыль но всё же)

# Заполняем поле и удаляем центр
filing()
del_center()

# Выводим конечный результат
answer()