#Здесь не ватает валидации для ввода диапазона!
print('Давай выведем только чётные числа из заданного диапазона')
print('i - начало диапазона')
print('x - конец диапазона')
# Создаём пустой список
num = []

def all_range(): # Прописываем функцию для сбора значений в диапазоне (с i до x)
    while True:
        try:
            i = int(input('Введи значение i\n'))
            x = int(input('Введи значение x\n'))
            if i < x:  # проверяем, что i < x
                for value in range(i, x):  # добавляем значения в список
                    num.append(value)
                return i, x  # возвращаем начальное и конечное значения
            else:
                print("Ошибка: начальное значение должно быть меньше конечного.")
        except ValueError:
            print("Пожалуйста, введите целые числа.")

i, x = all_range() # Собирам данные в список

# Создаём фильтрацию чётных чисел (вариант HARD)
even_numbers_hard = list(filter(lambda b: b % 2 == 0, num))

# Менее "заумная" фильтрация
even_numbers_simple = [b for b in range(i, x) if b % 2 == 0]

# Выбор варианта исполнения фильтрации
print('Вариант 1 - HARD\nВариант 2 - SIMPLE')
while True:
    version_output = input('Какой вариант использовать?\nПОДСКАЗКА: Просто выбери, 1 или 2\nВводи сюда: ')
    if version_output == '1':
        result = even_numbers_hard
        print('Выбран вариант 1 (HARD):', result)
        break
    elif version_output == '2':
        result = even_numbers_simple
        print('Выбран вариант 2 (SIMPLE):', result)
        break
    else:
        print('Неверный выбор, попробуйте снова.')
