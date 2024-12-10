import os # Загружаем модуль os

def all_run(): # Создаем функцию запуска всех своих команд
    commands = [
        article, # Статьи
        culture, # Культуры
        doc, # Документы
        history, # История
        news, # Новости
        page, # Страницы
        progress, # Достижения
        reference, # Полезные ссылки
        trenditem # Направления деятельности
    ]
    for command in commands: # Перебираем все команды
        os.system(f'python manage.py {command}') # Запускаем каждую команду

if __name__ == '__main__': # Если это файл с именем __main__, то запускаем функцию all_run()
    all_run() # Запускаем функцию all_run()