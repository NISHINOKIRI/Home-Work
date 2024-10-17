import random
import datetime
from lib.client.client import App
from lib.client.manage import manage_tasks_and_achievements
from lib.client.remove_tasks import num_done_tasks

app = App(
    username='Nishinokiri',
    age=27,
)

# Определяем возможные приоритеты с добавлением критического
priorities = ['trivial', 'low', 'medium', 'high', 'major', 'critical']

# Генерация случайных задач
task_ids = []
for i in range(1, 12):
    name = f'Task {i}'  # Название задачи
    priority = random.choice(priorities)  # Случайный выбор приоритета

    # Генерация случайной даты (пример: срок может быть от 0 до 10 дней)
    random_days_offset = random.randint(0, 10)
    deadline = datetime.datetime.now() + datetime.timedelta(days=random_days_offset)

    task_id = app.create_task(
        name=name,
        priority=priority,
        deadline=deadline
    )
    task_ids.append(task_id)

# print(app.get_profile())
# print(app.get_tasks())
# app.get_and_print_achievements()

# ach_manager() # Записываем ачивки в файл
# task_manager() # Записываем задачи в файл (из рефакторенного _get_tasks)
# read_tasks()
# read_achievements()
num_done_tasks(app)
manage_tasks_and_achievements(app)
