#Ejercicio 3
print("\n")

numbers_list = [4, 6, 2, 29]

def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


result = sum_list(numbers_list)
print(f"The sum of the list is: {result}")