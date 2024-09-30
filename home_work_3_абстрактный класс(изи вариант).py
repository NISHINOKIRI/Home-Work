# 1. Создайте класс с базовыми-абстрактными функциями. Класс должен иметь аргументы. Настройте поведение экземпляра
# класса с помощью дандер методов

class Users:
    def __init__(self):
        self.users = []

    def add_user(self, name='unknown', age=0, gender='not specified'):
        new_user = {
            'name': str(name),
            'age': int(age),
            'gender': str(gender)
        }
        self.users.append(new_user)

    def __str__(self):
        return '\n\n'.join(f"User name: {user['name']};\nАge: {user['age']};\nGender: {user['gender']};" for user in self.users)
        #Используем __str__ который будет вызваться автоматически при использовании print() и возвращать юзера в строковом формате
        #(без него судя по всему не обойтись)
        # \n\n используется для лучшей читаемости

user_list = Users() # Создание экземпляра класса
name1 = str(input('Enter the name of user 1: '))
age1 = int(input('Enter the age of user 1: '))
gen1 = str(input('Enter the gender of user 1: '))
user_list.add_user(name1, age1, gen1) # Добавление пользователя с вводом параметров
user_list.add_user('Some name 2', 57, 'some gender 2')# Добавление 2-го пользователя с готовыми параметрами
print() #Что бы выводилось красиво ^-^
print(user_list) #Выводим экземпляр класса с двумя юзерами (которых создали выше)
