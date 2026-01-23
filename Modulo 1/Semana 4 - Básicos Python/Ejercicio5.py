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