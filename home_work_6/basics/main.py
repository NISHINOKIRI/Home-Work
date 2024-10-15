import datetime
from lib.client.client import App

def task_manager():
    with open('task_list.txt', 'w', encoding='utf8') as file:
        file.write(app.get_tasks())

def ach_manager():
    with open('achivments_list.txt', 'w', encoding='utf8') as file:
        for achievement in app.get_achievements():
            file.write(f'Ачивка: "{achievement.name}"\nДата получения: {achievement.receipt_date}; \nУсловия выдачи: "{achievement.description}";\n\n')


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



