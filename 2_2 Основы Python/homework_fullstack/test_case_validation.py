# проверка корректности данных: ввод и валидация

while True:
    cases = input("Введите количество тест-кейсов: ")
    if cases.isdigit() and int(cases) > 0:
        cases = int(cases)
        break
    print("Некорректный ввод. Введите положительное число.")

if cases > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
