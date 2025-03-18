
# task 3 определение, является ли число положительным и чётным
number1 = int(input("Введи число: "))
if number1 > 0 and number1 % 2 == 0:
    print(f"Число {number1} является чётным.")
else:
    print(f"Число {number1} не четное.")