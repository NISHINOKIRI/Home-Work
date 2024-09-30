import random #для использования рандома собсвеннор

def generate_list(start, end, length):
   # Генерирует список заданной длины со случайными числами (так интереснее)
    return [random.randint(start, end) for _ in range(length)]

def merge_sort(list1, list2):
    # Объединяет два списка и сортирует их
    merged_list = list1 + list2
    sorted_list = sorted(merged_list)
    return sorted_list

def main():
    # Запрашиваем диапазон и длину списков
    start = int(input("Введите начальное значение диапазона: "))
    end = int(input("Введите конечное значение диапазона: "))
    length1 = int(input("Введите длину первого списка: "))
    length2 = int(input("Введите длину второго списка: "))

    # Генерируем списки
    list1 = generate_list(start, end, length1)
    list2 = generate_list(start, end, length2)

    # Выводим списки
    print("Сгенерированный список 1:", list1)
    print("Сгенерированный список 2:", list2)

    # Объединяем и сортируем
    sorted_list = merge_sort(list1, list2)
    print("Объединённый и отсортированный список:", sorted_list)
    
main()
