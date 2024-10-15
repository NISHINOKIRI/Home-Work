import datetime
from lib.client.client import App

def task_manager():
    with open('task_list.txt', 'w', encoding='utf8') as file:
        file.write(app.get_tasks())

def ach_manager():
    with open('achivments_list.txt', 'w', encoding='utf8') as file:
        for achievement in app.get_achievements():
            file.write(f'Ачивка: "{achievement.name}"\nДата получения: {achievement.receipt_date}; \nУсловия выдачи: "{achievement.description}";\n\n')


def read_tasks():
    try:
        with open('task_list.txt', 'r', encoding='utf8') as file:
            tasks = file.read()
            print()
            print(tasks)
    except FileNotFoundError:
        print("Файл с задачами не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла задач: {e}")

def read_achievements():
    try:
        with open('achivments_list.txt', 'r', encoding='utf8') as file:
            achievements = file.read()
            print("Список ачивок:\n")
            print(achievements)
    except FileNotFoundError:
        print("Файл с ачивками не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла ачивок: {e}")



app = App(
    username='Nishinokiri',
    age=27,
)

app.create_task(
    name='test 1',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)
app.create_task(
    name='test 2',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)
app.create_task(
    name='test 3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)
app.create_task(
    name='test 4',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)
app.create_task(
    name='test 5',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)
app.create_task(
    name='test 6',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )

)

print(app.remove_task(6))
# print(app.get_profile())
# print(app.get_tasks())
# app.get_and_print_achievements()

ach_manager() # Записываем ачивки в файл
task_manager() # Записываем задачи в файл (из рефакторенного _get_tasks)
read_tasks()
read_achievements()
