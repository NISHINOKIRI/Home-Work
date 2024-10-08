class Vehicle:
    """Суперкласс с базовыми опциями"""
    def __init__(self, maker, model, color):
        self.maker = maker
        self.model = model
        self.engine_started = False
        self.color = color

    def move_forward(self):
        if self.engine_started:
            print(f'{self.color} {self.maker} {self.model} движется вперед.')
        else:
            print(f'Запустите двигатель {self.maker} {self.model}, чтобы начать движение вперед.')

    def move_back(self):
        if self.engine_started:
            print(f'{self.color} {self.maker} {self.model} движется назад.')
        else:
            print(f'Двигатель {self.maker} {self.model} не запущен, чтобы начать движение назад, запустите двигатель.')

    def start_engine(self):
        self.engine_started = True
        print(f'Двигатель {self.color} {self.maker} {self.model} запущен.')

    def stop_engine(self):
        self.engine_started = False
        print(f'Двигатель {self.color} {self.maker} {self.model} заглушен.')


class Car(Vehicle):
    """Субкласс для автомобилей"""
    pass


class Motorcycle(Vehicle):
    """Субкласс с опциями для мотоциклов"""
    def move_back(self):
        if self.engine_started:
            print(f'{self.color} {self.maker} {self.model} не может ездить задним ходом.')
        else:
            print('Двигатель не запущен')


# Создание объектов
car = Car('Toyota', 'Camry', 'Красная')
motorcycle = Motorcycle('Kawasaki', 'Ninja', 'Пурпурный')

# Примеры использования:

print(f"\n{car.color} {car.maker} {car.model} c запущенным двигателем\n")
car.start_engine()
car.move_forward()
car.move_back()

print(f"\nЗаглушим двигатель {car.maker} {car.model}\n")
car.stop_engine()
car.move_forward()
car.move_back()

print(f"\n{motorcycle.color} {motorcycle.maker} {motorcycle.model} c запущенным двигателем\n")
motorcycle.start_engine()
motorcycle.move_forward()
motorcycle.move_back()

print(f"\nЗаглушим двигатель {motorcycle.maker} {motorcycle.model}\n")
motorcycle.stop_engine()
motorcycle.move_forward()
motorcycle.move_back()
