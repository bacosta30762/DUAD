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