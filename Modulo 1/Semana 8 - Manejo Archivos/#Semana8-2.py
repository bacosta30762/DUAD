import csv


videogame_headers = (
	'name',
	'genre',
	'developer',
	'ESRB rating',
)


def add_videogames(headers):
    with open('videogames.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        while True:
            print("Do yo want to add a videogame?")
            print("1. Yes")
            print("2. No")

            choice = input("Enter choice (1 or 2): ")

            if choice == '2':
                print("Exiting program...")
                break

            elif choice == '1':
                name = input("Name of the videogame: ")
                genre = input("Genre of the videogame: ")
                developer = input("Developer of the videogame: ")
                rating = input("ESRB rating of the videogame: ")
                writer.writerow({
                    'name': name,
                    'genre': genre,
                    'developer': developer,
                    'ESRB rating': rating
                })
                print("Game added")
                continue
            else:
                print("Invalid option. Try again.")


def add_videogamesTab(headers):
    with open('videogames.tsv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        while True:
            print("Do yo want to add a videogame?")
            print("1. Yes")
            print("2. No")

            choice = input("Enter choice (1 or 2): ")

            if choice == '2':
                print("Exiting program...")
                break

            elif choice == '1':
                name = input("Name of the videogame: ")
                genre = input("Genre of the videogame: ")
                developer = input("Developer of the videogame: ")
                rating = input("ESRB rating of the videogame: ")
                writer.writerow({
                    'name': name,
                    'genre': genre,
                    'developer': developer,
                    'ESRB rating': rating
                })
                print("Game added")
                continue
            else:
                print("Invalid option. Try again.")


add_videogames(videogame_headers)
add_videogamesTab(videogame_headers)