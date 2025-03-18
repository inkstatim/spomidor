# работа со списком багов

bugs = ["Ошибка 1 — High", "Ошибка 2 — Low", "Ошибка 3 — Medium", "Ошибка 4 — High", "Ошибка 5 — Low"]

new_bug = input("Введите новый баг с приоритетом (например, 'Ошибка 6 — Medium'): ")
bugs.append(new_bug)

bugs = [bug for bug in bugs if "Low" not in bug]

sorted_bugs = sorted(bugs, key=lambda x: x.split("—")[1].strip(), reverse=True)

print("Обновленный список багов:", sorted_bugs)
