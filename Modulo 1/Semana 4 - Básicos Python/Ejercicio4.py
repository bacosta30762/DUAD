#Ejercicio4
print("\n")
print("Ejercicio 4")
print("\n")

number_one = int(input("Ingrese su primer número entero: "))
number_two = int(input("Ingrese su segundo número entero: "))
number_three = int(input("Ingrese su tercer número entero: "))

if(number_one <= number_two < number_three):
    print(f"El número mayor es el: {number_three}")
elif(number_two <= number_one < number_three):
    print(f"El número mayor es el: {number_three}")
elif(number_one <= number_three < number_two):
    print(f"El número mayor es el: {number_two}")
elif(number_three <= number_one < number_two):
    print(f"El número mayor es el: {number_two}")
else:
    print(f"El número mayor es el: {number_one}")