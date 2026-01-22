def show_menu():
    print("\nWelcome to the simple calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Erase Result")
    print("0. Exit")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def divide(result, number):
    if number == 0:
        print("Error: Division by zero is not allowed.")
        return result
    return result / number


def add(result, number):
    return result + number


def subtract(result, number):
    return result - number


def multiply(result, number):
    return result * number

def operations_calculator(choice, result):
    if choice == '5':
        print("Result erased.")
        return 0

    number = get_number("Enter your number: ")

    if choice == '1':
        return add(result, number)
    elif choice == '2':
        return subtract(result, number)
    elif choice == '3':
        return multiply(result, number)
    elif choice == '4':
        return divide(result, number)

def main():
    result = 0

    while True:
        print("\nCurrent result:", result)
        show_menu()

        choice = input("Enter choice (0/1/2/3/4/5): ")

        if choice == '0':
            print("Exiting program...")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid option. Try again.")
            continue

        result = operations_calculator(choice, result)
        print("Result:", result)


main()