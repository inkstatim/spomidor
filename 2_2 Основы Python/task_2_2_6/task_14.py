# task 14 изменение элемента в словаре, находящемся внутри списка
students = [{"name": "Ivan", "age": 20}, {"name": "Petya", "age": 22}]
for student in students:
    if student["name"] == "Petya":
        student["age"] = 23
print(students)
