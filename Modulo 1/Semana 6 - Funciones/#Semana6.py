#Ejercicio1
def first_sentence():
    return "code"


def second_sentence(string):
    print(f"Let's {string}")


second_sentence(first_sentence())

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

#Ejercicio 4
print("\n")

hello_world = "Hola mundo"

def return_string(string):
    for index in range(len(string)-1, -1, -1):
        print(string[index])


return_string(hello_world)

#Ejercicio 5
print("\n")

sushi = "I love Nación Sushi"

def count_strings(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    print(f"There's {uppercase_count} upper cases and {lowercase_count} lower cases in the string.")


count_strings(sushi)

#Ejercicio 6
print("\n")

words = input("Enter a series of words separated by -: ")
string_list = words.split("-")

def alfabetical_order(string):
    sorted_list = sorted(string_list)
    new_string = "-".join(sorted_list)
    print(f"The words in alfabetical order are: {new_string}")


alfabetical_order(string_list)

#Ejercicio 7
print("\n")

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def list_primes(list):
    primes = []
    for num in list:
        if prime_number(num):
            primes.append(num)
    return primes


numbers = [1, 4, 6, 7, 13, 9, 67]
prime_numbers = list_primes(numbers)
print(f"The prime numbers in the list are: {prime_numbers}")