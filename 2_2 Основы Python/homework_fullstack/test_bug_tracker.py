# работа со словарями: статистика тестов

testers = {"Анна": 3, "Иван": 5, "Дмитрий": 7}

tester_name = input("Введите имя тестировщика: ")

if tester_name in testers:
    testers[tester_name] += 1
else:
    testers[tester_name] = 1

print("Обновленные данные:", testers)
