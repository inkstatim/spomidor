# фильтрация баг-репортов: работа со списками

bugs = ["Ошибка 1 — High", "Ошибка 2 — Medium", "Ошибка 3 — Low", "Ошибка 4 — High", "Ошибка 5 — Medium", "Ошибка 6 — Low"]

priority = input("Введите приоритет для поиска (High, Medium, Low): ")

filt_bugs = [bug for bug in bugs if priority in bug]

if filt_bugs:
    print("Найденные баги:", filt_bugs)
else:
    print("Баги с таким приоритетом не найдены.")
