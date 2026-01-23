#Ejercicio2
print("\n")
print("Ejercicio 2")
print("\n")

name_ask = input("Ingrese su nombre: ")
lastname_ask = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
if (age <= 2):
    print(name_ask + " " + lastname_ask + " " + "es un bebé")
elif (age <= 10):
    print(name_ask + " " + lastname_ask + " " +"es un niño")
elif (age <= 12):
    print(name_ask + " " + lastname_ask + " " +"es un preadolescente")
elif (age <= 17):
    print(name_ask + " " + lastname_ask + " " +"es un adolescente")
elif (age <= 25):
    print(name_ask + " " + lastname_ask + " " +"es un adulto joven")
elif (age <= 64):
    print(name_ask + " " + lastname_ask + " " +"es un adulto")
else:
    print(name_ask + " " + lastname_ask + " " +"es un adulto mayor")
