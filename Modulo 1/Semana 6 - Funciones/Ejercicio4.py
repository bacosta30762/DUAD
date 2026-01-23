#Ejercicio 4
print("\n")

hello_world = "Hola mundo"

def return_string(string):
    for index in range(len(string)-1, -1, -1):
        print(string[index])


return_string(hello_world)