# 3. Напишите функцию, принимающую в качестве аргументов 2 списка. Функция должна соединить и отсортировать их.
#
# Пример 1:
# Вход: список1 = [1,2,4], список2 = [1,3,4]
#  Выход: [1,1,2,3,4,4]
#
# Пример 2:
# Ввод: список1 = [], список2 = []
#  Вывод: []
#
# Пример 3:
# Ввод: список1 = [], список2 = [0]
#  Вывод: [0]

import random

def main():
   
    start = int(input("Введите начальное значение диапазона: "))
    end = int(input("Введите конечное значение диапазона: "))
    length1 = int(input("Введите длину первого списка: "))
    length2 = int(input("Введите длину второго списка: "))
    
    list1 = [random.randint(start, end) for _ in range(length1)]
    list2 = [random.randint(start, end) for _ in range(length2)]
    
    print("Сгенерированный список 1:", list1)
    print("Сгенерированный список 2:", list2)
    
    merged_list = list1 + list2
    sorted_list = sorted(merged_list)
    
    print("Объединённый и отсортированный список:", sorted_list)
    
main()
