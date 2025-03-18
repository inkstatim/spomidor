# анализ логов

log_message = input("Введите строку лога: ").strip()

processed_log = log_message.replace("Ошибка", "Ошибка критическая")

words = processed_log.split()

print("Обработанная строка:", processed_log)
print("Разбитый текст:", words)
