import random
import datetime
from lib.client.client import App
from lib.client.manage import manage_tasks_and_achievements
from lib.client.added_task_number import show_added_task_number
from lib.client.remove_tasks import num_done_tasks

app = App(
    username='Nishinokiri',
    age=27,
)

# Вынести это блок в отдельный файл
# Начало блока

# Определяем возможные приоритеты с добавлением критического
priorities_list = ['trivial (-1)', 'low (0)', 'medium (1)', 'high (2)', 'major (3)', 'critical (99)']
# Генерация случайных задач
task_ids = []
num_tasks = random.randint(1, 15) # Генерация случайного количества (от 1 до 15)
for i in range(1, num_tasks + 1): # Генерация случайного числа (от 1 до нам)
    tn = f'Задача {i}'  # Название задачи
    priority = random.choice(priorities_list)  # Случайный выбор приоритета

    # Генерация случайной даты
    d_gen = random.randint(0, 10)
    dl_gen = datetime.datetime.now() + datetime.timedelta(days=d_gen)

    # Генерация случайного времени (часы и минуты)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    deadline = dl_gen.replace(hour=random_hours, minute=random_minutes, second=0)

    task_id = app.create_task(
        name=tn,
        priority=priority,
        deadline=deadline
    )
    task_ids.append(task_id)

# Конец блока
show_added_task_number(num_tasks)
num_done_tasks(app, num_tasks)
manage_tasks_and_achievements(app)