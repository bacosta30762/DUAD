#Ejercicio1
horas_trabajadas = int(input("Ingrese sus horas trabajadas: "))
tarifa_por_hora = int(input("Ingrese su tarifa por hora: "))

salario = horas_trabajadas * tarifa_por_hora

print(f"Su salario es de: {salario}")


#Ejercicio2
print("\n")

nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su primer apellido: ")
dominio_empresa = input("Ingrese el nombre del dominio de su empresa: ")

print(f"El email es: {nombre}.{apellido}@{dominio_empresa}.com")
