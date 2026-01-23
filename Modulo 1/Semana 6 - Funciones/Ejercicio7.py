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