# изменение списка и кортежа

numbers_list = [4, 7, 9, 2, 5]
numbers_tuple = (4, 7, 9, 2, 5)

numbers_list[1] = 10

try:
    numbers_tuple[1] = 10
except TypeError:
    print("Ошибка: Кортеж нельзя изменить!")

numbers_list.append(6)

print("Измененный список:", numbers_list)
print("Исходный кортеж:", numbers_tuple)
