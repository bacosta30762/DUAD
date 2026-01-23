#Ejercicio3
print("\n")
print("Ejercicio 3")
print("\n")

def ask_for_number():
    while True:
        try:
            choose_number = int(input("Escoge un número entero entre el 1 al 10: "))
            if 1 <= choose_number <=10:
                return choose_number
            else:
                print("Debes elegir un número entero entre el 1 y el 10")
        except ValueError:
            print("Solo se pueden elegir números enteros entre el 1 y el 10")

secret_number = 7

number = ask_for_number()
while(number != secret_number):
    print("El número es incorrecto, elige otro")
    number = ask_for_number()

print("Felicidades, adivinaste el número secreto")