#Ejercicio 6
print("\n")

words = input("Enter a series of words separated by -: ")
string_list = words.split("-")

def alfabetical_order(string):
    sorted_list = sorted(string_list)
    new_string = "-".join(sorted_list)
    print(f"The words in alfabetical order are: {new_string}")


alfabetical_order(string_list)