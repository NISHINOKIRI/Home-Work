# Функция для выбора варианта исполнения
def select_variant():

    inp = input('Выберите вариант 1 или 2\nИли введите "3" для выхода\n')
    if inp == '1':
        func_1()
    elif inp == '2':
        func_2()
    elif inp == '3':
        func_3()
    else:
        print('Нет доступных вариантов.')
        select_variant()

# Вариант с рандомной генерацией массива
def func_1():
    from random import sample
    pairs_number = sample(range(1, 21), 20) #Генерируем массив (20 рандомных чисел в диапазоне от 1 до 21)
    def output_answer():
        for i in range(0, len(pairs_number), 2):
            pair = (pairs_number[i], pairs_number[i + 1])  # Определяем пару
            pair_sum = pairs_number[i] + pairs_number[i + 1]
            print(f"Пара: {pair}, Сумма: {pair_sum}")
    print('Сгенерированный массив:', pairs_number)
    output_answer()
    print('\nЗавершение программы')

# Вариант без импорта рандома\с использованием готового массива
def func_2():
    pairs_number = (1, 2, 3, 4, 5, 6)
    def output_answer():
        for i in range(0, len(pairs_number), 2):
            pair = (pairs_number[i], pairs_number[i + 1])  # Определяем пару
            pair_sum = pairs_number[i] + pairs_number[i + 1]
            print(f"Пара: {pair}, Сумма: {pair_sum}")
    print('Массив:', pairs_number)
    output_answer()
    print('\nЗавершение программы')

# Реализация выхода
def func_3():
    print('\nЗавершение программы')

select_variant()
