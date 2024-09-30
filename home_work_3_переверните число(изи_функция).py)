# 2. Дано целое число x, вернуть x с обратными цифрами
# Пример 1:
#  Вход: x = 123
#  Выход: 321

# Пример 2:
# Вход: x = -123
# Выход: -321
#
# Пример 3:
# Вход: x = 120
# Выход: 21

input_value = input('Введите что-то: ')
def reverse(value):
    try:
        if_num = int(value)
        sign = -1 if if_num < 0 else 1
        reversed_num = int(''.join(reversed(str(abs(if_num)))))
        return sign * reversed_num
    except ValueError:
        return ''.join(reversed(value))
result = reverse(input_value)
print(result)
