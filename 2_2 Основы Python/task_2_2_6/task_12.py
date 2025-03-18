# task 12 изменение элемента во вложенном словаре
student = {"name": "Ivan", "address": {"city": "Moscow", "street": "Lenina"}}
student["address"]["city"] = "Saint Petersburg"
print(student)
