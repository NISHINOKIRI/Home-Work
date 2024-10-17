def manage_tasks_and_achievements(app):
    # Сохранение задач
    with open('task_list.txt', 'w', encoding='utf8') as file:
        file.write(app.get_tasks())  # Уберите <code>app</code> как аргумент

    # Сохранение ачивок
    with open('achivments_list.txt', 'w', encoding='utf8') as file:
        for achievement in app.get_achievements():  # Уберите <code>app</code> как аргумент
            file.write(f'Ачивка: "{achievement.name}"\nДата получения: {achievement.receipt_date}; \nУсловия выдачи: "{achievement.description}";\n\n')

    # Чтение задач
    with open('task_list.txt', 'r', encoding='utf8') as file:
        print()
        print(file.read())

    # Чтение ачивок
    with open('achivments_list.txt', 'r', encoding='utf8') as file:
        print("Список ачивок:\n")
        print(file.read())