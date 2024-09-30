class ValueReverser:
    def __init__(self):
        self.input_value = input('Введите что-то: ')
        self.result = self.get_reversed_value()
        print(f'Результат: {self.result}')

    def reverse_value_int(self, value):
        try:
            if_num = int(value)
            sign = -1 if if_num < 0 else 1
            reversed_num = int(str(abs(if_num))[::-1])
            return sign * reversed_num
        except ValueError:
            return None  # Если это не целое число

    def reverse_value(self, value):
        try:
            if_foloat_num = float(value)
            sign = -1 if if_foloat_num < 0 else 1
            str_num = str(abs(if_foloat_num))
            reversed_num = str_num[::-1]
            return sign * float(reversed_num)
        except ValueError:
            return value[::-1]

    def get_reversed_value(self):
        result = self.reverse_value_int(self.input_value)
        if result is not None:
            return result
        result = self.reverse_value(self.input_value)
        return result

reverser = ValueReverser()
