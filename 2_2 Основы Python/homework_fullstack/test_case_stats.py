#  обработка количества тест-кейсов

cases = []
for i in range(7):
    count = int(input(f"Введите количество тест-кейсов за день {i + 1}: "))
    cases.append(count)

total_cases = sum(cases)
avg_cases = total_cases / 7

print(f"Всего тест-кейсов за неделю: {total_cases}")
print(f"Среднее количество тестов в день: {avg_cases:.2f}")

if avg_cases > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
