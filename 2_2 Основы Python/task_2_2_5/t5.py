# task 5 проверка, что число НЕ кратно 3
number2 = int(input("Enter a number: "))
if number2 % 3 != 0:
    print(f"Число {number2} не кратно 3.")
else:
    print(f"Число {number2} кратно 3.")