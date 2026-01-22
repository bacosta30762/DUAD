
#Ejercicio1
print("Ejercicio 1")
print("\n")
name = "Brandon"
lastname = "Acosta"
one = 1
two = 2
cars = ["Toyota", "Nissan", "Hyundai"]
numbers = [10, 11, 12]
numbers2 = [1, 2, 3]
number_decimal = 3.14
yes = True
no = False

# i. string + string
print(name +" "+ lastname)

# ii. string + int 
#print(name + one) #Error 

# iii. int + string
#print(one + name) #Error

# iv. list + list 
print(cars + numbers)
print(numbers2 + numbers)

# v. string + list
#print(name + cars) #Error

# vi. float + int
print(number_decimal + one) 

# vii. bool + bool 
print (yes + no)
print (yes + yes)
print (no/yes)


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

#Ejercicio5
print("\n")
print("Ejercicio 5")
print("\n")

total_grades = int(input("¿Cuantas notas va a ingresar al sistema?"))
grade_counter = 1
passed_grades_count = 0
failed_grades_count = 0
passed_grades_sum = 0
failed_grades_sum = 0
total_grades_average = 0

while(grade_counter <= total_grades):
    current_grade = int(input(f"Ingrese la nota número {grade_counter}: "))
    if(current_grade < 70):
        failed_grades_count += 1
        failed_grades_sum += current_grade
    else:
        passed_grades_count += 1
        passed_grades_sum += current_grade
    total_grades_average += (current_grade / total_grades)
    grade_counter += 1

# Avoid division by zero
if failed_grades_count > 0:
    failed_grades_average = failed_grades_sum / failed_grades_count
else:
    failed_grades_average = 0

if passed_grades_count > 0:
    passed_grades_average = passed_grades_sum / passed_grades_count
else:
    passed_grades_average = 0

print(f"El estudiante tiene esta cantidad de notas aprobadas: {passed_grades_count}")
print(f"Este es el promedio de notas aprobadas: {passed_grades_average}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_grades_count}")
print(f"Este es el promedio de notas desaprobadas: {failed_grades_average}")
print(f"Este es el promedio total de notas: {total_grades_average}")