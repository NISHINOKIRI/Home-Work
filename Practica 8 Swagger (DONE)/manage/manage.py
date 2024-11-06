from Decor.Decor import Decs
from utils.swagger import SwaggerPetID
import requests

class Manage:
    @staticmethod
    def request_info():
        # Пример использования класса
        swagger_pet = SwaggerPetID()  # Создаём экземпляр
        pet_id = swagger_pet.get_id_from_user()  # Получаем ID питомца
        swagger_pet.request_processing(pet_id)  # Получаем данные о питомце (если они есть в обработанном ответе)
        json_data = swagger_pet.return_answer_json(pet_id)  # Получаем JSON

    @staticmethod
    def dell():
        # Создаём экземпляр SwaggerPetID
        swagger_pet = SwaggerPetID()
        # Получаем ID питомца
        pet_id = swagger_pet.get_id_from_user()
        # Удаляем питомца
        response_data = swagger_pet.dell(pet_id)  # Выполняем удаление питомца
        # Проверяем, успешно ли прошло удаление

    # @staticmethod
    # def add():
    #     swagger_pet = SwaggerPetID()
    #     # Получаем данные о питомце от пользователя
    #     while True:
    #         pet_id = input("\nВведите ID для нового питомца: ")
    #         if id is None or id <= 0:
    #             raise ValueError("ID питомца должен быть больше 0 и не может быть пустым.")
    #         pet_name = input("Введите имя питомца: ")
    #         category_name = input("Введите категорию питомца: ")
    #         pet_status = input("Введите статус питомца (доступен/нет): ")
    #         # Вызываем метод добавления питомца
    #         response_data = swagger_pet.add_pet(id=pet_id, name=pet_name, category_name=category_name, status=pet_status)
    #         if response_data is not None:
    #             print("Питомец успешно добавлен.")
    #         else:
    #             print(f"Не удалось добавить питомца с ID {pet_id}.")

    @staticmethod
    def add():
        swagger_pet = SwaggerPetID()
        # Получаем данные о питомце от пользователя (да, да, я помню что лучше без этого, но я захотел реализовать так)
        while True:
            pet_id = input("\nВведите ID для нового питомца: ")
            try:
                pet_id = int(pet_id)
                if pet_id <= 0:
                    raise ValueError("ID питомца должен быть больше 0.")
            except:
                print("Нет! Только целые числа!")
                continue  # Возвращаемся на начало цикла, чтобы запросить ID снова

            pet_name = input("Введите имя питомца: ")
            category_name = input("Введите категорию питомца: ")
            pet_status = input("Введите статус питомца (доступен/нет): ")

            # Вызываем метод добавления питомца
            response_data = swagger_pet.add_pet(
                id=pet_id,
                name=pet_name,
                category_name=category_name,
                status=pet_status)

            if response_data is not None:
                print("Питомец успешно добавлен.")
                break  # Выходим из цикла, если добавление прошло успешно
            else:
                print(f"Не удалось добавить питомца с ID {pet_id}.")