#Ejercicio 2
print("\n")

#a)
# def sum_numbers():
#     number_one = 6
#     number_two = 4
#     return number_one + number_two

# def multiply_numbers():
#     return number_one * number_two

# multiply_numbers()  # This will raise an error because number_one and number_two are not defined in this scope


#b)
number_three = 10
def sum_numbers_two():
    global number_three     
    number_two = 4
    number_three = number_two + number_three
    return number_three


sum_numbers_two()
print(number_three) 