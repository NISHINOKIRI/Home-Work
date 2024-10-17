def num_done_tasks(app):
    num_tasks_to_remove = int(input("Сколько задач вы хотите удалить? "))
    for i in range(1, num_tasks_to_remove + 1):
        app.remove_task(int(i))

