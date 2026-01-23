#Ejercicio 5    
print("\n")

counter = 1
my_list = []
actual_number = 0

while counter <= 10:
    number = int(input(f"Enter your {counter} number: "))
    my_list.append(number)
    counter += 1


highest_number = my_list[0]
for index in range(1, len(my_list)):
    actual_number = my_list[index]
    if actual_number > highest_number:
        highest_number = actual_number

print(f"The highest number is: {highest_number}")