#Ejercicio 2
print("\n")

list_a = ["first_name", "last_name", "role"]
list_b = ["Brandon", "Acosta", "Software Engineer"]

name_position = {}


for index in range(len(list_a)):
    name_position[list_a[index]] = list_b[index]

for key, item in name_position.items():
    print(key, ":", item)