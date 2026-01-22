#Ejercicio 1
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

index = 0
while index < len(first_list):
    print(f"{first_list[index]} {second_list[index]}")
    index += 1

#Ejercicio 2
print("\n")
my_string = "Pizza con piña"
for char in range (len (my_string)-1, -1, -1):
    #print(char)
    print(my_string[char])

#Ejercicio 3
print("\n")
my_list = [4, 3, 6, 1, 7]
first = my_list[0]
last = my_list[-1]
my_list[0] = last
my_list[-1] = first

print(my_list)


#Ejercicio 4    
print("\n")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range (len(my_list)-1, -1, -1):
    if my_list[index] % 2 != 0:
        eliminate = my_list.pop(index)

print(my_list)

#Ejercicio 4    
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