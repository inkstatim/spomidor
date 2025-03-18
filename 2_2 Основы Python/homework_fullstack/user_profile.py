# работа с переменными и вводом данных

name = input("Введите ваше имя: ")
profession = input("Введите вашу профессию: ")
tool = input("Введите ваш любимый инструмент для тестирования: ")

if not name or not profession or not tool:
    print("Ошибка: все поля должны быть заполнены.")
else:
    print(f"Имя: {name}, Профессия: {profession}, Любимый инструмент: {tool}.")
