#Ejercicio 3
print("\n")

list_of_keys = ["access_level", "age"]
employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28}

for index in range(len(list_of_keys)):
    value = list_of_keys[index]
    for key in list(employee.keys()):
        if key == value:
            employee.pop(key)

print(employee)